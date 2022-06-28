# import sys
# from ui import Ui_MainWindow
# from PyQt5 import QtWidgets
# from PyQt5.QtCore import Qt
# app = QtWidgets.QApplication(sys.argv)
#
# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#
#         checkbox = QtWidgets.QCheckBox()
#         income = (("1", "2"), ("3", "4"))
#         for rowi, i in enumerate(income):
#             checkbox = QtWidgets.QCheckBox()
#             self.ui.tableWidget.insertRow(rowi)
#             self.ui.tableWidget.setCellWidget(rowi, 2, checkbox)
#             for coli, datai in enumerate(i):
#                 celli = QtWidgets.QTableWidgetItem(str(datai))
#                 self.ui.tableWidget.setItem(rowi, coli, celli)
#                 celli.setTextAlignment(Qt.AlignHCenter)
#
# window = MainWindow()
# window.show()
# sys.exit(app.exec_())

from PyQt5 import QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.tableModel = QtGui.QStandardItemModel(self)
        self.tableModel.itemChanged.connect(self.itemChanged)
        l=[1,2,3,4,5]
        for i in range(0,len(l)):
            item = QtGui.QStandardItem(l[i])
            item.setCheckable(True)
            self.tableModel.appendRow(item)

            self.mainLayout = QtWidgets.QVBoxLayout()
            self.setLayout(self.mainLayout)

            self.tableView = QtWidgets.QTableView()
            self.tableView.setModel(self.tableModel)
            self.mainLayout.addWidget(self.tableView)

    def itemChanged(self, item):
        print("Item {!r} checkState: {}".format(item.text(), item.checkState()))


def main():
    app = QtWidgets.QApplication([])

    win = MyWidget()
    win.show()
    win.raise_()
    app.exec_()

if __name__ == "__main__":
    main()