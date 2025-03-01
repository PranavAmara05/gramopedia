from PyQt6 import QtCore, QtGui, QtWidgets
from ErrorBox import Ui_Form_Error
import FetchData

occ = ['Student','Unemployed','Agriculture','House Keeping','Government Sector', 'Public Sector',
       'Private Sector','Sports','Cattle','Farming','Defence','Business','Teacher','Politician']

class Ui_Form_AddMember(object):
    
    def openErrorBox(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Form_Error()
        self.ui.setupUi(self.window, 'Wrong Details!!!!!')
        self.window.show()
        
    def clickDone(self, uid, Form_AddMember):
        fname = self.lineEdit_firstName.text().strip().title()
        lname = self.lineEdit_lastName.text().strip().title()
        aadhar = self.lineEdit_AadharNumber.text()
        contact = self.lineEdit_contactNumber.text()
        occ = self.comboBox_Occupation.currentText()
        date = self.dob.text()
        lang = []; edu = None; sex = None; marr = 'Unmarried/Single'

        if self.checkBox_marr.isChecked() == True:
            marr = 'Married'
             
        if self.radioButton_Female.isChecked() == True:
            sex = 'Female'
        if self.radioButton_Male.isChecked() == True:
            sex = 'Male'
        if self.radioButton_Other.isChecked() == True:
            sex = 'Other'
            
        if self.checkBox_English.isChecked() == True:
            lang.append('English')
        if self.checkBox_Hindi.isChecked() == True:
            lang.append('Hindi')
        if self.checkBox_Regional.isChecked() == True:
            lang.append('Regional')
        if self.checkBox_Other.isChecked() == True:
            lang.append('Other')

        if self.radioButton_0.isChecked() == True:
            edu = '0'
        if self.radioButton_5th.isChecked() == True:
            edu = '5th'
        if self.radioButton_10th.isChecked() == True:
            edu = '10th'
        if self.radioButton_12th.isChecked() == True:
            edu = '12th'
        if self.radioButton_ug.isChecked() == True:
            edu = 'UG'
        if self.radioButton_pg.isChecked() == True:
            edu = 'PG'

        if sex == None or edu == None or len(lang) == 0:
            self.openErrorBox()
        elif occ == 'Choose Your Occupation':
            self.openErrorBox()
        elif len(aadhar)!=12 or len(contact)!=10 or fname=='' or lname=='':
            self.openErrorBox()
        elif aadhar.isdigit() and contact.isdigit():
            FetchData.reg(uid,fname, lname, aadhar, contact, occ, date, lang, edu, sex, marr)
            Form_AddMember.hide()
        else:
            self.openErrorBox()
        
    def setupUi(self, Form_AddMember, uid):
        Form_AddMember.setObjectName("Form_AddMember")
        Form_AddMember.resize(900, 480)
        Form_AddMember.setMinimumSize(QtCore.QSize(900, 480))
        Form_AddMember.setMaximumSize(QtCore.QSize(900, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/add-user (2).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_AddMember.setWindowIcon(icon)
        self.label_bgcolor = QtWidgets.QLabel(Form_AddMember)
        self.label_bgcolor.setGeometry(QtCore.QRect(0, 0, 300, 480))
        self.label_bgcolor.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00568182, y1:0.045, x2:1, y2:1, stop:0 rgba(255, 0, 0, 200), stop:0.166 rgba(255, 255, 0, 194), stop:0.333 rgba(0, 255, 0, 196), stop:0.5 rgba(0, 255, 255, 198), stop:0.666 rgba(0, 0, 255, 203), stop:0.833 rgba(255, 0, 255, 201), stop:1 rgba(255, 0, 0, 200));")
        self.label_bgcolor.setText("")
        self.label_bgcolor.setObjectName("label_bgcolor")
        self.label_bgwhite = QtWidgets.QLabel(Form_AddMember)
        self.label_bgwhite.setGeometry(QtCore.QRect(300, 0, 600, 480))
        self.label_bgwhite.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_bgwhite.setText("")
        self.label_bgwhite.setObjectName("label_bgwhite")
        self.label_registerauser = QtWidgets.QLabel(Form_AddMember)
        self.label_registerauser.setGeometry(QtCore.QRect(500, 50, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_registerauser.setFont(font)
        self.label_registerauser.setStyleSheet("color:rgba(0, 0, 0, 200)")
        self.label_registerauser.setObjectName("label_registerauser")
        self.graphicsView_homeIcon = QtWidgets.QGraphicsView(Form_AddMember)
        self.graphicsView_homeIcon.setGeometry(QtCore.QRect(20, 110, 250, 250))
        self.graphicsView_homeIcon.setStyleSheet("border-image: url(Icon_pack/home.png);")
        self.graphicsView_homeIcon.setObjectName("graphicsView_homeIcon")
        self.label_Gramopedia = QtWidgets.QLabel(Form_AddMember)
        self.label_Gramopedia.setGeometry(QtCore.QRect(30, 160, 251, 61))
        self.label_Gramopedia.setStyleSheet("font: 90 30pt \"Comic Sans MS\";\n"
"color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(0, 174, 255, 255), stop:1 rgba(151, 75, 196, 255));")
        self.label_Gramopedia.setObjectName("label_Gramopedia")
        self.lineEdit_firstName = QtWidgets.QLineEdit(Form_AddMember)
        self.lineEdit_firstName.setGeometry(QtCore.QRect(320, 130, 100, 40))
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
        self.lineEdit_lastName = QtWidgets.QLineEdit(Form_AddMember)
        self.lineEdit_lastName.setGeometry(QtCore.QRect(440, 130, 100, 40))
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
        self.dob = QtWidgets.QDateEdit(Form_AddMember)
        self.dob.setGeometry(QtCore.QRect(360, 340, 180, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dob.setFont(font)
        self.dob.setStyleSheet("background-color:rgba(255 255, 255, 240);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.dob.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.dob.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.dob.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 8, 9), QtCore.QTime(0, 0, 0)))
        self.dob.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dob.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dob.setCalendarPopup(True)
        self.dob.setDate(QtCore.QDate(2022, 1, 1))
        self.dob.setObjectName("dob")

        self.lineEdit_AadharNumber = QtWidgets.QLineEdit(Form_AddMember)
        self.lineEdit_AadharNumber.setGeometry(QtCore.QRect(320, 200, 220, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_AadharNumber.setFont(font)
        self.lineEdit_AadharNumber.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_AadharNumber.setMaxLength(12)
        self.lineEdit_AadharNumber.setObjectName("lineEdit_AadharNumber")
        self.lineEdit_contactNumber = QtWidgets.QLineEdit(Form_AddMember)
        self.lineEdit_contactNumber.setGeometry(QtCore.QRect(320, 270, 220, 40))
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form_AddMember)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(690, 130, 171, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_Sex = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_Sex.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Sex.setObjectName("horizontalLayout_Sex")
        self.radioButton_Female = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_Female.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.radioButton_Female.setObjectName("radioButton_Female")
        self.horizontalLayout_Sex.addWidget(self.radioButton_Female)
        self.radioButton_Male = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_Male.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.radioButton_Male.setObjectName("radioButton_Male")
        self.horizontalLayout_Sex.addWidget(self.radioButton_Male)
        self.radioButton_Other = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_Other.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.radioButton_Other.setObjectName("radioButton_Other")
        self.horizontalLayout_Sex.addWidget(self.radioButton_Other)
        self.label_sex = QtWidgets.QLabel(Form_AddMember)
        self.label_sex.setGeometry(QtCore.QRect(600, 130, 70, 40))
        self.label_sex.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"\n"
"color:rgba(0, 0, 0, 240);\n"
"")
        self.label_sex.setObjectName("label_sex")
        self.label_marr = QtWidgets.QLabel(Form_AddMember)
        self.label_marr.setGeometry(QtCore.QRect(320, 380, 100, 40))
        self.label_marr.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"\n"
"color:rgba(0, 0, 0, 240);\n"
"")
        self.label_marr.setObjectName("label_marr")
        self.checkBox_marr = QtWidgets.QCheckBox(Form_AddMember)
        self.checkBox_marr.setGeometry(QtCore.QRect(420, 380, 60, 40))
        self.checkBox_marr.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"color:rgba(0, 0, 0, 240);")
        self.checkBox_marr.setObjectName("checkBox_marr")
        self.label_languages = QtWidgets.QLabel(Form_AddMember)
        self.label_languages.setGeometry(QtCore.QRect(600, 270, 70, 40))
        self.label_languages.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"\n"
"color:rgba(0, 0, 0, 240);\n"
"")
        self.label_languages.setObjectName("label_languages")
        self.gridLayoutWidget = QtWidgets.QWidget(Form_AddMember)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(690, 280, 171, 52))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_Languages = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_Languages.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Languages.setObjectName("gridLayout_Languages")
        self.checkBox_Other = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Other.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.checkBox_Other.setObjectName("checkBox_Other")
        self.gridLayout_Languages.addWidget(self.checkBox_Other, 2, 1, 1, 1)
        self.checkBox_Regional = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Regional.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;\n"
"")
        self.checkBox_Regional.setObjectName("checkBox_Regional")
        self.gridLayout_Languages.addWidget(self.checkBox_Regional, 2, 0, 1, 1)
        self.checkBox_Hindi = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Hindi.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.checkBox_Hindi.setObjectName("checkBox_Hindi")
        self.gridLayout_Languages.addWidget(self.checkBox_Hindi, 0, 1, 1, 1)
        self.checkBox_English = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_English.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.checkBox_English.setObjectName("checkBox_English")
        self.gridLayout_Languages.addWidget(self.checkBox_English, 0, 0, 1, 1)
        self.label_education = QtWidgets.QLabel(Form_AddMember)
        self.label_education.setGeometry(QtCore.QRect(600, 200, 70, 40))
        self.label_education.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"\n"
"color:rgba(0, 0, 0, 240);\n"
"")
        self.label_education.setObjectName("label_education")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form_AddMember)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(690, 190, 172, 75))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_Education = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_Education.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Education.setObjectName("gridLayout_Education")
        self.radioButton_5th = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_5th.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.radioButton_5th.setObjectName("radioButton_5th")
        self.gridLayout_Education.addWidget(self.radioButton_5th, 0, 1, 1, 1)
        self.radioButton_0 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_0.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.radioButton_0.setObjectName("radioButton_0")
        self.gridLayout_Education.addWidget(self.radioButton_0, 0, 0, 1, 1)
        self.radioButton_10th = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_10th.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.radioButton_10th.setObjectName("radioButton_10th")
        self.gridLayout_Education.addWidget(self.radioButton_10th, 1, 0, 1, 1)
        self.radioButton_12th = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_12th.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.radioButton_12th.setObjectName("radioButton_12th")
        self.gridLayout_Education.addWidget(self.radioButton_12th, 1, 1, 1, 1)
        self.radioButton_ug = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_ug.setObjectName("radioButton_ug")
        self.gridLayout_Education.addWidget(self.radioButton_ug, 2, 0, 1, 1)
        self.radioButton_pg = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_pg.setObjectName("radioButton_pg")
        self.gridLayout_Education.addWidget(self.radioButton_pg, 2, 1, 1, 1)
        self.label_Occupation = QtWidgets.QLabel(Form_AddMember)
        self.label_Occupation.setGeometry(QtCore.QRect(600, 340, 70, 40))
        self.label_Occupation.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"\n"
