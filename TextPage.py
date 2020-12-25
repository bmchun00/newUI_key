from PyQt5 import QtCore, QtGui, QtWidgets
from getText import *
import random

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

class TextPage(QtWidgets.QWidget):
    def __init__(self, type):
        super(TextPage, self).__init__()
        self.initUI(type)

    def initUI(self, type):
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(90, 70, 621, 331))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
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
        self.input.setFont(font)
        self.input.setStyleSheet("border:1px solid #ffffff;\n"
                                 "border-radius:10px;\n"
                                 "min-width:400px;\n"
                                 "background-color:#ffffff;\n"
                                 "")
        self.input.setObjectName("input")
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
                                   "")
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

        if type == 'internal':
            self.toList = getInternal()
        if type == 'news' :
            self.toList = getNews()

    type = type
    prevtime = 0
    progressNum = 0
    maxNum = 0
    toList = []
    userList = []
    wrongList = []
    atList = []
