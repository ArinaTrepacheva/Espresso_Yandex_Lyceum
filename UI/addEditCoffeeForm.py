# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 566)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 411, 41))
        self.label.setStyleSheet("font-size:20px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 101, 31))
        self.label_2.setStyleSheet("font-size: 20px;")
        self.label_2.setObjectName("label_2")
        self.sort = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.sort.setGeometry(QtCore.QRect(150, 90, 461, 31))
        self.sort.setObjectName("sort")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 161, 71))
        self.label_3.setStyleSheet("font-size: 20px;")
        self.label_3.setObjectName("label_3")
        self.roasting = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.roasting.setGeometry(QtCore.QRect(210, 160, 401, 31))
        self.roasting.setObjectName("roasting")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 210, 161, 71))
        self.label_4.setStyleSheet("font-size: 20px;")
        self.label_4.setObjectName("label_4")
        self.type = QtWidgets.QComboBox(parent=self.centralwidget)
        self.type.setGeometry(QtCore.QRect(90, 230, 271, 31))
        self.type.setObjectName("type")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 280, 161, 71))
        self.label_5.setStyleSheet("font-size: 20px;")
        self.label_5.setObjectName("label_5")
        self.description = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.description.setGeometry(QtCore.QRect(150, 300, 401, 31))
        self.description.setObjectName("description")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 350, 161, 71))
        self.label_7.setStyleSheet("font-size: 20px;")
        self.label_7.setObjectName("label_7")
        self.price = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.price.setGeometry(QtCore.QRect(120, 380, 281, 21))
        self.price.setObjectName("price")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 410, 161, 71))
        self.label_8.setStyleSheet("font-size: 20px;")
        self.label_8.setObjectName("label_8")
        self.volume = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(120, 440, 281, 21))
        self.volume.setObjectName("volume")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(490, 440, 201, 61))
        self.pushButton.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: white;\n"
"font-size: 20px;\n"
"border-radius: 40px;")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Добавление/Редактирование"))
        self.label_2.setText(_translate("MainWindow", "сорт"))
        self.label_3.setText(_translate("MainWindow", "степень обжарки"))
        self.label_4.setText(_translate("MainWindow", "тип"))
        self.label_5.setText(_translate("MainWindow", "описание"))
        self.label_7.setText(_translate("MainWindow", "цена"))
        self.label_8.setText(_translate("MainWindow", "объём"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить"))
