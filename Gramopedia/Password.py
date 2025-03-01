from PyQt6 import QtCore, QtGui, QtWidgets
from ErrorBox import Ui_Form_Error
from GenUid import Ui_Form_GenUid
import mysql.connector as ms

class Ui_Form_Password(object):

    def openErrorBox(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Form_Error()
        self.ui.setupUi(self.window, 'Invalid Passwords!!!!!')
        self.window.show()

    def opengpuid(self, vill,  Form_Login):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_GenUid()
        self.ui.setupUi(self.window, vill,  Form_Login)
        self.window.show()
    
    def clickedS(self, vill,  Form_Login, Form_Password):
        a = self.lineEdit_SetPassword.text()
        b = self.lineEdit_ConfirmPassword.text()
        if a!=b or a=='':
            self.openErrorBox()
        else:
            f = open('signup.txt','a+')
            f.write(a+':')
            f.close()
            self.opengpuid(vill,  Form_Login)
            Form_Password.hide()

    def clickedC(self, Form_Password, uid):
        a = self.lineEdit_SetPassword.text()
        b = self.lineEdit_ConfirmPassword.text()
        if a!=b or a=='':
            self.openErrorBox()
        else:
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            c = m.cursor()
            c.execute('select unique_id from admins')
            jkl = []
            for i in c.fetchall():
                jkl.append(i[0])
            if uid not in jkl:
                c.execute('''update users set password = '{}' where unique_id = '{}';'''.format(a,uid))
            else:
                c.execute('''update admins set password = '{}' where unique_id = '{}';'''.format(a,uid))
            m.commit()
            m.close()
            Form_Password.hide()
        
    def setupUi(self, Form_Password, mode, gpass, Form_Login = ''):
        Form_Password.setObjectName("Form_Password")
        Form_Password.resize(300, 350)
        Form_Password.setMinimumSize(QtCore.QSize(300, 350))
        Form_Password.setMaximumSize(QtCore.QSize(300, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/key.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_Password.setWindowIcon(icon)
        self.label_bg = QtWidgets.QLabel(Form_Password)
        self.label_bg.setGeometry(QtCore.QRect(0, 0, 300, 350))
        self.label_bg.setStyleSheet("border-image: url(Icon_pack/Gramopedia_logo.jpg);")
        self.label_bg.setText("")
        self.label_bg.setObjectName("label_bg")
        self.lineEdit_SetPassword = QtWidgets.QLineEdit(Form_Password)
        self.lineEdit_SetPassword.setGeometry(QtCore.QRect(30, 100, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_SetPassword.setFont(font)
        self.lineEdit_SetPassword.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_SetPassword.setMaxLength(20)
        self.lineEdit_SetPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_SetPassword.setObjectName("lineEdit_SetPassword")
        self.lineEdit_ConfirmPassword = QtWidgets.QLineEdit(Form_Password)
        self.lineEdit_ConfirmPassword.setGeometry(QtCore.QRect(30, 180, 230, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_ConfirmPassword.setFont(font)
        self.lineEdit_ConfirmPassword.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_ConfirmPassword.setMaxLength(20)
        self.lineEdit_ConfirmPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_ConfirmPassword.setObjectName("lineEdit_ConfirmPassword")
        self.label_setnewpasssword = QtWidgets.QLabel(Form_Password)
        self.label_setnewpasssword.setGeometry(QtCore.QRect(50, 10, 250, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_setnewpasssword.setFont(font)
        self.label_setnewpasssword.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_setnewpasssword.setObjectName("label_setnewpasssword")
        if mode == 'ChangeP':
            self.pushButton_Done = QtWidgets.QPushButton(Form_Password, clicked = lambda: self.clickedC(Form_Password, gpass))
        elif mode == 'SetNewP':
            self.pushButton_Done = QtWidgets.QPushButton(Form_Password, clicked = lambda: self.clickedS(gpass,  Form_Login, Form_Password))
        self.pushButton_Done.setGeometry(QtCore.QRect(55, 260, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Done.setFont(font)
        self.pushButton_Done.setStyleSheet("QPushButton#pushButton_Done{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_Done:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton_Done:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.pushButton_Done.setObjectName("pushButton_Done")

        self.retranslateUi(Form_Password, mode)
        self.lineEdit_SetPassword.editingFinished.connect(self.lineEdit_ConfirmPassword.setFocus)
        self.lineEdit_ConfirmPassword.editingFinished.connect(self.pushButton_Done.animateClick)
        QtCore.QMetaObject.connectSlotsByName(Form_Password)

    def retranslateUi(self, Form_Password, mode):
        _translate = QtCore.QCoreApplication.translate
        Form_Password.setWindowTitle(_translate("Form_Password", "Password"))
        if mode == 'ChangeP':
            self.lineEdit_SetPassword.setPlaceholderText(_translate("Form_Password", "Set New Password"))
            self.lineEdit_ConfirmPassword.setPlaceholderText(_translate("Form_Password", "Confirm New Password "))
            self.label_setnewpasssword.setText(_translate("Form_Password", "Change Password"))
        elif mode == 'SetNewP':
            self.lineEdit_SetPassword.setPlaceholderText(_translate("Form_Password", "Set Password"))
            self.lineEdit_ConfirmPassword.setPlaceholderText(_translate("Form_Password", "Confirm Password "))
            self.label_setnewpasssword.setText(_translate("Form_Password", "Set Password"))
        self.pushButton_Done.setText(_translate("Form_Password", "D o n e"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Password = QtWidgets.QWidget()
    ui = Ui_Form_Password()
    ui.setupUi(Form_Password, 'a', 'b')
    Form_Password.show()
    sys.exit(app.exec())
