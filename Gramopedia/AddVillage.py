from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Add_Village(object):

    def clickDone(self, Form_Add_Village):
        import mysql.connector as ms
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        cur = m.cursor()
        cur.execute('select v_code from villages;')
        jkl=[]
        for i in cur.fetchall():
            jkl.append(i[0])
        vc = self.lineEdit_vCode.text().upper().strip()
        vn = self.lineEdit_vName.text().title().strip()
        ds = self.lineEdit_district.text().title().strip()
        bl = self.lineEdit_block.text().title().strip()
        st = self.lineEdit_state.text().title().strip()
        pn = self.lineEdit_pin.text().strip()
        alt = self.lineEdit_alt.text().strip()
        if vc and vn and ds and bl and st and pn and alt and (alt+pn).isdigit() and len(pn)==6:
            if vc not in jkl and len(vc)==3 and vc.isalpha():
                cur.execute('''insert into villages values ('{}','{}','{}','{}','{}',{},{});'''.format(vc,vn,bl,ds,st,alt,pn))
                cur.execute('''insert into users values ('{}','{}','gp','{}');'''.format(vc+'Sarpanch',vc+'000',vc))
                m.commit()
                m.close()
                Form_Add_Village.close()
            else:
                self.lineEdit_vCode.clear()
        else:
            self.lineEdit_vCode.clear()
            self.lineEdit_vName.clear()
            self.lineEdit_district.clear()
            self.lineEdit_block.clear()
            self.lineEdit_state.clear()
            self.lineEdit_pin.clear()
            self.lineEdit_alt.clear()
        
    def setupUi(self, Form_Add_Village):
        Form_Add_Village.setObjectName("Form_Add_Village")
        Form_Add_Village.resize(520, 400)
        Form_Add_Village.setMinimumSize(QtCore.QSize(520, 400))
        Form_Add_Village.setMaximumSize(QtCore.QSize(520, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_Add_Village.setWindowIcon(icon)
        self.label_image = QtWidgets.QLabel(Form_Add_Village)
        self.label_image.setGeometry(QtCore.QRect(10, 10, 500, 380))
        self.label_image.setStyleSheet("border-image: url(Icon_pack/IMG-20220612-WA0020.jpg);")
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.label_addVillage = QtWidgets.QLabel(Form_Add_Village)
        self.label_addVillage.setGeometry(QtCore.QRect(170, 20, 200, 61))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_addVillage.setFont(font)
        self.label_addVillage.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));\n"
