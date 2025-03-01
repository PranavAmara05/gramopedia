from PyQt6 import QtCore, QtGui, QtWidgets
from FetchData import genuid
import mysql.connector as ms

class Ui_Form_GenUid(object):
    def clickDone(self,  Form_Login, Form_GenUid, vill):
        Form_Login.show()
        Form_GenUid.hide()
        f = open('signup.txt','a+')
        f.write(genuid(vill)+':')
        f.close()
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        c = m.cursor()
        data = open('signup.txt').read().split(':')
        c.execute('''insert into users values ('{}','{}','{}','{}');'''.format(data[0],data[5],data[4],data[5][:3]))
        m.commit()
        data = open('signup.txt').read().split(':')
        c.execute('''insert into people values ('{}','{}','{}','{}','','','0',date'2022-01-01','','');'''.format(data[0],data[5],data[1],data[2]))
        m.commit()
        m.close()
        
    def setupUi(self, Form_GenUid, vill,  Form_Login):
        Form_GenUid.setObjectName("Form_GenUid")
        Form_GenUid.resize(600, 400)
        Form_GenUid.setMinimumSize(QtCore.QSize(600, 400))
        Form_GenUid.setMaximumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/check.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_GenUid.setWindowIcon(icon)
        self.label_bgcolor = QtWidgets.QLabel(Form_GenUid)
        self.label_bgcolor.setGeometry(QtCore.QRect(0, 0, 600, 451))
        self.label_bgcolor.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.00568182, y1:0.045, x2:1, y2:1, stop:0 rgba(255, 0, 0, 200), stop:0.166 rgba(255, 255, 0, 194), stop:0.333 rgba(0, 255, 0, 196), stop:0.5 rgba(0, 255, 255, 198), stop:0.666 rgba(0, 0, 255, 203), stop:0.833 rgba(255, 0, 255, 201), stop:1 rgba(255, 0, 0, 200));")
        self.label_bgcolor.setText("")
        self.label_bgcolor.setObjectName("label_bgcolor")
        self.label_bglogo = QtWidgets.QLabel(Form_GenUid)
        self.label_bglogo.setGeometry(QtCore.QRect(0, 0, 300, 400))
        self.label_bglogo.setStyleSheet("border-image: url(Icon_pack/Gramopedia_logo.jpg);")
        self.label_bglogo.setText("")
        self.label_bglogo.setObjectName("label_bglogo")
        self.label_dispMess = QtWidgets.QLabel(Form_GenUid)
        self.label_dispMess.setGeometry(QtCore.QRect(295, 10, 300, 240))
        font = QtGui.QFont()
        font.setBold(True)
        self.label_dispMess.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"font: 90 12pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255, 255);")
        self.label_dispMess.setObjectName("label_dispMess")
        self.push_confirm = QtWidgets.QPushButton(Form_GenUid,clicked=lambda:self.clickDone(Form_Login, Form_GenUid, vill))
        self.push_confirm.setGeometry(QtCore.QRect(350, 320, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.push_confirm.setFont(font)
        self.push_confirm.setStyleSheet("QPushButton#push_confirm{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#push_confirm:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#push_confirm:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_confirm.setObjectName("push_confirm")
        self.label_uid = QtWidgets.QLabel(Form_GenUid)
        self.label_uid.setGeometry(QtCore.QRect(380, 260, 135, 40))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_uid.setFont(font)
        self.label_uid.setStyleSheet("color:rgb(240, 240, 240)\n"
"font: \"Comic Sans MS\";\n")
        self.label_uid.setObjectName("label_uid")

        self.retranslateUi(Form_GenUid,vill)
        QtCore.QMetaObject.connectSlotsByName(Form_GenUid)

    def retranslateUi(self, Form_GenUid, vill):
        _translate = QtCore.QCoreApplication.translate
        Form_GenUid.setWindowTitle(_translate("Form_GenUid", "Unique_id_Confirmation"))
        self.label_dispMess.setText(_translate("Form_GenUid", "                   WELCOME                   \n\n"
                                                                        "     To The Digital Community Of Grams   \n\n"
                                                                        "   Your Unique Id Has Been Generated   \n\n"
                                                                        " Remember it as this will be used to login \n\n"
                                                                        "                    hereafter."))
        self.push_confirm.setText(_translate("Form_GenUid", "C o n f i r m   S i g n i n"))
        self.label_uid.setText(_translate("Form_GenUid", genuid(vill)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_GenUid = QtWidgets.QWidget()
    ui = Ui_Form_GenUid()
    ui.setupUi(Form_GenUid)
    Form_GenUid.show()
    sys.exit(app.exec())
