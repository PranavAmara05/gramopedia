from PyQt6 import QtCore, QtGui, QtWidgets
from CreateAdmin import Ui_Form_Create_admin
from ViewPeople import Ui_Form_View_People
from Password import Ui_Form_Password
from AddVillage import Ui_Form_Add_Village

cbinfo =["Search", "Literacy Stats", "Language Stats", "Employment Stats", "Population Stats"]

sname = []
questions = []
dlog = ['Select A Message']

import mysql.connector as ms
m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
c = m.cursor()

cwsSub = ['Seek Information','Seek Help','Suggestion/Reform','Other']
cwsTo = []
c.execute('select unique_id from users where unique_id like "___000";')
for i in c.fetchall():
    cwsTo.append(i[0])

c.execute('select unique_id from admins;')
adm = ['Search Admin']
for i in c.fetchall():
    adm.append(i[0])
    
c.execute('select v_code,v_name from villages;')
v_name = ['Search Villages']
for i in c.fetchall():
    v_name.append(i[0]+'  '+i[1])
    
c.execute('select distinct subject from communication;')
sublist = ['By Subject','Unreplied']
for i in c.fetchall():
    sublist.append(i[0])

filvil = ['By Village/GP','GP','Sent']+v_name[1:len(v_name)]

m.close()

