from PyQt6 import QtCore, QtGui, QtWidgets
from Password import Ui_Form_Password
from ViewPeople import Ui_Form_View_People
import FetchData
import mysql.connector as ms

########
m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
c = m.cursor()

cwsSub = ['Seek Information','Seek Help','Suggestion/Reform','Other']
cwsTo = []
c.execute('select desig from admins;')
for i in c.fetchall():
    cwsTo.append(i[0])

c.execute('select distinct subject from communication;')
sublist = ['By Subject', 'Unreplied']
for i in c.fetchall():
    sublist.append(i[0])

filvil = ['By Sender', 'Sent']+cwsTo
########
    
sname = []
questions = []
opt = []

cbinfo =["Search", "Literacy Stats", "Language Stats", "Employment Stats", "Population Stats"]

def comDlog(uid):
    c.execute('''select * from communication where to_='{}' or from_='{}';'''.format(uid,uid))
    dlog=list()
    for rec in c.fetchall():
        st=rec[0]+':'+rec[1]+':'+rec[2]+':'+rec[3]
        dlog.append(st)
    return dlog

def comMes(uid,dlog):
    dlog=dlog.split(':')
    c.execute('''select message,response from communication where from_='{}'
                and to_='{}' and subject='{}' and message='{}';'''.format(dlog[0],dlog[1],dlog[2],dlog[3]))
    return c.fetchone()

