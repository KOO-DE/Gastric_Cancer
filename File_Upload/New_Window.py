import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import sqlalchemy
pymysql.install_as_MySQLdb()

form_class = uic.loadUiType("File_Upload/New_Window.ui")[0]

class NewWindow(QDialog, QWidget, form_class):
    
    def __init__(self):
        super(NewWindow,self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        
        self.new_homebtn.clicked.connect(self.Home)
        
        self.new_importbtn.clicked.connect(self.openFileNamesDialog)   
        # excel 파일 불러오기 버튼 클릭
        
        self.new_selectbtn.clicked.connect(self.FileNamesSelect) 
        
        
        self.new_savebtn.clicked.connect(self.saveFileName)
        
        
        self.new_actbtn.clicked.connect(self.RunProgram)
        
    def Home(self):
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
        
        self.showtext.setText("파일을 열었습니다.\n\nDB 이름을 설정해 주세요.")
        # self.btn1.setDisabled(True)
        
    def FileNamesSelect(self):
        
        print("comboBox index:", self.setdbname.currentText())
        if self.setdbname.currentText() == "환자정보":
            self.showdbname.setText("patient")
        elif self.setdbname.currentText() == "진단":
            self.showdbname.setText("diagnosis")
        elif self.setdbname.currentText() == "수술":
            self.showdbname.setText("operation")
        elif self.setdbname.currentText() == "혈액검사":
            self.showdbname.setText("blood_test")
        elif self.setdbname.currentText() == "간호기록":
            self.showdbname.setText("nursing_record")
        elif self.setdbname.currentText() == "조직검사":
            self.showdbname.setText("biopsy")
        elif self.setdbname.currentText() == "마취기록":
            self.showdbname.setText("anesthetic")
        elif self.setdbname.currentText() == "미생물":
            self.showdbname.setText("microorganism")
        elif self.setdbname.currentText() == "영상검사":
            self.showdbname.setText("image")
        elif self.setdbname.currentText() == "수술기록지":
            self.showdbname.setText("operation_record")
        elif self.setdbname.currentText() == "내시경검사":
            self.showdbname.setText("endoscope")
        elif self.setdbname.currentText() == "항암제":
            self.showdbname.setText("anticancer_drug")
        elif self.setdbname.currentText() == "외래초진":
            self.showdbname.setText("outpatient")
        elif self.setdbname.currentText() == "ASA":
            self.showdbname.setText("asa_score")
            
    def saveFileName(self):
        
        global text
        text = self.showdbname.text()
        self.showtext.setText(text)
        
    def RunProgram(self):
        
        engine = create_engine("mysql+mysqldb://cnuh:cnuh12345!!@127.0.0.1:3306/raw_file", encoding = 'utf-8')
        conn = engine.connect()
        self.showtext.setText("DB에 연결됐습니다.")
        
        dtypedict = {}
        
        if text == "patient":
            
            for i,j in zip(frames.columns, frames.dtypes):
                if "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "최초수진일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                    
                elif "최종수진일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "수진(진료)일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "입원일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "퇴원일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                    
                elif "입실시각(응급실)" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                
                elif "퇴실시각(응급실)" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                    
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
        
        if text == "diagnosis":
            
            for i,j in zip(frames.columns, frames.dtypes):
                if "첫 진단일자" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                    
                elif "진단일자" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                    
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})

                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})

                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
                    
        if text == "operation":
            
            for i,j in zip(frames.columns, frames.dtypes):
                if "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "수술일자" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                    
                elif "마취시작(간)" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "입실일시" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                
                elif "수술시작시간" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                
                elif "수술종료시간" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "마취종료(간)" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                
                elif "퇴실시간" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                
                elif "회복실입실일시" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "회복실퇴실일시" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                    
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
                    
        if text == "blood_test":
            
            for i,j in zip(frames.columns, frames.dtypes):    
                if "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "검사시행일" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "검사처방일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "검사결과-수치값" in i:
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                    
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                    
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
                    
        if text == "nursing_record":
            
            for i,j in zip(frames.columns, frames.dtypes):    
                if "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "[간호기록]기록작성일시" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                    
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
                    
        if text == "biopsy":
            
            for i,j in zip(frames.columns, frames.dtypes):    
                if "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "검사시행일" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "검사처방일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})    
                    
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                    
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
                    
        if text == "anesthetic":
            
            for i,j in zip(frames.columns, frames.dtypes):    
                if "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "의무기록작성일" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "수정기록일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})    
                    
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                    
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
        '''
        if text == "microorganism":
        
            for i,j in zip(frames.columns, frames.dtypes):    
                if "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()}) 
                    
        #         elif "object" in str(j):
        #             dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
        #         elif "datetime" in str(j):
        #             dtypedict.update({i: sqlalchemy.types.DateTime()})

        #         elif "float" in str(j):
        #             dtypedict.update({i: sqlalchemy.types.Float(precision=3, asdecimal=True)})

        #         elif "int" in str(j):
        #             dtypedict.update({i: sqlalchemy.types.INT()})
        '''
        if text == "image":
            
            for i,j in zip(frames.columns, frames.dtypes):    
                if "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "검사시행일" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "검사처방일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})  
                    
                elif "검사결과-수치값" in i:
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                    
                elif "검사결과-음성양성" in i:
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                    
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                    
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
                    
        if text == "operation_record":
            
            for i,j in zip(frames.columns, frames.dtypes):    
                if "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "의무기록작성일" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "수정기록일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})    
                    
                elif "의무기록내용-수치값" in i:
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                    
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                    
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
                    
        if text == "endoscope":
            
            for i,j in zip(frames.columns, frames.dtypes):    
                if "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "검사시행일" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "검사처방일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})    
                    
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                    
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
        '''
        # if text == "anticancer_drug":
        #     for i,j in zip(frames.columns, frames.dtypes):    
        #         if "생년월일" in i:
        #             dtypedict.update({i: sqlalchemy.types.Date()})
                
        #         elif "의무기록작성일" in i:
        #             dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
        #         elif "수정기록일" in i:
        #             dtypedict.update({i: sqlalchemy.types.Date()})    
                    
        #         elif "object" in str(j):
        #             dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
        #         elif "datetime" in str(j):
        #             dtypedict.update({i: sqlalchemy.types.DateTime()})

        #         elif "float" in str(j):
        #             dtypedict.update({i: sqlalchemy.types.Float(precision=3, asdecimal=True)})

        #         elif "int" in str(j):
        #             dtypedict.update({i: sqlalchemy.types.INT()})
        '''
        if text == "outpatient":
            
            for i,j in zip(frames.columns, frames.dtypes):    
                if "생년월일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "의무기록작성일" in i:
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "수정기록일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})    
                    
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                                            
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                    
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
                    
        if text == "asa_score":
            
            for i,j in zip(frames.columns, frames.dtypes):    
                if "수술일" in i:
                    dtypedict.update({i: sqlalchemy.types.Date()})
                
                elif "object" in str(j):
                    dtypedict.update({i: sqlalchemy.types.TEXT()})
                
                elif "datetime" in str(j):
                    dtypedict.update({i: sqlalchemy.types.DateTime()})
                    
                elif "float" in str(j):
                    dtypedict.update({i: sqlalchemy.types.Float(precision = 3, asdecimal = True)})
                    
                elif "int" in str(j):
                    dtypedict.update({i: sqlalchemy.types.INTEGER()})
        
        # outputdict = self.sqlcol(frames)
                
        frames.to_sql(name = text, con = engine, if_exists = 'replace', index = False, dtype = dtypedict) 
        self.showtext.setText("DB에 파일이 업로드 되었습니다.")
        
        conn.close
    
    # def sqlcol(dfparam):    
        

    #     return dtypedict