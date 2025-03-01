from PyQt6 import QtCore, QtGui, QtWidgets

occ = ['Student','Unemployed','Agriculture','House Keeping','Government Sector',
       'Private Sector','Sports','Cattle','Farming']


class Ui_Form_Edit_Profile(object):

    def clickUpdate(self, data, Form_Edit_Profile):
        aadhar = self.lineEdit_AadharNumber.text()
        contact = self.lineEdit_Contact.text()
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

        if len(lang) and len(aadhar)==12 and len(contact)==10 and aadhar.isdigit() and contact.isdigit() and edu and sex:
            import mysql.connector as ms
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            cur = m.cursor()
            dob = 'date\''+date+'\''
            name = data[0]
            lan = lang[0]
            if len(lang)>1:
                for i in range(1,len(lang)):
                    lan = lan + ',' + lang[i]
            cur.execute('''delete from people where name = '{}' and unique_id = '{}';'''.format(name,data[1]))      
            cur.execute('''insert into people values ('{}','{}','{}','{}','{}','{}','{}',{},'{}','{}');'''.format(name,data[1],aadhar,contact,sex,lan,edu,dob,occ,marr))
            m.commit()
            m.close()
            Form_Edit_Profile.close()
        if len(aadhar)!=12 or not aadhar.isdigit():
            self.lineEdit_AadharNumber.clear()
        if len(contact)!=10 or not contact.isdigit():
            self.lineEdit_Contact.clear()
            
                
    def setupUi(self, Form_Edit_Profile,data):
        Form_Edit_Profile.setObjectName("Form_Edit_Profile")
        Form_Edit_Profile.resize(620, 480)
        Form_Edit_Profile.setMinimumSize(QtCore.QSize(620, 480))
        Form_Edit_Profile.setMaximumSize(QtCore.QSize(620, 490))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/plus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_Edit_Profile.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Form_Edit_Profile)
        self.label.setGeometry(QtCore.QRect(5, 5, 610, 470))
        self.label.setStyleSheet("border-image: url(Icon_pack/green-field.webp);\n"
"border-radius: 40px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_bgcolor = QtWidgets.QLabel(Form_Edit_Profile)
        self.label_bgcolor.setGeometry(QtCore.QRect(0, 0, 620, 480))
        self.label_bgcolor.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00568182, y1:0.045, x2:1, y2:1, stop:0 rgba(255, 0, 0, 100), stop:0.166 rgba(255, 255, 0, 94), stop:0.333 rgba(0, 255, 0, 96), stop:0.5 rgba(0, 255, 255, 98), stop:0.666 rgba(0, 0, 255, 103), stop:0.833 rgba(255, 0, 255, 101), stop:1 rgba(255, 0, 0, 100));")
        self.label_bgcolor.setText("")
        self.label_bgcolor.setObjectName("label_bgcolor")
        self.label_uid = QtWidgets.QLabel(Form_Edit_Profile)
        self.label_uid.setGeometry(QtCore.QRect(0, 60, 620, 30))
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
        self.label_editProfile = QtWidgets.QLabel(Form_Edit_Profile)
        self.label_editProfile.setGeometry(QtCore.QRect(200, 10, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_editProfile.setFont(font)
        self.label_editProfile.setStyleSheet("color:rgba(0, 0, 0, 200);\n"
"font: 75 20pt \"Comic Sans MS\";")
        self.label_editProfile.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_editProfile.setObjectName("label_editProfile")
        self.label_name = QtWidgets.QLabel(Form_Edit_Profile)
        self.label_name.setGeometry(QtCore.QRect(0, 100, 620, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 15pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.lineEdit_AadharNumber = QtWidgets.QLineEdit(Form_Edit_Profile)
        self.lineEdit_AadharNumber.setGeometry(QtCore.QRect(0, 150, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_AadharNumber.setFont(font)
        self.lineEdit_AadharNumber.setAccessibleName("")
        self.lineEdit_AadharNumber.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.lineEdit_AadharNumber.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lineEdit_AadharNumber.setInputMask("")
        self.lineEdit_AadharNumber.setMaxLength(12)
        self.lineEdit_AadharNumber.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_AadharNumber.setClearButtonEnabled(False)
        self.lineEdit_AadharNumber.setObjectName("lineEdit_AadharNumber")
        self.lineEdit_Contact = QtWidgets.QLineEdit(Form_Edit_Profile)
        self.lineEdit_Contact.setGeometry(QtCore.QRect(0, 200, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lineEdit_Contact.setFont(font)
        self.lineEdit_Contact.setAccessibleName("")
        self.lineEdit_Contact.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.lineEdit_Contact.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lineEdit_Contact.setInputMask("")
        self.lineEdit_Contact.setMaxLength(10)
        self.lineEdit_Contact.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_Contact.setClearButtonEnabled(False)
        self.lineEdit_Contact.setObjectName("lineEdit_Contact")
        self.dob = QtWidgets.QDateEdit(Form_Edit_Profile)
        self.dob.setGeometry(QtCore.QRect(55, 250, 195, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.dob.setFont(font)
        self.dob.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.dob.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dob.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.dob.setDateTime(QtCore.QDateTime(QtCore.QDate(2016, 8, 9), QtCore.QTime(0, 0, 0)))
        self.dob.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2023, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dob.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(1900, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dob.setCalendarPopup(True)
        self.dob.setDate(QtCore.QDate(2016, 8, 9))
        self.dob.setObjectName("dob")
        self.label_DOB = QtWidgets.QLabel(Form_Edit_Profile)
        self.label_DOB.setGeometry(QtCore.QRect(0, 250, 50, 40))
        self.label_DOB.setStyleSheet("color:rgba(0,0,0, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 200), stop:1 rgba(155, 75, 196, 150));")
        self.label_DOB.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_DOB.setObjectName("label_DOB")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form_Edit_Profile)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(390, 350, 221, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_Sex = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_Sex.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_Sex.setObjectName("horizontalLayout_Sex")
        self.radioButton_Female = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_Female.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.radioButton_Female.setObjectName("radioButton_Female")
        self.horizontalLayout_Sex.addWidget(self.radioButton_Female)
        self.radioButton_Male = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_Male.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.radioButton_Male.setObjectName("radioButton_Male")
        self.horizontalLayout_Sex.addWidget(self.radioButton_Male)
        self.radioButton_Other = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_Other.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.radioButton_Other.setObjectName("radioButton_Other")
        self.horizontalLayout_Sex.addWidget(self.radioButton_Other)
        self.label_sex = QtWidgets.QLabel(Form_Edit_Profile)
        self.label_sex.setGeometry(QtCore.QRect(310, 350, 90, 40))
        self.label_sex.setStyleSheet("color:rgba(0,0,0, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_sex.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_sex.setObjectName("label_sex")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form_Edit_Profile)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(400, 150, 221, 71))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_Education = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_Education.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Education.setObjectName("gridLayout_Education")
        self.radioButton_0 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_0.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.radioButton_0.setObjectName("radioButton_0")
        self.gridLayout_Education.addWidget(self.radioButton_0, 0, 0, 1, 1)
        self.radioButton_5th = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_5th.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.radioButton_5th.setObjectName("radioButton_5th")
        self.gridLayout_Education.addWidget(self.radioButton_5th, 0, 1, 1, 1)
        self.radioButton_10th = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_10th.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.radioButton_10th.setObjectName("radioButton_10th")
        self.gridLayout_Education.addWidget(self.radioButton_10th, 0, 2, 1, 1)
        self.radioButton_12th = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_12th.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.radioButton_12th.setObjectName("radioButton_12th")
        self.gridLayout_Education.addWidget(self.radioButton_12th, 2, 0, 1, 1)
        self.radioButton_pg = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_pg.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.radioButton_pg.setObjectName("radioButton_pg")
        self.gridLayout_Education.addWidget(self.radioButton_pg, 2, 2, 1, 1)
        self.radioButton_ug = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_ug.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.radioButton_ug.setObjectName("radioButton_ug")
        self.gridLayout_Education.addWidget(self.radioButton_ug, 2, 1, 1, 1)
        self.label_education = QtWidgets.QLabel(Form_Edit_Profile)
        self.label_education.setGeometry(QtCore.QRect(310, 150, 90, 40))
        self.label_education.setStyleSheet("color:rgba(0,0,0, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_education.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_education.setObjectName("label_education")
        self.comboBox_Occupation = QtWidgets.QComboBox(Form_Edit_Profile)
        self.comboBox_Occupation.setGeometry(QtCore.QRect(0, 300, 250, 40))
        self.comboBox_Occupation.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.comboBox_Occupation.setObjectName("comboBox_Occupation")
        for i in range(len(occ)+1):
            self.comboBox_Occupation.addItem("")
        self.label_languages = QtWidgets.QLabel(Form_Edit_Profile)
        self.label_languages.setGeometry(QtCore.QRect(310, 250, 90, 40))
        self.label_languages.setStyleSheet("color:rgba(0,0,0, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_languages.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_languages.setObjectName("label_languages")
        self.gridLayoutWidget = QtWidgets.QWidget(Form_Edit_Profile)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(400, 245, 221, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_Languages = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_Languages.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_Languages.setObjectName("gridLayout_Languages")
        self.checkBox_Other = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Other.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.checkBox_Other.setObjectName("checkBox_Other")
        self.gridLayout_Languages.addWidget(self.checkBox_Other, 2, 1, 1, 1)
        self.checkBox_Regional = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Regional.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.checkBox_Regional.setObjectName("checkBox_Regional")
        self.gridLayout_Languages.addWidget(self.checkBox_Regional, 2, 0, 1, 1)
        self.checkBox_Hindi = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_Hindi.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.checkBox_Hindi.setObjectName("checkBox_Hindi")
        self.gridLayout_Languages.addWidget(self.checkBox_Hindi, 0, 1, 1, 1)
        self.checkBox_English = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBox_English.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.checkBox_English.setObjectName("checkBox_English")
        self.gridLayout_Languages.addWidget(self.checkBox_English, 0, 0, 1, 1)
        self.label_marrSt = QtWidgets.QLabel(Form_Edit_Profile)
        self.label_marrSt.setGeometry(QtCore.QRect(0, 350, 140, 40))
        self.label_marrSt.setStyleSheet("color:rgba(0,0,0, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.label_marrSt.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_marrSt.setObjectName("label_marrSt")
        self.checkBox_marr = QtWidgets.QCheckBox(Form_Edit_Profile)
        self.checkBox_marr.setGeometry(QtCore.QRect(145, 350, 105, 40))
        self.checkBox_marr.setStyleSheet("color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"font: 75 13pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 100), stop:1 rgba(155, 75, 196, 50));")
        self.checkBox_marr.setObjectName("checkBox_marr")
        self.push_update = QtWidgets.QPushButton(Form_Edit_Profile, clicked = lambda: self.clickUpdate(data, Form_Edit_Profile))
        self.push_update.setGeometry(QtCore.QRect(0, 410, 620, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.push_update.setFont(font)
        self.push_update.setStyleSheet("QPushButton{\n"
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
        self.push_update.setObjectName("push_update")
        self.label_bgcolor.raise_()
        self.label.raise_()
        self.label_uid.raise_()
        self.label_editProfile.raise_()
        self.label_name.raise_()
        self.lineEdit_AadharNumber.raise_()
        self.lineEdit_Contact.raise_()
        self.dob.raise_()
        self.label_DOB.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_sex.raise_()
        self.gridLayoutWidget_2.raise_()
        self.label_education.raise_()
        self.comboBox_Occupation.raise_()
        self.label_languages.raise_()
        self.gridLayoutWidget.raise_()
        self.label_marrSt.raise_()
        self.checkBox_marr.raise_()
        self.push_update.raise_()

        self.retranslateUi(Form_Edit_Profile, data)
        QtCore.QMetaObject.connectSlotsByName(Form_Edit_Profile)

    def retranslateUi(self, Form_Edit_Profile, data):
        _translate = QtCore.QCoreApplication.translate
        Form_Edit_Profile.setWindowTitle(_translate("Form_Edit_Profile", "Edit Profile"))
        self.label_uid.setText(_translate("Form_Edit_Profile", data[1]))
        self.label_editProfile.setText(_translate("Form_Edit_Profile", "Edit Profile"))
        self.label_name.setText(_translate("Form_Edit_Profile", data[0]))
        self.lineEdit_AadharNumber.setText(_translate("Form_Edit_Profile", data[2]))
        self.lineEdit_AadharNumber.setPlaceholderText(_translate("Form_Edit_Profile", "Aadhar Number"))
        self.lineEdit_Contact.setText(_translate("Form_Edit_Profile", data[3]))
        self.lineEdit_Contact.setPlaceholderText(_translate("Form_Edit_Profile", "Contact Number"))
        self.dob.setDisplayFormat(_translate("Form_Edit_Profile", "yyyy/M/d"))
        self.label_DOB.setText(_translate("Form_Edit_Profile", "DOB:"))
        self.radioButton_Female.setText(_translate("Form_Edit_Profile", "Female"))
        self.radioButton_Male.setText(_translate("Form_Edit_Profile", "Male"))
        self.radioButton_Other.setText(_translate("Form_Edit_Profile", "Other"))
        self.label_sex.setText(_translate("Form_Edit_Profile", "Gender:"))
        self.radioButton_0.setText(_translate("Form_Edit_Profile", "0"))
        self.radioButton_5th.setText(_translate("Form_Edit_Profile", "5th"))
        self.radioButton_10th.setText(_translate("Form_Edit_Profile", "10th"))
        self.radioButton_12th.setText(_translate("Form_Edit_Profile", "12th"))
        self.radioButton_pg.setText(_translate("Form_Edit_Profile", "PG"))
        self.radioButton_ug.setText(_translate("Form_Edit_Profile", "UG"))
        self.label_education.setText(_translate("Form_Edit_Profile", "Education:"))
        self.comboBox_Occupation.setItemText(0, _translate("Form_Edit_Profile", data[8]))
        for i in range(0,len(occ)):
            self.comboBox_Occupation.setItemText(i+1, _translate("Form_SignIn", occ[i]))
        self.label_languages.setText(_translate("Form_Edit_Profile", "Languages:"))
        self.checkBox_Other.setText(_translate("Form_Edit_Profile", "Other"))
        self.checkBox_Regional.setText(_translate("Form_Edit_Profile", "Regional"))
        self.checkBox_Hindi.setText(_translate("Form_Edit_Profile", "Hindi"))
        self.checkBox_English.setText(_translate("Form_Edit_Profile", "English"))
        self.label_marrSt.setText(_translate("Form_Edit_Profile", "Marital Status:"))
        self.checkBox_marr.setText(_translate("Form_Edit_Profile", "Married"))
        self.push_update.setText(_translate("Form_Edit_Profile", "U p d a t e   P r o f i l e"))

        if 'Other' in data[5]:
            self.checkBox_Other.setChecked(True)
        if 'Regional' in data[5]:
            self.checkBox_Regional.setChecked(True)
        if 'Hindi' in data[5]:
            self.checkBox_Hindi.setChecked(True)
        if 'English' in data[5]:
            self.checkBox_English.setChecked(True)

        
        self.dob.setDateTime(QtCore.QDateTime(QtCore.QDate(int(str(data[7])[:4]), int(str(data[7])[5:7]),
                                                           int(str(data[7])[8:]) ), QtCore.QTime(0, 0, 0)))

        if data[9]=='Married':
            self.checkBox_marr.setChecked(True)

        if data[4]=='Female':
            self.radioButton_Female.setChecked(True)
        if data[4]=='Male':
            self.radioButton_Male.setChecked(True)
        if data[4]=='Other':
            self.radioButton_Other.setChecked(True)

        if data[6]=='0':
            self.radioButton_0.setChecked(True)
        if data[6]=='5th':
            self.radioButton_5th.setChecked(True)
        if data[6]=='10th':
            self.radioButton_10th.setChecked(True)
        if data[6]=='12th':
            self.radioButton_12th.setChecked(True)
        if data[6]=='PG':
            self.radioButton_pg.setChecked(True)
        if data[6]=='UG':
            self.radioButton_ug.setChecked(True)

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Edit_Profile = QtWidgets.QWidget()
    ui = Ui_Form_Edit_Profile()
    ui.setupUi(Form_Edit_Profile)
    Form_Edit_Profile.show()
    sys.exit(app.exec())
