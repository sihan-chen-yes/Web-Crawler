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
        MainWindow.resize(677, 740)
        MainWindow.setWindowTitle("DouBanTop250")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name_search_button = QtWidgets.QPushButton(self.centralwidget)
        self.name_search_button.setGeometry(QtCore.QRect(570, 640, 93, 28))
        self.name_search_button.setObjectName("name_search_button")
        self.rank_search_button = QtWidgets.QPushButton(self.centralwidget)
        self.rank_search_button.setGeometry(QtCore.QRect(570, 600, 93, 28))
        self.rank_search_button.setObjectName("rank_search_button")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(11, 11, 256, 351))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 490, 240, 16))
        self.label.setMaximumSize(QtCore.QSize(580, 16777215))
        self.label.setObjectName("label")
        self.rank_line = QtWidgets.QLineEdit(self.centralwidget)
        self.rank_line.setGeometry(QtCore.QRect(340, 600, 171, 24))
        self.rank_line.setObjectName("rank_line")
        self.name_line = QtWidgets.QLineEdit(self.centralwidget)
        self.name_line.setGeometry(QtCore.QRect(341, 645, 171, 24))
        self.name_line.setObjectName("name_line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 600, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 650, 45, 16))
        self.label_3.setObjectName("label_3")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(11, 393, 256, 261))
        self.graphicsView.setStyleSheet("border-image: url(:/douban.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(330, 40, 281, 421))
        self.picture_label.setText("")
        self.picture_label.setObjectName("picture_label")
        self.close_button = QtWidgets.QPushButton(self.centralwidget)
        self.close_button.setGeometry(QtCore.QRect(341, 676, 93, 28))
        self.close_button.setObjectName("close_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 570, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 530, 72, 15))
        self.label_5.setObjectName("label_5")
        self.judge_person_line = QtWidgets.QLineEdit(self.centralwidget)
        self.judge_person_line.setGeometry(QtCore.QRect(340, 520, 171, 31))
        self.judge_person_line.setObjectName("judge_person_line")
        self.score_line = QtWidgets.QLineEdit(self.centralwidget)
        self.score_line.setGeometry(QtCore.QRect(340, 560, 171, 31))
        self.score_line.setObjectName("score_line")
        self.judge_person_search_button = QtWidgets.QPushButton(self.centralwidget)
        self.judge_person_search_button.setGeometry(QtCore.QRect(570, 520, 93, 28))
        self.judge_person_search_button.setObjectName("judge_person_search_button")
        self.score_search_button = QtWidgets.QPushButton(self.centralwidget)
        self.score_search_button.setGeometry(QtCore.QRect(570, 560, 93, 28))
        self.score_search_button.setObjectName("score_search_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.close_button.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.name_search_button.setText(_translate("MainWindow", "search"))
        self.rank_search_button.setText(_translate("MainWindow", "search"))
        self.label.setText(_translate("MainWindow", "请问想通过哪种方式查找电影信息？"))
        self.label_2.setText(_translate("MainWindow", "豆瓣排名"))
        self.label_3.setText(_translate("MainWindow", "电影名"))
        self.close_button.setText(_translate("MainWindow", "退出"))
        self.label_4.setText(_translate("MainWindow", "评分"))
        self.label_5.setText(_translate("MainWindow", "评分人数"))
        self.judge_person_search_button.setText(_translate("MainWindow", "search"))
        self.score_search_button.setText(_translate("MainWindow", "search"))
import picture_rc