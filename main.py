#!/usr/bin/env python3                                    #
# -.- coding: utf-8 -.-                                   #
# Author mahamdi amine                                    #
# Github https://github.com/MahamdiAmine                  #
###########################################################


import sys
import PyQt5
from PyQt5 import QtWidgets
from ui.Ui_main import Ui_MainWindow

class ApplicationWindow(QtWidgets.QMainWindow):
    # Instantiate the app
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()# lunch the application
    application.setFixedSize(772, 549)# with fixed size
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()