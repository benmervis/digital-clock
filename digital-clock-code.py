from PyQt5.QtWidgets import QLCDNumber, QApplication
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QColor, QIcon
import sys

class Clock(QLCDNumber):
    def __init__(self):
        super().__init__()

        title = "Digital Clock"
        top = 350
        left = 350
        width = 400
        height = 400

        colors = self.palette()

        #for determine the text color
        colors.setColor(colors.WindowText,QColor("blue"))

        #for determine the window color
        colors.setColor(colors.Window,QColor("red"))

        #for apply the specified colors
        self.setPalette(colors)

        self.setWindowTitle(title)
        self.setGeometry(top,left,width,height)

        self.setSegmentStyle(QLCDNumber.Filled)
        timer = QTimer(self)
        timer.timeout.connect(self.showTheTime)
        timer.start(1000)
        self.showTheTime()

        def showTheTime(self):
            time = QTime.currentTime()
            text = time.toString('hh:mm')
            print(text)
            if (time.second()%2)==0:
                text = text[:2]+" "+text[3:]

            self.display(text)

    #if __name__ == "__main__":
        app = QApplication(sys.argv)
        clock = Clock()
        clock.show()
        app.exec()
