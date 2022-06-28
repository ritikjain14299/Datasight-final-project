import sys
from final import *
from Custom_Widgets.Widgets import *  # install GTK+
from final import Ui_MainWindow
import sys
import platform
from gtts import gTTS
from playsound import playsound
from PySide2 import QtCore, QtGui
from PyQt5 import QtWidgets as qtw
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        qtw.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.ui.RefreshButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.RefreshWindow))
        self.ui.CleanButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.CleanWindow))
        self.ui.SearchButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.SearchTypeWindow))

        self.ui.searchindevButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.SearchinDevWindow))
        self.ui.searchindocButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.SearchinDocWindow))
        #self.ui.searchdevButton_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.SearchinDevWindow))
        #self.searchdevButton_2.clicked.connect(self.on_click)
        self.ui.HomeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.HomeWindow))
        self.ui.AboutButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.AboutWindow))
        self.ui.FAQButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.FAQWindow))
        self.ui.ExitButton.clicked.connect(sys.exit)


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    text_val = 'Welcome to Datasight A File Searching Tool.'
    language = 'en'
    t1 = gTTS(text=text_val, lang=language, slow=False)
    t1.save("welcome.mp3")
    playsound("welcome.mp3")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
