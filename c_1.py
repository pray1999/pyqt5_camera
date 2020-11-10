import cv2
import numpy as numpy
from PIL import *
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from threading import *


# 一大堆引用,乱七八糟,都要用到
# 需要继承QWidget,初始化窗体
class initform(QWidget):
    def __init__(self):
        super().__init__()
        return self.initUI()

    def initUI(self):
        # 设置窗口左上边距,宽度高度
        self.setGeometry(300, 300, 800, 600)
        # 设置窗体标题
        self.setWindowTitle("myui")
        # self.layout=QGridLayout(self)
        # 设置lable文本内容
        self.lable = QLabel("iamlable", self)
        # self.lable.move(0,0)
        # label的对其方式,为左上对其
        self.lable.setAlignment(Qt.AlignTop)
        self.lable.setAlignment(Qt.AlignLeft)
        # 设置lable的大小
        self.lable.setGeometry(0, 0, 800, 600)
        # self.lable.size(800,600)
        self.lable.setScaledContents(True)
        # self.lable.setWordWrap(True)
        # self.lable.setFixedSize(800,600)
        # self.lable.setFixedWidth(800)
        # self.lable.setFixedHeight(600)
        # lable加入窗体
        # self.layout.addWidget(self.lable)

        # self.lable.setAutoFillBackground(True)
        # self.lable.alignment(Qt.AlignCenter)
        # pe=QPalette()
        # pe.setColor(QPalette.windowText,Qt.blue)
        # pe.setColor(QPalette.window,Qt.red)
        # self.lable.setPalette(pe)
        # self.lable.move(0,0)
        # 读取图片
        self.show()

    def SetPic(self, img):
        # self.lable.setPixmap(QPixmap(imgPath))
        # 图片显示
        self.lable.setPixmap(QPixmap.fromImage(img))
        # print(QPixmap(imgPath))


thstop = False


# 上面的这个来控制进程结束
def showcamre():
    # 参数0代表系统第一个摄像头,第二就用1 以此类推
    cap = cv2.VideoCapture(0)
    # 设置显示分辨率和FPS ,不设置的话会非常卡
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    cap.set(cv2.CAP_PROP_FPS, 20)
    while cap.isOpened():
        if thstop:
            return
        ret, frame = cap.read()
        if ret == False:
            continue
        # 水平翻转,很有必要
        frame = cv2.flip(frame, 1)
        # opencv 默认图像格式是rgb qimage要使用BRG,这里进行格式转换,不用这个的话,图像就变色了,困扰了半天,翻了一堆资料
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        # mat-->qimage
        a = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        ex.SetPic(a)


app = QApplication(sys.argv)

ex = initform()
# 全屏显示
# ex.showFullScreen()
# 使用线程,否则程序卡死
th = Thread(target=showcamre)
th.start()
app.exec_()
# 退出的时候,结束进程,否则,关不掉进程
thstop = True