class Ui_Form_AdminWindow(object):

    def clickViewInfo(self,uid):
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        c = m.cursor()
        a = self.comboBox_info.currentText()
        disp = 'Select An Option'
        self.textBrowser_info.setText(disp)
        
        if a=='Literacy Stats':
            c.execute('''select count(*) from people where education!='0';''')
            alpha = c.fetchone()[0]
            c.execute('''select count(*) from people;''')
            beta = c.fetchone()[0]            
            litr = str((alpha/beta)*100)
            c.execute('''select count(*) from people where education='0';''')
            c0 = str(c.fetchone()[0])
            c.execute('''select count(*) from people where education='5th';''')
            c5 = str(c.fetchone()[0])
            c.execute('''select count(*) from people where education='10th';''')
            c10 = str(c.fetchone()[0])
            c.execute('''select count(*) from people where education='12th';''')
            c12 = str(c.fetchone()[0])
            c.execute('''select count(*) from people where education='UG';''')
            cUG = str(c.fetchone()[0])
            c.execute('''select count(*) from people where education='PG';''')
            cPG = str(c.fetchone()[0])
            
            disp = str('Literacy Rate: '+litr+'\nUneducated: '+c0+'\n5+ Educated: '+c5+'\n10+ Educated: '+c10+
                    '\n12+ Educated: '+c12+'\nUnder Graduates: '+cUG+'\nPost Graduates: '+cPG)
            self.textBrowser_info.setText(disp)
            
        if a=='Population Stats':
            c.execute('''select count(*) from people where sex='male';''')
            alpha = c.fetchone()[0]
            c.execute('''select count(*) from people where sex='female';''')
            beta = c.fetchone()[0]
            c.execute('''select count(*) from people where sex='other';''')
            delta = c.fetchone()[0]
            c.execute('''select dob from people;''')
            tpop  = alpha+beta+delta
            c18 = 0
            for i in c.fetchall():
                if int(str(i[0])[:4]) <= 2005:
                    c18+=1
            c17 = tpop - c18
            sratio = 'Can Not be Defined'
            if beta and alpha:
                sratio = str((beta / alpha)*1000)+':1000  (F:M)'
            
            disp = str('Sex Ratio: '+sratio+'\nMale: '+str(alpha)+'\nFemale: '+str(beta)+'\nOther: '+str(delta)+
                    '\nTotal Population: '+str(tpop)+'\n18 and Above: '+str(c18)+'\nBelow 18: '+str(c17))
            self.textBrowser_info.setText(disp)

        if a=='Language Stats':
            eng,hin,oth,reg = 0,0,0,0
            c1,c2,c3,c4 = 0,0,0,0
            c.execute('''select lang from people;''')
            for i in c.fetchall():
                if 'English' in i[0]:
                    eng+=1
                if 'Hindi' in i[0]:
                    hin+=1
                if 'Regional' in i[0]:
                    reg+=1
                if 'Other' in i[0]:
                    oth+=1
                if len(i[0].split(','))==1:
                    c1+=1
                if len(i[0].split(','))==2:
                    c2+=1
                if len(i[0].split(','))==3:
                    c3+=1
                if len(i[0].split(','))==4:
                    c4+=1
                    
            disp = ('Only One Lang: '+str(c1)+'\nTwo Lang: '+str(c2)+'\nThree Lang: '+str(c3)+'\nFour Lang: '+str(c4)
                    +'\nEnglish: '+str(eng)+'\nHindi: '+str(hin)+'\nRegional: '+str(reg)+'\nOther: '+str(oth))
            self.textBrowser_info.setText(disp)

        if a=='Employment Stats':
            c.execute('''select distinct occ from people;''')
            zeta = []
            meta = dict()
            for i in c.fetchall():
                zeta.append(i[0])
            c.execute('''select occ from people;''')
            eta = []
            for i in c.fetchall():
                eta.append(i[0])
            for i in zeta:
                meta[i] = str(eta.count(i))
            disp=''
            for occ,c in meta.items():
                disp+='\n'+occ+': '+c
            self.textBrowser_info.setText(disp[1:])
        m.close()

    
    def addVillage(self):
        self.window =QtWidgets.QWidget()
        self.ui = Ui_Form_Add_Village()
        self.ui.setupUi(self.window)
        self.window.show()

    def chPassword(self, uid):
        self.window =QtWidgets.QWidget()
        self.ui = Ui_Form_Password()
        self.ui.setupUi(self.window, 'ChangeP', uid)
        self.window.show()

    def logOut(self, Form_AdminWindow):
        Form_AdminWindow.close()
        print('LOGGED OUT')

    def viewPeople(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_View_People()
        self.ui.setupUi(self.window, 'a')
        self.window.show()

    def createAdmin(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_Create_admin()
        self.ui.setupUi(self.window)
        self.window.show()

    def clickViewResS(self):
        s = self.comboBox_info_4.currentText()
        q = self.comboBox_info_5.currentText()
        if q!='' and s!='Select A Survey':
            s = s.split(':')
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            c = m.cursor()
            c.execute('''select optA,optB,optC,optD from surveys where sname='{}' and question='{}' and target = '{}';'''.format(s[1],q,s[0]))
            opt = c.fetchall()
            res = c.execute('''select A,B,C,D from surveys where sname='{}' and question='{}' and target = '{}';'''.format(s[1],q,s[0]))
            res = c.fetchall()
            m.close()
            l1 = '(A)'+opt[0][0]+'   ('+str(res[0][0])
            l2 = ')\n(B)'+opt[0][1]+'   ('+str(res[0][1])
            l3 = ')\n(C)'+opt[0][2]+'   ('+str(res[0][2])
            l4 = ')\n(D)'+opt[0][3]+'   ('+str(res[0][3])+')'
            disp = l1 + l2 + l3 + l4
            self.textBrowser_3.setText(disp)

    def createSurvey(self):
        if (self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text() and self.lineEdit_4.text()
        and self.lineEdit_5.text() and self.lineEdit_6.text()):
            s = self.lineEdit.text()
            t = self.comboBox_info_6.currentText()
            q = self.lineEdit_5.text()
            a = self.lineEdit_3.text()
            b = self.lineEdit_2.text()
            c = self.lineEdit_6.text()
            d = self.lineEdit_4.text()
            m = ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            cur = m.cursor()
            cur.execute('''insert into surveys values ('{}', '{}', '{}', '{}', '{}', '{}', 0, 0, 0, 0, '{}');'''.format(s,q,a,b,c,d,t))
            m.commit()
            m.close()
            open("Surveys/{}.txt".format(t+'_'+s+'_'+q[:-1]),'w').close()
            self.lineEdit.clear()
            self.comboBox_info_6.setCurrentIndex(0)
            self.lineEdit_5.clear()
            self.lineEdit_3.clear()
            self.lineEdit_2.clear()
            self.lineEdit_6.clear()
            self.lineEdit_4.clear()
        
    def clickViewSquest(self):
        _translate = QtCore.QCoreApplication.translate
        s = self.comboBox_info_4.currentText()
        self.comboBox_info_5.clear()
        self.textBrowser_3.setText('(A)    (0)\n(B)    (0)\n(C)    (0)\n(D)    (0)')
        if s!='Select A Survey':
            s=s.split(':')
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            c = m.cursor()
            c.execute('''select question from surveys where sname='{}' and target='{}';'''.format(s[1],s[0]))
            global questions
            questions = c.fetchall()
            m.close()
            for i in range(len(questions)):                
                self.comboBox_info_5.addItem("")
                self.comboBox_info_5.setItemText(i, _translate("Form_AdminWindow", questions[i][0]))
    

    def applyFilterCom(self,uid):
        _translate = QtCore.QCoreApplication.translate
        sub = self.comboBox_info_8.currentText()
        fv = self.comboBox_info_9.currentText()[:3]
        dclog = ['Select A Message']
        m = ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        c = m.cursor()
        cmd = ''
        if sub not in ['By Subject','Unreplied'] and fv not in ['By ','GP','Sen']:
            cmd='''select from_, subject, message from communication where subject = '{}' and from_ like '{}' and to_ = '{}';'''.format(sub,fv+'___',uid)
        if sub not in ['By Subject','Unreplied'] and fv == 'GP':
            cmd='''select from_, subject, message from communication where subject = '{}' and from_ like '___000' and to_ = '{}';'''.format(sub,uid)
        if sub not in ['By Subject','Unreplied'] and fv == 'By ':
            cmd='''select from_, subject, message from communication where subject = '{}' and to_ = '{}';'''.format(sub,uid)
        if sub=='By Subject' and fv not in ['By ','GP','Sen']:
            cmd='''select from_, subject, message from communication where from_ like '{}' and to_ = '{}';'''.format(fv+'___',uid)
        if sub=='By Subject' and fv == 'GP':
            cmd='''select from_, subject, message from communication where from_ like '___000' and to_ = '{}';'''.format(uid)
        if sub=='By Subject' and fv == 'By ':
            cmd='''select from_, subject, message from communication where to_ = '{}';'''.format(uid)
        if sub=='Unreplied' and fv not in ['By ','GP','Sen']:
            cmd='''select from_, subject, message from communication where from_ like '{}' and to_ = '{}' and response is null;'''.format(fv+'___',uid)
        if sub=='Unreplied' and fv == 'GP':
            cmd='''select from_, subject, message from communication where from_ like '___000' and to_ = '{}' and response is null;'''.format(uid)
        if sub=='Unreplied' and fv == 'By ':
            cmd='''select from_, subject, message from communication where to_ = '{}' and response is null;'''.format(uid)
        if fv == 'Sen' and sub not in ['By Subject','Unreplied']:
            cmd='''select to_, subject, message from communication where from_ = '{}' and subject = '{}';'''.format(uid, sub)
        if fv == 'Sen' and sub=='By Subject':
            cmd='''select to_, subject, message from communication where from_ = '{}';'''.format(uid)
        if fv == 'Sen' and sub=='Unreplied':
            cmd='''select to_, subject, message from communication where from_ = '{}' and response is null;'''.format(uid)
        c.execute(cmd)
        for rec in c.fetchall():
            dclog.append(rec[0]+':'+rec[1]+':'+rec[2])
        m.close()
        self.comboBox_info_7.clear()
        self.textEdit.clear()
        self.textBrowser_message.clear()
        self.textBrowser_response.clear()
        for i in range(len(dclog)):
            self.comboBox_info_7.addItem('')
            self.comboBox_info_7.setItemText(i, _translate("Form_AdminWindow", dclog[i]))
        dclog.clear()

    def clickViewMes(self, uid):
        self.textEdit.clear()
        self.textBrowser_message.clear()
        self.textBrowser_response.clear()
        a = self.comboBox_info_7.currentText()
        s = self.comboBox_info_9.currentText()
        if a!='Select A Message':
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            c = m.cursor()
            dlog=a.split(':')
            if s=='Sent':
                c.execute('''select message,response from communication where from_='{}' and to_='{}'
                        and message='{}' and subject='{}';'''.format(uid,dlog[0],dlog[2],dlog[1]))
            else:
                c.execute('''select message,response from communication where from_='{}' and to_='{}'
                        and message='{}' and subject='{}';'''.format(dlog[0],uid,dlog[2],dlog[1]))
            jkl = c.fetchone()
            m.close()
            self.textBrowser_message.setText(jkl[0])
            self.textBrowser_response.setText(jkl[1])

    def respond(self, uid):
        a = self.comboBox_info_7.currentText()
        s = self.comboBox_info_9.currentText()
        if a!='Select A Message':
            if not (self.textBrowser_response.toPlainText()) and s!='Sent':
                m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
                c = m.cursor()
                res = self.textEdit.toPlainText()[:99]
                from_ = a.split(':')[0]
                to_ = uid
                sub = a.split(':')[1]
                message = a.split(':')[2]
                c.execute('''update communication set response = '{}' where from_='{}' and to_='{}'
                            and message='{}' and subject='{}';'''.format(res,from_,to_,message,sub))
                m.commit()
                m.close()
                self.textEdit.clear()
            else:
                self.textEdit.setText('Already Responded / Cannot Reply To Sent Message')
        else:
            self.textEdit.clear()                

    def clickMesS(self, uid):
        mes = self.textEdit_2.toPlainText()
        sub = self.comboBox_info_10.currentText()
        to = self.comboBox_info_11.currentText()[:99]
        if mes!='' and sub!='Subject' and to!='To':
            self.textEdit_2.clear()
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            c = m.cursor()
            c.execute('''insert into communication values ('{}','{}','{}','{}',null);'''.format(uid,to,sub,mes))
            m.commit()
            m.close()
            
    def viewAdmins(self):
        _translate = QtCore.QCoreApplication.translate
        a = self.comboBox_info_2.currentText()
        self.label_info_2.setText(_translate("Form_AdminWindow", "V i e w   A d m i n   I n f o"))
        if a!='Search Admin':
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            c = m.cursor()
            c.execute('''select desig,name from admins where unique_id='{}';'''.format(a))
            a = c.fetchone()
            self.label_info_2.setText(_translate("Form_AdminWindow", a[0]+'   '+a[1]))

    def viewVillages(self):
        _translate = QtCore.QCoreApplication.translate
        v = self.comboBox_info_3.currentText()[:3]
        self.label_info_3.setText(_translate("Form_AdminWindow", "Block"))
        self.label_info_4.setText(_translate("Form_AdminWindow", "District"))
        self.label_info_5.setText(_translate("Form_AdminWindow", "State "))
        self.label_info_6.setText(_translate("Form_AdminWindow", "People"))
        self.label_info_7.setText(_translate("Form_AdminWindow", "Pin Code "))
        self.label_info_8.setText(_translate("Form_AdminWindow", "Altitude"))
        if v!='Sea':
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            c = m.cursor()
            c.execute('''select * from villages where v_code='{}';'''.format(v))
            a = c.fetchone()
            c.execute('''select count(*) from people where unique_id like '{}';'''.format(v+'___'))
            b = str(c.fetchone()[0])
            c.execute('''select count(*) from users where unique_id like '{}';'''.format(v+'___'))
            b = b+' U: '+str(c.fetchone()[0])
            self.label_info_3.setText(_translate("Form_AdminWindow", "B: "+a[2]))
            self.label_info_4.setText(_translate("Form_AdminWindow", "D: "+a[3]))
            self.label_info_5.setText(_translate("Form_AdminWindow", "S: "+a[4]))
            self.label_info_6.setText(_translate("Form_AdminWindow", "P: "+b))
            self.label_info_7.setText(_translate("Form_AdminWindow", "Pin: "+str(a[6])))
            self.label_info_8.setText(_translate("Form_AdminWindow", "Alt: "+str(a[5])+'m'))
            
    def setupUi(self, Form_AdminWindow, s, uid):
        global unique_id
        unique_id = uid
        Form_AdminWindow.setObjectName("Form_AdminWindow")
        Form_AdminWindow.resize(800, 500)
        Form_AdminWindow.setMinimumSize(QtCore.QSize(800, 500))
        Form_AdminWindow.setMaximumSize(QtCore.QSize(800, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_AdminWindow.setWindowIcon(icon)
        self.label_bgcolor = QtWidgets.QLabel(Form_AdminWindow)
        self.label_bgcolor.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.label_bgcolor.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));")
        self.label_bgcolor.setText("")
        self.label_bgcolor.setObjectName("label_bgcolor")
        self.label_logo = QtWidgets.QLabel(Form_AdminWindow)
        self.label_logo.setGeometry(QtCore.QRect(720, 5, 75, 75))
        self.label_logo.setStyleSheet("border-image: url(Icon_pack/Gramopedia_logo.jpg);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.tabWidget = QtWidgets.QTabWidget(Form_AdminWindow)
        self.tabWidget.setGeometry(QtCore.QRect(10, 80, 780, 410))
        self.tabWidget.setStyleSheet("color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Home = QtWidgets.QWidget()
        self.tab_Home.setObjectName("tab_Home")
        self.groupBox_infobox = QtWidgets.QGroupBox(self.tab_Home)
        self.groupBox_infobox.setGeometry(QtCore.QRect(10, 140, 380, 220))
        self.groupBox_infobox.setStyleSheet("color: qlineargradient(spread:repeat, x1:0, y1:0.398, x2:1, y2:0.420455, stop:0 rgba(227, 69, 69, 223), stop:0.531073 rgba(232, 61, 147, 232), stop:0.960452 rgba(41, 90, 180, 238));")
        self.groupBox_infobox.setObjectName("groupBox_infobox")
        self.comboBox_info = QtWidgets.QComboBox(self.groupBox_infobox)
        self.comboBox_info.setGeometry(QtCore.QRect(30, 50, 200, 50))
        self.comboBox_info.setStyleSheet("background-color:rgba(255, 255, 255, 50);\n"
"color: qlineargradient(spread:repeat, x1:0, y1:0.398, x2:1, y2:0.420455, stop:0 rgba(227, 69, 69, 223), stop:0.531073 rgba(232, 61, 147, 232), stop:0.960452 rgba(41, 90, 180, 238));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.comboBox_info.setObjectName("comboBox_info")
        for i in range(len(cbinfo)):
            self.comboBox_info.addItem("")
        #######################################
        self.textBrowser_info = QtWidgets.QTextBrowser(self.groupBox_infobox)
        self.textBrowser_info.setGeometry(QtCore.QRect(25, 120, 350, 100))
        self.textBrowser_info.setStyleSheet("background-color:rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"border-radius:15px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.textBrowser_info.setObjectName("textBrowser_info")
        #######################################
        self.push_info = QtWidgets.QPushButton(self.groupBox_infobox, clicked = lambda:self.clickViewInfo(uid))
        self.push_info.setGeometry(QtCore.QRect(250, 50, 80, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info.setFont(font)
        self.push_info.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info.setIconSize(QtCore.QSize(20, 20))
        self.push_info.setObjectName("push_info")
        self.label_fpop = QtWidgets.QLabel(self.tab_Home)
        self.label_fpop.setGeometry(QtCore.QRect(595, 280, 70, 70))
        self.label_fpop.setStyleSheet("border-image: url(Icon_pack/female.png);")
        self.label_fpop.setText("")
        self.label_fpop.setObjectName("label_fpop")
        self.label_fpopc = QtWidgets.QLabel(self.tab_Home)
        self.label_fpopc.setGeometry(QtCore.QRect(655, 300, 100, 50))
        self.label_fpopc.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.label_fpopc.setObjectName("label_fpopc")
        self.label_desig = QtWidgets.QLabel(self.tab_Home)
        self.label_desig.setGeometry(QtCore.QRect(10, 10, 160, 60))
        self.label_desig.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 28pt \"Comic Sans MS\";")
        self.label_desig.setObjectName("label_desig")
        self.label_name = QtWidgets.QLabel(self.tab_Home)
        self.label_name.setGeometry(QtCore.QRect(180, 10, 380, 60))
        self.label_name.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 28pt \"Comic Sans MS\";")
        self.label_name.setObjectName("label_name")
        self.label_mpopc = QtWidgets.QLabel(self.tab_Home)
        self.label_mpopc.setGeometry(QtCore.QRect(655, 220, 100, 50))
        self.label_mpopc.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.label_mpopc.setObjectName("label_mpopc")
        self.label_popc = QtWidgets.QLabel(self.tab_Home)
        self.label_popc.setGeometry(QtCore.QRect(655, 143, 100, 50))
        self.label_popc.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.label_popc.setObjectName("label_popc")
        self.label_mpop = QtWidgets.QLabel(self.tab_Home)
        self.label_mpop.setGeometry(QtCore.QRect(590, 200, 70, 70))
        self.label_mpop.setStyleSheet("border-image: url(Icon_pack/male.png);")
        self.label_mpop.setText("")
        self.label_mpop.setObjectName("label_mpop")
        self.label_pop = QtWidgets.QLabel(self.tab_Home)
        self.label_pop.setGeometry(QtCore.QRect(580, 130, 80, 80))
        self.label_pop.setStyleSheet("border-image: url(Icon_pack/group.png);")
        self.label_pop.setText("")
        self.label_pop.setObjectName("label_pop")
        self.label_upop = QtWidgets.QLabel(self.tab_Home)
        self.label_upop.setGeometry(QtCore.QRect(410, 220, 50, 50))
        self.label_upop.setStyleSheet("border-image: url(Icon_pack/user (2).png);")
        self.label_upop.setText("")
        self.label_upop.setObjectName("label_upop")
        self.label_vpop = QtWidgets.QLabel(self.tab_Home)
        self.label_vpop.setGeometry(QtCore.QRect(415, 300, 50, 50))
        self.label_vpop.setStyleSheet("border-image: url(Icon_pack/home.png);")
        self.label_vpop.setText("")
        self.label_vpop.setObjectName("label_vpop")
        self.label_upopc = QtWidgets.QLabel(self.tab_Home)
        self.label_upopc.setGeometry(QtCore.QRect(460, 220, 100, 50))
        self.label_upopc.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.label_upopc.setObjectName("label_upopc")
        self.label_vpopc = QtWidgets.QLabel(self.tab_Home)
        self.label_vpopc.setGeometry(QtCore.QRect(460, 300, 100, 50))
        self.label_vpopc.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;\n"
"padding-left:7px;")
        self.label_vpopc.setObjectName("label_vpopc")
        self.push_chpw = QtWidgets.QPushButton(self.tab_Home, clicked = lambda: self.chPassword(uid))
        self.push_chpw.setGeometry(QtCore.QRect(550, 15, 200, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_chpw.setFont(font)
        self.push_chpw.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icon_pack/key.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.push_chpw.setIcon(icon1)
        self.push_chpw.setIconSize(QtCore.QSize(20, 20))
        self.push_chpw.setObjectName("push_chpw")
        self.label_bgcolor_2 = QtWidgets.QLabel(self.tab_Home)
        self.label_bgcolor_2.setGeometry(QtCore.QRect(0, 0, 780, 380))
        self.label_bgcolor_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));")
        self.label_bgcolor_2.setText("")
        self.label_bgcolor_2.setObjectName("label_bgcolor_2")
        self.push_logOut = QtWidgets.QPushButton(self.tab_Home,clicked = lambda: self.logOut(Form_AdminWindow))
        self.push_logOut.setGeometry(QtCore.QRect(600, 80, 150, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_logOut.setFont(font)
        self.push_logOut.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon_pack/log-out.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.push_logOut.setIcon(icon2)
        self.push_logOut.setIconSize(QtCore.QSize(20, 20))
        self.push_logOut.setObjectName("push_logOut")
        self.label_bgcolor_2.raise_()
        self.groupBox_infobox.raise_()
        self.label_fpop.raise_()
        self.label_fpopc.raise_()
        self.label_desig.raise_()
        self.label_name.raise_()
        self.label_mpopc.raise_()
        self.label_popc.raise_()
        self.label_mpop.raise_()
        self.label_pop.raise_()
        self.label_upop.raise_()
        self.label_vpop.raise_()
        self.label_upopc.raise_()
        self.label_vpopc.raise_()
        self.push_chpw.raise_()
        self.push_logOut.raise_()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icon_pack/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_Home, icon3, "")
        self.tab_AdminControls = QtWidgets.QWidget()
        self.tab_AdminControls.setObjectName("tab_AdminControls")
        self.label_bgcolor_3 = QtWidgets.QLabel(self.tab_AdminControls)
        self.label_bgcolor_3.setGeometry(QtCore.QRect(0, 0, 780, 380))
        self.label_bgcolor_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));")
        self.label_bgcolor_3.setText("")
        self.label_bgcolor_3.setObjectName("label_bgcolor_3")
        self.groupBox = QtWidgets.QGroupBox(self.tab_AdminControls)
        self.groupBox.setGeometry(QtCore.QRect(15, 5, 360, 280))
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.groupBox.setObjectName("groupBox")
        self.comboBox_info_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_info_2.setGeometry(QtCore.QRect(30, 60, 200, 50))
        self.comboBox_info_2.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.comboBox_info_2.setObjectName("comboBox_info_2")
        for i in range(len(adm)):
            self.comboBox_info_2.addItem("")
        self.push_info_2 = QtWidgets.QPushButton(self.groupBox,clicked=lambda:self.viewAdmins())
        self.push_info_2.setGeometry(QtCore.QRect(250, 65, 80, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_2.setFont(font)
        self.push_info_2.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_2.setIconSize(QtCore.QSize(20, 20))
        self.push_info_2.setObjectName("push_info_2")
        self.label_info_2 = QtWidgets.QLabel(self.groupBox)
        self.label_info_2.setGeometry(QtCore.QRect(30, 140, 300, 50))
        self.label_info_2.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_info_2.setObjectName("label_info_2")
        self.push_info_3 = QtWidgets.QPushButton(self.groupBox, clicked = lambda: self.createAdmin())
        self.push_info_3.setGeometry(QtCore.QRect(55, 220, 250, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_3.setFont(font)
        self.push_info_3.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_3.setIconSize(QtCore.QSize(20, 20))
        self.push_info_3.setObjectName("push_info_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_AdminControls)
        self.groupBox_2.setGeometry(QtCore.QRect(400, 5, 360, 360))
        self.groupBox_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox_info_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_info_3.setGeometry(QtCore.QRect(30, 60, 200, 50))
        self.comboBox_info_3.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.comboBox_info_3.setObjectName("comboBox_info_3")
        for i in range(len(v_name)):
            self.comboBox_info_3.addItem("")
        self.push_info_5 = QtWidgets.QPushButton(self.groupBox_2,clicked=lambda:self.viewVillages())
        self.push_info_5.setGeometry(QtCore.QRect(250, 65, 80, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_5.setFont(font)
        self.push_info_5.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_5.setIconSize(QtCore.QSize(20, 20))
        self.push_info_5.setObjectName("push_info_5")
        self.label_info_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_info_3.setGeometry(QtCore.QRect(30, 140, 120, 50))
        self.label_info_3.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_info_3.setObjectName("label_info_3")
        self.label_info_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_info_4.setGeometry(QtCore.QRect(30, 190, 120, 50))
        self.label_info_4.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_info_4.setObjectName("label_info_4")
        self.label_info_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_info_5.setGeometry(QtCore.QRect(30, 240, 120, 50))
        self.label_info_5.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_info_5.setObjectName("label_info_5")
        self.label_info_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_info_6.setGeometry(QtCore.QRect(210, 240, 120, 50))
        self.label_info_6.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.label_info_6.setObjectName("label_info_6")
        self.label_info_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_info_7.setGeometry(QtCore.QRect(210, 190, 120, 50))
        self.label_info_7.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_info_7.setObjectName("label_info_7")
        self.label_info_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_info_8.setGeometry(QtCore.QRect(210, 140, 120, 50))
        self.label_info_8.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.label_info_8.setObjectName("label_info_8")
        self.push_info_6 = QtWidgets.QPushButton(self.groupBox_2, clicked=lambda:self.addVillage())
        self.push_info_6.setGeometry(QtCore.QRect(60, 305, 250, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_6.setFont(font)
        self.push_info_6.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_6.setIconSize(QtCore.QSize(20, 20))
        self.push_info_6.setObjectName("push_info_6")
        self.push_info_4 = QtWidgets.QPushButton(self.tab_AdminControls, clicked=lambda:self.viewPeople())
        self.push_info_4.setGeometry(QtCore.QRect(75, 310, 250, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_4.setFont(font)
        self.push_info_4.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_4.setIconSize(QtCore.QSize(20, 20))
        self.push_info_4.setObjectName("push_info_4")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Icon_pack/dashboard.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_AdminControls, icon4, "")
        self.tab_Communication = QtWidgets.QWidget()
        self.tab_Communication.setObjectName("tab_Communication")
        self.label_bgcolor_4 = QtWidgets.QLabel(self.tab_Communication)
        self.label_bgcolor_4.setGeometry(QtCore.QRect(0, 0, 780, 380))
        self.label_bgcolor_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));")
        self.label_bgcolor_4.setText("")
        self.label_bgcolor_4.setObjectName("label_bgcolor_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_Communication)
        self.groupBox_5.setGeometry(QtCore.QRect(420, 120, 351, 241))
        self.groupBox_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.groupBox_5.setObjectName("groupBox_5")
        self.comboBox_info_10 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_info_10.setGeometry(QtCore.QRect(30, 40, 180, 40))
        self.comboBox_info_10.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.comboBox_info_10.setObjectName("comboBox_info_10")
        self.comboBox_info_11 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_info_11.setGeometry(QtCore.QRect(230, 40, 100, 40))
        self.comboBox_info_11.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.comboBox_info_11.setObjectName("comboBox_info_11")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 100, 300, 120))
        self.textEdit_2.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.push_info_13 = QtWidgets.QPushButton(self.groupBox_5, clicked=lambda: self.clickMesS(uid))
        self.push_info_13.setGeometry(QtCore.QRect(300, 180, 40, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_13.setFont(font)
        self.push_info_13.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    border-image: url(Icon_pack/send.png);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_13.setText("")
        self.push_info_13.setIconSize(QtCore.QSize(20, 20))
        self.push_info_13.setObjectName("push_info_13")
        self.comboBox_info_7 = QtWidgets.QComboBox(self.tab_Communication)
        self.comboBox_info_7.setGeometry(QtCore.QRect(20, 70, 380, 40))
        self.comboBox_info_7.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.comboBox_info_7.setObjectName("comboBox_info_7")
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        c = m.cursor()
        c.execute('''select from_,subject,message from communication where to_='{}';'''.format(uid))
        global dlog
        for rec in c.fetchall():
            dlog.append(rec[0]+':'+rec[1]+':'+rec[2])
        for i in range(len(dlog)):
            self.comboBox_info_7.addItem('')
        self.textBrowser_message = QtWidgets.QTextBrowser(self.tab_Communication)
        self.textBrowser_message.setGeometry(QtCore.QRect(20, 130, 380, 70))
        self.textBrowser_message.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.textBrowser_message.setObjectName("textBrowser_message")
        self.textBrowser_response = QtWidgets.QTextBrowser(self.tab_Communication)
        self.textBrowser_response.setGeometry(QtCore.QRect(20, 220, 380, 70))
        self.textBrowser_response.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.textBrowser_response.setObjectName("textBrowser_response")
        self.push_info_9 = QtWidgets.QPushButton(self.tab_Communication, clicked = lambda: self.clickViewMes(uid))
        self.push_info_9.setGeometry(QtCore.QRect(420, 70, 80, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_9.setFont(font)
        self.push_info_9.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_9.setIconSize(QtCore.QSize(20, 20))
        self.push_info_9.setObjectName("push_info_9")
        self.comboBox_info_8 = QtWidgets.QComboBox(self.tab_Communication)
        self.comboBox_info_8.setGeometry(QtCore.QRect(100, 20, 140, 40))
        self.comboBox_info_8.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.comboBox_info_8.setObjectName("comboBox_info_8")
        for i in range(len(sublist)):
            self.comboBox_info_8.addItem("")
        self.comboBox_info_9 = QtWidgets.QComboBox(self.tab_Communication)
        self.comboBox_info_9.setGeometry(QtCore.QRect(260, 20, 140, 40))
        self.comboBox_info_9.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.comboBox_info_9.setObjectName("comboBox_info_9")
        for i in range(len(filvil)):
            self.comboBox_info_9.addItem("")
        self.label_info_9 = QtWidgets.QLabel(self.tab_Communication)
        self.label_info_9.setGeometry(QtCore.QRect(20, 20, 60, 40))
        self.label_info_9.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.label_info_9.setObjectName("label_info_9")
        self.push_info_11 = QtWidgets.QPushButton(self.tab_Communication,clicked=lambda:self.applyFilterCom(uid))
        self.push_info_11.setGeometry(QtCore.QRect(420, 20, 80, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_11.setFont(font)
        self.push_info_11.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_11.setIconSize(QtCore.QSize(20, 20))
        self.push_info_11.setObjectName("push_info_11")
        self.textEdit = QtWidgets.QTextEdit(self.tab_Communication)
        self.textEdit.setGeometry(QtCore.QRect(20, 300, 380, 70))
        self.textEdit.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.textEdit.setObjectName("textEdit")
        self.push_info_12 = QtWidgets.QPushButton(self.tab_Communication, clicked=lambda:self.respond(uid))
        self.push_info_12.setGeometry(QtCore.QRect(365, 330, 40, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_12.setFont(font)
        self.push_info_12.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    border-image: url(Icon_pack/send.png);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_12.setText("")
        self.push_info_12.setIconSize(QtCore.QSize(20, 20))
        self.push_info_12.setObjectName("push_info_12")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icon_pack/chat.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_Communication, icon5, "")
        self.tab_Survey = QtWidgets.QWidget()
        self.tab_Survey.setObjectName("tab_Survey")
        self.label_bgcolor_5 = QtWidgets.QLabel(self.tab_Survey)
        self.label_bgcolor_5.setGeometry(QtCore.QRect(0, 0, 780, 380))
        self.label_bgcolor_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));")
        self.label_bgcolor_5.setText("")
        self.label_bgcolor_5.setObjectName("label_bgcolor_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_Survey)
        self.groupBox_3.setGeometry(QtCore.QRect(15, 5, 360, 360))
        self.groupBox_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox_info_4 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_info_4.setGeometry(QtCore.QRect(30, 40, 200, 50))
        self.comboBox_info_4.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.comboBox_info_4.setObjectName("comboBox_info_4")
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        c = m.cursor()
        c.execute('select distinct target,sname from surveys;')
        global sname
        for i in c.fetchall():
            sname.append(i[0]+':'+i[1])
        m.close()
        for i in range(len(sname)+1):
            self.comboBox_info_4.addItem("")
        self.push_info_7 = QtWidgets.QPushButton(self.groupBox_3, clicked=lambda:self.clickViewSquest())
        self.push_info_7.setGeometry(QtCore.QRect(250, 45, 80, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_7.setFont(font)
        self.push_info_7.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_7.setIconSize(QtCore.QSize(20, 20))
        self.push_info_7.setObjectName("push_info_7")
        self.push_info_8 = QtWidgets.QPushButton(self.groupBox_3,clicked=lambda:self.clickViewResS())
        self.push_info_8.setGeometry(QtCore.QRect(45, 305, 270, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_8.setFont(font)
        self.push_info_8.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_8.setIconSize(QtCore.QSize(20, 20))
        self.push_info_8.setObjectName("push_info_8")
        self.comboBox_info_5 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_info_5.setGeometry(QtCore.QRect(30, 100, 300, 50))
        self.comboBox_info_5.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.comboBox_info_5.setObjectName("comboBox_info_5")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(30, 170, 300, 120))
        self.textBrowser_3.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_Survey)
        self.groupBox_4.setGeometry(QtCore.QRect(400, 5, 360, 360))
        self.groupBox_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.groupBox_4.setObjectName("groupBox_4")
        self.push_info_10 = QtWidgets.QPushButton(self.groupBox_4, clicked= lambda:self.createSurvey())
        self.push_info_10.setGeometry(QtCore.QRect(80, 300, 200, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_info_10.setFont(font)
        self.push_info_10.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_info_10.setIconSize(QtCore.QSize(20, 20))
        self.push_info_10.setObjectName("push_info_10")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 220, 50))
        self.lineEdit.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 170, 150, 50))
        self.lineEdit_2.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setMaxLength(20)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 170, 150, 50))
        self.lineEdit_3.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setMaxLength(20)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 220, 150, 50))
        self.lineEdit_4.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setMaxLength(20)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 100, 310, 50))
        self.lineEdit_5.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setMaxLength(50)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 220, 150, 50))
        self.lineEdit_6.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.lineEdit_6.setMaxLength(20)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.comboBox_info_6 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_info_6.setGeometry(QtCore.QRect(270, 40, 70, 50))
        self.comboBox_info_6.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"MS Shell Dlg 2\";")
        self.comboBox_info_6.setObjectName("comboBox_info_6")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icon_pack/followers.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.tab_Survey, icon6, "")
        self.label_uid = QtWidgets.QLabel(Form_AdminWindow)
        self.label_uid.setGeometry(QtCore.QRect(10, 5, 250, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_uid.setFont(font)
        self.label_uid.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 28pt \"Comic Sans MS\";")
        self.label_uid.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_uid.setObjectName("label_uid")
        self.label_gramopedia = QtWidgets.QLabel(Form_AdminWindow)
        self.label_gramopedia.setGeometry(QtCore.QRect(370, 5, 350, 70))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_gramopedia.setFont(font)
        self.label_gramopedia.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.label_gramopedia.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_gramopedia.setObjectName("label_gramopedia")

        ########################################
        self.label_mail = QtWidgets.QLabel(Form_AdminWindow)
        self.label_mail.setGeometry(QtCore.QRect(400, 80, 400, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(20)
        self.label_mail.setFont(font)
        self.label_mail.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(250, 250, 250, 255);\n"
"border:none;\n"
"font: 75 12pt \"Comic Sans MS\";")
        self.label_mail.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_mail.setObjectName("label_mail")
        
########################################

        self.retranslateUi(Form_AdminWindow, s, uid)
        self.tabWidget.setCurrentIndex(0)
        self.lineEdit.editingFinished.connect(self.lineEdit_5.setFocus)
        self.lineEdit_5.editingFinished.connect(self.lineEdit_3.setFocus)
        self.lineEdit_3.editingFinished.connect(self.lineEdit_2.setFocus)
        self.lineEdit_2.editingFinished.connect(self.lineEdit_6.setFocus)
        self.lineEdit_6.editingFinished.connect(self.lineEdit_4.setFocus)
        QtCore.QMetaObject.connectSlotsByName(Form_AdminWindow)

    def retranslateUi(self, Form_AdminWindow, s, uid):
        _translate = QtCore.QCoreApplication.translate
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        c = m.cursor()
        c.execute('''select name from admins where unique_id='{}';'''.format(uid))
        name = c.fetchone()[0]
        c.execute('''select desig from admins where unique_id='{}';'''.format(uid))
        desig = c.fetchone()[0]
        c.execute('select count(*) from people;')
        popc = str(c.fetchone()[0])+'+'
        c.execute('''select count(*) from people where sex = 'Male';''')
        mpopc = str(c.fetchone()[0])+'+'
        c.execute('''select count(*) from people where sex = 'Female';''')
        fpopc = str(c.fetchone()[0])+'+'
        c.execute('select count(*) from users;')
        uc = str(c.fetchone()[0])+'+'
        c.execute('select count(*) from villages;')
        vc = str(c.fetchone()[0])+'+'
        tg = ['All']
        c.execute('''select v_code  from villages;''')
        for i in c.fetchall():
            tg.append(i[0])

        m.close()
        Form_AdminWindow.setWindowTitle(_translate("Form_AdminWindow", "AdminWindow"))
        self.groupBox_infobox.setTitle(_translate("Form_AdminWindow", "I n f o r m a t i o n   B o x"))
        for i in range(len(cbinfo)):
            self.comboBox_info.setItemText(i, _translate("Form_UserWindow", cbinfo[i]))
        self.push_info.setText(_translate("Form_AdminWindow", "V i e w"))
        self.label_fpopc.setText(_translate("Form_AdminWindow", fpopc))
        self.label_desig.setText(_translate("Form_AdminWindow", desig))
        self.label_name.setText(_translate("Form_AdminWindow", name))
        self.label_mpopc.setText(_translate("Form_AdminWindow", mpopc))
        self.label_popc.setText(_translate("Form_AdminWindow", popc))
        self.label_upopc.setText(_translate("Form_AdminWindow", uc))
        self.label_vpopc.setText(_translate("Form_AdminWindow", vc))
        self.push_chpw.setText(_translate("Form_AdminWindow", "C h a n g e   P a s s w o r d"))
        self.push_logOut.setText(_translate("Form_AdminWindow", "L  o g   O u t"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Home), _translate("Form_AdminWindow", "Home"))
        self.groupBox.setTitle(_translate("Form_AdminWindow", "A d m i n s"))
        for i in range(len(adm)):
            self.comboBox_info_2.setItemText(i, _translate("Form_AdminWindow", adm[i]))
        self.push_info_2.setText(_translate("Form_AdminWindow", "V i e w"))
        self.label_info_2.setText(_translate("Form_AdminWindow", "V i e w   A d m i n   I n f o"))
        self.push_info_3.setText(_translate("Form_AdminWindow", "C r e a t e   A d m i n"))
        self.groupBox_2.setTitle(_translate("Form_AdminWindow", "V i l l a g e s"))
        for i in range(len(v_name)):
            self.comboBox_info_3.setItemText(i, _translate("Form_AdminWindow", v_name[i]))
        self.push_info_5.setText(_translate("Form_AdminWindow", "V i e w"))
        self.label_info_3.setText(_translate("Form_AdminWindow", "Block"))
        self.label_info_4.setText(_translate("Form_AdminWindow", "District"))
        self.label_info_5.setText(_translate("Form_AdminWindow", "State"))
        self.label_info_6.setText(_translate("Form_AdminWindow", "People"))
        self.label_info_7.setText(_translate("Form_AdminWindow", "Pin Code"))
        self.label_info_8.setText(_translate("Form_AdminWindow", "Altitude"))
        self.push_info_6.setText(_translate("Form_AdminWindow", "A d d   A   V i l l a g e"))
        self.push_info_4.setText(_translate("Form_AdminWindow", "V i e w   P e o p l e"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_AdminControls), _translate("Form_AdminWindow", "Admin Controls"))
        self.groupBox_5.setTitle(_translate("Form_AdminWindow", "C o m m u n i c a t e   W i t h   S a r p a n c h"))
        self.comboBox_info_10.addItem('')
        self.comboBox_info_10.setItemText(0, _translate("Form_AdminWindow", "Subject"))
        for i in range(len(cwsSub)):
            self.comboBox_info_10.addItem('')
            self.comboBox_info_10.setItemText(i+1, _translate("Form_AdminWindow", cwsSub[i]))
        self.comboBox_info_11.addItem('')
        self.comboBox_info_11.setItemText(0, _translate("Form_AdminWindow", "To"))
        for i in range(len(cwsTo)):
            self.comboBox_info_11.addItem('')
            self.comboBox_info_11.setItemText(i+1, _translate("Form_AdminWindow", cwsTo[i]))
        self.textEdit_2.setPlaceholderText(_translate("Form_AdminWindow", "Type Your Message"))
        self.textBrowser_message.setHtml(_translate("Form_AdminWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:13pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_message.setPlaceholderText(_translate("Form_AdminWindow", "No Message...."))
        self.textBrowser_response.setPlaceholderText(_translate("Form_AdminWindow", "No Response....."))
        self.push_info_9.setText(_translate("Form_AdminWindow", "V i e w"))
        for i in range(len(sublist)):
            self.comboBox_info_8.setItemText(i, _translate("Form_AdminWindow", sublist[i]))
        for i in range(len(filvil)):
            self.comboBox_info_9.setItemText(i, _translate("Form_AdminWindow", filvil[i]))
        self.label_info_9.setText(_translate("Form_AdminWindow", "Filter:"))
        self.push_info_11.setText(_translate("Form_AdminWindow", "A p p l y"))
        for i in range(len(dlog)):
            self.comboBox_info_7.setItemText(i, _translate("Form_AdminWindow", dlog[i]))
        self.textEdit.setPlaceholderText(_translate("Form_AdminWindow", "Type Your Response"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Communication), _translate("Form_AdminWindow", "Communication"))
        self.groupBox_3.setTitle(_translate("Form_AdminWindow", "P u b l i c   R e s p o n s e"))
        self.comboBox_info_4.setItemText(0, _translate("Form_AdminWindow", "Select A Survey"))
        for i in range(len(sname)):
            self.comboBox_info_4.setItemText(i+1, _translate("Form_AdminWindow",sname[i]))
        self.push_info_7.setText(_translate("Form_AdminWindow", "V i e w"))
        self.push_info_8.setText(_translate("Form_AdminWindow", "V i e w   P u b l i c   R e s p o n s e"))
        self.textBrowser_3.setHtml(_translate("Form_AdminWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:13pt; font-weight:72; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(A)    (0)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(B)    (0)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(C)    (0)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(D)    (0)</p></body></html>"))
        self.textBrowser_3.setPlaceholderText(_translate("Form_AdminWindow", "No Response....."))
        self.groupBox_4.setTitle(_translate("Form_AdminWindow", "C r e a t e   S u r v e y"))
        self.push_info_10.setText(_translate("Form_AdminWindow", "D o n e"))
        self.lineEdit.setPlaceholderText(_translate("Form_AdminWindow", "Survey Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form_AdminWindow", "(B)"))
        self.lineEdit_3.setPlaceholderText(_translate("Form_AdminWindow", "(A)"))
        self.lineEdit_4.setPlaceholderText(_translate("Form_AdminWindow", "(D)"))
        self.lineEdit_5.setPlaceholderText(_translate("Form_AdminWindow", "Question"))
        self.lineEdit_6.setPlaceholderText(_translate("Form_AdminWindow", "(C)"))
        for i in range(len(tg)):
            self.comboBox_info_6.addItem("")
            self.comboBox_info_6.setItemText(i, _translate("Form_AdminWindow", tg[i]))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Survey), _translate("Form_AdminWindow", "Survey"))
        self.label_uid.setText(_translate("Form_AdminWindow", s))
        self.label_gramopedia.setText(_translate("Form_AdminWindow", "G r a m O \' p e d i a"))
        self.textBrowser_info.setPlaceholderText(_translate("Form_AdminWindow", "Select An Option"))

        ######################################
        self.label_mail.setText(_translate("Form_AdminWindow", "                       Contact us @ gramopedia@gmail.com"))
        ######################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_AdminWindow = QtWidgets.QWidget()
    ui = Ui_Form_AdminWindow()
    ui.setupUi(Form_AdminWindow, 'A D M 0 0 1', 'ADM001')
    Form_AdminWindow.show()
    sys.exit(app.exec())
