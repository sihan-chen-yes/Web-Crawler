# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 513)
        MainWindow.setWindowTitle("DouBanTop250")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setStyleSheet("border-image: url(:/douban.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(580, 16777215))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.rank_search_button = QtWidgets.QPushButton(self.centralwidget)
        self.rank_search_button.setObjectName("rank_search_button")
        self.verticalLayout.addWidget(self.rank_search_button, 0, QtCore.Qt.AlignHCenter)
        self.name_search_button = QtWidgets.QPushButton(self.centralwidget)
        self.name_search_button.setObjectName("name_search_button")
        self.verticalLayout.addWidget(self.name_search_button, 0, QtCore.Qt.AlignHCenter)
        self.score_search_button = QtWidgets.QPushButton(self.centralwidget)
        self.score_search_button.setObjectName("score_search_button")
        self.verticalLayout.addWidget(self.score_search_button, 0, QtCore.Qt.AlignHCenter)
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setObjectName("close_button")
        self.verticalLayout.addWidget(self.close_button, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.close_button.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "请问想通过哪种方式查找电影信息？"))
        self.rank_search_button.setText(_translate("MainWindow", "豆瓣排名"))
        self.name_search_button.setText(_translate("MainWindow", "电影名"))
        self.score_search_button.setText(_translate("MainWindow", "豆瓣评分"))
        self.close_button.setText(_translate("MainWindow", "退出"))
import picture_rc
