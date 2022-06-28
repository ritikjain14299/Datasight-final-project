from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import os
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton

rubbishExt = ['.tmp', '.bak', '.prv', '.old', '.wbk', '.err', '.xlk', '_mp', '.gid', '.chk', '.syd', '.$$$', '.@@@',
              ".~*"]
filext = ['.txt', '.pdf', '.docx']

LastStateRole = QtCore.Qt.UserRole

def GetDrives():
    drives = []
    for i in range(65, 91):
        vol = chr(i) + ":/"
        if os.path.isdir(vol):
            drives.append(vol)
    return tuple(drives)


class Ui_MainWindow(object):

    def __init__(self):
        self.file_index = []
        self.record = 0
        self.searchl = []
        self.index2 = []
        self.l = []
        self.widgetList = []



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 700))
        MainWindow.setMaximumSize(QtCore.QSize(800, 700))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("*{\n"
                                 "    border:none;\n"
                                 "    background-color:transparent;\n"
                                 "    background:transparent;\n"
                                 "    padding:0;\n"
                                 "    margin:0;\n"
                                 "    color:#fff;\n"
                                 "}\n"
                                 "#centralwidget{\n"
                                 "    background-color: #16191d;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 60, 771, 601))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.drives = GetDrives()
        t = threading.Thread(target=self.ScanRubbish, args=(self.drives,))
        t.start()
        self.HomeWindow = QtWidgets.QWidget()
        self.HomeWindow.setObjectName("HomeWindow")
        self.RefreshButton = QtWidgets.QPushButton(self.HomeWindow)
        self.RefreshButton.setGeometry(QtCore.QRect(280, 120, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.RefreshButton.setFont(font)
        self.RefreshButton.setAutoFillBackground(False)
        self.RefreshButton.setStyleSheet("border-width: 3px;\n"
                                         "border-style: outset;\n"
                                         "border-color: black;\n"
                                         "border-radius: 20px;\n"
                                         "color: rgb(255, 255, 255);\n"
                                         "background-color:#1f232a;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/refresh-ccw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RefreshButton.setIcon(icon)
        self.RefreshButton.setIconSize(QtCore.QSize(30, 30))
        self.RefreshButton.setObjectName("RefreshButton")

        self.CleanButton = QtWidgets.QPushButton(self.HomeWindow, clicked = lambda: self.clean)
        self.CleanButton.setGeometry(QtCore.QRect(280, 250, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.CleanButton.setFont(font)
        self.CleanButton.setStyleSheet("border-width: 3px;\n"
                                       "border-style: outset;\n"
                                       "border-color: black;\n"
                                       "border-radius: 20px;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color:#1f232a;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/trash-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CleanButton.setIcon(icon1)
        self.CleanButton.setIconSize(QtCore.QSize(30, 30))
        self.CleanButton.setObjectName("CleanButton")
        self.SearchButton = QtWidgets.QPushButton(self.HomeWindow)
        self.SearchButton.setGeometry(QtCore.QRect(280, 370, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.SearchButton.setFont(font)
        self.SearchButton.setStyleSheet("border-width: 3px;\n"
                                        "border-style: outset;\n"
                                        "border-color: black;\n"
                                        "border-radius: 20px;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color:#1f232a;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SearchButton.setIcon(icon2)
        self.SearchButton.setIconSize(QtCore.QSize(30, 30))
        self.SearchButton.setObjectName("SearchButton")
        self.label = QtWidgets.QLabel(self.HomeWindow)
        self.label.setGeometry(QtCore.QRect(150, 60, 481, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.HomeWindow)
        self.RefreshWindow = QtWidgets.QWidget()
        self.RefreshWindow.setStyleSheet("")
        self.RefreshWindow.setObjectName("RefreshWindow")
        self.stackedWidget.addWidget(self.RefreshWindow)
        self.CleanWindow = QtWidgets.QWidget()
        self.CleanWindow.setObjectName("CleanWindow")

        self.notificationclean = QtWidgets.QTextEdit(self.CleanWindow)
        self.notificationclean.setGeometry(QtCore.QRect(130, 460, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notificationclean.setFont(font)
        self.notificationclean.setStyleSheet("border-width: 2px;\n"
                                             "border-style: outset;\n"
                                             "border-color: black;\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "background-color:#1f232a;\n"
                                             "")
        self.notificationclean.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.notificationclean.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.notificationclean.setObjectName("notificationclean")
        self.SelectAllButton = QtWidgets.QCommandLinkButton(self.CleanWindow)
        self.SelectAllButton.setGeometry(QtCore.QRect(80, 520, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.SelectAllButton.setFont(font)
        self.SelectAllButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SelectAllButton.setAutoFillBackground(False)
        self.SelectAllButton.setStyleSheet("border-width: 3px;\n"
                                           "border-style: outset;\n"
                                           "border-color: black;\n"
                                           "border-radius: 20px;\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "background-color:#1f232a;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SelectAllButton.setIcon(icon3)
        self.SelectAllButton.setIconSize(QtCore.QSize(25, 25))
        self.SelectAllButton.setCheckable(False)
        self.SelectAllButton.setObjectName("SelectAllButton")
        self.DeleteButton = QtWidgets.QCommandLinkButton(self.CleanWindow)
        self.DeleteButton.setGeometry(QtCore.QRect(590, 520, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteButton.setFont(font)
        self.DeleteButton.setStyleSheet("border-width: 3px;\n"
                                        "border-style: outset;\n"
                                        "border-color: black;\n"
                                        "border-radius: 20px;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color:#1f232a;")
        self.DeleteButton.setIcon(icon1)
        self.DeleteButton.setIconSize(QtCore.QSize(25, 25))
        self.DeleteButton.setObjectName("DeleteButton")
        self.tableWidgetClean = QtWidgets.QTableWidget(len(self.l)+1,1,self.CleanWindow)
        self.tableWidgetClean.setGeometry(QtCore.QRect(15, 21, 751, 421))
        self.tableWidgetClean.setStyleSheet("border-width: 5px;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "background-color:#1f232a;")
        self.tableWidgetClean.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableWidgetClean.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetClean.setObjectName("tableWidgetClean")
        #self.tableWidgetClean.horizontalHeaderItem(QtGui.QColor(0, 0, 0))
        stylesheet = "::section{Background-color:rgb(0,0,0);border-radius:10px;}"
        self.tableWidgetClean.setStyleSheet(stylesheet)
        #self.tableWidgetClean.setColumnCount(1)
        self.tableWidgetClean.setHorizontalHeaderLabels(['File Path'])

        self.tableWidgetClean.setColumnWidth(0, 750)


        for row in range(len(self.l)+1):
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Checked)
            item.setData(LastStateRole, item.checkState())

            self.tableWidgetClean.setItem(row, 1, item)
        self.tableWidgetClean.cellChanged.connect(self.onCellChanged)

        self.stackedWidget.addWidget(self.CleanWindow)
        self.SearchTypeWindow = QtWidgets.QWidget()
        self.SearchTypeWindow.setObjectName("SearchTypeWindow")
        self.searchindevButton = QtWidgets.QPushButton(self.SearchTypeWindow)
        self.searchindevButton.setGeometry(QtCore.QRect(290, 110, 231, 121))
        self.searchindevButton.setStyleSheet("border-width: 3px;\n"
                                             "border-style: outset;\n"
                                             "border-color: black;\n"
                                             "border-radius: 30px;\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "background-color:#1f232a;\n"
                                             "")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icons/monitor.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchindevButton.setIcon(icon4)
        self.searchindevButton.setIconSize(QtCore.QSize(35, 35))
        self.searchindevButton.setObjectName("searchindevButton")
        self.searchindocButton = QtWidgets.QPushButton(self.SearchTypeWindow)
        self.searchindocButton.setGeometry(QtCore.QRect(290, 330, 231, 121))
        self.searchindocButton.setStyleSheet("border-width: 3px;\n"
                                             "border-style: outset;\n"
                                             "border-color: black;\n"
                                             "border-radius: 30px;\n"
                                             "color: rgb(255, 255, 255);\n"
                                             "background-color:#1f232a;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/icons/file-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchindocButton.setIcon(icon5)
        self.searchindocButton.setIconSize(QtCore.QSize(35, 35))
        self.searchindocButton.setObjectName("searchindocButton")
        self.stackedWidget.addWidget(self.SearchTypeWindow)
        self.SearchinDevWindow = QtWidgets.QWidget()
        self.SearchinDevWindow.setObjectName("SearchinDevWindow")
        self.comboBox = QtWidgets.QComboBox(self.SearchinDevWindow)
        self.comboBox.setGeometry(QtCore.QRect(310, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("border-width: 2px;\n"
                                    "border-style: outset;\n"
                                    "border-color: black;\n"
                                    "border-radius: 5px;\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color:#1f232a;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.keywordtext = QtWidgets.QTextEdit(self.SearchinDevWindow)
        self.keywordtext.setGeometry(QtCore.QRect(20, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.keywordtext.setFont(font)
        self.keywordtext.setStyleSheet("border-width: 2px;\n"
                                       "border-style: outset;\n"
                                       "border-color: black;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color:#1f232a;")
        self.keywordtext.setObjectName("keywordtext")
        self.notificationtext = QtWidgets.QTextEdit(self.SearchinDevWindow)
        self.notificationtext.setGeometry(QtCore.QRect(150, 540, 531, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.notificationtext.setFont(font)
        self.notificationtext.setStyleSheet("border-width: 2px;\n"
                                            "border-style: outset;\n"
                                            "border-color: black;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "background-color:#1f232a;")
        self.notificationtext.setObjectName("notificationtext")
        self.SearchDevButton = QtWidgets.QCommandLinkButton(self.SearchinDevWindow, clicked = lambda: self.SearchDev)
        self.SearchDevButton.setGeometry(QtCore.QRect(460, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SearchDevButton.setFont(font)
        self.SearchDevButton.setStyleSheet("border-width: 2px;\n"
                                           "border-style: outset;\n"
                                           "border-color: black;\n"
                                           "border-radius: 10px;\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "background-color:#1f232a;\n"
                                           "")
        self.SearchDevButton.setIcon(icon2)
        self.SearchDevButton.setObjectName("SearchDevButton")
        self.PreviewDevButton = QtWidgets.QCommandLinkButton(self.SearchinDevWindow)
        self.PreviewDevButton.setGeometry(QtCore.QRect(620, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PreviewDevButton.setFont(font)
        self.PreviewDevButton.setStyleSheet("border-width: 2px;\n"
                                            "border-style: outset;\n"
                                            "border-color: black;\n"
                                            "border-radius: 10px;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "background-color:#1f232a;\n"
                                            "")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/icons/clipboard.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PreviewDevButton.setIcon(icon6)
        self.PreviewDevButton.setObjectName("PreviewDevButton")
        # self.tableWidgetDev = QtWidgets.QTableWidget(self.SearchinDevWindow)
        # self.tableWidgetDev.setGeometry(QtCore.QRect(20, 70, 751, 441))
        # self.tableWidgetDev.setStyleSheet("border-width: 5px;\n"
        #                                   "color: rgb(255, 255, 255);\n"
        #                                   "background-color:#1f232a;")
        # self.tableWidgetDev.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.tableWidgetDev.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.tableWidgetDev.setObjectName("tableWidgetDev")
        #
        # stylesheet = "::section{Background-color:rgb(0,0,0);border-radius:10px;}"
        # self.tableWidgetDev.setStyleSheet(stylesheet)
        # self.tableWidgetDev.setColumnCount(2)
        # self.tableWidgetDev.setHorizontalHeaderLabels(['checkbox', 'File Path'])
        #
        # self.tableWidgetDev.setColumnWidth(0, 151)
        # self.tableWidgetDev.setColumnWidth(1, 600)
        self.stackedWidget.addWidget(self.SearchinDevWindow)
        self.SearchinDocWindow = QtWidgets.QWidget()
        self.SearchinDocWindow.setObjectName("SearchinDocWindow")
        self.keyworddoctext = QtWidgets.QTextEdit(self.SearchinDocWindow)
        self.keyworddoctext.setGeometry(QtCore.QRect(10, 10, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.keyworddoctext.setFont(font)
        self.keyworddoctext.setStyleSheet("border-width: 2px;\n"
                                          "border-style: outset;\n"
                                          "border-color: black;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "background-color:#1f232a;")
        self.keyworddoctext.setObjectName("keyworddoctext")
        self.SearchDocButton = QtWidgets.QCommandLinkButton(self.SearchinDocWindow)
        self.SearchDocButton.setGeometry(QtCore.QRect(410, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SearchDocButton.setFont(font)
        self.SearchDocButton.setStyleSheet("border-width: 2px;\n"
                                           "border-style: outset;\n"
                                           "border-color: black;\n"
                                           "border-radius: 10px;\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "background-color:#1f232a;\n"
                                           "")
        self.SearchDocButton.setIcon(icon2)
        self.SearchDocButton.setIconSize(QtCore.QSize(25, 25))
        self.SearchDocButton.setObjectName("SearchDocButton")
        self.PreviewDocButton = QtWidgets.QCommandLinkButton(self.SearchinDocWindow)
        self.PreviewDocButton.setGeometry(QtCore.QRect(600, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PreviewDocButton.setFont(font)
        self.PreviewDocButton.setStyleSheet("border-width: 2px;\n"
                                            "border-style: outset;\n"
                                            "border-color: black;\n"
                                            "border-radius: 10px;\n"
                                            "color: rgb(255, 255, 255);\n"
                                            "background-color:#1f232a;\n"
                                            "")
        self.PreviewDocButton.setIcon(icon6)
        self.PreviewDocButton.setIconSize(QtCore.QSize(25, 25))
        self.PreviewDocButton.setObjectName("PreviewDocButton")
        # self.tableWidgetDoc = QtWidgets.QTableWidget(self.SearchinDocWindow)
        # self.tableWidgetDoc.setGeometry(QtCore.QRect(10, 70, 761, 511))
        # self.tableWidgetDoc.setStyleSheet("border-width: 5px;\n"
        #                                   "color: rgb(255, 255, 255);\n"
        #                                   "background-color:#1f232a;")
        # self.tableWidgetDoc.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.tableWidgetDoc.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # self.tableWidgetDoc.setObjectName("tableWidgetDoc")
        # stylesheet = "::section{Background-color:rgb(0,0,0);border-radius:10px;}"
        # self.tableWidgetDoc.setStyleSheet(stylesheet)
        # self.tableWidgetDoc.setColumnCount(2)
        # self.tableWidgetDoc.setHorizontalHeaderLabels(['checkbox', 'File Path'])
        #
        # self.tableWidgetDoc.setColumnWidth(0, 151)
        # self.tableWidgetDoc.setColumnWidth(1, 600)
        self.stackedWidget.addWidget(self.SearchinDocWindow)
        self.AboutWindow = QtWidgets.QWidget()
        #self.AboutWindow.setStyleSheet("image: url(:/newPrefix/datasight_logo-removebg-preview.png);")
        styleshet = "image: url(:/datasight_logo-removebg-preview.png)"
        self.AboutWindow.setStyleSheet(styleshet)
        self.AboutWindow.setObjectName("AboutWindow")
        self.label_2 = QtWidgets.QLabel(self.AboutWindow)
        self.label_2.setGeometry(QtCore.QRect(220, 420, 540, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.AboutWindow)
        self.label_3.setGeometry(QtCore.QRect(130, 200, 500, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.AboutWindow)
        self.label_4.setGeometry(QtCore.QRect(360, 480, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.AboutWindow)
        self.FAQWindow = QtWidgets.QWidget()
        self.FAQWindow.setObjectName("FAQWindow")
        self.stackedWidget.addWidget(self.FAQWindow)
        self.HomeButton = QtWidgets.QPushButton(self.centralwidget)
        self.HomeButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.HomeButton.setFont(font)
        self.HomeButton.setStyleSheet("border-width: 2px;\n"
                                      "border-style: outset;\n"
                                      "border-color: black;\n"
                                      "border-radius: 10px;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color:#1f232a;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeButton.setIcon(icon7)
        self.HomeButton.setObjectName("HomeButton")
        self.AboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.AboutButton.setGeometry(QtCore.QRect(90, 10, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AboutButton.setFont(font)
        self.AboutButton.setStyleSheet("border-width: 2px;\n"
                                       "border-style: outset;\n"
                                       "border-color: black;\n"
                                       "border-radius: 10px;\n"
                                       "color: rgb(255, 255, 255);\n"
                                       "background-color:#1f232a;")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/icons/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AboutButton.setIcon(icon8)
        self.AboutButton.setObjectName("AboutButton")
        self.FAQButton = QtWidgets.QPushButton(self.centralwidget)
        self.FAQButton.setGeometry(QtCore.QRect(170, 10, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.FAQButton.setFont(font)
        self.FAQButton.setStyleSheet("border-width: 2px;\n"
                                     "border-style: outset;\n"
                                     "border-color: black;\n"
                                     "border-radius: 10px;\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color:#1f232a;")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/icons/loader.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FAQButton.setIcon(icon9)
        self.FAQButton.setObjectName("FAQButton")
        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(250, 10, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ExitButton.setFont(font)
        self.ExitButton.setStyleSheet("border-width: 2px;\n"
                                      "border-style: outset;\n"
                                      "border-color: black;\n"
                                      "border-radius: 10px;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color:#1f232a;")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/icons/external-link.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon10)
        self.ExitButton.setObjectName("ExitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionHome = QtWidgets.QAction(MainWindow)
        self.actionHome.setObjectName("actionHome")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFAQ = QtWidgets.QAction(MainWindow)
        self.actionFAQ.setObjectName("actionFAQ")

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.SearchDevButton.clicked.connect(self.SearchDev)

    def ScanRubbish(self, scanpath):
        global rubbishExt
        total = 0
        filesize = 0
        lst = []
        for drive in scanpath:
            print(drive)

            for root, dirs, files in os.walk(drive):

                # print(root,dirs,files)
                self.index2.append((root, files))
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:
                                fname = os.path.join(
                                    os.path.abspath(root), fil)
                                filesize += os.path.getsize(fname)
                                #self.b.insertPlainText(fname + "\n")
                                self.l.append(fname)
                                total += 1
                            else:
                                fname = os.path.join(os.path.abspath(root), fil)

                        except ValueError:
                            pass

                except Exception as e:
                    print(e)
                    pass
                if files:
                    self.file_index: list = [(root, files)]
                    lst.append(self.file_index)
        self.searchl.append(lst)
        with open("outfile.txt", "w", encoding="utf-8") as output:
            output.write(str(lst))

        # for row in range(5):
        #     item = QtWidgets.QTableWidgetItem()
        #     item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        #     item.setCheckState(QtCore.Qt.Checked)
        #     item.setData(LastStateRole, item.checkState())
        #
        #     self.tableWidgetClean.setItem(row, 0, item)
        # self.tableWidgetClean.cellChanged.connect(self.onCellChanged)
    # def on_state(self, state):
    #     for checkbox in self.checkboxes:
    #         checkbox.setCheckState(state)

    def clean(self):
        self.widgetList.clear()
        self.ui.pathlist.setRowCount(len(self.l))


    def SearchDev(self):
        term = self.keywordtext.toPlainText()
        ftype= self.comboBox.currentText()
        for path, files in self.index2:
            for file in files:
                if len(term)>0 and ftype!="ALL":
                    if (term.lower() in file.lower() and file.lower().endswith(ftype.lower())):
                        result = path.replace('\\', '/') + '/' + file
                        result = result.replace(" ", '')
                        url = bytearray(QtCore.QUrl.fromLocalFile(result).toEncoded()).decode()
                        print(url)

                elif ftype=="ALL":
                    if len(term)>0:
                        if term.lower() in file.lower():
                            result = path.replace('\\', '/') + '/' + file
                            result = result.replace(" ",'')
                            url = bytearray(QtCore.QUrl.fromLocalFile(result).toEncoded()).decode()
                            print(url)

                else:
                    if file.lower().endswith(ftype.lower()):
                        result = path.replace('\\', '/') + '/' + file
                        result = result.replace(" ", '')
                        url = bytearray(QtCore.QUrl.fromLocalFile(result).toEncoded()).decode()
                        print(url)
        #self.notificationtext.setPlainText("hello")
    def onCellChanged(self, row, column):
        item = self.tablewidget.item(row, column)
        lastState = item.data(LastStateRole)
        currentState = item.checkState()
        if currentState != lastState:
            print("changed: ")
            if currentState == QtCore.Qt.Checked:
                print("checked")
            else:
                print("unchecked")
            item.setData(LastStateRole, currentState)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RefreshButton.setText(_translate("MainWindow", "Refresh"))
        self.CleanButton.setText(_translate("MainWindow", "Clean"))
        self.SearchButton.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "*Note    After Starting the Application, please click on the Refresh Button"))
        self.SelectAllButton.setText(_translate("MainWindow", "Select All"))
        self.DeleteButton.setText(_translate("MainWindow", "Delete"))
        self.searchindevButton.setText(_translate("MainWindow", "Search In Device"))
        self.searchindocButton.setText(_translate("MainWindow", "Search In Document"))
        self.comboBox.setItemText(0, _translate("MainWindow", "PDF"))
        self.comboBox.setItemText(1, _translate("MainWindow", "DOC"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ODT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "RTF"))
        self.comboBox.setItemText(4, _translate("MainWindow", "JPG"))
        self.comboBox.setItemText(5, _translate("MainWindow", "PNG"))
        self.comboBox.setItemText(6, _translate("MainWindow", "MP4"))
        self.comboBox.setItemText(7, _translate("MainWindow", "ALL"))
        self.SearchDevButton.setText(_translate("MainWindow", "Search"))
        self.PreviewDevButton.setText(_translate("MainWindow", "Preview"))
        self.SearchDocButton.setText(_translate("MainWindow", "   Search"))
        self.PreviewDocButton.setText(_translate("MainWindow", "    Preview"))
        # self.tableWidgetDoc.setSortingEnabled(False)
        self.label_2.setText(_translate("MainWindow", "Made By : Prasuk Jain, Aman Jain, Ritik Jain, Sankalp Jain"))
        self.label_3.setText(_translate("MainWindow", "A File Searching And Cleaning Tool"))
        self.label_4.setText(_translate("MainWindow", "Final Year B. Tech. CSE-A"))
        self.HomeButton.setText(_translate("MainWindow", "Home"))
        self.AboutButton.setText(_translate("MainWindow", "About"))
        self.FAQButton.setText(_translate("MainWindow", "FAQ"))
        self.ExitButton.setText(_translate("MainWindow", "Exit"))



import img

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
