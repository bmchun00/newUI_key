from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from getText import *
import random

QSSDialog = '''
QInputDialog{
    background-color: rgb(209, 223, 232);
}
QSpinBox {
    border : 0px;
    border-radius : 10px;
    min-width:100px;
    min-height:24px;
    background-color: #ffffff;
}
QSpinBox::up-button  {
    background-color: transparent;
}
QSpinBox::down-button  {
    background-color: transparent;
}
QPushButton {
    min-height : 24px;
    border:0px solid #ffffff;
    border-radius : 10px;
    max-width:100px;
    min-width:100px;
    background-color: rgb(249, 217, 202);
    color:#ffffff;
}
QPushButton:hover {
    min-height : 24px;
    border:0px solid #ffffff;
    border-radius : 10px;
    max-width:100px;
    min-width:100px;
    background-color: rgb(170, 217, 202);
    color:#ffffff;
}
QPushButton:pressed {
    min-height : 24px;
    border:0px solid #ffffff;
    border-radius : 10px;
    max-width:100px;
    min-width:100px;
    background-color: rgb(249, 217, 150);
    color:#ffffff;
}
'''


QSSPB = '''
QProgressBar{
    border: 1px solid white;
    border-radius: 5px;
    max-height:10px;
    min-width:150px;
}

QProgressBar::chunk {
    background-color: rgb(249, 217, 202);
    border : 0px;
    border-radius:2px;
    width: 10px;
    margin: 1px;
}
'''
QSSList = '''
QListWidget {
    border : 0px;
    border-radius : 14px;
    background-color : white;
    min-width:500px;
    min-height: 230px;
}

QListWidget::item{
    border : 0px;
    border-radius:5px;
    color:black;
    max-width : 400px;
    min-height : 30px;
}

QListWidget::item:hover{
    color:white;
    background-color : rgb(170, 217, 202);
}

QListWidget::item:selected{
    border : 0px;
    color:white;
    background-color : rgb(249, 217, 150);
}

 QScrollBar:vertical {
     border: 0px;
     border-radius:6px;
     background-color:transparent;
     width: 14px;
 }
 QScrollBar::handle:vertical {
     border: 0px;
     border-radius:3px;
     background: white;
     min-height: 20px;
     margin : 0 2px 0 2px;
     background-color : rgb(249, 217, 202);
 }
 QScrollBar::add-line:vertical {
     border: 0px;
 }

 QScrollBar::sub-line:vertical {
     border: 0px;
 }
 
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}
 QScrollBar:horizontal {
	height:0px;
 }
'''
QSSlbutton = '''
QPushButton {
    max-height : 30px;
    min-height : 30px;
    border:0px solid #ffffff;
    border-radius : 15px;
    min-width : 100px;
    max-width : 100px;
    background-color: rgb(249, 217, 202);
    color:#ffffff;
}
QPushButton:hover {
    max-height :  30px;
    min-height : 30px;
    border:0px solid #ffffff;
    border-radius : 15px;
    min-width : 100px;
    max-width : 100px;
    background-color: rgb(170, 217, 202);
    color:#ffffff;
}
QPushButton:pressed {
    max-height :  30px;
    min-height : 30px;
    border:0px solid #ffffff;
    border-radius : 15px;
    min-width : 100px;
    max-width : 100px;
    background-color: rgb(249, 217, 150);
    color:#ffffff;
}
'''