"color: rgb(255, 255, 255);")
        self.label_addVillage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_addVillage.setObjectName("label_addVillage")
        self.lineEdit_vCode = QtWidgets.QLineEdit(Form_Add_Village)
        self.lineEdit_vCode.setGeometry(QtCore.QRect(100, 300, 140, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lineEdit_vCode.setFont(font)
        self.lineEdit_vCode.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_vCode.setMaxLength(3)
        self.lineEdit_vCode.setObjectName("lineEdit_vCode")
        self.lineEdit_vName = QtWidgets.QLineEdit(Form_Add_Village)
        self.lineEdit_vName.setGeometry(QtCore.QRect(40, 120, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lineEdit_vName.setFont(font)
        self.lineEdit_vName.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_vName.setMaxLength(20)
        self.lineEdit_vName.setFrame(False)
        self.lineEdit_vName.setObjectName("lineEdit_vName")
        self.lineEdit_district = QtWidgets.QLineEdit(Form_Add_Village)
        self.lineEdit_district.setGeometry(QtCore.QRect(60, 180, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lineEdit_district.setFont(font)
        self.lineEdit_district.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_district.setMaxLength(20)
        self.lineEdit_district.setObjectName("lineEdit_district")
        self.lineEdit_block = QtWidgets.QLineEdit(Form_Add_Village)
        self.lineEdit_block.setGeometry(QtCore.QRect(280, 120, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lineEdit_block.setFont(font)
        self.lineEdit_block.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_block.setMaxLength(20)
        self.lineEdit_block.setObjectName("lineEdit_block")
        self.lineEdit_state = QtWidgets.QLineEdit(Form_Add_Village)
        self.lineEdit_state.setGeometry(QtCore.QRect(280, 180, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lineEdit_state.setFont(font)
        self.lineEdit_state.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_state.setMaxLength(30)
        self.lineEdit_state.setObjectName("lineEdit_state")
        self.lineEdit_pin = QtWidgets.QLineEdit(Form_Add_Village)
        self.lineEdit_pin.setGeometry(QtCore.QRect(80, 240, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lineEdit_pin.setFont(font)
        self.lineEdit_pin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_pin.setMaxLength(6)
        self.lineEdit_pin.setObjectName("lineEdit_pin")
        self.lineEdit_alt = QtWidgets.QLineEdit(Form_Add_Village)
        self.lineEdit_alt.setGeometry(QtCore.QRect(280, 240, 160, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        self.lineEdit_alt.setFont(font)
        self.lineEdit_alt.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(255, 255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_alt.setMaxLength(4)
        self.lineEdit_alt.setObjectName("lineEdit_alt")
        self.pushButton_Done = QtWidgets.QPushButton(Form_Add_Village, clicked = lambda: self.clickDone(Form_Add_Village))
        self.pushButton_Done.setGeometry(QtCore.QRect(280, 300, 140, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Done.setFont(font)
        self.pushButton_Done.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 119), stop:1 rgba(85, 98, 112, 126));\n"
"    color:rgba(255, 255, 255, 240);\n"
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
        self.pushButton_Done.setObjectName("pushButton_Done")

        self.retranslateUi(Form_Add_Village)
        self.lineEdit_vName.editingFinished.connect(self.lineEdit_block.setFocus)
        self.lineEdit_block.editingFinished.connect(self.lineEdit_district.setFocus)
        self.lineEdit_district.editingFinished.connect(self.lineEdit_state.setFocus)
        self.lineEdit_state.editingFinished.connect(self.lineEdit_pin.setFocus)
        self.lineEdit_pin.editingFinished.connect(self.lineEdit_alt.setFocus)
        self.lineEdit_alt.editingFinished.connect(self.lineEdit_vCode.setFocus)
        self.lineEdit_vCode.editingFinished.connect(self.pushButton_Done.animateClick)
        QtCore.QMetaObject.connectSlotsByName(Form_Add_Village)
        
        self.lineEdit_vCode.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.lineEdit_vName.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.lineEdit_district.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        self.lineEdit_pin.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

    def retranslateUi(self, Form_Add_Village):
        _translate = QtCore.QCoreApplication.translate
        Form_Add_Village.setWindowTitle(_translate("Form_Add_Village", "Add Village"))
        self.label_addVillage.setText(_translate("Form_Add_Village", "Add A Village"))
        self.lineEdit_vCode.setPlaceholderText(_translate("Form_Add_Village", "Village Code"))
        self.lineEdit_vName.setPlaceholderText(_translate("Form_Add_Village", "Village Name"))
        self.lineEdit_district.setPlaceholderText(_translate("Form_Add_Village", "District"))
        self.lineEdit_block.setPlaceholderText(_translate("Form_Add_Village", "Block"))
        self.lineEdit_state.setPlaceholderText(_translate("Form_Add_Village", "State"))
        self.lineEdit_pin.setPlaceholderText(_translate("Form_Add_Village", "PIN Code"))
        self.lineEdit_alt.setPlaceholderText(_translate("Form_Add_Village", "Altitude (metres)"))
        self.pushButton_Done.setText(_translate("Form_Add_Village", "D o n e"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Add_Village = QtWidgets.QWidget()
    ui = Ui_Form_Add_Village()
    ui.setupUi(Form_Add_Village)
    Form_Add_Village.show()
    sys.exit(app.exec())
