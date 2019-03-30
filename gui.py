#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:57:43 2019

@author: harsh
"""
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QToolTip,QMessageBox,QInputDialog, QLineEdit,QLabel
from PyQt5.QtCore import QCoreApplication
import sys
from PyQt5.QtWidgets import  QWidget, QAction,QComboBox,QHBoxLayout, QFrame, QSplitter,QStyleFactory,QTabWidget,QVBoxLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Web Analizer"
        self.top = 20
        self.left = 20
        self.width = 900
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
        #close button
        button2 = QPushButton("Close",self)
        button2.move(780,650)
        button2.setToolTip("<p>Button for Close </p>")
        button2.clicked.connect(self.CloseApp)
        
    def CloseApp(self):
        reply = QMessageBox.question(self,"Close Message","Are you Sure You want to close it", QMessageBox.Yes | QMessageBox.No , QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
            
    def getText(self):
        Textbox1 = QLineEdit(self)
        Textbox1.resize(200,32)
        Textbox1.move(300,50)
        Textbox1.setPlaceholderText("Enter the Search Key Word")
        Textbox2 = QLineEdit(self)
        Textbox2.resize(200,32)
        Textbox2.move(300,150)
        Textbox2.setPlaceholderText("Enter the Other Key Words Seprated by comma")
    
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
        self.Labelchoice = QLabel('',self)
        styleChoice = QComboBox(self)
        styleChoice.addItems(["USA","UK","Canada","Austraila"])
        styleChoice.move(300,100)
        self.Labelchoice.move(780,300)
        styleChoice.activated[str].connect(self.onActivated)
        
    def onActivated(self,text):
        self.Labelchoice.setText(text)
        self.Labelchoice.adjustSize()

    def tabwidget(self):
        self.table_widget = MyTableWidget(self)
        self.table_widget.resize(880,450)
        self.table_widget.move(10,200)
    
        #tabs.addTab(tab3,'WordCloud')
        #tabs.addTab(tab4,'Bar Chart')
      
class MyTableWidget(QWidget):        

    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen                
        self.tabs = QTabWidget()
        self.tab1 = QWidget()	
        self.tab2 = QWidget()
        self.tab3 = QWidget()	
        self.tab4 = QWidget()                
        self.tabs.resize(300,200)       
        # Add tabs
        self.tabs.addTab(self.tab1,"Tab 1")
        self.tabs.addTab(self.tab2,"Tab 2")
        self.tabs.addTab(self.tab3,"Tab 3")
        self.tabs.addTab(self.tab4,"Tab 4")
        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)
        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
    
if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())