class Ui_Form_SarpanchWindow(object):

    def applyFilterCom(self,uid):
        _translate = QtCore.QCoreApplication.translate
        sub = self.comboBox_info_8.currentText()
        fv = self.comboBox_info_9.currentText()
        dclog = ['Select A Message']
        m = ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        c = m.cursor()
        cmd = ''
        if sub not in ['By Subject','Unreplied'] and fv not in ['By Sender', 'Sent']:
            cmd='''select from_, to_, subject, message from communication where subject = '{}' and to_ = '{}' and from_ = '{}';'''.format(sub,uid,fv)
        elif sub not in ['By Subject','Unreplied'] and fv == 'By Sender':
            cmd='''select from_, to_, subject, message from communication where subject = '{}' and to_ = '{}';'''.format(sub,uid)
        elif sub=='By Subject' and fv not in ['By Sender', 'Sent']:
            cmd='''select from_, to_, subject, message from communication where from_ = '{}' and to_ = '{}';'''.format(fv,uid)
        elif sub=='By Subject' and fv == 'By Sender':
            cmd='''select from_, to_, subject, message from communication where to_ = '{}';'''.format(uid)
        elif sub=='Unreplied' and fv not in ['By Sender', 'Sent']:
            cmd='''select from_, to_, subject, message from communication where from_ = '{}' and to_ = '{}' and response is null;'''.format(fv,uid)
        elif sub=='Unreplied' and fv == 'By Sender':
            cmd='''select from_, to_, subject, message from communication where to_ = '{}' and response is null;'''.format(uid)
        elif fv == 'Sent' and sub not in ['By Subject','Unreplied']:
            cmd='''select from_, to_, subject, message from communication where from_ = '{}' and subject = '{}';'''.format(uid, sub)
        elif fv == 'Sent' and sub=='By Subject':
            cmd='''select from_, to_, subject, message from communication where from_ = '{}';'''.format(uid)
        elif fv == 'Sent' and sub=='Unreplied':
            cmd='''select from_, to_, subject, message from communication where from_ = '{}' and response is null;'''.format(uid)
        c.execute(cmd)
        for rec in c.fetchall():
            dclog.append(rec[0]+':'+rec[1]+':'+rec[2]+':'+rec[3])
        m.close()
        self.comboBox_message.clear()
        self.textEdit.clear()
        self.textBrowser_message.clear()
        self.textBrowser_response.clear()
        for i in range(len(dclog)):
            self.comboBox_message.addItem('')
            self.comboBox_message.setItemText(i, _translate("Form_SarpanchWindow", dclog[i]))
        dclog.clear()


    def viewPeople(self, uid):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form_View_People()
        self.ui.setupUi(self.window, uid[:3])
        self.window.show()

    def respond(self, uid):
        a = self.comboBox_message.currentText()
        if a!='Select A Message':
            if not (self.textBrowser_response.toPlainText()) and a.split(':')[0]!=uid:
                if a.split(':')[1]==uid:
                    m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
                    c = m.cursor()
                    res = self.textEdit.toPlainText()[:99]
                    from_ = a.split(':')[0]
                    to_ = uid
                    sub = a.split(':')[2]
                    message = a.split(':')[3]
                    c.execute('''update communication set response = '{}' where from_='{}' and to_='{}'
                                and message='{}' and subject='{}';'''.format(res,from_,to_,message,sub))
                    m.commit()
                    m.close()
                    self.textEdit.clear()
                else:
                    self.textEdit.clear()
            else:
                self.textEdit.setText('Already Responded / Cannot reply to sent messages')
        else:
            self.textEdit.clear()                

    
    def clickMesS(self, uid):
        mes = self.textEdit_2.toPlainText()[:99]
        sub = self.comboBox_info_10.currentText()
        to = self.comboBox_info_11.currentText()
        if to!='To':
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            c = m.cursor()
            c.execute('''select unique_id from admins where desig = '{}';'''.format(to))
            to = c.fetchone()[0]
            m.close()
        if mes!='' and sub!='Subject' and to!='To':
            self.textEdit_2.clear()
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            c = m.cursor()
            c.execute('''insert into communication values ('{}','{}','{}','{}',null);'''.format(uid,to,sub,mes))
            m.commit()
            m.close()
            
    def clickViewResS(self,uid):
        s = self.comboBox_sname.currentText()
        q = self.comboBox_sque.currentText()
        if q!='' and s!='Select A Survey':
            s = s.split(':')
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            c = m.cursor()
            c.execute('''select optA,optB,optC,optD from surveys where sname='{}' and question='{}' and target = '{}';'''.format(s[0],q,s[1]))
            opt = c.fetchall()
            res = c.execute('''select A,B,C,D from surveys where sname='{}' and question='{}' and target = '{}';'''.format(s[0],q,s[1]))
            res = c.fetchall()
            m.close()
            l1 = '(A)'+opt[0][0]+'   ('+str(res[0][0])
            l2 = ')\n(B)'+opt[0][1]+'   ('+str(res[0][1])
            l3 = ')\n(C)'+opt[0][2]+'   ('+str(res[0][2])
            l4 = ')\n(D)'+opt[0][3]+'   ('+str(res[0][3])+')'
            disp = l1 + l2 + l3 + l4
            self.textBrowser_3.setText(disp)

    def clickViewSquest(self):
        _translate = QtCore.QCoreApplication.translate
        s = self.comboBox_sname.currentText()
        self.textBrowser_3.clear()
        if s!='Select A Survey':
            m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
            c = m.cursor()
            c.execute('''select question from surveys where sname='{}' and target='{}';'''.format(s.split(':')[0],s.split(':')[1]))
            global questions
            questions = c.fetchall()
            m.close()
            self.comboBox_sque.clear()
            for i in range(len(questions)):
                self.comboBox_sque.addItem("")
            for i in range(len(questions)):
                self.comboBox_sque.setItemText(i, _translate("Form_SarpanchWindow", questions[i][0]))
        else:
            self.comboBox_sque.clear()
        
    
    def clickViewInfo(self,uid):
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        c = m.cursor()
        a = self.comboBox_info.currentText()
        disp = 'Select An Option'
        self.textBrowser_info.setText(disp)
        if a=='Literacy Stats':
            c.execute('''select count(*) from people where unique_id like '{}' and education!='0';'''.format(uid[0:3]+'___'))
            alpha = c.fetchone()[0]
            c.execute('''select count(*) from people where unique_id like '{}';'''.format(uid[0:3]+'___'))
            beta = c.fetchone()[0]            
            litr = str((alpha/beta)*100)
            c.execute('''select count(*) from people where unique_id like '{}' and education='0';'''.format(uid[0:3]+'___'))
            c0 = str(c.fetchone()[0])
            c.execute('''select count(*) from people where unique_id like '{}' and education='5th';'''.format(uid[0:3]+'___'))
            c5 = str(c.fetchone()[0])
            c.execute('''select count(*) from people where unique_id like '{}' and education='10th';'''.format(uid[0:3]+'___'))
            c10 = str(c.fetchone()[0])
            c.execute('''select count(*) from people where unique_id like '{}' and education='12th';'''.format(uid[0:3]+'___'))
            c12 = str(c.fetchone()[0])
            c.execute('''select count(*) from people where unique_id like '{}' and education='UG';'''.format(uid[0:3]+'___'))
            cUG = str(c.fetchone()[0])
            c.execute('''select count(*) from people where unique_id like '{}' and education='PG';'''.format(uid[0:3]+'___'))
            cPG = str(c.fetchone()[0])
            
            disp = str('Literacy Rate: '+litr+'\nUneducated: '+c0+'\n5+ Educated: '+c5+'\n10+ Educated: '+c10+
                    '\n12+ Educated: '+c12+'\nUnder Graduates: '+cUG+'\nPost Graduates: '+cPG)
            self.textBrowser_info.setText(disp)
            
        if a=='Population Stats':
            c.execute('''select count(*) from people where unique_id like '{}' and sex='male';'''.format(uid[0:3]+'___'))
            alpha = c.fetchone()[0]
            c.execute('''select count(*) from people where unique_id like '{}' and sex='female';'''.format(uid[0:3]+'___'))
            beta = c.fetchone()[0]
            c.execute('''select count(*) from people where unique_id like '{}' and sex='other';'''.format(uid[0:3]+'___'))
            delta = c.fetchone()[0]
            c.execute('''select dob from people where unique_id like '{}';'''.format(uid[:3]+'___'))
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
            c.execute('''select lang from people where unique_id like '{}';'''.format(uid[:3]+'___'))
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
            c.execute('''select distinct occ from people where unique_id like '{}';'''.format(uid[:3]+'___'))
            zeta = []
            meta = dict()
            for i in c.fetchall():
                zeta.append(i[0])
            c.execute('''select occ from people where unique_id like '{}';'''.format(uid[:3]+'___'))
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

    def clickLogOut(self):
        print('Logged Out')
        Form_SarpanchWindow.close()

    def clickPW(self,uid):
        self.window =QtWidgets.QWidget()
        self.ui = Ui_Form_Password()
        self.ui.setupUi(self.window, 'ChangeP', uid)
        self.window.show()

    def clickViewMes(self,uid):
        self.textEdit.clear()
        self.textBrowser_message.clear()
        self.textBrowser_response.clear()
        a = self.comboBox_message.currentText()
        if a!='Select A Message':
            jkl = comMes(uid,a)
            self.textBrowser_message.setText('Subject : '+a.split(':')[2]+'\n'+jkl[0])
            self.textBrowser_response.setText(jkl[1])     


    def setupUi(self, Form_SarpanchWindow, s, uid):
        mi=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        ci = mi.cursor()
        global filvil
        ci.execute('''select unique_id from users where v_code = '{}';'''.format(uid[:3]))
        for i in ci.fetchall():
            filvil.append(i[0])
        mi.close
        Form_SarpanchWindow.setObjectName("Form_SarpanchWindow")
        Form_SarpanchWindow.resize(800, 500)
        Form_SarpanchWindow.setMinimumSize(QtCore.QSize(800, 500))
        Form_SarpanchWindow.setMaximumSize(QtCore.QSize(800, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/menu.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_SarpanchWindow.setWindowIcon(icon)
        self.tabWidget_UserWindow = QtWidgets.QTabWidget(Form_SarpanchWindow)
        self.tabWidget_UserWindow.setGeometry(QtCore.QRect(10, 80, 780, 410))
        self.tabWidget_UserWindow.setStyleSheet("color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"")
        self.tabWidget_UserWindow.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tabWidget_UserWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget_UserWindow.setTabBarAutoHide(False)
        self.tabWidget_UserWindow.setObjectName("tabWidget_UserWindow")
        self.tab_home = QtWidgets.QWidget()
        self.tab_home.setObjectName("tab_home")
        self.label_village = QtWidgets.QLabel(self.tab_home)
        self.label_village.setGeometry(QtCore.QRect(50, 20, 325, 60))
        self.label_village.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 28pt \"Comic Sans MS\";")
        self.label_village.setObjectName("label_village")
        self.label_bgwhite = QtWidgets.QLabel(self.tab_home)
        self.label_bgwhite.setGeometry(QtCore.QRect(0, 0, 800, 410))
        self.label_bgwhite.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));")
        self.label_bgwhite.setText("")
        self.label_bgwhite.setObjectName("label_bgwhite")
        self.label_alt = QtWidgets.QLabel(self.tab_home)
        self.label_alt.setGeometry(QtCore.QRect(620, -14, 81, 80))
        self.label_alt.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"font: 75 14pt \"Comic Sans MS\";\n"
