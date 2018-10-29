#!/usr/bin/env python3                                    #
# -.- coding: utf-8 -.-                                   #
# Author mahamdi amine                                    #
# Github https://github.com/MahamdiAmine                  #
###########################################################

import PyQt5
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem, QWidget, QHBoxLayout
from com.knapsac_problem import Knapsac as K
from com.object import Object
from ui.Ui_maxWeight import Ui_Dialog as DialogForm
from ui.Ui_Error import Ui_KnapsacError as ErrorForm

try:
     _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
      _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    # the  main Ui class
    #u can easely inderstand the code , the variable names are representatives

    def __init__(self):
        #init the params
        self.items=[]#items vector
        self.maxWeight=0
        self.rowCount = 60
        self.columnCount = 4
        self.stylesheetTables = "QHeaderView::section{Background-color:#224966; border - radius: 14 px;}"
    def setupUi(self, MainWindow):
        #Setup the Ui
        css='''/*  Author mahamdi amine
                   Github https://github.com/MahamdiAmine */
                   
                    QPushButton:hover {
                            background-color: #161CCB;
                            color: #000000; 
                            qproperty-iconSize: 34px;     
                    }
                   
                   QWidget { 
                        /*background-color: C65528;*/
                        color: rgba(39, 102, 21, 0.88)
                    }
                    
                    QPushButton:pressed {
                        background-color: #bbdefb;
                    }
                    '''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 549)
        MainWindow.setStyleSheet(css)# apply the styleSheet
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
        self.viewSelectedItemsButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewSelectedItemsButton.setGeometry(QtCore.QRect(290, 330, 161, 61))
        self.viewSelectedItemsButton.setObjectName("viewPackedItemsButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(47, 150, 671, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 10, 151, 131))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./img/knap.png"))#Sac icon
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
        self.label_4.setGeometry(QtCore.QRect(50, 70, 450, 81))
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(210, 410, 391, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setupTable(self):
        #setup the table when the user wants the add objects
        def __init__(self, parent=None):
            super().__init__(parent)
        self.items.clear()
        self.table = QTableWidget()
        self.table.setFixedSize(500,400)#fix the size
        self.table.setWindowTitle("Please submit objects proprieties ")
        self.table.setColumnCount(self.columnCount)
        self.table.setRowCount(self.rowCount)
        self.table.setHorizontalHeaderLabels(['Object Id', 'Weight', 'Value','Confirm' ])
        self.table.verticalHeader().hide()#do not need a vertical header
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.table.setStyleSheet(self.stylesheetTables)
        allRows = self.table.rowCount()
        for row in range(0, allRows):
            item = QTableWidgetItem()
            item.setText(str(row))
            item.setTextAlignment(Qt.AlignHCenter)
            item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
            self.table.setItem(row, 0, item)
        for i in range(self.table.rowCount()):
            ch = QtWidgets.QCheckBox(parent=self.table)
            #if the check box state is changed ,onStateChanged method is invoked
            ch.clicked.connect(lambda checked, row=i, col=3: self.onStateChanged(checked, row, col))
            cell_widget = QWidget()
            lay_out = QHBoxLayout(cell_widget)
            lay_out.addWidget(ch)
            lay_out.setAlignment(Qt.AlignCenter)
            lay_out.setContentsMargins(0, 0, 0, 0)
            cell_widget.setLayout(lay_out)
            self.table.setCellWidget(i, 3, cell_widget)
        self.table.show()

    def packedItems(self):
        #Display packed items in a table
        #almoust the same as previous table , just change the check box with a label
        def __init__(self, parent=None):
            super().__init__(parent)
        self.selectedItemsTable = QTableWidget()
        self.selectedItemsTable.setStyleSheet(self.stylesheetTables)#apply the css
        self.selectedItemsTable.setFixedSize(500, 400)
        self.selectedItemsTable.setWindowTitle("Packed Items : ")
        self.selectedItemsTable.setColumnCount(self.columnCount)
        self.selectedItemsTable.setRowCount(self.rowCount)
        self.selectedItemsTable.setHorizontalHeaderLabels(['Object Id', 'Weight', 'Value', 'Packed'])
        self.selectedItemsTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.selectedItemsTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.selectedItemsTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.selectedItemsTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)
        self.selectedItemsTable.verticalHeader().hide()
        if  self.items:
            for i in range(0, len(self.items)):
                item_id = QTableWidgetItem()
                item_w = QTableWidgetItem()
                item_v = QTableWidgetItem()
                item_packed = QTableWidgetItem()
                item_id.setText(str(self.items[i].id))
                item_id.setTextAlignment(Qt.AlignHCenter)
                item_w.setText(str(self.items[i].weight))
                item_w.setTextAlignment(Qt.AlignHCenter)
                item_v.setText(str(self.items[i].value))
                item_v.setTextAlignment(Qt.AlignHCenter)#center the text
                item_id.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item_w.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item_v.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                item_packed.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.selectedItemsTable.setItem(i, 0, item_id)
                self.selectedItemsTable.setItem(i, 1, item_w)
                self.selectedItemsTable.setItem(i, 2, item_v)
                packed = self.items[i].packed
                if packed != 0:
                    item_packed.setText("Packed")
                else:
                    item_packed.setText("Not packed")
                item_packed.setTextAlignment(Qt.AlignHCenter)
                self.selectedItemsTable.setItem(i, 3, item_packed)
        self.selectedItemsTable.show()
        self.viewSelectedItemsButton.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Knapsac problem"))
        self.submitButton.setText(_translate("MainWindow", "Add Objects"))
        self.submitButton.clicked.connect(self.setupTable)
        self.maxWeightButton.setText(_translate("MainWindow", "Enter the maximumm weight :"))
        self.maxWeightButton.clicked.connect(self.open_dialog)
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.exitButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))
        self.calculateButton.clicked.connect(self.calculate)
        self.viewSelectedItemsButton.setText(_translate("MainWindow", "View selected items"))
        self.viewSelectedItemsButton.clicked.connect(self.packedItems)
        self.viewSelectedItemsButton.hide()
        self.copyright.setText(_translate("MainWindow", "<html><head/><body><p><a href="
                                                        "\"https://github.com/MahamdiAmine/MahamdiAmine.github.io/blob/master/LICENSE.md\"><span style=\" text-decoration: underline; color:#0000ff;\">Copyright © 2018 Mahamdi Mohammed and Adrao Nassim</span></a></p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color :red;font-style:italic;\"> Resolving the Knapsac problem with Dynamic programation </span></p></body></html>"))
        self.maxValueLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\"> Max value :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;color :#000000\">    Given a set of items, each with a weight and a value,determine the number of "
                                                       " </span></p><p><span style=\" font-size:10pt;color :#000000\"> each item to include in a collection so that the total weight is less"
                                                      "</span></p><p><span style=\" font-size:10pt;color :#000000\"> than or equal to a given limit and the total value is as large as possible.</span></p></body></html>"))

    def calculate(self):
        #calculate the results and update the progress bar
        self.progressBar.show()
        for i in range(33): #progress bar level =33
            time.sleep(0.01)
            self.progressBar.setValue(i)
        self.lcdNumber.show()
        self.maxValueLabel.show()
        w = []#weights vector
        v = []#values vector
        for x in range(len(self.items)):#
            w.insert(x, self.items[x].weight)
            v.insert(x, self.items[x].value)
        matrix=K.knapSack(self.maxWeight, w, v)
        for i in range(33):#progress bar level =66
            time.sleep(0.01)
            self.progressBar.setValue(i+33)
        selectedItems=K.check_items(w, matrix, self.maxWeight)
        for i in range(35):#progress bar level =66 to 100
            time.sleep(0.01)
            self.progressBar.setValue(i+66)
        self.lcdNumber.setStyleSheet("""QLCDNumber {background-color:green; color: red;}""")
        self.lcdNumber.display(matrix[len(w)][self.maxWeight])#display the maximum value
        for counter in range(len(selectedItems)):#mark packed items as selected
            index=selectedItems[counter]
            self.items[index].set_packed(1)
        self.viewSelectedItemsButton.show()

    def open_dialog(self):
        #open the Frame that asks the user tp enter the max value
        self.maxWeightLabel.setSizePolicy(30,30)
        self.maxWeightLabel.setText(str(self.maxWeight))
        self.maxWeightLabel.setStyleSheet("font: 30pt Comic Sans MS")
        self.maxWeightLabel.show()
        dialog = QtWidgets.QDialog()
        dialog.ui = DialogForm()
        dialog.ui.setupUi(dialog)
        dialog.setFixedSize(415,320)
        dialog.exec_()
        dialog.show()
        text=dialog.ui.accept()
        self.maxWeight=text
        self.maxWeightLabel.setText(str(text))
    def openError(self):
        #open the error caused by invalid number entered by the user
        dialog = QtWidgets.QDialog()
        dialog.ui = ErrorForm()
        dialog.ui.setupUi(dialog)
        dialog.setFixedSize(415,320)
        dialog.exec_()
        dialog.show()

    def onStateChanged(self, checked, row, column):
        #handle the event when the user check the check box
        #by adding the current row as an item
        if checked:
            try:
                id = int(self.table.item(row, 0).text())
                weight =int( self.table.item(row, 1).text())
                value = int(self.table.item(row, 2).text())
                index = len(self.items)
                # TODO check the conditions about the weight and the values
                # if weight < 0 or value < 0 :
                #     print("Weight or value bellow 0 is not allowed")
                #     self.openError()
                self.items.insert(index, Object(id, weight, value))
            except ValueError:
                self.openError()
                exit(1)
            except Exception :
                self.openError()
                exit(2)
