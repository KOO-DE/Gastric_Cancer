import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import sqlalchemy
pymysql.install_as_MySQLdb()

form_class = uic.loadUiType("File_Upload/Excel_Window.ui")[0]

class ExcelWindow(QDialog, QWidget, form_class):
    
    def __init__(self):
        super(ExcelWindow, self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        
        self.excel_closebtn.clicked.connect(self.Cancel)
        
        self.excel_importbtn.clicked.connect(self.openFileNamesDialog)   
        # excel 파일 불러오기 버튼 클릭
        
        self.excel_selectbtn.clicked.connect(self.FileNamesSelect) 
        
        self.excel_savebtn.clicked.connect(self.saveFileName)
        
        self.excel_editbtn.clicked.connect(self.printFileName)
        
        self.excel_actbtn.clicked.connect(self.RunProgram)
        
    def Cancel(self):
        self.close()
        
    def openFileNamesDialog(self):

        files = QFileDialog.getOpenFileName(None, "Open Excel File", '.', "(*.xlsx)")[0]

        # ⓐ '.' = 현재 디렉토리 기준
        # ⓑ ".xlsx" = xlsx 파일을 기본적으로 선택할 수 있음
        # ⓒ "Open Excel File" = "Open Excel File" 을 캡션으로 정함
        # ⓓ [0] = ['파일명'] 처럼 list 형태로 반환, 그것을 처리해주기 위함
        
        if files:
            self.showfilename.setText(files)
            
            global frames
            if self.setsheet.currentText() == "sheet1":
                frames = pd.read_excel(files, skiprows = [0], sheet_name = 0)
            elif self.setsheet.currentText() == "sheet2":
                frames = pd.read_excel(files, sheet_name=1)
                
            print(frames)
        
        self.showtext1.setText("파일을 열었습니다.\n\nDB 이름을 설정해 주세요.")
        # self.btn1.setDisabled(True)
        
    def FileNamesSelect(self):
        
        print("comboBox index:", self.setdbname.currentText())
        if self.setdbname.currentText() == "Biopsy":
            self.showdbname.setText("biopsy_protocol")
        elif self.setdbname.currentText() == "Block Mapping":
            self.showdbname.setText("block_mapping_protocol")
        elif self.setdbname.currentText() == "Comorbidity":
            self.showdbname.setText("comorbidity_protocol")
        elif self.setdbname.currentText() == "Endoscope":
            self.showdbname.setText("endoscope_protocol")
        elif self.setdbname.currentText() == "Genetic":
            self.showdbname.setText("genetic_protocol")
        elif self.setdbname.currentText() == "Operation Record":
            self.showdbname.setText("operation_record_protocol")
        elif self.setdbname.currentText() == "Pathology":
            self.showdbname.setText("pathology_protocol")
        elif self.setdbname.currentText() == "Patient":
            self.showdbname.setText("patient_protocol")
        elif self.setdbname.currentText() == "Registry":
            self.showdbname.setText("registry_protocol")
        elif self.setdbname.currentText() == "Wash Cytology":
            self.showdbname.setText("wash_cytology_protocol")
        
    def saveFileName(self):
        
        global db_name
        
        db_name = self.showdbname.text()
        self.showtext2.setText(db_name)
        
    def printFileName(self):
        
        global file_name
        
        file_name = self.editfilename.text()
        self.showtext3.setText(file_name)
        
    def RunProgram(self):
        
        engine = create_engine("mysql+mysqldb://cnuh:cnuh12345!!@127.0.0.1:3306/{}".format(db_name), encoding = 'utf-8')
        conn = engine.connect()
        
        self.showtext4.setText("DB에 연결됐습니다.")
        
        dtypedict = {}
        
        if file_name != None:
            
            for i,j in zip(frames.columns, frames.dtypes):
                if "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
            
        # outputdict = self.sqlcol(frames)
        
        frames.to_sql(name = file_name, con = engine, if_exists = 'replace', index = False, dtype = dtypedict) 
        self.showtext4.setText("DB에 파일이 업로드 되었습니다.")
        
        conn.close
    
    # def sqlcol(dfparam):    
        

    #     return dtypedict