"color:rgba(0, 0, 0, 240);\n"
"")
        self.label_Occupation.setObjectName("label_Occupation")
        self.comboBox_Occupation = QtWidgets.QComboBox(Form_AddMember)
        self.comboBox_Occupation.setGeometry(QtCore.QRect(690, 340, 170, 40))
        self.comboBox_Occupation.setStyleSheet("background-color:rgba(255, 255, 255, 240);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.comboBox_Occupation.setObjectName("comboBox_Occupation")
        for i in range(len(occ)+1):
            self.comboBox_Occupation.addItem("")
        self.label_DOB = QtWidgets.QLabel(Form_AddMember)
        self.label_DOB.setGeometry(QtCore.QRect(320, 330, 31, 41))
        self.label_DOB.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"\n"
"color:rgba(0, 0, 0, 240);\n"
"")
        self.label_DOB.setObjectName("label_DOB")
        self.pushButton_Done = QtWidgets.QPushButton(Form_AddMember, clicked = lambda: self.clickDone(uid, Form_AddMember))
        self.pushButton_Done.setGeometry(QtCore.QRect(500, 410, 220, 40))
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

        self.retranslateUi(Form_AddMember)
        self.lineEdit_firstName.editingFinished.connect(self.lineEdit_lastName.setFocus)
        self.lineEdit_lastName.editingFinished.connect(self.lineEdit_AadharNumber.setFocus)
        self.lineEdit_AadharNumber.editingFinished.connect(self.lineEdit_contactNumber.setFocus)
        self.lineEdit_contactNumber.editingFinished.connect(self.dob.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Form_AddMember)

    def retranslateUi(self, Form_AddMember):
        _translate = QtCore.QCoreApplication.translate
        Form_AddMember.setWindowTitle(_translate("Form_AddMember", "Add Member"))
        self.label_registerauser.setText(_translate("Form_AddMember", "Add a Member"))
        self.label_Gramopedia.setText(_translate("Form_AddMember", "GramO\'pedia"))
        self.lineEdit_firstName.setPlaceholderText(_translate("Form_AddMember", "First Name"))
        self.lineEdit_lastName.setPlaceholderText(_translate("Form_AddMember", "Last Name"))
        self.lineEdit_AadharNumber.setPlaceholderText(_translate("Form_AddMember", "Aadhar Number"))
        self.lineEdit_contactNumber.setPlaceholderText(_translate("Form_AddMember", "Contact Number"))
        self.radioButton_Female.setText(_translate("Form_AddMember", "Female"))
        self.radioButton_Male.setText(_translate("Form_AddMember", "Male"))
        self.radioButton_Other.setText(_translate("Form_AddMember", "Other"))
        self.label_sex.setText(_translate("Form_AddMember", "Gender:"))
        self.label_languages.setText(_translate("Form_AddMember", "Languages:"))
        self.checkBox_Other.setText(_translate("Form_AddMember", "Other"))
        self.checkBox_Regional.setText(_translate("Form_AddMember", "Regional"))
        self.checkBox_Hindi.setText(_translate("Form_AddMember", "Hindi"))
        self.checkBox_English.setText(_translate("Form_AddMember", "English"))
        self.label_education.setText(_translate("Form_AddMember", "Education:"))
        self.label_marr.setText(_translate("Form_AddMember", "Marital Status:"))
        self.checkBox_marr.setText(_translate("Form_AddMember", "Married"))
        self.radioButton_5th.setText(_translate("Form_AddMember", "5th"))
        self.radioButton_0.setText(_translate("Form_AddMember", "0"))
        self.radioButton_10th.setText(_translate("Form_AddMember", "10th"))
        self.radioButton_12th.setText(_translate("Form_AddMember", "12th"))
        self.radioButton_ug.setText(_translate("Form_AddMember", "UG"))
        self.radioButton_pg.setText(_translate("Form_AddMember", "PG"))
        self.label_Occupation.setText(_translate("Form_AddMember", "Occupation:"))
        self.comboBox_Occupation.setItemText(0, _translate("Form_AddMember", "Choose Your Occupation"))
        for i in range(0,len(occ)):
            self.comboBox_Occupation.setItemText(i+1, _translate("Form_SignIn", occ[i]))
        self.label_DOB.setText(_translate("Form_AddMember", "DOB:"))
        self.pushButton_Done.setText(_translate("Form_AddMember", "D o n e"))
        self.dob.setDisplayFormat(_translate("Form_AddMember", "yyyy/M/d"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_AddMember = QtWidgets.QWidget()
    ui = Ui_Form_AddMember()
    ui.setupUi(Form_AddMember, 'CPR001')
    Form_AddMember.show()
    sys.exit(app.exec())
