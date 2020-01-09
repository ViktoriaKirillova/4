import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from UI import Ui_MainWindow
import sqlite3


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.params = {}
        self.con = sqlite3.connect("films.db")
        self.selectGenres()
        self.pushButton.clicked.connect(self.select)

    def selectGenres(self):
        req = "SELECT * from genres"
        cur = self.con.cursor()
        for value, key in cur.execute(req).fetchall():
            self.params[key] = value
        self.comboBox.addItems(list(self.params.keys()))

    def select(self):
        req = "SELECT * FROM Films WHERE genre = {}".format(self.params.get(self.comboBox.currentText()))
        cur = self.con.cursor()
        result = cur.execute(req).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())