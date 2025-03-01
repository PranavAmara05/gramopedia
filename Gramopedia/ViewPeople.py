from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as ms

class Ui_Form_View_People(object):

    def clickView(self, mode):        
        _translate = QtCore.QCoreApplication.translate
        a = self.comboBox_Villages.currentText()
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        cur = m.cursor()
        if mode == 'a':
            if a[:3]=='ALL':
                cur.execute('''select name,unique_id,aadhar,contact,dob,sex from people order by unique_id;'''.format())
            else:
                cur.execute('''select name,unique_id,aadhar,contact,dob,sex from people where unique_id like
                                  '{}' order by unique_id;'''.format(a[:3]+'___'))
        else:
            if a[:3]=='ALL':
                cur.execute('''select name,unique_id,aadhar,contact,dob,sex from people where unique_id like
                                  '{}' order by unique_id;'''.format(mode+'___'))
            else:
                cur.execute('''select name,unique_id,aadhar,contact,dob,sex from people where unique_id = 
                                  '{}';'''.format(a))
        p = cur.fetchall()
        m.close()
        self.tableWidget.setRowCount(len(p))
        for i in range(len(p)):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
            self.tableWidget.verticalHeaderItem(i).setText(_translate("Form_View_People", str(i)))
            for j in range(6):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(i, j, item)
                item = self.tableWidget.item(i, j)
                item.setText(_translate("Form_View_People", str(p[i][j])))        
        self.label_total.setText(_translate("Form_View_People", "Total: "+str(len(p))))

        
    def setupUi(self, Form_View_People,  mode):
        ##########################################
        m=ms.connect(host='localhost',user='root',password='root',database='gramopedia')
        c = m.cursor()
        if mode == 'a':
            c.execute('select v_code,v_name from villages;')
            v_name = ['ALL Villages']
            for i in c.fetchall():
                v_name.append(i[0]+'  '+i[1])
            gpass = v_name
        else:
            c.execute('''select unique_id from users where v_code = '{}';'''.format(mode))
            u_list = ['ALL Users']
            for i in c.fetchall():
                u_list.append(i[0])
            gpass = u_list
        m.close()
        ##########################################
        Form_View_People.setObjectName("Form_View_People")
        Form_View_People.resize(800, 500)
        Form_View_People.setMinimumSize(QtCore.QSize(800, 500))
        Form_View_People.setMaximumSize(QtCore.QSize(800, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon_pack/followers.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form_View_People.setWindowIcon(icon)
        Form_View_People.setStyleSheet("")
        self.label_bgwhite = QtWidgets.QLabel(Form_View_People)
        self.label_bgwhite.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.label_bgwhite.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.label_bgwhite.setText("")
        self.label_bgwhite.setObjectName("label_bgwhite")
        self.tableWidget = QtWidgets.QTableWidget(Form_View_People)
        self.tableWidget.setGeometry(QtCore.QRect(30, 200, 750, 230))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tableWidget.setFont(font)
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tableWidget.setAcceptDrops(False)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("background-color:rgba(255, 255, 255, 50);\n"
"font: 75 10pt \"Comic Sans MS\";\n"
"selection-background-color: rgb(0, 0, 0, 120);\n"
"selection-color: rgb(255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:2px;")
        self.tableWidget.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(True)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDefaultDropAction(QtCore.Qt.DropAction.IgnoreAction)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.TextElideMode.ElideLeft)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        for i in range(6):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setFamily("Comic Sans MS")
            font.setPointSize(10)
            font.setBold(False)
            font.setWeight(50)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label_bgcolor_2 = QtWidgets.QLabel(Form_View_People)
        self.label_bgcolor_2.setGeometry(QtCore.QRect(10, 170, 780, 320))
        self.label_bgcolor_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));\n"
"border-top:5px solid rgba(255, 255, 255, 255);")
        self.label_bgcolor_2.setText("")
        self.label_bgcolor_2.setObjectName("label_bgcolor_2")
        self.label_bgcolor_3 = QtWidgets.QLabel(Form_View_People)
        self.label_bgcolor_3.setGeometry(QtCore.QRect(10, 10, 780, 480))
        self.label_bgcolor_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.0170455, y1:0.858, x2:1, y2:0.181818, stop:0.102273 rgba(0, 255, 201, 248), stop:0.539773 rgba(140, 50, 255, 252), stop:0.920455 rgba(230, 0, 214, 245));")
        self.label_bgcolor_3.setText("")
        self.label_bgcolor_3.setObjectName("label_bgcolor_3")
        self.comboBox_Villages = QtWidgets.QComboBox(Form_View_People)
        self.comboBox_Villages.setGeometry(QtCore.QRect(150, 90, 300, 50))
        self.comboBox_Villages.setStyleSheet("background-color:rgba(255, 255, 255, 20);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.comboBox_Villages.setObjectName("comboBox_Villages")
        self.label_name = QtWidgets.QLabel(Form_View_People)
        self.label_name.setGeometry(QtCore.QRect(200, 0, 400, 60))
        self.label_name.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));\n"
"border:none;\n"
"padding-bottom:7px;\n"
"font: 75 28pt \"Comic Sans MS\";")
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.push_View = QtWidgets.QPushButton(Form_View_People, clicked = lambda: self.clickView(mode))
        self.push_View.setGeometry(QtCore.QRect(500, 95, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.push_View.setFont(font)
        self.push_View.setStyleSheet("QPushButton{\n"
"    font: 75 12pt \"Comic Sans MS\";\n"
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
        self.push_View.setIconSize(QtCore.QSize(20, 20))
        self.push_View.setObjectName("push_View")
        self.label_total = QtWidgets.QLabel(Form_View_People)
        self.label_total.setGeometry(QtCore.QRect(650, 440, 120, 40))
        self.label_total.setStyleSheet("background-color:rgba(255, 255, 255, 0);\n"
"color:rgba(255, 255, 255, 255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"padding-bottom:7px;\n"
"font: 75 13pt \"Comic Sans MS\";")
        self.label_total.setObjectName("label_total")
        self.label_bgwhite.raise_()
        self.label_bgcolor_3.raise_()
        self.label_bgcolor_2.raise_()
        self.tableWidget.raise_()
        self.comboBox_Villages.raise_()
        self.label_name.raise_()
        self.push_View.raise_()
        self.label_total.raise_()

        self.retranslateUi(Form_View_People, mode, gpass)
        QtCore.QMetaObject.connectSlotsByName(Form_View_People)

    def retranslateUi(self, Form_View_People, mode, gpass):
        _translate = QtCore.QCoreApplication.translate
        Form_View_People.setWindowTitle(_translate("Form_View_People", "View People"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_View_People", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_View_People", "Unique ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form_View_People", "Aadhar"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form_View_People", "Contact"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form_View_People", "D.O.B."))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form_View_People", "Gender"))
        for i in range(len(gpass)):
            self.comboBox_Villages.addItem("")
            self.comboBox_Villages.setItemText(i, _translate("Form_AdminWindow", gpass[i]))
        self.label_name.setText(_translate("Form_View_People", "V I E W   P E O P L E"))
        self.push_View.setText(_translate("Form_View_People", "V i e w"))
        self.label_total.setText(_translate("Form_View_People", "Total: 0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_View_People = QtWidgets.QWidget()
    ui = Ui_Form_View_People()
    ui.setupUi(Form_View_People, 'a')
    Form_View_People.show()
    sys.exit(app.exec())