"border:none;\n"
"border-bottom:5px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.label_alt.setObjectName("label_alt")
        self.label_mount = QtWidgets.QLabel(self.tab_home)
        self.label_mount.setGeometry(QtCore.QRect(550, 0, 100, 80))
        self.label_mount.setStyleSheet("border-image: url(Icon_pack/mountain.png);")
        self.label_mount.setText("")
        self.label_mount.setObjectName("label_mount")
        self.label_block = QtWidgets.QLabel(self.tab_home)
        self.label_block.setGeometry(QtCore.QRect(50, 90, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_block.setFont(font)
        self.label_block.setStyleSheet("color: rgba(255, 255, 255, 255);\n"
"font: 75 13pt \"Comic Sans MS\";\n")
        self.label_block.setObjectName("label_block")
        self.label_dist = QtWidgets.QLabel(self.tab_home)
        self.label_dist.setGeometry(QtCore.QRect(140, 90, 120, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dist.setFont(font)
        self.label_dist.setStyleSheet("color: rgba(255, 255, 255, 255);\n"
"font: 75 13pt \"Comic Sans MS\";\n")
        self.label_dist.setObjectName("label_dist")
        self.label_state = QtWidgets.QLabel(self.tab_home)
        self.label_state.setGeometry(QtCore.QRect(240, 90, 140, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_state.setFont(font)
        self.label_state.setStyleSheet("color: rgba(255, 255, 255, 255);\n"
"font: 75 13pt \"Comic Sans MS\";\n")
        self.label_state.setObjectName("label_state")
        self.label_pop = QtWidgets.QLabel(self.tab_home)
        self.label_pop.setGeometry(QtCore.QRect(500, 150, 80, 80))
        self.label_pop.setStyleSheet("border-image: url(Icon_pack/group.png);")
        self.label_pop.setText("")
        self.label_pop.setObjectName("label_pop")
        self.label_fpop = QtWidgets.QLabel(self.tab_home)
        self.label_fpop.setGeometry(QtCore.QRect(510, 300, 70, 70))
        self.label_fpop.setStyleSheet("border-image: url(Icon_pack/female.png);")
        self.label_fpop.setText("")
        self.label_fpop.setObjectName("label_fpop")
        self.label_mpop = QtWidgets.QLabel(self.tab_home)
        self.label_mpop.setGeometry(QtCore.QRect(510, 220, 70, 70))
        self.label_mpop.setStyleSheet("border-image: url(Icon_pack/male.png);")
        self.label_mpop.setText("")
        self.label_mpop.setObjectName("label_mpop")
        self.label_popc = QtWidgets.QLabel(self.tab_home)
        self.label_popc.setGeometry(QtCore.QRect(590, 160, 100, 50))
        self.label_popc.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.label_popc.setObjectName("label_popc")
        self.label_mpopc = QtWidgets.QLabel(self.tab_home)
        self.label_mpopc.setGeometry(QtCore.QRect(590, 240, 100, 50))
        self.label_mpopc.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.label_mpopc.setObjectName("label_mpopc")
        self.label_fpopc = QtWidgets.QLabel(self.tab_home)
        self.label_fpopc.setGeometry(QtCore.QRect(590, 320, 100, 50))
        self.label_fpopc.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: rgba(255, 255, 255, 255);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"\n"
"padding-bottom:7px;")
        self.label_fpopc.setObjectName("label_fpopc")
        self.groupBox_infobox = QtWidgets.QGroupBox(self.tab_home)
        self.groupBox_infobox.setGeometry(QtCore.QRect(50, 160, 400, 220))
        self.groupBox_infobox.setStyleSheet("color: qlineargradient(spread:repeat, x1:0, y1:0.398, x2:1, y2:0.420455, stop:0 rgba(227, 69, 69, 223), stop:0.531073 rgba(232, 61, 147, 232), stop:0.960452 rgba(41, 90, 180, 238));")
        self.groupBox_infobox.setObjectName("groupBox_infobox")
        #######################################
        self.textBrowser_info = QtWidgets.QTextBrowser(self.groupBox_infobox)
        self.textBrowser_info.setGeometry(QtCore.QRect(25, 100, 350, 100))
        self.textBrowser_info.setStyleSheet("background-color:rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"border-radius:15px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.textBrowser_info.setObjectName("textBrowser_info")
        #######################################
        self.comboBox_info = QtWidgets.QComboBox(self.groupBox_infobox)
        self.comboBox_info.setGeometry(QtCore.QRect(30, 40, 200, 50))
        self.comboBox_info.setStyleSheet("background-color:rgba(255, 255, 255, 50);\n"
"color: qlineargradient(spread:repeat, x1:0, y1:0.398, x2:1, y2:0.420455, stop:0 rgba(227, 69, 69, 223), stop:0.531073 rgba(232, 61, 147, 232), stop:0.960452 rgba(41, 90, 180, 238));\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.comboBox_info.setObjectName("comboBox_info")
        for i in range(len(cbinfo)):
            self.comboBox_info.addItem("")
        self.push_info = QtWidgets.QPushButton(self.groupBox_infobox,clicked=lambda:self.clickViewInfo(uid))
        self.push_info.setGeometry(QtCore.QRect(240, 45, 80, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_info.setFont(font)
        self.push_info.setStyleSheet("QPushButton#push_info{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#push_info:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#push_info:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Icon_pack/loupe.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.push_info.setIcon(icon1)
        self.push_info.setIconSize(QtCore.QSize(20, 20))
        self.push_info.setObjectName("push_info")
        self.label_bgwhite.raise_()
        self.label_village.raise_()
        self.label_alt.raise_()
        self.label_mount.raise_()
        self.label_block.raise_()
        self.label_dist.raise_()
        self.label_state.raise_()
        self.label_pop.raise_()
        self.label_fpop.raise_()
        self.label_mpop.raise_()
        self.label_popc.raise_()
        self.label_mpopc.raise_()
        self.label_fpopc.raise_()
        self.groupBox_infobox.raise_()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icon_pack/home.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget_UserWindow.addTab(self.tab_home, icon2, "")
        self.tab_myacc = QtWidgets.QWidget()
        self.tab_myacc.setObjectName("tab_myacc")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icon_pack/user (2).png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.push_chpw = QtWidgets.QPushButton(self.tab_myacc,clicked=lambda:self.clickPW(uid))
        self.push_chpw.setGeometry(QtCore.QRect(230, 220, 280, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_chpw.setFont(font)
        self.push_chpw.setStyleSheet("QPushButton#push_chpw{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#push_chpw:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#push_chpw:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Icon_pack/key.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.push_chpw.setIcon(icon5)
        self.push_chpw.setIconSize(QtCore.QSize(20, 20))
        self.push_chpw.setObjectName("push_chpw")
        self.push_logout = QtWidgets.QPushButton(self.tab_myacc,clicked=lambda:self.clickLogOut())
        self.push_logout.setGeometry(QtCore.QRect(125, 320, 500, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_logout.setFont(font)
        self.push_logout.setStyleSheet("QPushButton#push_logout{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#push_logout:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#push_logout:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Icon_pack/log-out.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.push_logout.setIcon(icon6)
        self.push_logout.setIconSize(QtCore.QSize(20, 20))
        self.push_logout.setObjectName("push_logout")
        self.label_bgcolor_2 = QtWidgets.QLabel(self.tab_myacc)
        self.label_bgcolor_2.setGeometry(QtCore.QRect(0, 0, 800, 410))
        self.label_bgcolor_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));")
        self.label_bgcolor_2.setText("")
        self.label_bgcolor_2.setObjectName("label_bgcolor_2")
        self.label_bgcolor_2.raise_()
        self.push_chpw.raise_()
        self.push_logout.raise_()
        self.tabWidget_UserWindow.addTab(self.tab_myacc, icon3, "")
        self.tab_Communication = QtWidgets.QWidget()
        self.tab_Communication.setObjectName("tab_Communication")
        ##########################################################
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_Communication)
        self.groupBox_5.setGeometry(QtCore.QRect(390, 120, 350, 240))
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

        self.textEdit = QtWidgets.QTextEdit(self.tab_Communication)
        self.textEdit.setGeometry(QtCore.QRect(20, 300, 350, 70))
        self.textEdit.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.textEdit.setObjectName("textEdit")
        self.push_info_12 = QtWidgets.QPushButton(self.tab_Communication, clicked=lambda:self.respond(uid))
        self.push_info_12.setGeometry(QtCore.QRect(335, 330, 40, 40))
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

        self.comboBox_info_8 = QtWidgets.QComboBox(self.tab_Communication)
        self.comboBox_info_8.setGeometry(QtCore.QRect(90, 20, 140, 40))
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
        self.comboBox_info_9.setGeometry(QtCore.QRect(250, 20, 140, 40))
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
        self.label_info_9.setGeometry(QtCore.QRect(10, 20, 60, 40))
        self.label_info_9.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.label_info_9.setObjectName("label_info_9")
        self.push_info_11 = QtWidgets.QPushButton(self.tab_Communication,clicked=lambda:self.applyFilterCom(uid))
        self.push_info_11.setGeometry(QtCore.QRect(410, 20, 80, 40))
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
        
        ##########################################################
        self.comboBox_message = QtWidgets.QComboBox(self.tab_Communication)
        self.comboBox_message.setGeometry(QtCore.QRect(20, 70, 350, 50))
        self.comboBox_message.setStyleSheet("background-color:rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.comboBox_message.setObjectName("comboBox_message")
        for i in range(len(comDlog(uid))+1):        
            self.comboBox_message.addItem("")
        self.push_viewm = QtWidgets.QPushButton(self.tab_Communication,clicked = lambda: self.clickViewMes(uid))
        self.push_viewm.setGeometry(QtCore.QRect(400, 75, 140, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_viewm.setFont(font)
        self.push_viewm.setStyleSheet("QPushButton#push_viewm{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#push_viewm:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#push_viewm:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_viewm.setIcon(icon1)
        self.push_viewm.setIconSize(QtCore.QSize(20, 20))
        self.push_viewm.setObjectName("push_viewm")
        self.textBrowser_message = QtWidgets.QTextBrowser(self.tab_Communication)
        self.textBrowser_message.setGeometry(QtCore.QRect(20, 120, 350, 80))
        self.textBrowser_message.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.textBrowser_message.setObjectName("textBrowser_message")
        self.textBrowser_response = QtWidgets.QTextBrowser(self.tab_Communication)
        self.textBrowser_response.setGeometry(QtCore.QRect(20, 210, 350, 80))
        self.textBrowser_response.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.textBrowser_response.setObjectName("textBrowser_response")
        self.label_bgcolor_3 = QtWidgets.QLabel(self.tab_Communication)
        self.label_bgcolor_3.setGeometry(QtCore.QRect(0, 0, 800, 410))
        self.label_bgcolor_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));")
        self.label_bgcolor_3.setText("")
        self.label_bgcolor_3.setObjectName("label_bgcolor_3")
        self.label_bgcolor_3.raise_()
        self.comboBox_message.raise_()
        self.push_viewm.raise_()
        self.textBrowser_message.raise_()
        self.textBrowser_response.raise_()
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("Icon_pack/chat.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget_UserWindow.addTab(self.tab_Communication, icon8, "")
        self.tab_survey = QtWidgets.QWidget()
        self.tab_survey.setObjectName("tab_survey")
        self.comboBox_sname = QtWidgets.QComboBox(self.tab_survey)
        self.comboBox_sname.setGeometry(QtCore.QRect(60, 70, 391, 40))
        self.comboBox_sname.setStyleSheet("background-color:rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.comboBox_sname.setObjectName("comboBox_sname")
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        c = m.cursor()
        c.execute('''select distinct sname, target from surveys where target in ('All','{}');'''.format(uid[:3]))
        global sname
        sk = c.fetchall()
        for i in sk:
            sname.append(i[0]+':'+i[1])
        m.close()
        for i in range(len(sname)+1):
            self.comboBox_sname.addItem("")
        self.comboBox_sque = QtWidgets.QComboBox(self.tab_survey)
        self.comboBox_sque.setGeometry(QtCore.QRect(60, 130, 391, 40))
        self.comboBox_sque.setStyleSheet("background-color:rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.comboBox_sque.setObjectName("comboBox_sque")
        global questions
        for i in range(len(questions)):
            self.comboBox_sque.addItem("")
        self.push_viewS = QtWidgets.QPushButton(self.tab_survey,clicked=lambda:self.clickViewSquest())
        self.push_viewS.setGeometry(QtCore.QRect(480, 70, 200, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_viewS.setFont(font)
        self.push_viewS.setStyleSheet("QPushButton#push_viewS{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#push_viewS:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#push_viewS:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_viewS.setObjectName("push_viewS")
        self.push_viewResS = QtWidgets.QPushButton(self.tab_survey,clicked=lambda:self.clickViewResS(uid))
        self.push_viewResS.setGeometry(QtCore.QRect(480, 130, 220, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.push_viewResS.setFont(font)
        self.push_viewResS.setStyleSheet("QPushButton#push_viewResS{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#push_viewResS:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#push_viewResS:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}")
        self.push_viewResS.setObjectName("push_viewResS")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_survey)
        self.textBrowser_3.setGeometry(QtCore.QRect(60, 190, 391, 171))
        self.textBrowser_3.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_bgcolor_4 = QtWidgets.QLabel(self.tab_survey)
        self.label_bgcolor_4.setGeometry(QtCore.QRect(0, 0, 800, 410))
        self.label_bgcolor_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));")
        self.label_bgcolor_4.setText("")
        self.label_bgcolor_4.setObjectName("label_bgcolor_4")
        self.label_bgcolor_4.raise_()
        self.comboBox_sname.raise_()
        self.comboBox_sque.raise_()
        self.push_viewS.raise_()
        self.push_viewResS.raise_()
        self.textBrowser_3.raise_()
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Icon_pack/dashboard.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget_UserWindow.addTab(self.tab_survey, icon9, "")
        self.label_uid = QtWidgets.QLabel(Form_SarpanchWindow)
        self.label_uid.setGeometry(QtCore.QRect(530, 0, 250, 70))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
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
        self.label_bgcolor = QtWidgets.QLabel(Form_SarpanchWindow)
        self.label_bgcolor.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.label_bgcolor.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));")
        self.label_bgcolor.setText("")
        self.label_bgcolor.setObjectName("label_bgcolor")
        self.label_logo = QtWidgets.QLabel(Form_SarpanchWindow)
        self.label_logo.setGeometry(QtCore.QRect(10, 5, 70, 70))
        self.label_logo.setStyleSheet("border-image: url(Icon_pack/Gramopedia_logo.jpg);")
        self.label_logo.setText("")
        self.label_logo.setObjectName("label_logo")
        self.label_gramopedia = QtWidgets.QLabel(Form_SarpanchWindow)
        self.label_gramopedia.setGeometry(QtCore.QRect(80, 5, 350, 70))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
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
"font: 75 28pt \"Comic Sans MS\";")
        self.label_gramopedia.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_gramopedia.setObjectName("label_gramopedia")
        self.label_bgcolor.raise_()
        self.tabWidget_UserWindow.raise_()
        self.label_uid.raise_()
        self.label_logo.raise_()
        self.label_gramopedia.raise_()

        ########################################
        self.label_mail = QtWidgets.QLabel(Form_SarpanchWindow)
        self.label_mail.setGeometry(QtCore.QRect(380, 465, 400, 20))
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
        
        ##################
        
        self.groupBox_5.raise_()
        self.comboBox_info_8.raise_()
        self.comboBox_info_9.raise_()
        self.label_info_9.raise_()
        self.push_info_11.raise_()
        self.textEdit.raise_()
        self.push_info_12.raise_()

        ##################

        ###########33333
        self.label_mail.raise_()
        ###########33333333333333333

        self.push_info_4 = QtWidgets.QPushButton(self.tab_myacc, clicked=lambda:self.viewPeople(uid))
        self.push_info_4.setGeometry(QtCore.QRect(220, 100, 300, 40))
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
        
        ##################
        
        self.retranslateUi(Form_SarpanchWindow, s, uid)
        self.tabWidget_UserWindow.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form_SarpanchWindow)

    def retranslateUi(self, Form_SarpanchWindow, s, uid):
        _translate = QtCore.QCoreApplication.translate
        Form_SarpanchWindow.setWindowTitle(_translate("Form_SarpanchWindow", "SarpanchWindow"))
        self.label_village.setText(_translate("Form_SarpanchWindow", FetchData.info(uid)[0]))
        self.label_alt.setText(_translate("Form_SarpanchWindow", FetchData.info(uid)[1]))
        self.label_block.setText(_translate("Form_SarpanchWindow", FetchData.info(uid)[2]))
        self.label_dist.setText(_translate("Form_SarpanchWindow", FetchData.info(uid)[3]))
        self.label_state.setText(_translate("Form_SarpanchWindow", FetchData.info(uid)[4]))
        self.label_popc.setText(_translate("Form_SarpanchWindow", FetchData.pop(uid)[0]))
        self.label_mpopc.setText(_translate("Form_SarpanchWindow", FetchData.pop(uid)[1]))
        self.label_fpopc.setText(_translate("Form_SarpanchWindow", FetchData.pop(uid)[2]))
        self.groupBox_infobox.setTitle(_translate("Form_SarpanchWindow", "I n f o r m a t i o n   B o x"))
        for i in range(len(cbinfo)):
            self.comboBox_info.setItemText(i, _translate("Form_SarpanchWindow", cbinfo[i]))
        self.push_info.setText(_translate("Form_SarpanchWindow", "V i e w"))
        self.tabWidget_UserWindow.setTabText(self.tabWidget_UserWindow.indexOf(self.tab_home), _translate("Form_SarpanchWindow", "Home"))
        self.push_chpw.setText(_translate("Form_SarpanchWindow", "C h a n g e   P a s s w o r d"))
        self.push_logout.setText(_translate("Form_SarpanchWindow", "L o g   O u t"))
        self.tabWidget_UserWindow.setTabText(self.tabWidget_UserWindow.indexOf(self.tab_myacc), _translate("Form_SarpanchWindow", "Controls"))
        self.comboBox_message.setItemText(0, _translate("Form_SarpanchWindow", "Select A Message"))
        jkl = comDlog(uid)
        for i in range(len(jkl)):
            self.comboBox_message.setItemText(i+1, _translate("Form_SarpanchWindow", jkl[i]))
        self.push_viewm.setText(_translate("Form_SarpanchWindow", "V i e w"))
        self.textBrowser_message.setHtml(_translate("Form_SarpanchWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:13pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_message.setPlaceholderText(_translate("Form_SarpanchWindow", "No Message...."))
        self.textBrowser_response.setPlaceholderText(_translate("Form_SarpanchWindow", "No Response....."))
        self.tabWidget_UserWindow.setTabText(self.tabWidget_UserWindow.indexOf(self.tab_Communication), _translate("Form_SarpanchWindow", "Communication"))
        self.comboBox_sname.setItemText(0, _translate("Form_SarpanchWindow", "Select A Survey"))
        for i in range(len(sname)):
            self.comboBox_sname.setItemText(i+1, _translate("Form_SarpanchWindow",sname[i]))
        self.push_viewS.setText(_translate("Form_SarpanchWindow", "V i e w"))
        self.push_viewResS.setText(_translate("Form_SarpanchWindow", "V i e w   P u b l i c   R e s p o n s e"))
        self.textBrowser_3.setPlaceholderText(_translate("Form_SarpanchWindow", "No Response....."))
        self.tabWidget_UserWindow.setTabText(self.tabWidget_UserWindow.indexOf(self.tab_survey), _translate("Form_SarpanchWindow", "Survey"))
        self.label_uid.setText(_translate("Form_SarpanchWindow", s))
        self.label_gramopedia.setText(_translate("Form_SarpanchWindow", "G r a m O \' p e d i a"))
        ##################################
        self.groupBox_5.setTitle(_translate("Form_SarpanchWindow", "C o m m u n i c a t e   W i t h   A d m i n"))
        self.comboBox_info_10.addItem('')
        self.comboBox_info_10.setItemText(0, _translate("Form_SarpanchWindow", "Subject"))
        for i in range(len(cwsSub)):
            self.comboBox_info_10.addItem('')
            self.comboBox_info_10.setItemText(i+1, _translate("Form_SarpanchWindow", cwsSub[i]))
        self.comboBox_info_11.addItem('')
        self.comboBox_info_11.setItemText(0, _translate("Form_SarpanchWindow", "To"))
        for i in range(len(cwsTo)):
            self.comboBox_info_11.addItem('')
            self.comboBox_info_11.setItemText(i+1, _translate("Form_SarpanchWindow", cwsTo[i]))
        self.textEdit_2.setPlaceholderText(_translate("Form_SarpanchWindow", "Type Your Message"))        
        self.textEdit.setPlaceholderText(_translate("Form_SarpanchWindow", "Type Your Response"))
        self.push_info_4.setText(_translate("Form_SarpanchWindow", "V i e w   P e o p l e"))
        self.textEdit.setPlaceholderText(_translate("Form_SarpanchWindow", "Type Your Response"))
        for i in range(len(sublist)):
            self.comboBox_info_8.setItemText(i, _translate("Form_SarpanchWindow", sublist[i]))
        for i in range(len(filvil)):
            self.comboBox_info_9.setItemText(i, _translate("Form_SarpanchWindow", filvil[i]))
        self.label_info_9.setText(_translate("Form_SarpanchWindow", "Filter:"))
        self.push_info_11.setText(_translate("Form_SarpanchWindow", "A p p l y"))
        self.textBrowser_info.setPlaceholderText(_translate("Form_SarpanchWindow", "Select An Option"))
        ##################################

         ######################################
        self.label_mail.setText(_translate("Form_SarpanchWindow", "                       Contact us @ gramopedia@gmail.com"))
        ######################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_SarpanchWindow = QtWidgets.QWidget()
    ui = Ui_Form_SarpanchWindow()
    ui.setupUi(Form_SarpanchWindow,'U S K 0 0 0','CPR000')
    Form_SarpanchWindow.show()
    sys.exit(app.exec())
