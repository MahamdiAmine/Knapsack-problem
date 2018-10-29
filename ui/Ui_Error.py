#!/usr/bin/env python3                                    #
# -.- coding: utf-8 -.-                                   #
# Author mahamdi amine                                    #
# Github https://github.com/MahamdiAmine                  #
###########################################################

from PyQt5 import QtCore, QtWidgets

class Ui_KnapsacError(object):
    def setupUi(self, KnapsacError):
        KnapsacError.setObjectName("Knapsac Error !")
        KnapsacError.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(KnapsacError)
        self.buttonBox.setGeometry(QtCore.QRect(170, 230, 81, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(KnapsacError)
        self.label.setGeometry(QtCore.QRect(30, 100, 321, 141))
        self.label.setObjectName("label")
        self.retranslateUi(KnapsacError)
        self.buttonBox.accepted.connect(KnapsacError.accept)
        QtCore.QMetaObject.connectSlotsByName(KnapsacError)

    def retranslateUi(self, KnapsacError):
        _translate = QtCore.QCoreApplication.translate
        KnapsacError.setWindowTitle(_translate("KnapsacError", "Dialog"))
        self.label.setText(_translate("KnapsacError", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Oops! That was no valid number.</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\"> Try again...</span><br/></p></body></html>"))

