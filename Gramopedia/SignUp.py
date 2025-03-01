from PyQt6 import QtCore, QtGui, QtWidgets
from FetchData import villages_combo
from Password import Ui_Form_Password
from ErrorBox import Ui_Form_Error

class Ui_Form_SignUp(object):

    def openErrorBox(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Form_Error()
        self.ui.setupUi(self.window)
        self.window.show()
    
    def openSetPassword(self, vill,  Form_Login):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_Password()
        self.ui.setupUi(self.window, 'SetNewP', vill,  Form_Login)
        self.window.show()
        
    def clickedSignin(self,  Form_Login, Form_SignUp):
        fname = self.lineEdit_firstName.text().title().strip()
        lname = self.lineEdit_lastName.text().title().strip()
        aadhar = self.lineEdit_aadharNumber.text()
        contact = self.lineEdit_contactNumber.text()
        village = self.comboBox_Villages.currentText().split(', ')[1]
        if len(aadhar)==12 and len(contact)==10 and fname!='' and aadhar.isdigit() and contact.isdigit():
            f = open('signup.txt','w')
            f.write(fname+' '+lname+':'+aadhar+':'+contact+':'+village+':')
            f.close()
            self.openSetPassword(village,  Form_Login)
            Form_SignUp.hide()
        else:
            self.openErrorBox()

        
    def openForm_Login(self,login_w,s):
        login_w.show()
        s.hide()

    def setupUi(self, Form_SignUp,  Form_Login):
        Form_SignUp.setObjectName("Form_SignUp")
        Form_SignUp.resize(600, 480)
        Form_SignUp.setMinimumSize(QtCore.QSize(600, 480))
        Form_SignUp.setMaximumSize(QtCore.QSize(600, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/add-user (2).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_SignUp.setWindowIcon(icon)
        self.label_color = QtWidgets.QLabel(Form_SignUp)
        self.label_color.setGeometry(QtCore.QRect(310, 0, 291, 481))
        self.label_color.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00568182, y1:0.045, x2:1, y2:1, stop:0 rgba(255, 0, 0, 200), stop:0.166 rgba(255, 255, 0, 194), stop:0.333 rgba(0, 255, 0, 196), stop:0.5 rgba(0, 255, 255, 198), stop:0.666 rgba(0, 0, 255, 203), stop:0.833 rgba(255, 0, 255, 201), stop:1 rgba(255, 0, 0, 200));")
        self.label_color.setText("")
        self.label_color.setObjectName("label_color")
        self.label_bgwhite = QtWidgets.QLabel(Form_SignUp)
        self.label_bgwhite.setGeometry(QtCore.QRect(0, 0, 311, 481))
        self.label_bgwhite.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_bgwhite.setText("")
        self.label_bgwhite.setObjectName("label_bgwhite")
        self.graphicsView_homeIcon = QtWidgets.QGraphicsView(Form_SignUp)
        self.graphicsView_homeIcon.setGeometry(QtCore.QRect(330, 110, 250, 250))
        self.graphicsView_homeIcon.setStyleSheet("border-image: url(Icon_pack/home.png);")
        self.graphicsView_homeIcon.setObjectName("graphicsView_homeIcon")
        self.label_gramopedia = QtWidgets.QLabel(Form_SignUp)
        self.label_gramopedia.setGeometry(QtCore.QRect(330, 160, 251, 61))
        self.label_gramopedia.setStyleSheet("font: 90 30pt \"Comic Sans MS\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(0, 174, 255, 255), stop:1 rgba(151, 75, 196, 255));")
        self.label_gramopedia.setObjectName("label_gramopedia")
        self.label_signin = QtWidgets.QLabel(Form_SignUp)
        self.label_signin.setGeometry(QtCore.QRect(100, 50, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_signin.setFont(font)
        self.label_signin.setStyleSheet("color:rgba(0, 0, 0, 200)")
        self.label_signin.setObjectName("label_signin")
        self.lineEdit_firstName = QtWidgets.QLineEdit(Form_SignUp)
        self.lineEdit_firstName.setGeometry(QtCore.QRect(30, 120, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_firstName.setFont(font)
        self.lineEdit_firstName.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_firstName.setMaxLength(15)
        self.lineEdit_firstName.setObjectName("lineEdit_firstName")
        self.lineEdit_lastName = QtWidgets.QLineEdit(Form_SignUp)
        self.lineEdit_lastName.setGeometry(QtCore.QRect(150, 120, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_lastName.setFont(font)
        self.lineEdit_lastName.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_lastName.setMaxLength(15)
        self.lineEdit_lastName.setObjectName("lineEdit_lastName")
        self.lineEdit_aadharNumber = QtWidgets.QLineEdit(Form_SignUp)
        self.lineEdit_aadharNumber.setGeometry(QtCore.QRect(30, 180, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_aadharNumber.setFont(font)
        self.lineEdit_aadharNumber.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_aadharNumber.setMaxLength(12)
        self.lineEdit_aadharNumber.setObjectName("lineEdit_aadharNumber")
        self.lineEdit_contactNumber = QtWidgets.QLineEdit(Form_SignUp)
        self.lineEdit_contactNumber.setGeometry(QtCore.QRect(30, 240, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_contactNumber.setFont(font)
        self.lineEdit_contactNumber.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_contactNumber.setMaxLength(10)
        self.lineEdit_contactNumber.setObjectName("lineEdit_contactNumber")
        self.comboBox_Villages = QtWidgets.QComboBox(Form_SignUp)
        self.comboBox_Villages.setGeometry(QtCore.QRect(30, 300, 220, 40))
        self.comboBox_Villages.setStyleSheet("background-color:rgba(255, 255, 255, 240);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.comboBox_Villages.setEditable(False)
        self.comboBox_Villages.setObjectName("comboBox_Villages")
        a=len(villages_combo())
        for i in range(a):
            self.comboBox_Villages.addItem("")
        self.pushButton_signin = QtWidgets.QPushButton(Form_SignUp, clicked = lambda: self.clickedSignin(Form_Login, Form_SignUp))
        self.pushButton_signin.setGeometry(QtCore.QRect(30, 360, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_signin.setFont(font)
        self.pushButton_signin.setStyleSheet("QPushButton#pushButton_signin{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_signin:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton_signin:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.pushButton_signin.setObjectName("pushButton_signin")
        self.label_AlreadyAnExistingUser = QtWidgets.QLabel(Form_SignUp)
        self.label_AlreadyAnExistingUser.setGeometry(QtCore.QRect(30, 410, 220, 16))
        self.label_AlreadyAnExistingUser.setStyleSheet("color:rgba(0, 0, 0, 210);\n"
"color: rgb(5, 159, 255);")
        self.label_AlreadyAnExistingUser.setObjectName("label_AlreadyAnExistingUser")
        self.pushButton_login = QtWidgets.QPushButton(Form_SignUp, clicked = lambda: self.openForm_Login(Form_Login,Form_SignUp))
        self.pushButton_login.setGeometry(QtCore.QRect(95, 435, 75, 23))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("QPushButton#pushButton_login{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_login:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"QPushButton#pushButton_login:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"")
        self.pushButton_login.setObjectName("pushButton_login")

        self.retranslateUi(Form_SignUp)
        self.lineEdit_firstName.editingFinished.connect(self.lineEdit_lastName.setFocus)
        self.lineEdit_lastName.editingFinished.connect(self.lineEdit_aadharNumber.setFocus)
        self.lineEdit_aadharNumber.editingFinished.connect(self.lineEdit_contactNumber.setFocus)
        self.lineEdit_contactNumber.editingFinished.connect(self.comboBox_Villages.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Form_SignUp)

    def retranslateUi(self, Form_SignUp):
        _translate = QtCore.QCoreApplication.translate
        Form_SignUp.setWindowTitle(_translate("Form_SignUp", "Sign Up"))
        self.label_gramopedia.setText(_translate("Form_SignUp", "GramO\'pedia"))
        self.label_signin.setText(_translate("Form_SignUp", "Sign Up"))
        self.lineEdit_firstName.setPlaceholderText(_translate("Form_SignUp", "First Name"))
        self.lineEdit_lastName.setPlaceholderText(_translate("Form_SignUp", "Last Name"))
        self.lineEdit_aadharNumber.setPlaceholderText(_translate("Form_SignUp", "Aadhar Number"))
        self.lineEdit_contactNumber.setPlaceholderText(_translate("Form_SignUp", "Contact Number"))
        self.comboBox_Villages.setCurrentText(_translate("Form_SignUp", "Village"))
        a=villages_combo()
        for i in range(len(a)):
            self.comboBox_Villages.setItemText(i, _translate("Form_SignUp", a[i]))
        self.pushButton_signin.setText(_translate("Form_SignUp", "S i g n   U p"))
        self.label_AlreadyAnExistingUser.setText(_translate("Form_SignUp", "            Already an existing user?"))
        self.pushButton_login.setText(_translate("Form_SignUp", "L o g   I n"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_SignUp = QtWidgets.QWidget()
    ui = Ui_Form_SignUp()
    ui.setupUi(Form_SignUp)
    Form_SignUp.show()
    sys.exit(app.exec())