class TextPage(QtWidgets.QWidget):
    def __init__(self, type):
        super(TextPage, self).__init__()
        self.initUI(type)

    def initUI(self, type):
        self.type = type
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(90, 70, 621, 331))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(80, 80, 550, 230))
        self.frame.setStyleSheet("background-color:white;\n"
                                 "border : 0px;\n"
                                 "border-radius : 10px;")
        self.List = QtWidgets.QListWidget(self.frame)
        self.List.setGeometry(QtCore.QRect(30, 0, 500, 230))
        self.List.setStyleSheet(QSSList)
        self.additem(type)
        self.lbutton = QtWidgets.QPushButton(self)
        self.lbutton.setStyleSheet(QSSlbutton)
        self.lbutton.setGeometry(QtCore.QRect(300, 340, 102, 30))
        self.lbutton.clicked.connect(self.lbClicked)
        self.TextMainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.TextMainLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.TextMainLayout.setContentsMargins(0, 0, 0, 0)
        self.TextMainLayout.setSpacing(6)
        self.TextMainLayout.setObjectName("TextMainLayout")
        self.TextBrowserLayout = QtWidgets.QVBoxLayout()
        self.TextBrowserLayout.setObjectName("TextBrowserLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.TextBrowserLayout.addItem(spacerItem)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.Text = QtWidgets.QTextBrowser(self.verticalLayoutWidget_3)
        self.Text.setStyleSheet("border : 3px solid #ffffff;\n"
                                "border-radius : 15px;\n"
                                "max-width : 500px;\n"
                                "min-width: 500px;\n"
                                "max-height : 100px;\n"
                                "background-color: rgb(255, 255, 255);")
        self.Text.setObjectName("Text")
        self.Text.setFont(font)
        self.TextBrowserLayout.addWidget(self.Text, 0, QtCore.Qt.AlignHCenter)
        self.TextMainLayout.addLayout(self.TextBrowserLayout)
        self.TextCurrentLayout = QtWidgets.QVBoxLayout()
        self.TextCurrentLayout.setObjectName("TextCurrentLayout")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.TPMLayout = QtWidgets.QHBoxLayout()
        self.TPMLayout.setObjectName("TPMLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.TPMLayout.addItem(spacerItem1)
        self.TPM = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.TPM.setFont(font)
        self.TPM.setStyleSheet("color: rgb(255, 255, 255);")
        self.TPM.setObjectName("TPM")
        self.TPMLayout.addWidget(self.TPM)
        self.TextCurrentLayout.addLayout(self.TPMLayout)
        self.CurrencyLayout = QtWidgets.QHBoxLayout()
        self.CurrencyLayout.setObjectName("CurrencyLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.CurrencyLayout.addItem(spacerItem2)
        self.Currency = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Currency.setFont(font)
        self.Currency.setStyleSheet("color: rgb(255, 255, 255);")
        self.Currency.setObjectName("Currency")
        self.CurrencyLayout.addWidget(self.Currency)
        self.TextCurrentLayout.addLayout(self.CurrencyLayout)
        self.TextMainLayout.addLayout(self.TextCurrentLayout)
        self.InputLayout = QtWidgets.QHBoxLayout()
        self.InputLayout.setObjectName("InputLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputLayout.addItem(spacerItem3)
        self.input = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.lbutton.setFont(font)
        self.lbutton.setText('선택')
        self.input.setFont(font)
        self.input.setStyleSheet("border:1px solid #ffffff;\n"
                                 "border-radius:10px;\n"
                                 "min-width:400px;\n"
                                 "background-color:#ffffff;\n"
                                 "")
        self.input.setObjectName("input")
        self.input.setAlignment(QtCore.Qt.AlignCenter)
        self.InputLayout.addWidget(self.input)
        self.confirm = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm.setFont(font)
        self.confirm.setStyleSheet("border:1px solid #d18063;\n"
                                   "border-radius:10px;\n"
                                   "min-height:22px;\n"
                                   "background-color:#d18063;\n"
                                   "min-width:60px;\n"
                                   "color:#ffffff;\n"
                                   )
        self.confirm.setObjectName("confirm")
        self.InputLayout.addWidget(self.confirm)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.InputLayout.addItem(spacerItem4)
        self.TextMainLayout.addLayout(self.InputLayout)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_3)
        self.progressBar.setStyleSheet(QSSPB)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.TextMainLayout.addWidget(self.progressBar, 0, QtCore.Qt.AlignHCenter)

    def Listshow(self):
        self.frame.show()
        self.List.show()
        self.lbutton.show()

    def Listhide(self):
        self.frame.hide()
        self.List.hide()
        self.lbutton.hide()

    def Texthide(self):
        self.Text.hide()
        self.progressBar.hide()
        self.confirm.hide()
        self.TPM.hide()
        self.Currency.hide()
        self.input.hide()

    def Textshow(self):
        self.Text.show()
        self.progressBar.show()
        self.confirm.show()
        self.TPM.show()
        self.Currency.show()
        self.input.show()

    def lbClicked(self):
        rnum = self.List.currentRow()
        self.Listhide()
        self.Textshow()
        wid = QtWidgets.QWidget()
        wid.setStyleSheet(QSSDialog)
        if self.type == 'internal':
            self.toList = getInternal(rnum)
        if self.type == 'news':
            self.toList = getNews(self.url[rnum])
            print(self.toList)
        if self.type == 'lyrics' :
            self.toList = getLyrics(rnum)
        num, ok = QInputDialog.getInt(wid,'문장 수','<html style="font-size:12pt;font-family:''맑은 고딕'';color:''white'';">  문장 수를 입력해 주세요</html>', 1, 1, len(self.toList))
        if ok:
            self.Text.setText('아무거나 입력해 시작합니다.')
            self.progressBar.setMaximum(num)
            self.progressBar.setValue(0)
            self.progressNum = 0
            self.maxNum = num
            self.Text.setAlignment(QtCore.Qt.AlignCenter)
        else:
            self.stackWidget.setCurrentIndex(0)

    def additem(self,type):
        if type == 'internal':
            head = getInternalHead()
            for i in range(0, len(head)):
                self.List.addItem(head[i])

        if type == 'news':
            head, self.url = getNewsHead()
            for i in range(0, len(head)):
                self.List.addItem(head[i])

        if type == 'lyrics':
            head = getLyricsHead()
            for i in range(0, len(head)):
                self.List.addItem(head[i])

    prevtime = 0
    progressNum = 0
    maxNum = 0
    toList = []
    userList = []
    wrongList = []
    atList = []
