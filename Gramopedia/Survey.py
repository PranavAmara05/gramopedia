from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_Survey(object):
    
    def clickSubmit(self,uid,s,q):
        if self.radioButton_optionA.isChecked():
            rep = uid+'A\n' 
        elif self.radioButton_optionB.isChecked():
            rep = uid+'B\n'
        elif self.radioButton_optionC.isChecked():
            rep = uid+'C\n'
        elif self.radioButton_optionD.isChecked():
            rep = uid+'D\n'
        else:
            rep = ''
        if rep!='':
            import mysql.connector as ms
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            cur = m.cursor()
            cur.execute('''select {} from surveys where sname = '{}' and target = '{}' and question = '{}';'''.format(rep[6], s.split(':')[0], s.split(':')[1], q))
            cou = cur.fetchone()[0]+1
            cur.execute('''update surveys set {} = {} where sname = '{}' and target = '{}' and question = '{}';'''.format(rep[6], cou, s.split(':')[0], s.split(':')[1], q))
            m.commit()
            m.close()
            with open('Surveys/'+s.split(':')[1]+'_'+s.split(':')[0]+'_'+q[:-1]+'.txt','a') as f:
                f.write(rep)
            
    def setupUi(self, Form_Survey, uid, s, q, r):
        Form_Survey.setObjectName("Form_Survey")
        Form_Survey.resize(400, 500)
        Form_Survey.setMinimumSize(QtCore.QSize(400, 500))
        Form_Survey.setMaximumSize(QtCore.QSize(400, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_Survey.setWindowIcon(icon)
        self.label_bg = QtWidgets.QLabel(Form_Survey)
        self.label_bg.setGeometry(QtCore.QRect(0, 0, 400, 500))
        self.label_bg.setStyleSheet("border-image: url(Icon_pack/Gramopedia_logo.jpg);")
        self.label_bg.setText("")
        self.label_bg.setObjectName("label_bg")
        self.label_Survey = QtWidgets.QLabel(Form_Survey)
        self.label_Survey.setGeometry(QtCore.QRect(80, 20, 300, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_Survey.setFont(font)
        self.label_Survey.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_Survey.setObjectName("label_Survey")
        self.label_Question = QtWidgets.QLabel(Form_Survey)
        self.label_Question.setGeometry(QtCore.QRect(5, 100, 400, 70))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Question.setFont(font)
        self.label_Question.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.label_Question.setObjectName("label_Question")
        self.radioButton_optionA = QtWidgets.QRadioButton(Form_Survey)
        self.radioButton_optionA.setGeometry(QtCore.QRect(75, 200, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_optionA.setFont(font)
        self.radioButton_optionA.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.radioButton_optionA.setObjectName("radioButton_optionA")
        self.radioButton_optionB = QtWidgets.QRadioButton(Form_Survey)
        self.radioButton_optionB.setGeometry(QtCore.QRect(75, 250, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_optionB.setFont(font)
        self.radioButton_optionB.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.radioButton_optionB.setObjectName("radioButton_optionB")
        self.radioButton_optionC = QtWidgets.QRadioButton(Form_Survey)
        self.radioButton_optionC.setGeometry(QtCore.QRect(75, 300, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_optionC.setFont(font)
        self.radioButton_optionC.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.radioButton_optionC.setObjectName("radioButton_optionC")
        self.radioButton_optionD = QtWidgets.QRadioButton(Form_Survey)
        self.radioButton_optionD.setGeometry(QtCore.QRect(75, 350, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton_optionD.setFont(font)
        self.radioButton_optionD.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.04, x2:1, y2:0, stop:0 rgba(192, 218, 232, 210), stop:1 rgba(155, 75, 196, 169));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.radioButton_optionD.setObjectName("radioButton_optionD")
        self.pushButton_Submit = QtWidgets.QPushButton(Form_Survey, clicked=lambda:self.clickSubmit(uid,s,q))
        self.pushButton_Submit.setGeometry(QtCore.QRect(110, 420, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Submit.setFont(font)
        self.pushButton_Submit.setStyleSheet("QPushButton#pushButton_Submit{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_Submit:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton_Submit:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.pushButton_Submit.setObjectName("pushButton_Submit")

        self.retranslateUi(Form_Survey, s, q, r)
        self.pushButton_Submit.clicked.connect(Form_Survey.update)
        self.pushButton_Submit.clicked.connect(Form_Survey.close)
        QtCore.QMetaObject.connectSlotsByName(Form_Survey)

    def retranslateUi(self, Form_Survey, s, q, r):
        _translate = QtCore.QCoreApplication.translate
        Form_Survey.setWindowTitle(_translate("Form_Survey", "Survey"))
        self.label_Survey.setText(_translate("Form_Survey", s))
        self.label_Question.setText(_translate("Form_Survey", q))
        self.radioButton_optionA.setText(_translate("Form_Survey", "(A)"+r[0][0]))
        self.radioButton_optionB.setText(_translate("Form_Survey", "(B)"+r[0][1]))
        self.radioButton_optionC.setText(_translate("Form_Survey", "(C)"+r[0][2]))
        self.radioButton_optionD.setText(_translate("Form_Survey", "(D)"+r[0][3]))
        self.pushButton_Submit.setText(_translate("Form_Survey", "S u b m i t"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Survey = QtWidgets.QWidget()
    ui = Ui_Form_Survey()
    ui.setupUi(Form_Survey)
    Form_Survey.show()
    sys.exit(app.exec())
