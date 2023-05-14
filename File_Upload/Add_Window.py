import sys
import os
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pandas as pd
from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

form_class = uic.loadUiType("File_Upload/Add_Window.ui")[0]

class AddWindow(QDialog, QWidget, form_class):
    
    def __init__(self):
        super(AddWindow, self).__init__()
        self.initUI()
        self.show()
        
    def initUI(self):
        self.setupUi(self)
        self.add_closebtn.clicked.connect(self.Cancel)
        self.add_importbtn.clicked.connect(self.openFileNamesDialog)   
        self.add_selectbtn.clicked.connect(self.FileNamesSelect) 
        self.add_savebtn.clicked.connect(self.saveFileName)
        self.add_actbtn.clicked.connect(self.RunProgram)
        
    def Home(self):
        self.close()
        
    def openFileNamesDialog(self):

        files = QFileDialog.getOpenFileName(None, "Open Excel File", '.', "(*.*)")[0]

        # ⓐ '.' = 현재 디렉토리 기준
        # ⓑ ".xlsx" = xlsx 파일을 기본적으로 선택할 수 있음
        # ⓒ "Open Excel File" = "Open Excel File" 을 캡션으로 정함
        # ⓓ [0] = ['파일명'] 처럼 list 형태로 반환, 그것을 처리해주기 위함
        
        if files:
            self.showfiilename.setText(files)
            
            global frames
            
            if self.setsheet.currentText() == "sheet1":
                frames = pd.read_excel(files, skiprows = [0], sheet_name = 0)
            elif self.setsheet.currentText() == "sheet2":
                frames = pd.read_excel(files, sheet_name = 1)
                
            print(frames)
            # frames.to_csv("C:/Users/Hyunjeong Ki/Gastric_Cancer_xlsx/data.csv",encoding='UTF8',index=False)
            # data = pd.read_csv("C:/Users/Hyunjeong Ki/Gastric_Cancer_xlsx/data.csv", sep=",")
            # print(data)
            
            # global f
            # f = open("C:/Users/Hyunjeong Ki/Gastric_Cancer_xlsx/data.csv",'r',encoding='UTF8')

            # global csvReader
            # csvReader = csv.reader(f)
            # print(csvReader)
        
        self.showtext1.setText("파일을 열었습니다.\n\nDB 이름을 설정해 주세요")
        # self.btn1.setDisabled(True)
    
    def selectDBName(self):
        
        print("DB Name:", self.setdbname.currentText())
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
    
    def saveTableName(self):
        
        global table_name
        
        table_name = self.showtablename.text()
        self.show
    def saveDBName(self):
        
        global db_name
        
        db_name = self.showdbname.text()
        self.showtext3.setText(db_name)
    
    def RunProgram(self):
        
        engine = create_engine("mysql+mysqldb://cnuh:cnuh12345!!@127.0.0.1:3306/{}".format(table_name), encoding = 'utf-8')
        conn = engine.connect()
        
        con = pymysql.connect(host = 'localhost',
                        user = 'cnuh',
                        password = 'cnuh12345!!',
                        port = 3306,
                        charset = 'utf8')
        
        cursor = con.cursor()
        
        self.showtext.setText("DB에 연결 되었습니다")
        
        if db_name == "operation":
            
            for 원무접수ID, 환자번호, 환자명, 성별, 생년월일, 수술일자, 수술코드, 수술명, ICD9CM코드, ICD9CM명, 수술_진료과코드, 수술_진료과, 집도의_사번, 집도의, 수석의_사번, 수석의, 수술후퇴실장소코드, 수술후퇴실장소, 마취종류코드, 마취종류, 수술진단코드, 수술진단명, 입실일시, 마취시작, 수술시작시간, 수술종료시간, 마취종료, 퇴실시간, 회복실입실일시, 회복실퇴실일시  in zip(
                frames["원무접수ID"], frames["환자번호"], frames["환자명"], frames["성별"], frames["생년월일"], frames["수술일자"], frames["수술코드"], frames["수술명"],
                frames["ICD9CM코드"], frames["ICD9CM명"], frames["수술 진료과코드"], frames["수술 진료과"], frames["집도의 사번"], frames["집도의"], frames["수석의 사번"], frames["수석의"],
                frames["수술후퇴실장소코드"], frames["수술후퇴실장소"], frames["마취종류코드"], frames["마취종류"], frames["수술진단코드"], frames["수술진단명"], frames["입실일시"], frames["마취시작(간)"],
                frames["수술시작시간"], frames["수술종료시간"], frames["마취종료(간)"], frames["퇴실시간"], frames["회복실입실일시"], frames["회복실퇴실일시"]):
                sql  = '''
                    INSERT INTO raw_file_total.{0} (
                        `원무접수ID`,
                        `환자번호`,
                        `환자명`,
                        `성별`,
                        `생년월일`,
                        `수술일자`,
                        `수술코드`,
                        `수술명`,
                        `ICD9CM코드`,
                        `ICD9CM명`,
                        `수술 진료과코드`,
                        `수술 진료과`,
                        `집도의 사번`,
                        `집도의`,
                        `수석의 사번`,
                        `수석의`,
                        `수술후퇴실장소코드`,
                        `수술후퇴실장소`,
                        `마취종류코드`,
                        `마취종류`,
                        `수술진단코드`,
                        `수술진단명`,
                        `입실일시`,
                        `마취시작(간)`,
                        `수술시작시간`,
                        `수술종료시간`,
                        `마취종료(간)`,
                        `퇴실시간`,
                        `회복실입실일시`,
                        `회복실퇴실일시`
                    )
                    VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' )
                '''.format(db_name)
                
                # if "float" in str(type(의무기록내용_수치값)):
                #     의무기록내용_수치값 = str(의무기록내용_수치값)
                if "str" in str(type(수술진단명)):
                    수술진단명 = str(수술진단명).replace('\\','').replace("'","\\'")
                    
                print(원무접수ID, 환자번호, 환자명, 성별, 생년월일, 수술일자, 수술코드, 수술명, ICD9CM코드, ICD9CM명, 수술_진료과코드, 수술_진료과, 집도의_사번, 집도의, 수석의_사번, 수석의, 수술후퇴실장소코드, 수술후퇴실장소, 마취종류코드, 마취종류, 수술진단코드, 수술진단명, 입실일시,  마취시작, 수술시작시간, 수술종료시간,마취종료, 퇴실시간, 회복실입실일시, 회복실퇴실일시)
                
                cursor.execute(sql %(원무접수ID, 환자번호, 환자명, 성별, 생년월일, 수술일자, 수술코드, 수술명, ICD9CM코드, ICD9CM명, 수술_진료과코드, 수술_진료과, 집도의_사번, 집도의, 수석의_사번, 수석의,수술후퇴실장소코드, 수술후퇴실장소, 마취종류코드, 마취종류, 수술진단코드, 수술진단명, 입실일시, 마취시작, 수술시작시간, 수술종료시간,마취종료, 퇴실시간, 회복실입실일시, 회복실퇴실일시))
        
        if db_name == "operation_record":
            
            for 원무접수ID, 환자번호, 환자명, 성별, 생년월일, 의무기록작성일, 수정기록일, 의무기록작성_진료과코드, 의무기록작성_진료과, 작성의_사번, 작성의, 의무기록_환자진료과코드, 의무기록_환자진료과, 진료서식ID, 의무기록명, 진료서식구성원소ID, 의무기록항목명, 의무기록내용_수치값, 의무기록내용, 진료서식유형코드, 의무기록구분명, 진료기록서명여부  in zip(
                frames["원무접수ID"], frames["환자번호"], frames["환자명"], frames["성별"], frames["생년월일"], frames["의무기록작성일"], frames["수정기록일"], frames["의무기록작성 진료과코드"],
                frames["의무기록작성 진료과"], frames["작성의 사번"], frames["작성의"], frames["의무기록 환자진료과코드"], frames["의무기록 환자진료과"], frames["진료서식ID"], frames["의무기록명"], frames["진료서식구성원소ID"],
                frames["의무기록항목명"], frames["의무기록내용-수치값"], frames["의무기록내용"], frames["진료서식유형코드"], frames["의무기록구분명"], frames["진료기록서명여부"]):
                sql  = '''
                    INSERT INTO raw_file_total.{0} (
                        `원무접수ID`,
                        `환자번호`,
                        `환자명`,
                        `성별`,
                        `생년월일`,
                        `의무기록작성일`,
                        `수정기록일`,
                        `의무기록작성 진료과코드`,
                        `의무기록작성 진료과`,
                        `작성의 사번`,
                        `작성의`,
                        `의무기록 환자진료과코드`,
                        `의무기록 환자진료과`,
                        `진료서식ID`,
                        `의무기록명`,
                        `진료서식구성원소ID`,
                        `의무기록항목명`,
                        `의무기록내용-수치값`,
                        `의무기록내용`,
                        `진료서식유형코드`,
                        `의무기록구분명`,
                        `진료기록서명여부`
                    )
                    VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                    '''.format(db_name)
                    
                if "float" in str(type(의무기록내용_수치값)):
                    의무기록내용_수치값 = str(의무기록내용_수치값)
                    
                if "str" in str(type(의무기록내용)):
                    의무기록내용 = str(의무기록내용).replace('\\','').replace("'","\\'")
                    
                print(원무접수ID, 환자번호, 환자명, 성별, 생년월일, 의무기록작성일, 수정기록일, 의무기록작성_진료과코드, 의무기록작성_진료과, 작성의_사번, 작성의, 의무기록_환자진료과코드, 의무기록_환자진료과, 진료서식ID, 의무기록명, 진료서식구성원소ID, 의무기록항목명, 의무기록내용_수치값, 의무기록내용, 진료서식유형코드, 의무기록구분명, 진료기록서명여부)
                
                cursor.execute(sql %(원무접수ID, 환자번호, 환자명, 성별, 생년월일, 의무기록작성일, 수정기록일, 의무기록작성_진료과코드, 의무기록작성_진료과, 작성의_사번, 작성의, 의무기록_환자진료과코드, 의무기록_환자진료과, 진료서식ID, 의무기록명, 진료서식구성원소ID, 의무기록항목명, 의무기록내용_수치값, 의무기록내용, 진료서식유형코드, 의무기록구분명, 진료기록서명여부))

        if db_name == "blood_test":
            
            for 원무접수ID, 환자번호, 환자명, 성별, 생년월일, 검사시행일, 검사코드, 검사명, 검사세부항목명, 검사서식세부항목ID, 검사결과_수치값, 검사결과_음성양성, 검사결과, 판독의사번, 판독의, 검사처방일, 검사_처방의사번, 검사_처방의, 검사유형, 검사_시행처, 처방전표분류, 응급여부, 시행여부 in zip(
                frames["원무접수ID"], frames["환자번호"], frames["환자명"], frames["성별"], frames["생년월일"], frames["검사시행일"], frames["검사코드"], frames["검사명"],
                frames["검사세부항목명"], frames["검사서식세부항목ID"], frames["검사결과-수치값"], frames["검사결과-음성양성"], frames["검사결과"], frames["판독의사번"], frames["판독의"], frames["검사처방일"],
                frames["검사 처방의사번"], frames["검사 처방의"], frames["검사유형"], frames["검사 시행처"], frames["처방전표분류"], frames["응급여부"], frames["시행여부"]):
                sql  = '''
                    INSERT INTO raw_file_total.{0} (
                        `원무접수ID`
                        ,`환자번호`
                        ,`환자명`
                        ,`성별`
                        ,`생년월일`
                        , `검사시행일`
                        , `검사코드`
                        , `검사명`
                        , `검사세부항목명`
                        , `검사서식세부항목ID`
                        , `검사결과-수치값`
                        , `검사결과-음성양성`
                        , `검사결과`
                        , `판독의사번`
                        , `판독의`
                        , `검사처방일`
                        , `검사 처방의사번`
                        , `검사 처방의`
                        , `검사유형`
                        , `검사 시행처`
                        , `처방전표분류`
                        , `응급여부`
                        , `시행여부`
                    )
                    VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                '''.format(db_name)
                
                if "float" in str(type(검사결과_수치값)):
                    검사결과_수치값 = str(검사결과_수치값)
                    
                print(원무접수ID, 환자번호, 환자명, 성별, 생년월일, 검사시행일, 검사코드, 검사명, 검사세부항목명, 검사서식세부항목ID, 검사결과_수치값, 검사결과_음성양성, 검사결과, 판독의사번, 판독의, 검사처방일, 검사_처방의사번, 검사_처방의, 검사유형, 검사_시행처, 처방전표분류, 응급여부, 시행여부)
                
                cursor.execute(sql %(원무접수ID, 환자번호, 환자명, 성별, 생년월일, 검사시행일, 검사코드, 검사명, 검사세부항목명, 검사서식세부항목ID, 검사결과_수치값, 검사결과_음성양성, 검사결과, 판독의사번, 판독의, 검사처방일, 검사_처방의사번, 검사_처방의, 검사유형, 검사_시행처, 처방전표분류, 응급여부, 시행여부))
        
        if db_name == "nursing_record":
            
            for 원무접수ID, 환자번호, 환자명, 성별, 생년월일, 간호기록부서,기록작성일시, 기록종류명, 간호항목_진술문명, Entity, Attribute, Value, Ent_Atr_항목 in zip(
                frames["원무접수ID"], frames["환자번호"] , frames["환자명"], frames["성별"] , frames["생년월일"], frames["[간호기록]간호기록부서"], frames["[간호기록]기록작성일시"],
                frames["기록종류명"], frames["간호항목/진술문명"], frames["Entity"], frames["Attribute"], frames["Value"], frames["Ent:Atr:항목"]):
                sql  = '''
                    INSERT INTO raw_file_total.{0} (
                        `원무접수ID`,
                        `환자번호`,
                        `환자명`,
                        `성별`,
                        `생년월일`,
                        `[간호기록]간호기록부서`,
                        `[간호기록]기록작성일시`,
                        `기록종류명`,
                        `간호항목/진술문명`,
                        `Entity`,
                        `Attribute`,
                        `Value`,
                        `Ent:Atr:항목`
                    )
                    VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                    '''.format(db_name)
                    
                if "str" in str(type(간호항목_진술문명)):
                    간호항목_진술문명 = str(간호항목_진술문명).replace('\\','').replace("'","\\'")
                    
                if "str" in str(type(Value)):
                    Value = str(Value).replace('\\','').replace("'","\\'")
                    
                print(원무접수ID, 환자번호, 환자명, 성별, 생년월일, 간호기록부서, 기록작성일시, 기록종류명, 간호항목_진술문명, Entity, Attribute, Value, Ent_Atr_항목)
                
                cursor.execute(sql %(원무접수ID, 환자번호, 환자명, 성별, 생년월일, 간호기록부서, 기록작성일시, 기록종류명, 간호항목_진술문명, Entity, Attribute, Value, Ent_Atr_항목))
        
        if db_name == "image":
            
            for 원무접수ID, 환자번호, 환자명, 성별, 생년월일, 검사시행일, 검사코드, 검사명, 검사세부항목명, 검사서식세부항목ID, 검사결과_수치값, 검사결과_음성양성, 검사결과, 판독의사번, 판독의, 검사처방일, 검사_처방의사번, 검사_처방의, 검사유형, 검사_시행처, 처방전표분류, 응급여부, 시행여부 in zip(
                frames["원무접수ID"], frames["환자번호"], frames["환자명"], frames["성별"], frames["생년월일"], frames["검사시행일"], frames["검사코드"], frames["검사명"],
                frames["검사세부항목명"], frames["검사서식세부항목ID"], frames["검사결과-수치값"], frames["검사결과-음성양성"], frames["검사결과"], frames["판독의사번"], frames["판독의"], frames["검사처방일"],
                frames["검사 처방의사번"], frames["검사 처방의"], frames["검사유형"], frames["검사 시행처"], frames["처방전표분류"], frames["응급여부"], frames["시행여부"]):
                sql  = '''
                    INSERT INTO raw_file_total.{0} (
                        원무접수ID,
                        `환자번호`,
                        `환자명`,
                        `성별`,
                        `생년월일`,
                        `검사시행일`,
                        `검사코드`,
                        `검사명`,
                        `검사세부항목명`,
                        `검사서식세부항목ID`,
                        `검사결과-수치값`,
                        `검사결과-음성양성`,
                        `검사결과`,
                        `판독의사번`,
                        `판독의`,
                        `검사처방일`,
                        `검사 처방의사번`,
                        `검사 처방의`,
                        `검사유형`,
                        `검사 시행처`,
                        `처방전표분류`,
                        `응급여부`,
                        `시행여부`
                    )
                    VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                    '''.format(db_name)
                    
                if "str" in str(type(검사결과)):
                    검사결과 = str(검사결과).replace('\\','').replace("'","\\'")
                    
                # if "str" in str(type(Value)):
                #     Value = str(Value).replace('\\','').replace("'","\\'")
                
                if "float" in str(type(검사결과_수치값)):
                    검사결과_수치값 = float(검사결과_수치값)
                    
                if "float" in str(type(검사결과_음성양성)):
                    검사결과_음성양성 = str(검사결과_음성양성)
                    
                print(원무접수ID, 환자번호, 환자명, 성별, 생년월일, 검사시행일, 검사코드, 검사명, 검사세부항목명, 검사서식세부항목ID, 검사결과_수치값, 검사결과_음성양성, 검사결과, 판독의사번, 판독의, 검사처방일, 검사_처방의사번, 검사_처방의, 검사유형, 검사_시행처, 처방전표분류, 응급여부, 시행여부)
                
                cursor.execute(sql %(원무접수ID, 환자번호, 환자명, 성별, 생년월일, 검사시행일, 검사코드, 검사명, 검사세부항목명, 검사서식세부항목ID, 검사결과_수치값, 검사결과_음성양성, 검사결과, 판독의사번, 판독의, 검사처방일, 검사_처방의사번, 검사_처방의, 검사유형, 검사_시행처, 처방전표분류, 응급여부, 시행여부))
        
        con.commit()
        
        con.close
        
        sql = "SELECT DISTINCT * FROM {}.{}".format(table_name, db_name)
        
        df = pd.read_sql(sql, engine)
        df.to_sql(name = db_name, con = engine, if_exists = 'replace', index = False) 
        
        self.showtext.setText("DB에 파일이 업로드 되었습니다")
        
        conn.close()