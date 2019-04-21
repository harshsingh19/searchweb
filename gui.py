from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QToolTip,QMessageBox,QInputDialog, QLineEdit,QLabel
from PyQt5.QtCore import QCoreApplication
import sys
from PyQt5.QtWidgets import  QWidget, QAction,QComboBox,QHBoxLayout, QFrame, QSplitter,QStyleFactory,QTabWidget,QVBoxLayout,QListWidget
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtGui import QPixmap 
import pandas as pd
import os
from bargraphviewer import Viewer1
from wordcloudviewer import Viewer2
from scatterviewer import Viewer3
from pichartviewer import Viewer4
from search import main as final
class MyTableWidget(QWidget):        

    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.imagenumber=0
        self.tabs = QTabWidget()
        self.tab1 = QWidget()	
        self.tab2 = QWidget()            
        self.tabs.resize(300,200)       
        # Add tabs
        self.tabs.addTab(self.tab1,"Tab 1")
        self.tabs.addTab(self.tab2,"Tab 2")
        # Create first tab
        self.list_printer(0)

        self.tab1.layout.addWidget(self.listWidget)
        self.tab1.setLayout(self.tab1.layout)
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def keyPressEvent(self, event):
        key=event.key()
        if key==Qt.Key_Right:
            self.imagenumber=self.imagenumber+1
            self.list_printer(self.imagenumber)
            # self.show()
        elif key==Qt.Key_Left:
            self.imagenumber=self.imagenumber-1
            self.list_printer(self.imagenumber)


    def list_printer(self,imagenumber):
        filelist = os.listdir('xls_file_data')
        ls = pd.read_excel('xls_file_data/'+filelist[0])
        ls = ls['Website Address'].tolist()
        self.tab1.layout = QVBoxLayout(self)
        self.listWidget = QListWidget()
        self.listWidget.addItems(ls)
        self.listWidget.show()

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
    
class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Web Analizer"
        self.top = 20
        self.left = 20
        self.width = 700
        self.height = 700
        self.setWindowIcon(QtGui.QIcon("images.jpeg"))
            
        self.InitWindow()


    
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height);
        self.statusBar().showMessage("Ready")
        
        self.button()
        self.getText()
        self.llabel()
        self.menub()
        self.getChoice()
        self.tabwidget()
        self.show()
    def button(self):
        #search Button
        button1 = QPushButton("Search",self)
        button1.move(560,50)
        button1.setToolTip("<p>Button for Search Google</p>")
        button1.clicked.connect(self.on_click)
        #close button
        button2 = QPushButton("Close",self)
        button2.move(560,650)
        button2.setToolTip("<p>Button for Close </p>")
        button2.clicked.connect(self.CloseApp)
        #bar graph Button
        button3 = QPushButton("Bar Graphs",self)
        button3.move(560,250)
        button3.setToolTip("<p>Button Shows Bar Graphs</p>")
        button3.clicked.connect(self.imageview)
        #worcloud button
        button4 = QPushButton("Word Cloud",self)
        button4.move(560,300)
        button4.setToolTip("<p>Button Shows Word Cloud </p>")
        button4.clicked.connect(self.imageview1)
        #scatter plot Button
        button5 = QPushButton("Scatter Plot",self)
        button5.move(560,350)
        button5.setToolTip("<p>Button Shows Scatter Plot</p>")
        button5.clicked.connect(self.imageview2)
        #pie chart button
        button6 = QPushButton("Pie Chart",self)
        button6.move(560,400)
        button6.setToolTip("<p>Button Shows Pie Chart </p>")
        button6.clicked.connect(self.imageview3)
    def imageview(self):
        self.newapp = Viewer1()  
    def imageview1(self):
        self.newapp = Viewer2()  
    def imageview2(self):
        self.newapp = Viewer3()  
    def imageview3(self):
        self.newapp = Viewer4()  
    def CloseApp(self):
        reply = QMessageBox.question(self,"Close Message","Are you Sure You want to close it", QMessageBox.Yes | QMessageBox.No , QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            
    def getText(self):
        self.Textbox1 = QLineEdit(self)
        self.Textbox1.resize(200,32)
        self.Textbox1.move(300,50)
        self.Textbox1.setPlaceholderText("Enter the Search Key Word")
        self.Textbox2 = QLineEdit(self)
        self.Textbox2.resize(200,32)
        self.Textbox2.move(300,150)
        self.Textbox2.setPlaceholderText("Enter the Other Key Words Seprated by comma")
    
    def llabel(self):
        Label1 = QLabel('Search The Word with comma Seprated: ',self)
        Label1.move(20,50)
        Label1.resize(250,32)
        Label2 =QLabel('Select Domain Location',self)
        Label2.move(20,100)
        Label2.resize(250,32)
        Label3 = QLabel('Other Key Word with comma Seprated :',self)
        Label3.move(20,150)
        Label3.resize(250,32)
    
    def menub(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        helpMenu = mainMenu.addMenu('Help')
    
    def getChoice(self):
        styleChoice = QComboBox(self)
        styleChoice.addItems(['',"USA","UK","Canada","Austraila"])
        styleChoice.move(300,100)
        styleChoice.activated[str].connect(self.onActivated)
        
    def onActivated(self,text):
        self.country = text
 
    @pyqtSlot()
    def on_click(self):
        self.textboxValue1 = self.Textbox1.text()
        self.textboxValue2 = self.Textbox2.text()
        self.datasender()
        #self.textbox.setText("")

    def tabwidget(self):
        self.table_widget = MyTableWidget(self)
        self.table_widget.resize(500,450)
        self.table_widget.move(10,200)
    
        #tabs.addTab(tab3,'WordCloud')
        #tabs.addTab(tab4,'Bar Chart')
    def datasender(self):
        final(self.textboxValue1,self.textboxValue2,self.country)

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())