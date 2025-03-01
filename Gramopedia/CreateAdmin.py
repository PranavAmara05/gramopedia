from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Create_admin(object):

    def clickCreate(self, Form_Create_admin):
        fname = self.lineEdit_firstName.text().title().strip()
        lname = self.lineEdit_lastName.text().title().strip()
        desig = self.lineEdit_Designation.text().upper().strip()
        ud = self.lineEdit_uniqueId.text().upper().strip()
        sp =  self.lineEdit_SetPassword.text()
        cp = self.lineEdit_Confirm_password.text()
        
        import mysql.connector as ms
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        cur = m.cursor()
        cur.execute('select unique_id from admins;')
        ua = list()
        for i in cur.fetchall():
            ua.append(i[0])                
        if (fname and lname and desig and ud and ud not in ua and ud[:3].isalpha() and ud[3:].isdigit()
            and sp and cp and sp==cp):
            cur.execute('''insert into admins values ('{}','{}','{}','{}');'''.format(fname+' '+lname,ud,sp,desig))
            m.commit()
            Form_Create_admin.close()            
        m.close()
        
    def setupUi(self, Form_Create_admin):
        Form_Create_admin.setObjectName("Form_Create_admin")
        Form_Create_admin.resize(400, 520)
        Form_Create_admin.setMinimumSize(QtCore.QSize(400, 520))
        Form_Create_admin.setMaximumSize(QtCore.QSize(400, 520))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/add-user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_Create_admin.setWindowIcon(icon)
        Form_Create_admin.setStyleSheet("")
        self.label_bg = QtWidgets.QLabel(Form_Create_admin)
        self.label_bg.setGeometry(QtCore.QRect(0, 0, 400, 521))
        self.label_bg.setStyleSheet("border-image: url(Icon_pack/Gramopedia_logo.jpg);")
        self.label_bg.setText("")
        self.label_bg.setObjectName("label_bg")
        self.label_Create_admin = QtWidgets.QLabel(Form_Create_admin)
        self.label_Create_admin.setGeometry(QtCore.QRect(100, 20, 200, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Create_admin.setFont(font)
        self.label_Create_admin.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_Create_admin.setObjectName("label_Create_admin")
        self.lineEdit_firstName = QtWidgets.QLineEdit(Form_Create_admin)
        self.lineEdit_firstName.setGeometry(QtCore.QRect(60, 110, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_firstName.setFont(font)
        self.lineEdit_firstName.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_firstName.setMaxLength(15)
        self.lineEdit_firstName.setObjectName("lineEdit_firstName")
        self.lineEdit_lastName = QtWidgets.QLineEdit(Form_Create_admin)
        self.lineEdit_lastName.setGeometry(QtCore.QRect(220, 110, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_lastName.setFont(font)
        self.lineEdit_lastName.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_lastName.setMaxLength(15)
        self.lineEdit_lastName.setObjectName("lineEdit_lastName")
        self.lineEdit_uniqueId = QtWidgets.QLineEdit(Form_Create_admin)
        self.lineEdit_uniqueId.setGeometry(QtCore.QRect(60, 230, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_uniqueId.setFont(font)
        self.lineEdit_uniqueId.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_uniqueId.setMaxLength(6)
        self.lineEdit_uniqueId.setObjectName("lineEdit_uniqueId")
        self.lineEdit_Designation = QtWidgets.QLineEdit(Form_Create_admin)
        self.lineEdit_Designation.setGeometry(QtCore.QRect(60, 170, 280, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Designation.setFont(font)
        self.lineEdit_Designation.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_Designation.setMaxLength(20)
        self.lineEdit_Designation.setObjectName("lineEdit_Designation")
        self.lineEdit_Confirm_password = QtWidgets.QLineEdit(Form_Create_admin)
        self.lineEdit_Confirm_password.setGeometry(QtCore.QRect(220, 290, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_Confirm_password.setFont(font)
        self.lineEdit_Confirm_password.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_Confirm_password.setMaxLength(20)
        self.lineEdit_Confirm_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_Confirm_password.setObjectName("lineEdit_Confirm_password")
        self.lineEdit_SetPassword = QtWidgets.QLineEdit(Form_Create_admin)
        self.lineEdit_SetPassword.setGeometry(QtCore.QRect(60, 290, 120, 40))
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
        self.pushButton = QtWidgets.QPushButton(Form_Create_admin, clicked = lambda: self.clickCreate(Form_Create_admin))
        self.pushButton.setGeometry(QtCore.QRect(100, 350, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form_Create_admin)
        self.lineEdit_firstName.editingFinished.connect(self.lineEdit_lastName.setFocus)
        self.lineEdit_lastName.editingFinished.connect(self.lineEdit_Designation.setFocus)
        self.lineEdit_Designation.editingFinished.connect(self.lineEdit_uniqueId.setFocus)
        self.lineEdit_uniqueId.editingFinished.connect(self.lineEdit_SetPassword.setFocus)
        self.lineEdit_SetPassword.editingFinished.connect(self.lineEdit_Confirm_password.setFocus)
        self.lineEdit_Confirm_password.editingFinished.connect(self.pushButton.animateClick)
        QtCore.QMetaObject.connectSlotsByName(Form_Create_admin)

    def retranslateUi(self, Form_Create_admin):
        _translate = QtCore.QCoreApplication.translate
        Form_Create_admin.setWindowTitle(_translate("Form_Create_admin", "Create Admin  "))
        self.label_Create_admin.setText(_translate("Form_Create_admin", "  Create Admin"))
        self.lineEdit_firstName.setPlaceholderText(_translate("Form_Create_admin", "First Name"))
        self.lineEdit_lastName.setPlaceholderText(_translate("Form_Create_admin", "Last Name"))
        self.lineEdit_uniqueId.setPlaceholderText(_translate("Form_Create_admin", "Unique Id "))
        self.lineEdit_Designation.setPlaceholderText(_translate("Form_Create_admin", "Designation"))
        self.lineEdit_Confirm_password.setPlaceholderText(_translate("Form_Create_admin", "Confirm Password "))
        self.lineEdit_SetPassword.setPlaceholderText(_translate("Form_Create_admin", "Set Password"))
        self.pushButton.setText(_translate("Form_Create_admin", "C r e a t e"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Create_admin = QtWidgets.QWidget()
    ui = Ui_Form_Create_admin()
    ui.setupUi(Form_Create_admin)
    Form_Create_admin.show()
    sys.exit(app.exec())
