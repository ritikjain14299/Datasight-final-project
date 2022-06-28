from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea, QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow,QCheckBox)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
from PyQt5 import QtGui

# import Cleanwindow

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        l=['C:\\Users\\Prasuk Jain\\AppData\\Local\\Temp\\BRL00002590\\BRCDC.tmp', 'C:\\Users\\Prasuk Jain\\AppData\\Local\\Temp\\BRL00002590\\BRCED.tmp', 'C:\\Users\\Prasuk Jain\\AppData\\Local\\Temp\\is-8LN3B.tmp\\_isetup\\_setup64.tmp', 'C:\\Users\\Prasuk Jain\\AppData\\Local\\Temp\\is-L4E35.tmp\\_isetup\\_setup64.tmp', 'C:\\Users\\Prasuk Jain\\AppData\\Local\\Temp\\is-P1GF4.tmp\\_isetup\\_setup64.tmp', 'C:\\Users\\Prasuk Jain\\AppData\\Local\\Temp\\is-PJOK2.tmp\\_isetup\\_setup64.tmp', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\Local Storage\\leveldb\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\Service Worker\\Database\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\Session Storage\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\AutofillStrikeDatabase\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\BudgetDatabase\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\data_reduction_proxy_leveldb\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\Extension State\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\Feature Engagement Tracker\\AvailabilityDB\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\Feature Engagement Tracker\\EventDB\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\Local Storage\\leveldb\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\Platform Notifications\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\Session Storage\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\shared_proto_db\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\shared_proto_db\\metadata\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\Site Characteristics Database\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\Code\\User\\workspaceStorage\\2324bd24eee856d79eb355b660c83974\\ms-vscode.js-debug\\.profile\\Default\\Sync Data\\LevelDB\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\CodeBlocks\\cbKeyBinder10.ini.bak', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\GitHub Desktop\\IndexedDB\\file__0.indexeddb.leveldb\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\GitHub Desktop\\Local Storage\\leveldb\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\GitHub Desktop\\Session Storage\\LOG.old', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\npm\\node_modules\\@angular\\cli\\node_modules\\form-data\\README.md.bak', 'C:\\Users\\Prasuk Jain\\AppData\\Roaming\\OpenOffice\\4\\user\\uno_packages\\cache\\uno_packages\\sv45zgk4.tmp', 'C:\\Users\\Prasuk Jain\\Desktop\\project\\angular\\page\\node_modules\\form-data\\README.md.bak', 'C:\\Users\\Prasuk Jain\\Desktop\\react\\my\\node_modules\\form-data\\README.md.bak', 'C:\\Users\\Prasuk Jain\\IBA_IOAPDATA\\2021-09-19_08-51-59\\chrome_profile_ion\\Default\\LOG.old', 'C:\\Users\\Prasuk Jain\\IBA_IOAPDATA\\2021-09-19_08-51-59\\chrome_profile_ion\\Default\\Feature Engagement Tracker\\AvailabilityDB\\LOG.old', 'C:\\Users\\Prasuk Jain\\IBA_IOAPDATA\\2021-09-19_08-51-59\\chrome_profile_ion\\Default\\Feature Engagement Tracker\\EventDB\\LOG.old', 'C:\\Users\\Prasuk Jain\\IBA_IOAPDATA\\2021-09-19_08-51-59\\chrome_profile_ion\\Default\\GCM Store\\Encryption\\LOG.old', 'C:\\Users\\Prasuk Jain\\IBA_IOAPDATA\\2021-09-19_08-51-59\\chrome_profile_ion\\Default\\Local Storage\\leveldb\\LOG.old', 'C:\\Users\\Prasuk Jain\\IBA_IOAPDATA\\2021-09-19_08-51-59\\chrome_profile_ion\\Default\\optimization_guide_hint_cache_store\\LOG.old', 'C:\\Users\\Prasuk Jain\\IBA_IOAPDATA\\2021-09-19_08-51-59\\chrome_profile_ion\\Default\\optimization_guide_model_and_features_store\\LOG.old', 'C:\\Users\\Prasuk Jain\\IBA_IOAPDATA\\2021-09-19_08-51-59\\chrome_profile_ion\\Default\\shared_proto_db\\LOG.old', 'C:\\Users\\Prasuk Jain\\IBA_IOAPDATA\\2021-09-19_08-51-59\\chrome_profile_ion\\Default\\shared_proto_db\\metadata\\LOG.old', 'C:\\Users\\Prasuk Jain\\IBA_IOAPDATA\\2021-09-19_08-51-59\\chrome_profile_ion\\Default\\Site Characteristics Database\\LOG.old', 'C:\\Users\\Prasuk Jain\\IBA_IOAPDATA\\2021-09-19_08-51-59\\chrome_profile_ion\\Default\\Sync Data\\LevelDB\\LOG.old', 'C:\\Windows\\SMSS-PFRO3d28.tmp', 'C:\\Windows\\INF\\Intel Storage Counters\\tmp54CD.tmp', 'C:\\Windows\\INF\\Intel Storage Counters\\tmp54CE.tmp', 'C:\\Windows\\INF\\Intel Storage Counters\\0000\\tmp54CD.tmp', 'C:\\Windows\\INF\\Intel Storage Counters\\0009\\tmp54CD.tmp', 'C:\\Windows\\Panther\\_s_20DE.tmp', 'C:\\Windows\\SoftwareDistribution\\DataStore\\Logs\\edb.chk', 'C:\\Windows\\System32\\catroot2\\edb.chk', 'C:\\Windows\\System32\\wbem\\WMIObjectsMigration.bin.bak']

        self.checkboxes=[]
        self.checkboxall = QCheckBox(str("Select All Files"))
        self.checkboxall.setFixedHeight(30)
        self.checkboxall.setStyleSheet("color: blue;""QCheckBox::indicator{width : 40px;height : 40px;}")
        self.checkboxall.setChecked(False)
        self.checkboxall.setFont(QtGui.QFont('Times New Roman', 13))
        self.checkboxall.stateChanged.connect(self.on_state)
        self.vbox.addWidget(self.checkboxall)

        for a in l:
            btn = QCheckBox(str(a))
            self.checkboxes.append(btn)
            btn.setFixedHeight(30)
            btn.setStyleSheet("color: blue;""QCheckBox::indicator{width : 40px;height : 40px;}")
            btn.setFont(QtGui.QFont('Times New Roman', 13))

            self.vbox.addWidget(btn)

        self.b = QPushButton("Delete Files")
        self.b.clicked.connect(self.on)

        self.vbox.addWidget(self.b)
        self.widget.setLayout(self.vbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)



        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Cleaner')
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.show()


        return
    def on(self):
        print("prasuk")
    def on_state(self, state):
        for checkbox in self.checkboxes:
            checkbox.setCheckState(state)



app = QtWidgets.QApplication(sys.argv)

main = MainWindow()
sys.exit(app.exec_())

