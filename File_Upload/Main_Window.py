import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from New_Window import NewWindow
from Add_Window import AddWindow
from Excel_Window import ExcelWindow
from Download_Window import DownloadWindow

form_class = uic.loadUiType("File_Upload/Main_Window.ui")[0]

class MyWindow(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    
    def initUI(self):
        self.setupUi(self)
        
        self.FileVar.setShortcut('Ctrl+Q')
        self.FileVar.setStatusTip('Exit application')
        self.FileVar.triggered.connect(qApp.quit)
        
        self.NewFile.clicked.connect(self.ButtonNew)
        self.AddFile.clicked.connect(self.ButtonAdd)
        self.ExcelFile.clicked.connect(self.ButtonExcel)
        self.DownFile.clicked.connect(self.ButtonDownload)
    
    def ButtonNew(self):
        self.hide()
        self.new = NewWindow()
        self.new.exec()
        self.show()
    
    def ButtonAdd(self):
        self.hide()
        self.new = AddWindow()
        self.new.exec()
        self.show()
        
    def ButtonExcel(self):
        self.hide()
        self.new = ExcelWindow()
        self.new.exec()
        self.show()
        
    def ButtonDownload(self):
        self.hide()
        self.new = DownloadWindow()
        self.new.exec()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle('Fusion')
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()