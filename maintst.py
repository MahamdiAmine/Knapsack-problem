from PyQt5 import QtCore, QtWidgets

StyleSheet = '''
QPushButton#BlueButton {
    background-color: #2196f3;
    /* Ограничьте минимальный размер */
    min-width:  96px;
    max-width:  96px;
    min-height: 96px;
    max-height: 96px;
    border-radius: 48px;        /* круглый */
}

QPushButton#BlueButton:hover {
    background-color: #64b5f6;
    color: #fff;
}

QPushButton#BlueButton:pressed {
    background-color: #bbdefb;
}
'''


class Window2(QtWidgets.QDialog):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.setGeometry(750, 100, 300, 300)
        self.parent = parent
        self.setWindowTitle('Window2')
        self.setWindowIcon(self.style().standardIcon(QtWidgets.QStyle.SP_FileDialogInfoView))

        label1 = QtWidgets.QLabel(value)
        self.button = QtWidgets.QPushButton()
        self.button.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ArrowLeft))
        self.button.setIconSize(QtCore.QSize(200, 200))

        layoutV = QtWidgets.QVBoxLayout()
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setStyleSheet('background-color: rgb(0,0,255); color: #fff')
        self.pushButton.setText('Click me!')
        self.pushButton.clicked.connect(self.goMainWindow)
        layoutV.addWidget(self.pushButton)

        layoutH = QtWidgets.QHBoxLayout()
        layoutH.addWidget(label1)
        layoutH.addWidget(self.button)
        layoutV.addLayout(layoutH)
        self.setLayout(layoutV)

    def goMainWindow(self):
        self.parent.show()
        self.close()   


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.setGeometry(400, 100, 300, 300)

        hlay = QtWidgets.QHBoxLayout()
        hlay.addStretch(1)

        vlay = QtWidgets.QVBoxLayout(self)
        vlay.addStretch(1)

        self.btn = QtWidgets.QPushButton("Press me", objectName="BlueButton")
        self.btn.clicked.connect(self.btn_onClick)
        self.btn.installEventFilter(self)
        hlay.addWidget(self.btn)
        hlay.addStretch(1)

        vlay.addLayout(hlay)
        self.lineEdit = QtWidgets.QLineEdit("Type here what you want to transfer for [Window2].")
        vlay.addWidget(self.lineEdit)
        vlay.addStretch(1)
        self.setLayout(vlay)

    def eventFilter(self, obj, event):
        if obj == self.btn and event.type() == QtCore.QEvent.HoverEnter:
            self.onHovered()
        return super(Widget, self).eventFilter(obj, event)

    def onHovered(self):
        #print("hovered")
        self.btn.setText("Ok, \nbutton onHovered")    # <---

    def leaveEvent(self, e):
        self.btn.setText("Press me")                  # <---

    @QtCore.pyqtSlot()
    def btn_onClick(self):
        self.cams = Window2(self.lineEdit.text(), self) 
        self.cams.show()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    app.setStyleSheet(StyleSheet)                     # <---

    w = Widget()
    w.show()
    sys.exit(app.exec_())
