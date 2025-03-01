from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Error(object):
    def setupUi(self, Form_Error, message):
        Form_Error.setObjectName("Form_Error")
        Form_Error.resize(320, 220)
        Form_Error.setMinimumSize(QtCore.QSize(320, 220))
        Form_Error.setMaximumSize(QtCore.QSize(320, 220))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/question.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_Error.setWindowIcon(icon)
        self.label_bg2 = QtWidgets.QLabel(Form_Error)
        self.label_bg2.setGeometry(QtCore.QRect(0, 0, 320, 220))
        self.label_bg2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00568182, y1:0.045, x2:1, y2:1, stop:0 rgba(255, 0, 0, 200), stop:0.166 rgba(255, 255, 0, 194), stop:0.333 rgba(0, 255, 0, 196), stop:0.5 rgba(0, 255, 255, 198), stop:0.666 rgba(0, 0, 255, 203), stop:0.833 rgba(255, 0, 255, 201), stop:1 rgba(255, 0, 0, 200));")
        self.label_bg2.setText("")
        self.label_bg2.setObjectName("label_bg2")
        self.label_bg = QtWidgets.QLabel(Form_Error)
        self.label_bg.setGeometry(QtCore.QRect(5, 5, 310, 210))
        self.label_bg.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_bg.setText("")
        self.label_bg.setObjectName("label_bg")
        self.pushButton_ok = QtWidgets.QPushButton(Form_Error)
        self.pushButton_ok.setGeometry(QtCore.QRect(200, 160, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ok.setFont(font)
        self.pushButton_ok.setStyleSheet("QPushButton#pushButton_ok{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_ok:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton_ok:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.label_Message = QtWidgets.QLabel(Form_Error)
        self.label_Message.setGeometry(QtCore.QRect(74, 70, 211, 50))
        self.label_Message.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.label_Message.setObjectName("label_Message")
        self.graphicsView_errorLogo = QtWidgets.QGraphicsView(Form_Error)
        self.graphicsView_errorLogo.setGeometry(QtCore.QRect(20, 70, 50, 50))
        self.graphicsView_errorLogo.setStyleSheet("border-image: url(Icon_pack/loading.png);")
        self.graphicsView_errorLogo.setObjectName("graphicsView_errorLogo")

        self.retranslateUi(Form_Error, message)
        self.pushButton_ok.clicked.connect(Form_Error.close)
        QtCore.QMetaObject.connectSlotsByName(Form_Error)

    def retranslateUi(self, Form_Error, message):
        _translate = QtCore.QCoreApplication.translate
        Form_Error.setWindowTitle(_translate("Form_Error", "Error"))
        self.pushButton_ok.setText(_translate("Form_Error", "O K"))
        self.pushButton_ok.setShortcut(_translate("Form_Error", "Return"))
        self.label_Message.setText(_translate("Form_Error", message))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Error = QtWidgets.QDialog()
    ui = Ui_Form_Error()
    ui.setupUi(Form_Error)
    Form_Error.show()
    sys.exit(app.exec())
