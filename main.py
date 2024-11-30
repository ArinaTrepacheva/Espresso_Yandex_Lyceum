import io
import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from datetime import datetime

DB_NAME = "coffee.sqlite"


class AddWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.con = sqlite3.connect(DB_NAME)
        self.pushButton.clicked.connect(self.add_elem)
        self.type.addItems(['Молотый', 'В зёрнах'])
        self.__is_adding_successful = False
        self.price.setMaximum(1000)

    def add_elem(self):
        cur = self.con.cursor()
        try:
            id = cur.execute("SELECT max(id) FROM products").fetchone()[0] + 1
            sort = self.sort.text()
            roasting = self.roasting.text()
            type = self.type.currentText()
            description = self.description.text()
            price = int(self.price.value())
            volume = float(self.volume.value())
            if price <= 0 or volume <= 0:
                raise ValueError('price or volume <= 0')
            if len(sort) == 0 or len(description) == 0 or len(roasting) == 0:
                raise ValueError('sort or description or roasting len = 0')

            new_data = (id, sort, roasting, type, description, price, volume)
            title = cur.execute("SELECT sort from products").fetchall()
            if (sort,) in title:
                cur.execute("""UPDATE products 
                SET roasting = ?, type = ?, description = ?, price = ?, volume = ?
                WHERE sort = ?""", (roasting, type, description, price, volume, sort))
            else:
                cur.execute("INSERT INTO products VALUES (?,?,?,?,?,?,?)", new_data)
            self.__is_adding_successful = True
        except ValueError as ve:
            self.__is_adding_successful = False
            self.statusBar().showMessage("Неверно заполнена форма")
        else:
            self.con.commit()
            self.parent().update_result()
            self.close()

    def get_adding_verdict(self):
        return self.__is_adding_successful


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect(DB_NAME)
        self.update_result()
        self.pushButton.clicked.connect(self.adding)
        self.add_form = None

    def update_result(self):
        cur = self.con.cursor()
        que = 'select * from products'
        result = cur.execute(que).fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def adding(self):
        self.add_form = AddWidget(self)
        self.add_form.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
