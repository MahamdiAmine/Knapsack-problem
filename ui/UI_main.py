import numpy as np
import time

from Ui_Dialog import Ui_Dialog as Form
from object import Object
from knapsac_problem import Knapsac as K
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
import os


try:
     _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
      _fromUtf8 = lambda s: s

class Ui_MainWindow(object):


    def __init__(self):
        self.items=[]
        self.maxWeight=0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 549)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(50,180,161,41))
        self.maxWeightButton = QtWidgets.QPushButton(self.centralwidget)
        self.maxWeightButton.setGeometry(QtCore.QRect(50, 250,215,41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        self.submitButton.setObjectName("submitButton")
        self.maxWeightButton.setSizePolicy(sizePolicy)
        self.maxWeightButton.setObjectName("maxWeightButton")
        self.maxWeightLabel=QtWidgets.QLabel(self.centralwidget)
        self.maxWeightLabel.setGeometry(QtCore.QRect(300,250,161,41))
        self.maxWeightLabel.setText("0")
        self.maxWeightLabel.hide()
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(650, 450, 98, 31))
        self.exitButton.setObjectName("exitButton")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(290, 330, 161, 61))
        self.calculateButton.setObjectName("calculateButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(47, 150, 671, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 10, 151, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./knap.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(630, 360, 61, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.hide()
        self.copyright = QtWidgets.QLabel(self.centralwidget)
        self.copyright.setGeometry(QtCore.QRect(160, 480, 411, 31))
        self.copyright.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.copyright.setOpenExternalLinks(True)
        self.copyright.setObjectName("copyright")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 591, 71))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 310, 671, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.maxValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.maxValueLabel.setGeometry(QtCore.QRect(530, 350, 91, 51))
        self.maxValueLabel.setObjectName("maxValueLabel")
        self.maxValueLabel.hide()
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 70, 421, 81))
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(210, 410, 391, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 25))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        self.menuContact_Me = QtWidgets.QMenu(self.menubar)
        self.menuContact_Me.setObjectName("menuContact_Me")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCheck_for_updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_updates.setObjectName("actionCheck_for_updates")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionCheck_for_updates)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuContact_Me.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupTable(self,items):
        def __init__(self, parent=None):
            super().__init__(parent)
        self.items.clear()
        rowCount = 30
        columnCount = 4
        self.table = QTableWidget()
        self.table.resize(500,400)
        self.table.setWindowTitle("Please submit objects proprieties ")
        self.table.setColumnCount(columnCount)
        self.table.setRowCount(rowCount)
        self.table.setHorizontalHeaderLabels(['Object Id', 'Weight', 'Value','Confirm' ])
        self.table.verticalHeader().hide()
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        allRows = self.table.rowCount()
        for row in range(0, allRows):
            item = QTableWidgetItem()
            item.setText(str(row))
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table.setItem(row, 0, item)
        for i in range(self.table.rowCount()):
            ch = QtWidgets.QCheckBox(parent=self.table)
            ch.clicked.connect(lambda checked, row=i, col=3: self.onStateChanged(checked, row, col))
            self.table.setCellWidget(i, 3, ch)
        self.table.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.submitButton.setText(_translate("MainWindow", "Add Objects"))
        self.submitButton.clicked.connect(self.setupTable)
        self.maxWeightButton.setText(_translate("MainWindow", "Enter the maximumm weight :"))
        self.maxWeightButton.clicked.connect(self.open_dialog)
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))
        self.calculateButton.clicked.connect(self.calculate)
        self.copyright.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/MahamdiAmine/MahamdiAmine.github.io/blob/master/LICENSE.md\"><span style=\" text-decoration: underline; color:#0000ff;\">Copyright © 2018 Mahamdi Mohammed and Adrao Nassim</span></a></p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\"> Resolving the Knapsac problem with Dynamic programation </span></p></body></html>"))
        self.maxValueLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\"> Max value :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">bla bla bla bla bla bla bla bla bla bla bl</span></p><p><span style=\" font-size:10pt;\">a bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla</span></p><p><span style=\" font-size:10pt;\">bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla </span></p></body></html>"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.menuContact_Me.setTitle(_translate("MainWindow", "Contact Me"))
        self.actionCheck_for_updates.setText(_translate("MainWindow", "Check for updates"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def calculate(self):
        self.progressBar.show()
        for i in range(100):
            time.sleep(0.1)
            self.progressBar.setValue(i)
        self.lcdNumber.show()
        self.maxValueLabel.show()
        w = []
        v = []
        for x in range(len(self.items)):
            self.items[x].printObject()
            w.insert(x, int(self.items[x].get_weight()))
            v.insert(x, int(self.items[x].get_value()))
        print(w,v,self.maxWeight)
        matrix=K.knapSack(self.maxWeight, w, v)
        print(np.matrix(matrix))
        print(K.check_items(w, matrix, self.maxWeight))
        self.lcdNumber.setStyleSheet("""QLCDNumber {background-color:green; color: red;}""")
        self.lcdNumber.display(matrix[len(w)][self.maxWeight])

    def open_dialog(self):
        self.maxWeightLabel.setText(str(self.maxWeight))
        self.maxWeightLabel.show()
        dialog = QtWidgets.QDialog()
        dialog.ui = Form()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()
        text=dialog.ui.accept()
        self.maxWeight=text
        self.maxWeightLabel.setText(str(text))
    def onStateChanged(self, checked, row, column):
        if(checked):
            try:
                id = self.table.item(row, 0).text()
                weight = self.table.item(row, 1).text()
                value = self.table.item(row, 2).text()
                index = len(self.items)
                self.items.insert(index, Object(id, weight, value))
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")
                exit(88)
            except Exception :
                print("Oops!  That was no valid number.  Try again...")
                exit(99)

# import ui_rc
