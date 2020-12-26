from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import time
import os,glob
from TextPage import TextPage
from StatPage import StatPage
from getText import getLyrics
import random
import re


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

QSSTopButton = '''
QPushButton {
    min-height : 50px;
    border:1px solid #ffffff;
    border-radius : 15px;
    min-width : 100px;
    background-color: rgb(249, 217, 202);
    color:#ffffff;
}
QPushButton:hover {
    min-height : 50px;
    border:1px solid #ffffff;
    border-radius : 15px;
    min-width : 100px;
    background-color: rgb(170, 217, 202);
    color:#ffffff;
}
QPushButton:pressed {
    min-height : 50px;
    border:1px solid #ffffff;
    border-radius : 15px;
    min-width : 100px;
    background-color: rgb(249, 217, 150);
    color:#ffffff;
}
'''

mainContent = '''<p align="center">
PyQT5 기반 타자연습 프로그램 <br>
디자인을 대폭 수정했습니다. <br>
Internal Text에서 내부 텍스트를 불러올 수 있습니다.<br>
News에서 최신 랜덤 뉴스를 불러올 수 있습니다.<br>
Lyrics에서 멜론 Top50 랜덤 곡의 가사를 불러올 수 있습니다.<br><br><br><br>
이쯤에 잡다한 링크 등 넣을 예정</p>
'''

def writeTxt(at, wrong):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    flist = glob.glob(BASE_DIR + '\\record\stat.bstat')
    if not flist:
        tf = open(BASE_DIR+'\\record\stat.bstat',"w", encoding='UTF-8')
    else:
        tf = open(BASE_DIR+'\\record\stat.bstat',"a", encoding='UTF-8')
    tf.write(str(time.strftime('%Y%m%d%H%M',time.localtime(time.time())))+" "+str(at)+" "+str(wrong)+"\n")

def getAt(cor, time, wrong):
    base, cho, jung = 44032,588,28
    cnt = 0
    cl = list(cor)
    while cl:
        tmp = cl.pop(0)
        if re.match('.*[ㄱ-ㅎㅏ-ㅣ가-힣]+.*',tmp) is not None:
            char_code = ord(tmp) -base
            char1 = int(char_code/cho)
            char2 = int((char_code-cho*char1)/jung)
            char3 = int((char_code-cho*char1-jung*char2))
            cnt+=1
            if char2 != 0:
                cnt+=1
            if char3 != 0:
                cnt+=1
        else:
            cnt+=1
    return cnt/time*60*wrong/100

def getWrong(user, cor):
    cnt = 0
    lc = len(cor)
    if user == cor:
        return 100
    else:
        user = list(user)
        cor = list(cor)
        while cor:
            c = cor.pop(0)
            if user:
                u = user.pop(0)
                if c!=u:
                    cnt+=1
            else:
                cnt+=1
        return (lc-cnt)/lc * 100

class TopButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.setFont(font)
        self.setStyleSheet(QSSTopButton)

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 711, 461))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.MainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.MainLayout.setContentsMargins(0, 0, 0, 0)
        self.MainLayout.setObjectName("MainLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainButton = TopButton()
        self.mainButton.clicked.connect(self.mainButtonClicked)
        self.horizontalLayout.addWidget(self.mainButton)
        self.ITButton = TopButton()
        self.ITButton.clicked.connect(self.ITButtonClicked)
        self.horizontalLayout.addWidget(self.ITButton)
        self.newsButton = TopButton()
        self.newsButton.clicked.connect(self.NewsButtonClicked)
        self.horizontalLayout.addWidget(self.newsButton)
        self.lyricsButton = TopButton()
        self.lyricsButton.clicked.connect(self.LyricsButtonClicked)
        self.horizontalLayout.addWidget(self.lyricsButton)
        self.statButton = TopButton()
        self.statButton.clicked.connect(self.StatButtonClicked)
        self.horizontalLayout.addWidget(self.statButton)
        self.setButton = TopButton()
        self.horizontalLayout.addWidget(self.setButton)
        self.MainLayout.addLayout(self.horizontalLayout)
        self.stackWidget = QtWidgets.QStackedWidget(self.verticalLayoutWidget_2)
        self.stackWidget.setStyleSheet("border:1px soild #ffffff;\n"
"border-radius:15px;\n""background-color: rgb(209, 223, 232);")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.stackWidget.setObjectName("stackWidget")
        self.MainPage = QtWidgets.QWidget()
        self.MainPage.setObjectName("MainPage")
        self.MainTitle = QtWidgets.QLabel(self.MainPage)
        self.MainTitle.setGeometry(QtCore.QRect(315, 40, 120, 20))
        self.MainTitle.setFont(font)
        self.MainTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.MainContent = QtWidgets.QTextBrowser(self.MainPage)
        cfont = QtGui.QFont()
        cfont.setFamily("맑은 고딕")
        cfont.setPointSize(12)
        self.MainContent.setGeometry(QtCore.QRect(110,130,500,200))
        self.MainContent.setStyleSheet("color: rgb(255,255,255);")
        self.MainContent.setAlignment(Qt.AlignCenter)
        self.MainContent.setFont(cfont)


        self.stackWidget.addWidget(self.MainPage)
        self.TextPage = TextPage('internal')
        self.TextPage.setStyleSheet("background-color: rgb(209, 223, 232);")
        self.TextPage.setObjectName("TextPage")
        self.TextTitle = QtWidgets.QLabel(self.TextPage)
        self.TextTitle.setGeometry(QtCore.QRect(300, 40, 120, 20))
        self.TextTitle.setFont(font)
        self.TextTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.TextTitle.setObjectName("TextTitle")
        self.stackWidget.addWidget(self.TextPage)

        self.NewsPage = TextPage('news')
        self.NewsPage.setStyleSheet("background-color: rgb(209, 223, 232);")
        self.NewsPage.setObjectName("NewsPage")
        self.NewsTitle = QtWidgets.QLabel(self.NewsPage)
        self.NewsTitle.setGeometry(QtCore.QRect(330, 40, 120, 20))
        self.NewsTitle.setFont(font)
        self.NewsTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.stackWidget.addWidget(self.NewsPage)

        self.LyricsPage = TextPage('lyrics')
        self.LyricsPage.setStyleSheet("background-color: rgb(209, 223, 232);")
        self.LyricsPage.setObjectName("LyricsPage")
        self.LyricsTitle = QtWidgets.QLabel(self.LyricsPage)
        self.LyricsTitle.setGeometry(QtCore.QRect(330, 40, 120, 20))
        self.LyricsTitle.setFont(font)
        self.LyricsTitle.setStyleSheet("color: rgb(255, 255, 255);")
        self.stackWidget.addWidget(self.LyricsPage)
        self.StatPage = StatPage()
        self.stackWidget.addWidget(self.StatPage)
        self.MainLayout.addWidget(self.stackWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainButton.setText(_translate("MainWindow", "Main"))
        self.ITButton.setText(_translate("MainWindow", "Internal Text"))
        self.newsButton.setText(_translate("MainWindow", "News"))
        self.lyricsButton.setText(_translate("MainWindow", "Lyrics"))
        self.statButton.setText(_translate("MainWindow", "Stat"))
        self.setButton.setText(_translate("MainWindow", "Settings"))
        self.TextPage.TPM.setText(_translate("MainWindow", "분 당 타수 : 0"))
        self.TextPage.Currency.setText(_translate("MainWindow", "정확도 : 0%"))
        self.TextPage.confirm.setText(_translate("MainWindow", "확인"))

        self.NewsPage.TPM.setText(_translate("MainWindow", "분 당 타수 : 0"))
        self.NewsPage.Currency.setText(_translate("MainWindow", "정확도 : 0%"))
        self.NewsPage.confirm.setText(_translate("MainWindow", "확인"))

        self.LyricsPage.TPM.setText(_translate("MainWindow", "분 당 타수 : 0"))
        self.LyricsPage.Currency.setText(_translate("MainWindow", "정확도 : 0%"))
        self.LyricsPage.confirm.setText(_translate("MainWindow", "확인"))
        self.TextTitle.setText(_translate("MainWindow", "Internal Text"))
        self.NewsTitle.setText(_translate("MainWindow", "News"))
        self.LyricsTitle.setText(_translate("MainWindow", "Lyrics"))
        self.MainTitle.setText(_translate("MainWindow", "KeyUI 0.5a"))
        self.MainContent.setText(_translate("MainWindow", mainContent))


    def mainButtonClicked(self):
        self.stackWidget.setCurrentIndex(0)

    def ITButtonClicked(self):
        wid = QWidget()
        wid.setStyleSheet(QSSDialog)
        num, ok = QInputDialog.getInt(wid,'문장 수','<html style="font-size:12pt;font-family:''맑은 고딕'';color:''white'';">  문장 수를 입력해 주세요</html>', 1, 1, len(self.TextPage.toList))
        if ok:
            self.TextPage.progressBar.setMaximum(num)
            self.TextPage.progressBar.setValue(0)
            self.TextPage.progressNum = 0
            self.TextPage.maxNum = num
            self.stackWidget.setCurrentIndex(1)
        else:
            self.stackWidget.setCurrentIndex(0)

    def NewsButtonClicked(self):
        wid = QWidget()
        wid.setStyleSheet(QSSDialog)
        num, ok = QInputDialog.getInt(wid,'문장 수','<html style="font-size:12pt;font-family:''맑은 고딕'';color:''white'';">  문장 수를 입력해 주세요</html>', 1, 1, len(self.NewsPage.toList))
        if ok:
            self.NewsPage.progressBar.setMaximum(num)
            self.NewsPage.progressBar.setValue(0)
            self.NewsPage.progressNum = 0
            self.NewsPage.maxNum = num
            self.stackWidget.setCurrentIndex(2)
        else:
            self.stackWidget.setCurrentIndex(0)

    def LyricsButtonClicked(self):
        wid = QWidget()
        wid.setStyleSheet(QSSDialog)
        self.LyricsPage.toList = getLyrics(random.randint(1,50))
        num, ok = QInputDialog.getInt(wid,'문장 수','<html style="font-size:12pt;font-family:''맑은 고딕'';color:''white'';">  문장 수를 입력해 주세요</html>', 1, 1, len(self.LyricsPage.toList))
        if ok:
            self.LyricsPage.progressBar.setMaximum(num)
            self.LyricsPage.progressBar.setValue(0)
            self.LyricsPage.progressNum = 0
            self.LyricsPage.maxNum = num
            self.stackWidget.setCurrentIndex(3)
        else:
            self.stackWidget.setCurrentIndex(0)

    def StatButtonClicked(self):
        self.stackWidget.setCurrentIndex(4)
        self.StatPage.refresh()
        self.StatPage.initUI()

    def keyPressEvent(self, e):
        changedInd = self.stackWidget.currentIndex()
        if changedInd == 1:
            tab = self.TextPage
        if changedInd == 2:
            tab = self.NewsPage
        if changedInd == 3:
            tab = self.LyricsPage
        if changedInd in [1,2,3] and e.key() == Qt.Key_Return and tab.input.text() != '':
            if tab.progressNum == 0: #유예
                tab.prevtime = time.time()
                tab.Text.setText(tab.toList[tab.progressNum])
                tab.progressNum += 1
                tab.input.setText('')
            else:
                user = tab.input.text()
                cor = tab.toList[tab.progressNum-1]
                duringtime = time.time() - tab.prevtime
                tab.prevtime = time.time()
                tab.userList.append(user)
                tab.input.setText('')
                tab.input.setAlignment(Qt.AlignCenter)
                val = tab.progressBar.value()
                tab.progressBar.setValue(val + 1)
                tab.progressNum += 1
                wrong = getWrong(user,cor)
                tab.wrongList.append(wrong)
                tab.Currency.setText("정확도 : "+str(int(wrong))+"%")
                at = getAt(cor,duringtime,wrong)
                tab.atList.append(at)
                tab.TPM.setText("분당 타수 : "+str(int(at)))
                if tab.progressNum == tab.maxNum + 1:
                    cb = QCheckBox("결과를 기록할래요")
                    tab.Text.setText('')
                    res = QMessageBox()
                    res.setWindowTitle("결과")
                    res.setText("평균 분당 타수 : "+str(int(sum(tab.atList)/len(tab.atList)))+"\n평균 정확도 : "+str(int(sum(tab.wrongList)/len(tab.wrongList)))+"%")
                    res.setCheckBox(cb)
                    res.exec()
                    self.stackWidget.setCurrentIndex(0)
                    if cb.checkState():
                        writeTxt(int(sum(tab.atList)/len(tab.atList)), int(sum(tab.wrongList)/len(tab.wrongList)))
                    tab.atList = []
                    tab.wrongList = []
                else:
                    tab.Text.setText(tab.toList[tab.progressNum-1])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()

    sys.exit(app.exec_())