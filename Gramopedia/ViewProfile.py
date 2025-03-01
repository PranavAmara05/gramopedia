from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_View_Profile(object):
    def clickDel(self, data, Form_View_Profile):
        import mysql.connector as ms
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        cur = m.cursor()
        cur.execute('''delete from people where unique_id = '{}' and name = '{}';'''.format(data[1],data[0]))
        m.commit()
        m.close()
        Form_View_Profile.close()
        
    def setupUi(self, Form_View_Profile, data):
        Form_View_Profile.setObjectName("Form_View_Profile")
        Form_View_Profile.resize(560, 400)
        Form_View_Profile.setMinimumSize(QtCore.QSize(560, 400))
        Form_View_Profile.setMaximumSize(QtCore.QSize(560, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/user (2).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_View_Profile.setWindowIcon(icon)
        self.label_bgcolor = QtWidgets.QLabel(Form_View_Profile)
        self.label_bgcolor.setGeometry(QtCore.QRect(0, 0, 560, 400))
        self.label_bgcolor.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 88), stop:0.539773 rgba(140, 50, 255, 50), stop:0.920455 rgba(230, 0, 214, 30));")
        self.label_bgcolor.setText("")
        self.label_bgcolor.setObjectName("label_bgcolor")
        self.label_image = QtWidgets.QLabel(Form_View_Profile)
        self.label_image.setGeometry(QtCore.QRect(10, 10, 540, 380))
        self.label_image.setStyleSheet("border-image: url(Icon_pack/IMG-20220612-WA0022.jpg);\n"
"")
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.label_name = QtWidgets.QLabel(Form_View_Profile)
        self.label_name.setGeometry(QtCore.QRect(10, 80, 540, 40))
        self.label_name.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.label_edu = QtWidgets.QLabel(Form_View_Profile)
        self.label_edu.setGeometry(QtCore.QRect(300, 130, 250, 40))
        self.label_edu.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_edu.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_edu.setObjectName("label_edu")
        self.label_marr = QtWidgets.QLabel(Form_View_Profile)
        self.label_marr.setGeometry(QtCore.QRect(300, 230, 250, 40))
        self.label_marr.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_marr.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_marr.setObjectName("label_marr")
        self.label_dob = QtWidgets.QLabel(Form_View_Profile)
        self.label_dob.setGeometry(QtCore.QRect(10, 180, 250, 40))
        self.label_dob.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_dob.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_dob.setObjectName("label_dob")
        self.label_contact = QtWidgets.QLabel(Form_View_Profile)
        self.label_contact.setGeometry(QtCore.QRect(10, 280, 250, 40))
        self.label_contact.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_contact.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_contact.setObjectName("label_contact")
        self.label_occ = QtWidgets.QLabel(Form_View_Profile)
        self.label_occ.setGeometry(QtCore.QRect(300, 180, 250, 40))
        self.label_occ.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_occ.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_occ.setObjectName("label_occ")
        self.label_lang = QtWidgets.QLabel(Form_View_Profile)
        self.label_lang.setGeometry(QtCore.QRect(300, 280, 250, 40))
        self.label_lang.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_lang.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_lang.setObjectName("label_lang")
        self.label_sex = QtWidgets.QLabel(Form_View_Profile)
        self.label_sex.setGeometry(QtCore.QRect(10, 130, 250, 40))
        self.label_sex.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_sex.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_sex.setObjectName("label_sex")
        self.label_aadhar = QtWidgets.QLabel(Form_View_Profile)
        self.label_aadhar.setGeometry(QtCore.QRect(10, 230, 250, 40))
        self.label_aadhar.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_aadhar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_aadhar.setObjectName("label_aadhar")
        self.label_uid = QtWidgets.QLabel(Form_View_Profile)
        self.label_uid.setGeometry(QtCore.QRect(10, 20, 540, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_uid.setFont(font)
        self.label_uid.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 15pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_uid.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_uid.setObjectName("label_uid")
        self.push_del = QtWidgets.QPushButton(Form_View_Profile, clicked = lambda: self.clickDel(data, Form_View_Profile))
        self.push_del.setGeometry(QtCore.QRect(10, 340, 540, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.push_del.setFont(font)
        self.push_del.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 119), stop:1 rgba(85, 98, 112, 126));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 119), stop:1 rgba(85, 81, 84, 126));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 155);\n"
"}")
        self.push_del.setObjectName("push_del")
        self.label_image.raise_()
        self.label_bgcolor.raise_()
        self.label_name.raise_()
        self.label_edu.raise_()
        self.label_marr.raise_()
        self.label_dob.raise_()
        self.label_contact.raise_()
        self.label_occ.raise_()
        self.label_lang.raise_()
        self.label_sex.raise_()
        self.label_aadhar.raise_()
        self.label_uid.raise_()
        self.push_del.raise_()

        self.retranslateUi(Form_View_Profile, data)
        QtCore.QMetaObject.connectSlotsByName(Form_View_Profile)

    def retranslateUi(self, Form_View_Profile, data):
        _translate = QtCore.QCoreApplication.translate
        Form_View_Profile.setWindowTitle(_translate("Form_View_Profile", "View Profile"))
        self.label_name.setText(_translate("Form_View_Profile", data[0]))
        self.label_edu.setText(_translate("Form_View_Profile","Edu: "+data[6]))
        self.label_marr.setText(_translate("Form_View_Profile", data[9]))
        self.label_dob.setText(_translate("Form_View_Profile", "D.O.B: "+str(data[7])))
        self.label_contact.setText(_translate("Form_View_Profile", "Contact: "+data[3]))
        self.label_occ.setText(_translate("Form_View_Profile", data[8]))
        self.label_lang.setText(_translate("Form_View_Profile", data[5]))
        self.label_sex.setText(_translate("Form_View_Profile", data[4]))
        self.label_aadhar.setText(_translate("Form_View_Profile", "Aadhar: "+data[2]))
        self.label_uid.setText(_translate("Form_View_Profile", data[1]))
        self.push_del.setText(_translate("Form_View_Profile", "D e l e t e   P r o f i l e"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_View_Profile = QtWidgets.QWidget()
    ui = Ui_Form_View_Profile()
    ui.setupUi(Form_View_Profile)
    Form_View_Profile.show()
    sys.exit(app.exec())
