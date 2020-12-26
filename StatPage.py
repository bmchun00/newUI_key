from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os,glob
from PyQt5 import QtGui


def getDatas():
    dates=[]
    avgs=[]
    cors=[]
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    flist = glob.glob(BASE_DIR + '\\record\*.bstat')
    print(flist)
    for i in flist:
        tf = open(i, "rt", encoding='UTF-8')
        txtlist = tf.readlines()
        for j in range(0, len(txtlist)):
            tmp = txtlist[j].replace("\n", "")
            datalist = tmp.split()
            dates.append(datalist[0])
            avgs.append(int(datalist[1]))
            cors.append(int(datalist[2]))

    return dates, avgs, cors

class StatPage(QWidget):
    def __init__(self):
        super().__init__()
        font = {'size':6}
        matplotlib.rc('font',**font)
        self.constUI()

    def initUI(self):
        dates, avgs, cors = getDatas()
        self.setLayout(self.grid)
        self.avgsplot = self.avgfig.add_subplot(111)
        self.avgsplot.tick_params(direction = 'in',colors='white')

        self.x = list(map(str,range(1,len(avgs)+1)))
        self.avgsplot.plot(self.x,avgs,color='r',label='Words per minutes',linestyle=':')
        self.avgsplot.plot(self.x,avgs,'go',markersize=2,color='w',label='_nolegend_')
        self.avgsplot.legend()
        self.avgsplot.set_facecolor('none')
        self.avgfig.set_facecolor('none')
        self.avgcan = FigureCanvas(self.avgfig)
        self.thickness = 3
        for child in self.avgsplot.get_children():
            if isinstance(child, matplotlib.spines.Spine):
                child.set_color('#ffffff')

        self.avgcan.draw()

        self.corsplot = self.corfig.add_subplot(111)
        self.corsplot.tick_params(direction='in',colors='white')
        self.corsplot.plot(self.x,cors,color='b',label='Accuracy',linestyle=':')
        self.corsplot.plot(self.x,cors,'go',markersize=2,color='w',label='_nolegend_')
        self.corsplot.legend()
        self.corsplot.set_facecolor('none')
        self.corfig.set_facecolor('none')
        self.corcan = FigureCanvas(self.corfig)

        for child in self.corsplot.get_children():
            if isinstance(child, matplotlib.spines.Spine):
                child.set_color('#ffffff')
        self.corcan.draw()

        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)

        self.grid.addWidget(self.avgcan, 0, 0)
        self.grid.addWidget(self.corcan, 1, 0)
        if len(avgs)>0:
            self.l.setText("평균 분당 타수 : "+str(sum(avgs)//len(avgs))+"\n평균 정확도 : "+str(sum(cors)//len(cors))+"%")
        self.l.setFont(font)
        self.l.setStyleSheet("color : #ffffff")
        self.avgcan.show()

    def constUI(self):
        self.l = QLabel('',self)
        self.rbutton = QPushButton("기록 삭제",self)
        self.rbutton.setToolTip('현재까지의 모든 기록을 삭제합니다.')
        self.rbutton.clicked.connect(self.onClick)
        self.l.setAlignment(Qt.AlignHCenter)
        self.l.setAlignment(Qt.AlignBottom)
        self.l.setFixedWidth(300)
        self.grid.addWidget(self.rbutton,1,1)
        self.grid.addWidget(self.l,0,1)

    grid = QGridLayout()
    corfig = plt.Figure()
    avgfig = plt.Figure()

    def refresh(self):
        self.l.setText('')
        self.corfig.clf()
        self.avgfig.clf()

    def onClick(self):
        reply = QMessageBox.question(self, '기록 삭제', '정말로 삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                os.remove(self.BASE_DIR + '\\record\stat.bstat')
            except:
                print("두번삭제에러")
            self.refresh()
            self.initUI()


    BASE_DIR = os.path.dirname(os.path.abspath(__file__))