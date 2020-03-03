# -*-coding: utf-8 -*-

import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import requests
import json
import speech_recognition as sr
import keyboard
from subprocess import Popen
import os, requests
import webbrowser
import requests
import json
import sqlite3
from threading import Thread
import pyttsx3
from filelock import FileLock
import re
import time
import datetime
from random import choice
import subprocess
import zipfile
from PyQt5.QtWidgets import QWidget, QApplication, QHBoxLayout, QLabel, QDialog
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsLinearLayout, QGraphicsWidget
from PyQt5.QtGui import QMovie, QPixmap, QCursor, QIcon
from PyQt5.QtWidgets import QMainWindow, QCheckBox, QGridLayout, QSpacerItem, QSizePolicy, \
    QPushButton, QLineEdit, QInputDialog, QSizePolicy, QVBoxLayout, QAction
from PyQt5.QtCore import QCoreApplication, QSettings, QRect, QByteArray, pyqtSlot

speak_engine = pyttsx3.init()
candycash = 0
z = zipfile.ZipFile('CandyBase.zip')
pasw = 'Q5du7cc4opEQ1189'.encode()
z.extractall(pwd=pasw)
z.extract("CandyBase.db", pwd='Q5du7cc4opEQ1189'.encode())
level = 1
message_candy = ''
message_user = ''
name_user = "You"
translator = 1
message_user_array = []
interface = 1
sounds_and_voices = 1
message_candy_array = []
icon_user = 'Images/players/user.png'
count_candycash = 'Candycash:   ' + str(candycash)

def say(message):
    speak_engine.say(message)
    speak_engine.runAndWait()
    speak_engine.stop()


class CandyMarket(QWidget):
    def __init__(self, parent=None):
        global candycash
        global message_user
        global message_candy
        super().__init__()
        self.setupUi(self)
        self.candycash_print()
        self.setWindowIcon(QtGui.QIcon('logo_CA.ico'))
        self.pushButton_2.clicked.connect(self.open_INTERFACE_buy_iFace)
        self.pushButton_3.clicked.connect(self.open_INTERFACE_buy_soundsAndVoices)
        self.pushButton_4.clicked.connect(self.open_INTERFACE_buy_skills)
        self.settings = QSettings('CandyAssistent', 'CandyCompany', self)
        self.loadSettings()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(793, 477)
        Form.setStyleSheet("QWidget {background-color: white;}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {font-size: 70px; color: brown;}")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 86, 771, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(250, 10, 20, 91))
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 20, 75, 51))
        self.pushButton.setStyleSheet("QPushButton {border: None;}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/candycash_logo.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 251, 331))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {border: 2px solid brown;}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/CandyMarket/iFaces.jpg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 120, 251, 331))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {border: 2px solid brown;}")
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/CandyMarket/plays_and_skills.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 120, 251, 331))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {border: 2px solid brown;}")
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/CandyMarket/Sounds_And_Voices.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label.raise_()
        self.line_2.raise_()
        self.line.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CandyMarket"))
        self.label.setText(_translate("Form", "CandyMarket"))
        self.label_2.setText(_translate("Form", "0"))

    def open_INTERFACE_buy_iFace(self):
        self.close()
        self.open_iFace = Interface_candymarket_BUYiFace()
        self.open_iFace.show()

    def open_INTERFACE_buy_soundsAndVoices(self):
        self.close()
        self.open_iFace = CandyMarket_SoundsAndVoices()
        self.open_iFace.show()

    def open_INTERFACE_buy_skills(self):
        self.close()
        self.open_iFace = CandyMarket_skills()
        self.open_iFace.show()

    def candycash_print(self):
        global candycash
        self.label_2.setText(str(candycash))

    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def loadSettings(self):
        if self.settings.contains('geometry'):
            self.setGeometry(self.settings.value('geometry'))

    def saveSettings(self):
        global candycash
        global level, sounds_and_voices
        global interface, name_user, icon_user, translator
        con = sqlite3.connect('CandyBase.db')
        cur = con.cursor()
        sql = "DELETE FROM resources"
        cur.execute(sql)
        sql = "DELETE FROM settings"
        cur.execute(sql)
        sql = "DELETE FROM candymarket"
        cur.execute(sql)
        info_database = [str(candycash), str(level)]
        cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
        cur.execute('INSERT INTO candymarket VALUES(?, ?, ?)', (interface, sounds_and_voices, translator,))
        cur.execute('INSERT INTO settings VALUES(?, ?)', (name_user, icon_user,))
        con.commit()
        with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
            myzip.write('CandyBase.db')


class Interface_candymarket_BUYiFace(QWidget):
    def __init__(self, parent=None):
        global candycash, interface
        global message_user
        global message_candy
        super().__init__()
        self.setupUi(self)
        self.candycash_print()
        self.setWindowIcon(QtGui.QIcon('logo_CA.ico'))
        self.pushButton_3.clicked.connect(self.open_iFace_2)
        self.pushButton_2.clicked.connect(self.open_iFace_1)
        self.pushButton_4.clicked.connect(self.back_in_candymarket)
        self.settings = QSettings('CandyAssistent', 'CandyCompany', self)
        self.loadSettings()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(791, 533)
        Form.setStyleSheet("QWidget {background-color: white;}")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(250, 10, 20, 91))
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 120, 251, 331))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {border: 2px solid brown;}")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/CandyMarket/iFaces/iFaceCandy.jpg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 120, 251, 331))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {border: 2px solid brown;}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/CandyMarket/iFaces/iFaceDoughnut.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {font-size: 70px; color: brown;}")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 86, 771, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 20, 75, 51))
        self.pushButton.setStyleSheet("QPushButton {border: None;}")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/candycash_logo.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 460, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(510, 460, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 100, 51, 51))
        self.pushButton_4.setStyleSheet("QPushButton {border: none;}")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        global interface
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CandyMarket"))
        self.label_2.setText(_translate("Form", "0"))
        self.label.setText(_translate("Form", "CandyMarket"))
        self.label_3.setText(_translate("Form", "Куплено"))
        if interface == 1:
            self.label_4.setText(_translate("Form", "400 CandyCash"))
        elif interface == 2:
            self.label_4.setText(_translate("Form", "     Куплено"))

    def open_iFace_2(self):
        global candycash, interface
        if candycash >= 400 or interface == 2:
            if interface == 1:
                candycash -= 400
            interface = 2
            self.close()
            self.open_iFace = Interface2()
            self.open_iFace.show()

    def back_in_candymarket(self):
        self.close()
        self.open_iFace = CandyMarket()
        self.open_iFace.show()

    def open_iFace_1(self):
        self.close()
        self.open_iFace = Interface1()
        self.open_iFace.show()

    def candycash_print(self):
        global candycash
        self.label_2.setText(str(candycash))

    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def loadSettings(self):
        if self.settings.contains('geometry'):
            self.setGeometry(self.settings.value('geometry'))

    def saveSettings(self):
        global candycash
        global level, sounds_and_voices
        global interface, name_user, icon_user, translator
        con = sqlite3.connect('CandyBase.db')
        cur = con.cursor()
        sql = "DELETE FROM resources"
        cur.execute(sql)
        sql = "DELETE FROM settings"
        cur.execute(sql)
        sql = "DELETE FROM candymarket"
        cur.execute(sql)
        info_database = [str(candycash), str(level)]
        cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
        cur.execute('INSERT INTO candymarket VALUES(?, ?, ?)', (interface, sounds_and_voices, translator,))
        cur.execute('INSERT INTO settings VALUES(?, ?)', (name_user, icon_user,))
        con.commit()
        with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
            myzip.write('CandyBase.db')


class CandyMarket_SoundsAndVoices(QWidget):
    def __init__(self, parent=None):
        global candycash, sounds_and_voices
        global message_user
        global message_candy
        super().__init__()
        self.setupUi(self)
        self.candycash_print()
        self.setWindowIcon(QtGui.QIcon('logo_CA.ico'))
        self.pushButton_3.clicked.connect(self.open_iFace)
        self.pushButton_2.clicked.connect(self.open_iFace)
        self.pushButton_4.clicked.connect(self.back_in_candymarket)
        self.settings = QSettings('CandyAssistent', 'CandyCompany', self)
        self.loadSettings()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(790, 533)
        Form.setStyleSheet("QWidget {background-color: white;}")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 86, 771, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 460, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(510, 460, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 120, 251, 331))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {border: 2px solid brown;}")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/CandyMarket/sounds and voices/sounds-voice.jpg"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 100, 51, 51))
        self.pushButton_4.setStyleSheet("QPushButton {border: none;}")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 20, 75, 51))
        self.pushButton.setStyleSheet("QPushButton {border: None;}")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/candycash_logo.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 120, 251, 331))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {border: 2px solid brown;}")
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/CandyMarket/sounds and voices/sounds_1.jpg"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {font-size: 70px; color: brown;}")
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(250, 10, 20, 91))
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        global sounds_and_voices
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Куплено"))
        self.label_2.setText(_translate("Form", "0"))
        self.label.setText(_translate("Form", "CandyMarket"))
        if sounds_and_voices == 1:
            self.label_4.setText(_translate("Form", "160 CandyCash"))
        elif sounds_and_voices == 2:
            self.label_4.setText(_translate("Form", "     Куплено"))

    def open_iFace(self):
        global candycash, interface, sounds_and_voices
        if candycash >= 160 or sounds_and_voices == 2:
            if sounds_and_voices == 1:
                candycash -= 160
            sounds_and_voices = 2
            self.close()
            if interface == 1:
                self.open_iFace = Interface1()
            elif interface == 2:
                self.open_iFace = Interface2()
            self.open_iFace.show()

    def back_in_candymarket(self):
        self.close()
        self.open_iFace = CandyMarket()
        self.open_iFace.show()

    def candycash_print(self):
        global candycash
        self.label_2.setText(str(candycash))

    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def loadSettings(self):
        if self.settings.contains('geometry'):
            self.setGeometry(self.settings.value('geometry'))

    def saveSettings(self):
        global candycash
        global level, sounds_and_voices
        global interface, name_user, icon_user, translator
        con = sqlite3.connect('CandyBase.db')
        cur = con.cursor()
        sql = "DELETE FROM resources"
        cur.execute(sql)
        sql = "DELETE FROM settings"
        cur.execute(sql)
        sql = "DELETE FROM candymarket"
        cur.execute(sql)
        info_database = [str(candycash), str(level)]
        cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
        cur.execute('INSERT INTO candymarket VALUES(?, ?, ?)', (interface, sounds_and_voices, translator,))
        cur.execute('INSERT INTO settings VALUES(?, ?)', (name_user, icon_user,))
        con.commit()
        with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
            myzip.write('CandyBase.db')


class CandyMarket_skills(QWidget):
    def __init__(self, parent=None):
        global candycash, sounds_and_voices
        global message_user
        global message_candy
        super().__init__()
        self.setupUi(self)
        self.candycash_print()
        self.setWindowIcon(QtGui.QIcon('logo_CA.ico'))
        self.pushButton_4.clicked.connect(self.back_in_candymarket)
        self.pushButton_3.clicked.connect(self.candyTranslator)
        self.settings = QSettings('CandyAssistent', 'CandyCompany', self)
        self.loadSettings()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(797, 526)
        Form.setStyleSheet("QWidget {background-color: white;}")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 100, 51, 61))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {border: none;}")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 86, 771, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(260, 10, 20, 81))
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(310, 460, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 20, 75, 51))
        self.pushButton.setStyleSheet("QPushButton {border: None;}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/candycash_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 120, 251, 331))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {border: 2px solid brown;}")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/CandyMarket/skills/CandyTranslator.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 0, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Niagara Engraved")
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {font-size: 70px; color: brown;}")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CandyMarket"))
        self.label_4.setText(_translate("Form", "600 candycash"))
        self.label_2.setText(_translate("Form", "0"))
        self.label.setText(_translate("Form", "CandyMarket"))


    def back_in_candymarket(self):
        self.close()
        self.open_iFace = CandyMarket()
        self.open_iFace.show()

    def candyTranslator(self):
        global candycash, interface, translator
        if candycash >= 160 or translator == 2:
            if translator == 1:
                candycash -= 160
            translator = 2
            self.close()
            if interface == 1:
                self.open_iFace = Interface1()
            elif interface == 2:
                self.open_iFace = Interface2()
            self.open_iFace.show()

    def candycash_print(self):
        global candycash
        self.label_2.setText(str(candycash))


    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def loadSettings(self):
        if self.settings.contains('geometry'):
            self.setGeometry(self.settings.value('geometry'))

    def saveSettings(self):
        global candycash
        global level, sounds_and_voices, translator
        global interface, name_user, icon_user
        con = sqlite3.connect('CandyBase.db')
        cur = con.cursor()
        sql = "DELETE FROM resources"
        cur.execute(sql)
        sql = "DELETE FROM settings"
        cur.execute(sql)
        sql = "DELETE FROM candymarket"
        cur.execute(sql)
        info_database = [str(candycash), str(level)]
        cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
        cur.execute('INSERT INTO candymarket VALUES(?, ?, ?)', (interface, sounds_and_voices, translator,))
        cur.execute('INSERT INTO settings VALUES(?, ?)', (name_user, icon_user,))
        con.commit()
        with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
            myzip.write('CandyBase.db')


class Interface1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        global candycash
        global message_user
        global message_candy
        super().__init__()
        self.setupUi(self)
        self.candycash_print()
        self.level_print()
        self.setWindowIcon(QtGui.QIcon('logo_CA.ico'))
        self.pushButton.clicked.connect(self.interface_operation)
        self.pushButton_2.clicked.connect(self.open_CandyMarket)
        self.pushButton_3.clicked.connect(self.go_open_keyboard_interface)
        self.settings = QSettings('CandyAssistent', 'CandyCompany', self)
        self.loadSettings()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(413, 635)
        Form.setStyleSheet("QWidget {background-color: white;}")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 490, 131, 121))
        self.pushButton.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/CA_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(150, 150))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 530, 81, 81))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/candymarket_iFace_1.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(310, 530, 91, 81))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/candyKeyboard_iFace_1.jpg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 10, 75, 51))
        self.pushButton_4.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/candycash_logo.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(234, 10, 71, 51))
        self.pushButton_5.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/logo_lvl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 10, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 371, 401))
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit.setStyleSheet("QTextEdit {border: 2px solid red; font-size: 20px;}")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CandyAssistant"))
        self.label.setText(_translate("Form", "0"))
        self.label_2.setText(_translate("Form", "0"))
        self.textEdit.setReadOnly(True)

    def go_open_keyboard_interface(self):
        self.close()
        self.iFace_keyboard = Interface_1_keyboard()
        self.iFace_keyboard.show()

    def interface_operation(self):
        global count_temp
        global candycash, sounds_and_voices
        global message_user
        global message_candy
        self.add_gif()
        if sounds_and_voices == 2:
            self.load_mp3('Images/Sounds/input.mp3')
            self.player.play()
            for i in range(5):
                say("")
        Program_operation()
        Program_operation.answere_candy(self, message_user)
        try:
            self.print_message()
        except IndexError:
            pass
        self.remove_gif()
        if "вв" and 'код разработчика' in message_user:
            self.creatorCode_win()
        if ("pac" in message_user and "man" in message_user) or (
                "pac" in message_user and "ман" in message_user) or (
                "pac" in message_user and "мэн" in message_user) or (
                "пак" in message_user and "man" in message_user) or (
                "пак" in message_user and "ман" in message_user) or (
                "пак" in message_user and "мэн" in message_user):
            self.candycash_print()
            self.level_print()

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player2 = QtMultimedia.QMediaPlayer()
        self.player2.setMedia(content)

    def creatorCode_win(self):
        global candycash
        global message_user
        global creator
        global level
        text, ok = QInputDialog.getText(self, 'CreatorCode', 'Введите код разработчика: ')
        if ok:
            if text == 'Q5du7cc4opEQ1189':
                candycash = 9999999999
                level = 9999999999
                say('Код верный!')
                creator = True
                self.candycash_print()
                self.level_print()
            else:
                say('Код неверный!')

    def candycash_print(self):
        global candycash
        self.label.setText(str(candycash))

    def level_print(self):
        global level
        self.label_2.setText(str(level))

    def open_CandyMarket(self):
        self.close()
        self.CM = CandyMarket()
        self.CM.show()

    def add_gif(self):
        self._layout = self.layout()
        self._gif = QtWidgets.QLabel()
        self._gif.move(145, 495)
        movie = QtGui.QMovie("Images/CA_giphy_button.gif")
        self._gif.setMovie(movie)
        self._gif.resize(120, 120)
        movie.start()
        self._layout.addWidget(self._gif)

    def remove_gif(self):
        self._gif.hide()

    def print_message(self):
        global icon_user
        global name_user
        global message_user
        html = (
                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                    "<br><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; font-size: 30px; -qt-block-indent:0; text-indent:0px;\"><img src=" + icon_user + " align=\"top\">" + name_user + "</p>\n"
                                                                                                                                                                                                                            "<p style=\"font-size: 20px;\">" +
                    message_user[0].upper() + message_user[1:] + "</p>\n"
                                                                 "<br><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; font-size: 30px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Images/candy.png\" align=\"top\">Candy</p>\n"
                                                                 "<p style=\"font-size: 20px;\">" + message_candy + "</p></body></html>")
        self.textEdit.append(html)

    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def loadSettings(self):
        if self.settings.contains('geometry'):
            self.setGeometry(self.settings.value('geometry'))

    def saveSettings(self):
        global candycash
        global level, sounds_and_voices, translator
        global interface, name_user, icon_user
        con = sqlite3.connect('CandyBase.db')
        cur = con.cursor()
        sql = "DELETE FROM resources"
        cur.execute(sql)
        sql = "DELETE FROM settings"
        cur.execute(sql)
        sql = "DELETE FROM candymarket"
        cur.execute(sql)
        info_database = [str(candycash), str(level)]
        cur.execute('INSERT INTO candymarket VALUES(?, ?, ?)', (interface, sounds_and_voices, translator,))
        cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
        cur.execute('INSERT INTO settings VALUES(?, ?)', (name_user, icon_user,))
        con.commit()
        with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
            myzip.write('CandyBase.db')


class Interface_1_keyboard(QWidget):
    def __init__(self):
        global candycash
        global message_user
        global message_candy
        super().__init__()
        self.setupUi(self)
        self.candycash_print()
        self.level_print()
        self.setWindowIcon(QtGui.QIcon('logo_CA.ico'))
        self.pushButton_3.clicked.connect(self.go_text)
        self.pushButton_2.clicked.connect(self.open_CandyMarket)
        self.pushButton.clicked.connect(self.open_MainiFace)
        self.settings = QSettings('CandyAssistent', 'CandyCompany', self)
        self.loadSettings()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(414, 657)
        Form.setStyleSheet("QWidget {background-color: white;}")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(234, 10, 71, 51))
        self.pushButton_5.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/logo_lvl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 371, 401))
        self.textEdit.setStyleSheet("QTextEdit {border: 2px solid red;}")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 560, 81, 91))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/CA_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 570, 81, 81))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/candymarket_iFace_1.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 10, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 10, 75, 51))
        self.pushButton_4.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/candycash_logo.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 500, 91, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(
            "QPushButton {background-color: white; border: 2px solid red;}")
        self.pushButton_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/logo_go_mes.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QtCore.QSize(300, 300))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 500, 191, 51))
        self.lineEdit.setStyleSheet(
            "QLineEdit {background-color: white; font-size: 20px; border: 2px solid red;}")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CandyAssistant"))
        self.textEdit.setReadOnly(True)
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("Form", "0"))
        self.label_2.setText(_translate("Form", "0"))

    def open_MainiFace(self):
        self.close()
        self.iFace = Interface1()
        self.iFace.show()

    def interface_operation(self):
        global count_temp
        global candycash
        global message_user
        global message_candy
        Program_operation.answere_candy(self, message_user)
        self.print_message()
        if "вв" and 'код разработчика' in message_user:
            self.creatorCode_win()
        if ("pac" in message_user and "man" in message_user) or (
                "pac" in message_user and "ман" in message_user) or (
                "pac" in message_user and "мэн" in message_user) or (
                "пак" in message_user and "man" in message_user) or (
                "пак" in message_user and "ман" in message_user) or (
                "пак" in message_user and "мэн" in message_user):
            self.candycash_print()
            self.level_print()

    def print_message(self):
        global icon_user, message_user_array, message_candy_array
        global name_user
        global message_user
        html = ("<!DOCTYPE HTML <html><head>"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<br><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; font-size: 30px; -qt-block-indent:0; text-indent:0px;\"><img src=" + icon_user + " align=\"top\">" + name_user + "</p>\n"
                                                                                                                                                                                                                        "<p style=\"font-size: 20px;\">" +
                message_user[0].upper() + message_user[1:] + "</p>\n"
                                                             "<br><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; font-size: 30px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Images/candy.png\" align=\"top\">Candy</p>\n"
                                                             "<p style=\"font-size: 20px;\">" + message_candy + "</p></body></html>")
        self.textEdit.append(html)

    def go_text(self):
        global message_user
        message_user = self.lineEdit.text()
        message_user = message_user.lower()
        self.lineEdit.setText('')
        self.interface_operation()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.go_text()

    def creatorCode_win(self):
        global candycash
        global message_user
        global creator
        global level
        text, ok = QInputDialog.getText(self, 'CreatorCode', 'Введите код разработчика: ')
        if ok:
            if text == 'Q5du7cc4opEQ1189':
                candycash = 9999999999
                level = 9999999999
                say('Код верный!')
                creator = True
                self.candycash_print()
                self.level_print()
            else:
                say('Код неверный!')

    def candycash_print(self):
        global candycash
        self.label.setText(str(candycash))

    def level_print(self):
        global level
        self.label_2.setText(str(level))

    def open_CandyMarket(self):
        self.close()
        self.CM = CandyMarket()
        self.CM.show()

    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def loadSettings(self):
        if self.settings.contains('geometry'):
            self.setGeometry(self.settings.value('geometry'))

    def saveSettings(self):
        global candycash
        global level, sounds_and_voices, translator
        global interface, name_user, icon_user
        con = sqlite3.connect('CandyBase.db')
        cur = con.cursor()
        sql = "DELETE FROM resources"
        cur.execute(sql)
        sql = "DELETE FROM settings"
        cur.execute(sql)
        sql = "DELETE FROM candymarket"
        cur.execute(sql)
        info_database = [str(candycash), str(level)]
        cur.execute('INSERT INTO candymarket VALUES(?, ?, ?)', (interface, sounds_and_voices, translator))
        cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
        cur.execute('INSERT INTO settings VALUES(?, ?)', (name_user, icon_user,))
        con.commit()
        with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
            myzip.write('CandyBase.db')


class Interface2(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        global candycash
        global message_user
        global message_candy
        super().__init__()
        self.setupUi(self)
        self.candycash_print()
        self.level_print()
        self.setWindowIcon(QtGui.QIcon('logo_CA.ico'))
        self.pushButton.clicked.connect(self.interface_operation)
        self.pushButton_2.clicked.connect(self.open_CandyMarket)
        self.pushButton_3.clicked.connect(self.go_open_keyboard_interface)
        self.settings = QSettings('CandyAssistent', 'CandyCompany', self)
        self.loadSettings()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(412, 638)
        Form.setStyleSheet("QWidget  {background-color: white;}")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 520, 71, 101))
        self.pushButton.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/CA_giphy_button_iFace_2.gif"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 20, 75, 51))
        self.pushButton_4.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/candycash_logo_2.jpg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 20, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 530, 111, 91))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/candymarket_iFace_2.jpg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 540, 111, 81))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/candyKeyboard_iFace_2.jpg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QtCore.QSize(130, 130))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(234, 20, 71, 51))
        self.pushButton_5.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_5.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/logo_lvl_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 90, 371, 401))
        self.textEdit.setStyleSheet("QTextEdit {border: 2px solid pink;}")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CandyAssistant"))
        self.textEdit.setReadOnly(True)
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.label.setText(_translate("Form", "0"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Form", "101010"))

    def go_open_keyboard_interface(self):
        self.close()
        self.open_IFace = Interface2_keyboard()
        self.open_IFace.show()

    def interface_operation(self):
        global count_temp
        global candycash, sounds_and_voices
        global message_user
        global message_candy
        self.add_gif()
        if sounds_and_voices == 2:
            self.load_mp3('Images/Sounds/input.mp3')
            self.player.play()
            for i in range(5):
                say("")
        Program_operation()
        Program_operation.answere_candy(self, message_user)
        try:
            self.print_message()
        except IndexError:
            pass
        self.remove_gif()
        if "вв" and 'код разработчика' in message_user:
            self.creatorCode_win()
        if ("pac" in message_user and "man" in message_user) or (
                "pac" in message_user and "ман" in message_user) or (
                "pac" in message_user and "мэн" in message_user) or (
                "пак" in message_user and "man" in message_user) or (
                "пак" in message_user and "ман" in message_user) or (
                "пак" in message_user and "мэн" in message_user) or (
                "пэк" in message_user and "мэн" in message_user) or (
                "пэк" in message_user and "ман" in message_user):
            self.candycash_print()
            self.level_print()

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        self.player2 = QtMultimedia.QMediaPlayer()
        self.player2.setMedia(content)

    def creatorCode_win(self):
        global candycash
        global message_user
        global creator
        global level
        text, ok = QInputDialog.getText(self, 'CreatorCode', 'Введите код разработчика: ')
        if ok:
            if text == 'Q5du7cc4opEQ1189':
                candycash = 9999999999
                level = 9999999999
                say('Код верный!')
                creator = True
                self.candycash_print()
                self.level_print()
            else:
                say('Код неверный!')

    def candycash_print(self):
        global candycash
        self.label.setText(str(candycash))

    def level_print(self):
        global level
        self.label_2.setText(str(level))

    def open_CandyMarket(self):
        self.close()
        self.CM = CandyMarket()
        self.CM.show()

    def add_gif(self):
        self._layout = self.layout()
        self._gif = QtWidgets.QLabel()
        self._gif.move(175, 510)
        movie = QtGui.QMovie("Images/50x88_CA_giphy_button_iFace_2.gif")
        self._gif.resize(120, 120)
        self._gif.setMovie(movie)

        movie.start()
        self._layout.addWidget(self._gif)

    def remove_gif(self):
        self._gif.hide()

    def print_message(self):
        global icon_user
        global name_user
        global message_user
        html = (
                    "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                    "p, li { white-space: pre-wrap; }\n"
                    "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                    "<br><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; font-size: 30px; -qt-block-indent:0; text-indent:0px;\"><img src=" + icon_user + " align=\"top\">" + name_user + "</p>\n"
                                                                                                                                                                                                                            "<p style=\"font-size: 20px;\">" +
                    message_user[0].upper() + message_user[1:] + "</p>\n"
                                                                 "<br><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; font-size: 30px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Images/candy.png\" align=\"top\">Candy</p>\n"
                                                                 "<p style=\"font-size: 20px;\">" + message_candy + "</p></body></html>")
        self.textEdit.append(html)

    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def loadSettings(self):
        if self.settings.contains('geometry'):
            self.setGeometry(self.settings.value('geometry'))

    def saveSettings(self):
        global candycash
        global level, sounds_and_voices, translator
        global interface, name_user, icon_user
        con = sqlite3.connect('CandyBase.db')
        cur = con.cursor()
        sql = "DELETE FROM resources"
        cur.execute(sql)
        sql = "DELETE FROM settings"
        cur.execute(sql)
        sql = "DELETE FROM candymarket"
        cur.execute(sql)
        info_database = [str(candycash), str(level)]
        cur.execute('INSERT INTO candymarket VALUES(?, ?, ?)', (interface, sounds_and_voices, translator))
        cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
        cur.execute('INSERT INTO settings VALUES(?, ?)', (name_user, icon_user,))
        con.commit()
        with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
            myzip.write('CandyBase.db')


class Interface2_keyboard(QWidget):
    def __init__(self, parent=None):
        global candycash
        global message_user
        global message_candy
        super().__init__()
        self.setupUi(self)
        self.candycash_print()
        self.level_print()
        self.setWindowIcon(QtGui.QIcon('logo_CA.ico'))
        self.pushButton.clicked.connect(self.open_MainiFace)
        self.pushButton_2.clicked.connect(self.open_CandyMarket)
        self.pushButton_3.clicked.connect(self.interface_operation)
        self.settings = QSettings('CandyAssistent', 'CandyCompany', self)
        self.loadSettings()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(415, 654)
        Form.setStyleSheet("QWidget {background-color: white;}")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 570, 81, 81))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/candymarket_iFace_2.jpg"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 10, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 550, 61, 91))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/CA_giphy_button_iFace_2.gif"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 500, 191, 51))
        self.lineEdit.setStyleSheet(
            "QLineEdit {font-size: 20px; background-color: white; border: 2px solid pink;}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 10, 75, 51))
        self.pushButton_4.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_4.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/candycash_logo_2.jpg"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(234, 10, 71, 51))
        self.pushButton_5.setStyleSheet("QPushButton {background-color: white; border: None;}")
        self.pushButton_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/logo_lvl_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 80, 371, 401))
        self.textEdit.setStyleSheet("QTextEdit {border: 2px solid pink; font-size: 20px;}")
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 500, 91, 51))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(
            "QPushButton {background-color: white; border: 2px solid pink;}")
        self.pushButton_3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/logo_go_mes_2.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CandyAssistant"))
        self.textEdit.setReadOnly(True)
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.label.setText(_translate("Form", "101010"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Form", "101010"))

    def open_MainiFace(self):
        self.close()
        self.iFace = Interface2()
        self.iFace.show()

    def interface_operation(self):
        global count_temp
        global candycash
        global message_user
        global message_candy
        Program_operation.answere_candy(self, message_user)
        self.print_message()
        if "вв" in message_user and 'код разработчика' in message_user:
            self.creatorCode_win()
        if ("pac" in message_user and "man" in message_user) or (
                "pac" in message_user and "ман" in message_user) or (
                "pac" in message_user and "мэн" in message_user) or (
                "пак" in message_user and "man" in message_user) or (
                "пак" in message_user and "ман" in message_user) or (
                "пак" in message_user and "мэн" in message_user):
            self.candycash_print()
            self.level_print()

    def print_message(self):
        global icon_user, message_user_array, message_candy_array
        global name_user
        global message_user
        html = ("<!DOCTYPE HTML <html><head>"
                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                "<br><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; font-size: 30px; -qt-block-indent:0; text-indent:0px;\"><img src=" + icon_user + " align=\"top\">" + name_user + "</p>\n"
                                                                                                                                                                                                                        "<p style=\"font-size: 20px;\">" +
                message_user[0].upper() + message_user[1:] + "</p>\n"
                                                             "<br><p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; font-size: 30px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Images/candy.png\" align=\"top\">Candy</p>\n"
                                                             "<p style=\"font-size: 20px;\">" + message_candy + "</p></body></html>")
        self.textEdit.append(html)

    def go_text(self):
        global message_user
        message_user = self.lineEdit.text()
        message_user = message_user.lower()
        self.lineEdit.setText('')
        self.interface_operation()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.go_text()

    def creatorCode_win(self):
        global candycash
        global message_user
        global creator
        global level
        text, ok = QInputDialog.getText(self, 'CreatorCode', 'Введите код разработчика: ')
        if ok:
            if text == 'Q5du7cc4opEQ1189':
                candycash = 9999999999
                level = 9999999999
                say('Код верный!')
                creator = True
                self.candycash_print()
                self.level_print()
            else:
                say('Код неверный!')

    def candycash_print(self):
        global candycash
        self.label.setText(str(candycash))

    def level_print(self):
        global level
        self.label_2.setText(str(level))

    def open_CandyMarket(self):
        self.close()
        self.CM = CandyMarket()
        self.CM.show()

    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def loadSettings(self):
        if self.settings.contains('geometry'):
            self.setGeometry(self.settings.value('geometry'))

    def saveSettings(self):
        global candycash, translator
        global level, sounds_and_voices
        global interface, name_user, icon_user
        con = sqlite3.connect('CandyBase.db')
        cur = con.cursor()
        sql = "DELETE FROM resources"
        cur.execute(sql)
        sql = "DELETE FROM settings"
        cur.execute(sql)
        sql = "DELETE FROM candymarket"
        cur.execute(sql)
        info_database = [str(candycash), str(level)]
        cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
        cur.execute('INSERT INTO candymarket VALUES(?, ?, ?)', (interface, sounds_and_voices, translator,))
        cur.execute('INSERT INTO settings VALUES(?, ?)', (name_user, icon_user,))
        con.commit()
        with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
            myzip.write('CandyBase.db')


class Translator(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.program_operation)
        self.pushButton_2.clicked.connect(self.clear_all)
        self.settings = QSettings('CandyAssistent', 'CandyCompany', self)
        self.loadSettings()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(731, 524)
        Form.setStyleSheet("QWidget {background-color: white;}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 30, 91, 71))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 41, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {color: purple;}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 10, 41, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {color: purple;}")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 130, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(460, 130, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(30, 190, 321, 191))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit {border: 2px solid purple;;}")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(380, 190, 321, 191))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setStyleSheet("QTextEdit {border: 2px solid purple;;}")
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 420, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {border: 2px solid purple;}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self)
        self.pushButton_2.resize(150, 50)
        self.pushButton_2.move(280, 130)
        self.pushButton_2.setText("Очистить всё")
        self.pushButton_2.setStyleSheet("QPushButton {font-size: 20px; border: 2px solid purple;}")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(190, 40, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Viner Hand ITC")
        font.setPointSize(28)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CandyTranslator"))
        self.label.setText(_translate("Form", "andy"))
        self.label_2.setText(_translate("Form", "C"))
        self.label_3.setText(_translate("Form", "T"))
        self.label_5.setText(_translate("Form", "Русский"))
        self.label_6.setText(_translate("Form", "Английский"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Перевести"))
        self.label_4.setText(_translate("Form", "ranslator"))

    def program_operation(self):
        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
        key = 'trnsl.1.1.20200209T055922Z.f03d103126ba907a.eb91d24257070f1f856fcf650cc7672198088153'
        if len(self.textEdit.toPlainText()) != 0 and len(self.textEdit_2.toPlainText()) == 0:
            text = self.textEdit.toPlainText()
            lang = 'ru-en'
            r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
            self.textEdit_2.setPlainText(json.loads(r.text)['text'][0])
        elif len(self.textEdit.toPlainText()) == 0 and len(self.textEdit_2.toPlainText()) != 0:
            text = self.textEdit_2.toPlainText()
            lang = 'en-ru'
            r = requests.post(url, data={'key': key, 'text': text, 'lang': lang})
            self.textEdit.setPlainText(json.loads(r.text)['text'][0])
        else:
            text = "НЕ КОРРЕКТНЫЙ ВВОД!"
            lang = 'en-ru'
            self.textEdit.setPlainText(text)
            self.textEdit_2.setPlainText(text)

    def clear_all(self):
        self.textEdit.setPlainText("")
        self.textEdit_2.setPlainText("")

    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def loadSettings(self):
        if self.settings.contains('geometry'):
            self.setGeometry(self.settings.value('geometry'))

    def saveSettings(self):
        global candycash, sounds_and_voices
        global level, message_candy_array, message_user_array, translator
        global interface, name_user, icon_user
        con = sqlite3.connect('CandyBase.db')
        cur = con.cursor()
        sql = "DELETE FROM resources"
        cur.execute(sql)
        sql = "DELETE FROM settings"
        cur.execute(sql)
        sql = "DELETE FROM candymarket"
        cur.execute(sql)
        info_database = [str(candycash), str(level)]
        cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
        cur.execute('INSERT INTO candymarket VALUES(?, ?, ?)',
                    (interface, sounds_and_voices, translator,))
        cur.execute('INSERT INTO settings VALUES(?, ?)', (name_user, icon_user,))
        con.commit()
        with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
            myzip.write('CandyBase.db')
        con.close()


class CandyProfile(QWidget):
    def __init__(self):
        global candycash, name_user, icon_user
        global message_user
        global message_candy
        super().__init__()
        self.setupUi(self)
        self.icons = ['Images/players/alien.png', 'Images/players/bear.png',
                      'Images/players/demon.png', 'Images/players/glasses.png',
                      'Images/players/hare.png', 'Images/players/koala.png',
                      'Images/players/love.png', 'Images/players/monkey.png',
                      'Images/players/user.png']
        self.counter = 0
        self.setWindowIcon(QtGui.QIcon('logo_CA.ico'))
        self.pushButton_2.clicked.connect(self.change_icon)
        self.pushButton_3.clicked.connect(self.save)
        self.settings = QSettings('CandyAssistent', 'CandyCompany', self)
        self.loadSettings()

    def setupUi(self, Form):
        global icon_user
        Form.setObjectName("Form")
        Form.setFixedSize(615, 504)
        Form.setStyleSheet("QWidget {background-color: white;}")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 320, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {border: 2px solid coral;}")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 90, 111, 131))
        self.pushButton.setStyleSheet("QPushButton {border: 1px solid grey;}")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(icon_user), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 240, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {border: 2px solid lightblue;}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(250, 20, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 420, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {background-color: green; border: None;}")
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        global name_user
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CandyProfile"))
        self.lineEdit.setText(_translate("Form", name_user))
        self.label.setText(_translate("Form", "Nickname"))
        self.pushButton_2.setText(_translate("Form", "Изменить картинку профиля"))
        self.label_2.setText(_translate("Form", "CandyProfile"))
        self.pushButton_3.setText(_translate("Form", "Save"))

    def change_icon(self):
        global icon_user
        icon_user = self.icons[self.counter]
        if self.counter == 8:
            self.counter = 0
        else:
            self.counter += 1
        self.pushButton.setIcon(QIcon(icon_user))

    def save(self):
        global name_user, icon_user
        name_user = self.lineEdit.text()
        self.close()

    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def loadSettings(self):
        if self.settings.contains('geometry'):
            self.setGeometry(self.settings.value('geometry'))

    def saveSettings(self):
        global candycash, sounds_and_voices
        global level, message_candy_array, message_user_array, translator
        global interface, name_user, icon_user
        con = sqlite3.connect('CandyBase.db')
        cur = con.cursor()
        sql = "DELETE FROM resources"
        cur.execute(sql)
        sql = "DELETE FROM settings"
        cur.execute(sql)
        sql = "DELETE FROM candymarket"
        cur.execute(sql)
        info_database = [str(candycash), str(level)]
        cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
        cur.execute('INSERT INTO candymarket VALUES(?, ?, ?)', (interface, sounds_and_voices, translator,))
        cur.execute('INSERT INTO settings VALUES(?, ?)', (name_user, icon_user,))
        con.commit()
        with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
            myzip.write('CandyBase.db')
        con.close()


class Program_operation(Interface1):
    def __init__(self):
        super().__init__()
        self.commands_user()

    def answere_candy(self, message):
        global message_user
        global game, name_user, icon_user, interface
        global level, translator
        global candycash
        global message_candy
        if 'привет' in message_user or 'здравствйте' in message_user or 'прив' in message_user or 'салам' in message_user:
            if "ор" not in message_user and "реш" not in message_user:
                message_candy = 'Привет!'
                if int(level) >= 2:
                    message_candy = choice(['Ку!', 'Хай!', 'Хеллоу!', 'Бонжур!', 'Привет!'])
                say(message_candy)
        elif 'как' in message_user and 'дел' in message_user:
            message_candy = "У меня замечательно, ведь я общаюсь с вами. А как у вас?"
            if int(level) >= 3:
                message_candy = choice(
                    ['У меня замечательно, ведь я общаюсь с вами. А как у вас?',
                     'Всё хорошо, а как у вас?',
                     'Не очень, но если вы со мной поиграете будет лучше.'])
            say(message_candy)
        elif 'да' in message_user:
            if message_user == 'да':
                message_candy = 'Я с вами полностью согласна!'
                if int(level) >= 4:
                    message_candy = choice(['Я с вами полностью согласна!', 'Я рада!'])
                say(message_candy)
            else:
                temp = message_user.split()
                for i in temp:
                    if i == 'да':
                        message_candy = 'Я с вами полностью согласна!'
                        go_say = message_candy
                    if int(level) >= 4 and i == 'да':
                        message_candy = choice(['Я с вами полностью согласна!', 'Я рада!'])
                        go_say = message_candy
                if message_candy != ('Я с вами полностью согласна!' or 'Я рада!'):
                    message_candy = "Разработчик этого приложения не научил меня этому. Но вы можете сделать меня лучше и написать ему в директе (candycompany_official) или на почту (candy.company@yandex.ru)"
                    go_say = "Разработчик этого приложения не научил меня этому."
                say(go_say)
        elif 'любимый цвет' in message_user:
            message_candy = 'Мой любимый цвет красный. А какой у вас?'
            say(message_candy)
        elif 'нет' in message_user:
            if message_user == 'нет':
                message_candy = 'Как так-то?'
                if int(level) >= 4:
                    message_candy = choice(['Как так-то?', 'Печально.'])
                say(message_candy)
            else:
                temp = message_user.split()
                for i in temp:
                    if i == 'нет':
                        message_candy = 'Как так-то?'
                    if int(level) >= 5 and i == 'нет':
                        message_candy = choice(['Как так-то?', 'Печально.'])
                        go_say = message_candy
                if message_candy != ('Как так-то?' or 'Печально.'):
                    message_candy = "Разработчик этого приложения не научил меня этому. Но вы можете сделать меня лучше и написать ему в директе (candycompany_official) или на почту (candy.company@yandex.ru)"
                    go_say = "Разработчик этого приложения не научил меня этому."
                say(go_say)
        elif 'погод' in message_user and ('какая' in message_user or "что по" in message_user):
            message_candy = 'Вы можете подойти к окну и посмотреть.'
            say(message_candy)
        elif "врем" in message_user:
            now = datetime.datetime.now()
            message_candy = "Сейчас " + str(now.hour) + " часов " + str(now.minute) + " минут. "
            say(message_candy)
        elif "кого ты слушаешь" in message_user or "твой любымый исполнитель" in message_user:
            message_candy = choice(
                ['ДЭМ', 'FACE', 'MORGENSHTERN', 'Gone.Fludd', 'Big Babe Tape', 'YukiHaze',
                 'Молодой Шерра', 'Iroh', '2Pac', 'Maryana Ro', 'Yanix', 'Lil Pump',
                 'Алёна Швец', 'Lizer', 'ЛСП', "Джарахов", "Oxxxymiron", "Монеточка",
                 "Imagine Dragons", "Johnyboy", 'Cakeboy', 'Flipper Floyd', 'Markul'])
            say(message_candy)
        elif "анекд" in message_user or "шутк" in message_user or "шуток" in message_user or "шутеек" in message_user:
            message_candy = "На экзамене:   \n – Профессор, не подскажете, который час? \n – Учить надо было!  \n Ха-Ха-Ха"
            if int(level) >= 6:
                message_candy = choice([
                    'На экзамене:   \n – Профессор, не подскажете, который час? \n – Учить надо было!  \n Ха-Ха-Ха',
                    'Если вы в лесу встретили медведя, клещей уже не стоит бояться. \n Ха-Ха',
                    'В Ялте очень мало тротуаров, потому что их нельзя сдавать отдыхающим. \n Ха-Ха-Ха',
                    'Сейчас не хочется, может лучше поиграем?',
                    'Ничто так не украшает квартиру, как ребенок с фломастером! \n Ха-Ха-Ха-Ха'])
            say(message_candy)
        elif "спой" in message_user or "спеть" in message_user:
            message_candy = "Как сердце бьется он её заметит \n И похрюкивали чтобы ненасытные утробы \n Сниму очки: мне солнце светит. \n Бабочка хотела на вершину небоскрёба."
            if int(level) >= 7:
                message_candy = choice([
                    'Как сердце бьется он её заметит \n И похрюкивали чтобы ненасытные утробы \n Сниму очки: мне солнце светит. \n Бабочка хотела на вершину небоскрёба.',
                    'С ошибками и без подсказок \n Что ждет нас на исходе \n Он-как герой из сказок, \n Там и при пасмурной погоде',
                    'Прошло безмятежное время \n Он тайны строки и аккорды \n Вот посмотри: в землю упало семя, \n Рапортовать про новые рекорды.'])
            say(message_candy)
        elif "откр" in message_user and (
                "candy" in message_user or "кэнди" in message_user or "кенди" in message_user) and (
                "проф" in message_user or 'prof' in message_user):
            message_candy = "Открываю"
            say(message_candy)
            self.CP = CandyProfile()
            self.CP.show()
        elif "откр" in message_user and ("ютуб" in message_user or "youtube" in message_user):
            message_candy = "Открываю."
            say(message_candy)
            url = "https://www.youtube.com/"
            webbrowser.open(url)
        elif "откр" in message_user and (
                "вк" in message_user or "vk" in message_user or "вконтакте" in message_user):
            message_candy = "Открываю."
            say(message_candy)
            url = "https://www.vk.com"
            webbrowser.open(url)
        elif "откр" in message_user and (
                "фейсбук" in message_user or "facebook" in message_user):
            message_candy = "Открываю."
            say(message_candy)
            url = "https://www.facebook.com/"
            webbrowser.open(url)
        elif "откр" in message_user and (
                "инстаграм" in message_user or "instagram" in message_user):
            message_candy = "Открываю."
            say(message_candy)
            url = "https://www.instagram.com/"
            webbrowser.open(url)
        elif "откр" in message_user and (
                "твиттер" in message_user or "twitter" in message_user):
            message_candy = "Открываю."
            say(message_candy)
            url = "https://twitter.com/"
            webbrowser.open(url)
        elif "откр" in message_user and ("твитч" in message_user or "twitch" in message_user):
            message_candy = "Открываю."
            say(message_candy)
            url = "https://www.twitch.tv/"
            webbrowser.open(url)
        elif "откр" in message_user and (
                "ок" in message_user or "одноклассники" in message_user):
            message_candy = "Открываю."
            say(message_candy)
            url = "https://www.ok.ru"
            webbrowser.open(url)
        elif "откр" in message_user and (
                "candycompany" in message_user or "candy company" in message_user or 'кенди company' in message_user or 'кэнди company' in message_user or 'candy компани' in message_user or 'кенди компани' in message_user or 'кэнди компани' in message_user):
            message_candy = "Открываю."
            say(message_candy)
            url = "http://candycompany.ru/"
            webbrowser.open(url)
        elif "откр" in message_user and (
                "я музыку" in message_user or "яндекс музыку" in message_user):
            message_candy = "Открываю."
            say(message_candy)
            url = "https://music.yandex.ru/"
            webbrowser.open(url)
        elif ("пак" in message_user and "ман" in message_user) or (
                "pac" in message_user and "man" in message_user) or (
                "пак" in message_user and "man" in message_user) or (
                "pac" in message_user and "ман" in message_user):
            self.close()
            open_game = Popen("pythonw files/Pac-man/main.pyw")
            open_game.wait()
            # os.system('pythonw files/Pac-man/main.pyw')
            global interface
            global candycash
            con = sqlite3.connect('CandyBase.db')
            cur = con.cursor()
            cur.execute('SELECT [CandyCash], [CandyLevel] FROM [resources] LIMIT 500')
            temp = cur.fetchall()
            con.close()
            for i in temp:
                candycash = int(i[0])
                level = int(i[1])
            if interface == 1:
                self.iFace = Interface1()
                self.iFace.show()
            elif interface == 2:
                self.iFace = Interface2()
                self.iFace.show()
        elif "перевод" in message_user:
            if translator == 2:
                self.translator = Translator()
                self.translator.show()
        elif "дата" in message_user or "сегодня день" in message_user or "сегодня число" in message_user:
            now = datetime.datetime.now()
            if now.month == 1:
                month = 'января'
            elif now.month == 2:
                month = 'февраля'
            elif now.month == 3:
                month = 'марта'
            elif now.month == 4:
                month = 'апреля'
            elif now.month == 5:
                month = 'мая'
            elif now.month == 6:
                month = 'июня'
            elif now.month == 7:
                month = 'июля'
            elif now.month == 8:
                month = 'августа'
            elif now.month == 9:
                month = 'сентября'
            elif now.month == 10:
                month = "октября"
            elif now.month == 11:
                month = 'ноября'
            elif now.month == 12:
                month = 'декабря'
            message_candy = "Сегодня " + str(now.day) + " " + str(month) + "."
            say(message_candy)
        elif 'меня зовут' in message_user or "моё имя" in message_user:
            message_candy = "Я - Candy. Очень приятно."
            say(message_candy)
        elif "расс" in message_user and "о себе" in message_user:
            message_candy = "Я - Candy. Голосовой ассистент живущий у вас на компьютере. Я готова помочь вам в ответах на ваши некоторые вопросы."
            say(message_candy)
        elif 'хорошо' == message_user:
            message_candy = 'И это хорошо'
            say(message_candy)
        elif 'плохо' == message_user:
            message_candy = 'Очень жаль.'
            say(message_candy)
        elif (
                'откр' in message_user and 'candy market' in message_user) or 'открыть candy market' in message_user or 'открыть кэнди market' in message_user or 'открыть кенди market' in message_user or 'открыть кэнди маркет' in message_user or 'открыть кенди маркет' in message_user or 'открой candy маркет' in message_user or 'открой candy market' in message_user or 'открой кэнди market' in message_user or 'открой кенди market' in message_user or 'открой кэнди маркет' in message_user or 'открой кенди маркет' in message_user or 'открой candy маркет' in message_user:
            message_candy = 'Уже открываю'
            say(message_candy)
            self.close()
            self.candymarket_win = CandyMarket()
            self.candymarket_win.show()
        elif 'код разработчика' in message_user or 'разработчика код' in message_user and 'ввести' in message_user:
            message_candy = 'Вводите:'
            say(message_candy)
        elif 'candycash' in message_user or 'кенди кэш' in message_user or 'кэнди кэш' in message_user or 'кенди кеш' in message_user \
                or 'кэнди кеш' in message_user:
            message_candy = str(candycash)
            say(message_candy)
        elif 'путеводит' in message_user and 'гусь' in message_user and 'хруст' in message_user:
            self.iFace = MainWindow()
            self.iFace.show()
        elif message_user == 'пока' or message_user == 'до встречи' or message_user == 'бай' or message_user == 'аривидерчи':
            message_candy = 'Пока'
            if int(level) >= 8:
                message_candy = choice(['Пока', 'До встречи', 'Бай', 'Аривидерчи'])
            say(message_candy)
            global sounds_and_voices
            con = sqlite3.connect('CandyBase.db')
            cur = con.cursor()
            sql = "DELETE FROM resources"
            cur.execute(sql)
            sql = "DELETE FROM settings"
            cur.execute(sql)
            sql = "DELETE FROM candymarket"
            cur.execute(sql)
            info_database = [str(candycash), str(level)]
            cur.execute('INSERT INTO resources VALUES(?, ?)', info_database)
            cur.execute('INSERT INTO candymarket VALUES(?, ?, ?)', (interface, sounds_and_voices, translator,))
            cur.execute('INSERT INTO settings VALUES(?, ?)', (name_user, icon_user,))
            con.commit()
            with zipfile.ZipFile('CandyBase.zip', 'w') as myzip:
                myzip.write('CandyBase.db')
            con.close()
            sys.exit()
        else:
            if message_user != "":
                message_candy = "Разработчик этого приложения не научил меня этому. Но вы можете сделать меня лучше и написать ему на почту (candy.company@yandex.ru)"
                say("Разработчик этого приложения не научил меня этому.")
        message_user_array.append(message_user)
        message_candy_array.append(message_candy)

    def commands_user(self):
        global message_user
        global message_candy, sounds_and_voices
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 1
                if sounds_and_voices == 1:
                    say('Я вас слушаю...')
                r.adjust_for_ambient_noise(source, duration=2)
                audio = r.listen(source)
            try:
                message_user = r.recognize_google(audio, language="ru-RU").lower()
            except sr.UnknownValueError:
                if sounds_and_voices == 1:
                    say("Я вас не поняла")
                    self.commands_user()
                elif sounds_and_voices == 2:
                    message_user = ""
                    self.load_mp3('Images/Sounds/error.mp3')
                    self.player.play()
                    for i in range(5):
                        say("")
        except OSError:
            say("Подключите микрофон, для корректной работы программы!")
            sys.exit()
        except sr.RequestError:
            say("Проверьте подключение к интернету")
            sys.exit()

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)


# Главное окно
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = None
        self.y = None
        self.btn_plus.clicked.connect(self.plus)
        self.btn_osz.clicked.connect(self.factory_osz)
        self.btn_sv.clicked.connect(self.factory_sv)
        self.btn_gusar.clicked.connect(self.factory_gusar)
        self.btn_hrust.clicked.connect(self.factory_khrust)
        self.btn_museum.clicked.connect(self.museum)
        self.btn_beach.clicked.connect(self.beach)
        self.btn_um.clicked.connect(self.um)
        self.btn_vodoley.clicked.connect(self.vodoley)
        self.btn_undina.clicked.connect(self.undina)
        self.btn_meschera.clicked.connect(self.meschera)
        self.btn_hospitalTown.clicked.connect(self.hospitalTown)
        self.btn_childHospital1.clicked.connect(self.childHospital)
        self.btn_childHospital.clicked.connect(self.childHospital_2)
        self.btn_FAQ.clicked.connect(self.faq)
        self.btn_centerHospital.clicked.connect(self.centerHospital)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 692)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -20, 781, 731))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/main_map.jpg"))
        self.label.setObjectName("label")
        self.btn_osz = QtWidgets.QPushButton(Form)
        self.btn_osz.setGeometry(QtCore.QRect(640, 140, 41, 41))
        self.btn_osz.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/factory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_osz.setIcon(icon)
        self.btn_osz.setIconSize(QtCore.QSize(25, 25))
        self.btn_osz.setObjectName("btn_osz")
        self.btn_sv = QtWidgets.QPushButton(Form)
        self.btn_sv.setGeometry(QtCore.QRect(50, 80, 41, 41))
        self.btn_sv.setText("")
        self.btn_sv.setIcon(icon)
        self.btn_sv.setIconSize(QtCore.QSize(25, 25))
        self.btn_sv.setObjectName("btn_sv")
        self.btn_gusar = QtWidgets.QPushButton(Form)
        self.btn_gusar.setGeometry(QtCore.QRect(140, 150, 41, 41))
        self.btn_gusar.setText("")
        self.btn_gusar.setIcon(icon)
        self.btn_gusar.setIconSize(QtCore.QSize(25, 25))
        self.btn_gusar.setObjectName("btn_gusar")
        self.btn_hrust = QtWidgets.QPushButton(Form)
        self.btn_hrust.setGeometry(QtCore.QRect(410, 350, 31, 31))
        self.btn_hrust.setText("")
        self.btn_hrust.setIcon(icon)
        self.btn_hrust.setIconSize(QtCore.QSize(25, 25))
        self.btn_hrust.setObjectName("btn_hrust")
        self.btn_museum = QtWidgets.QPushButton(Form)
        self.btn_museum.setGeometry(QtCore.QRect(390, 310, 31, 31))
        self.btn_museum.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/musem.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_museum.setIcon(icon1)
        self.btn_museum.setIconSize(QtCore.QSize(25, 25))
        self.btn_museum.setObjectName("museum")
        self.btn_beach = QtWidgets.QPushButton(Form)
        self.btn_beach.setGeometry(QtCore.QRect(440, 230, 31, 31))
        self.btn_beach.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/beach.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_beach.setIcon(icon2)
        self.btn_beach.setIconSize(QtCore.QSize(25, 25))
        self.btn_beach.setObjectName("beach")
        self.btn_um = QtWidgets.QPushButton(Form)
        self.btn_um.setGeometry(QtCore.QRect(560, 130, 41, 41))
        self.btn_um.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/hotel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_um.setIcon(icon3)
        self.btn_um.setIconSize(QtCore.QSize(25, 25))
        self.btn_um.setObjectName("btn_um")
        self.btn_meschera = QtWidgets.QPushButton(Form)
        self.btn_meschera.setGeometry(QtCore.QRect(490, 340, 31, 31))
        self.btn_meschera.setText("")
        self.btn_meschera.setIcon(icon3)
        self.btn_meschera.setIconSize(QtCore.QSize(25, 25))
        self.btn_meschera.setObjectName("btn_meschera")
        self.btn_undina = QtWidgets.QPushButton(Form)
        self.btn_undina.setGeometry(QtCore.QRect(290, 190, 31, 31))
        self.btn_undina.setText("")
        self.btn_undina.setIcon(icon3)
        self.btn_undina.setIconSize(QtCore.QSize(25, 25))
        self.btn_undina.setObjectName("btn_undina")
        self.btn_vodoley = QtWidgets.QPushButton(Form)
        self.btn_vodoley.setGeometry(QtCore.QRect(170, 90, 31, 31))
        self.btn_vodoley.setText("")
        self.btn_vodoley.setIcon(icon3)
        self.btn_vodoley.setIconSize(QtCore.QSize(25, 25))
        self.btn_vodoley.setObjectName("btn_vodoley")
        self.btn_centerHospital = QtWidgets.QPushButton(Form)
        self.btn_centerHospital.setGeometry(QtCore.QRect(550, 390, 41, 41))
        self.btn_centerHospital.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_centerHospital.setIcon(icon4)
        self.btn_centerHospital.setIconSize(QtCore.QSize(25, 25))
        self.btn_centerHospital.setObjectName("btn_centerHospital")
        self.btn_childHospital = QtWidgets.QPushButton(Form)
        self.btn_childHospital.setGeometry(QtCore.QRect(250, 390, 41, 41))
        self.btn_childHospital.setText("")
        self.btn_childHospital.setIcon(icon4)
        self.btn_childHospital.setIconSize(QtCore.QSize(25, 25))
        self.btn_childHospital.setObjectName("btn_childHospital")
        self.btn_childHospital1 = QtWidgets.QPushButton(Form)
        self.btn_childHospital1.setGeometry(QtCore.QRect(450, 390, 41, 41))
        self.btn_childHospital1.setText("")
        self.btn_childHospital1.setIcon(icon4)
        self.btn_childHospital1.setIconSize(QtCore.QSize(25, 25))
        self.btn_childHospital1.setObjectName("btn_childHospital1")
        self.btn_hospitalTown = QtWidgets.QPushButton(Form)
        self.btn_hospitalTown.setGeometry(QtCore.QRect(520, 330, 31, 31))
        self.btn_hospitalTown.setText("")
        self.btn_hospitalTown.setIcon(icon4)
        self.btn_hospitalTown.setIconSize(QtCore.QSize(25, 25))
        self.btn_hospitalTown.setObjectName("btn_hospitalTown")
        self.btn_plus = QtWidgets.QPushButton(Form)
        self.btn_plus.setGeometry(QtCore.QRect(730, 610, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_plus.setFont(font)
        self.btn_plus.setIconSize(QtCore.QSize(25, 25))
        self.btn_plus.setObjectName("btn_plus")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 670, 531, 21))
        self.label_2.setObjectName("label_2")
        self.btn_FAQ = QtWidgets.QPushButton(Form)
        self.btn_FAQ.setGeometry(QtCore.QRect(20, 630, 41, 41))
        self.btn_FAQ.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/FAQ.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_FAQ.setIcon(icon5)
        self.btn_FAQ.setIconSize(QtCore.QSize(30, 30))
        self.btn_FAQ.setObjectName("btn_FAQ")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному"))
        self.btn_plus.setText(_translate("Form", "+"))
        self.label_2.setText(_translate("Form", "*Что бы приблизить карту кликните на ту часть"
                                                " которую нужно приблизить и после на кнопку +"))

    def factory_osz(self):  # Открытие окна с информацией об ОСЗ
        self.openInterface = FactoryOSZ()
        self.openInterface.show()

    def factory_sv(self):  # Открытие окна с информацией о заводе стекловолкно
        self.openInterface = FactorySV()
        self.openInterface.show()

    def factory_gusar(self):  # Открытие окна с информацией о заводе гусар
        self.openInterface = FactoryGusar()
        self.openInterface.show()

    def factory_khrust(self):  # Открытие окна с информацией о хрустальном заводе
        self.openInterface = FactoryKhrust()
        self.openInterface.show()

    def museum(self):  # Открытие окна с информацией о музее хрусталя
        self.openInterface = Museum()
        self.openInterface.show()

    def beach(self):  # Открытие окна с информацией о пляже
        self.openInterface = Beach()
        self.openInterface.show()

    def um(self):  # Открытие окна с информацией об отеле усадьба мещёрская
        self.openInterface = UM()
        self.openInterface.show()

    def vodoley(self):  # Открытие окна с информацией об отеле водолей
        self.openInterface = Vodoley()
        self.openInterface.show()

    def undina(self):  # Открытие окна с информацией об отеле ундина
        self.openInterface = Undina()
        self.openInterface.show()

    def meschera(self):  # Открытие окна с информацией об отеле мещёра
        self.openInterface = Meschera()
        self.openInterface.show()

    def hospitalTown(self):  # Открытие окна с информацией о больничном городке
        self.openInterface = HospitalTown()
        self.openInterface.show()

    def childHospital(self):  # Открытие окна с информацией о детской больнице №1
        self.openInterface = ChildHospital()
        self.openInterface.show()

    def childHospital_2(self):  # Открытие окна с информацией о детской больнице
        self.openInterface = ChildHospital_2()
        self.openInterface.show()

    def centerHospital(self):  # Открытие окна с информацией о центральной больнице
        self.openInterface = CenterHospital()
        self.openInterface.show()

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.x, self.y = event.x(), event.y()

    def plus(self):  # Метод открывающий приближённую часть карты
        if self.x is None and self.y is None:
            pass
        elif (0 <= self.x <= 436) and (0 <= self.y <= 392):
            self.close()
            self.openInterface = MapUpLeft()
            self.openInterface.show()
        elif (0 <= self.x <= 390) and (390 <= self.y <= 691):
            self.close()
            self.openInterface = MapDownLeft()
            self.openInterface.show()
        elif (390 <= self.x <= 779) and (390 <= self.y <= 779):
            self.close()
            self.openInterface = MapDownRight()
            self.openInterface.show()
        elif (0 <= self.x <= 779) and (2 <= self.y <= 390):
            self.close()
            self.openInterface = MapUpRight()
            self.openInterface.show()

    def faq(self):
        self.openInterface = FAQ()
        self.openInterface.show()


class FAQ(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(421, 254)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 40, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 311, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному"))
        self.label.setText('Автор: CandyCreator')
        self.label_2.setText('Приложение "CandyAssistant"\nзащищено авторским правом')


class MapUpLeft(QWidget):  # Верхняя левая часть карты
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_mines.clicked.connect(self.mines)
        self.btn_sv.clicked.connect(self.factory_sv)
        self.btn_gusar.clicked.connect(self.factory_gusar)
        self.btn_hrust.clicked.connect(self.factory_khrust)
        self.btn_museum.clicked.connect(self.museum)
        self.btn_vodoley.clicked.connect(self.vodoley)
        self.btn_undina.clicked.connect(self.undina)
        self.btn_church.clicked.connect(self.church)
        self.btn_school4.clicked.connect(self.school4)
        self.btn_azs.clicked.connect(self.azs)
        self.btn_school5.clicked.connect(self.school5)
        self.btn_school15.clicked.connect(self.school15)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(839, 697)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -20, 861, 731))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/map_up_left.jpg"))
        self.label.setObjectName("label")
        self.btn_sv = QtWidgets.QPushButton(Form)
        self.btn_sv.setGeometry(QtCore.QRect(60, 60, 61, 61))
        self.btn_sv.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/factory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_sv.setIcon(icon)
        self.btn_sv.setIconSize(QtCore.QSize(50, 50))
        self.btn_sv.setObjectName("btn_sv")
        self.btn_gusar = QtWidgets.QPushButton(Form)
        self.btn_gusar.setGeometry(QtCore.QRect(270, 180, 61, 61))
        self.btn_gusar.setText("")
        self.btn_gusar.setIcon(icon)
        self.btn_gusar.setIconSize(QtCore.QSize(50, 50))
        self.btn_gusar.setObjectName("btn_gusar")
        self.btn_vodoley = QtWidgets.QPushButton(Form)
        self.btn_vodoley.setGeometry(QtCore.QRect(270, 50, 61, 61))
        self.btn_vodoley.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/hotel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_vodoley.setIcon(icon1)
        self.btn_vodoley.setIconSize(QtCore.QSize(50, 50))
        self.btn_vodoley.setObjectName("btn_vodoley")
        self.btn_undina = QtWidgets.QPushButton(Form)
        self.btn_undina.setGeometry(QtCore.QRect(530, 270, 41, 31))
        self.btn_undina.setText("")
        self.btn_undina.setIcon(icon1)
        self.btn_undina.setIconSize(QtCore.QSize(30, 30))
        self.btn_undina.setObjectName("btn_undina")
        self.btn_church = QtWidgets.QPushButton(Form)
        self.btn_church.setGeometry(QtCore.QRect(330, 110, 41, 51))
        self.btn_church.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/church.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_church.setIcon(icon2)
        self.btn_church.setIconSize(QtCore.QSize(50, 50))
        self.btn_church.setObjectName("btn_church")
        self.btn_school5 = QtWidgets.QPushButton(Form)
        self.btn_school5.setGeometry(QtCore.QRect(540, 300, 41, 31))
        self.btn_school5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/school.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_school5.setIcon(icon3)
        self.btn_school5.setIconSize(QtCore.QSize(30, 30))
        self.btn_school5.setObjectName("btn_school5")
        self.btn_azs = QtWidgets.QPushButton(Form)
        self.btn_azs.setGeometry(QtCore.QRect(390, 250, 31, 41))
        self.btn_azs.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/gas station.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btn_azs.setIcon(icon4)
        self.btn_azs.setIconSize(QtCore.QSize(20, 20))
        self.btn_azs.setObjectName("btn_azs")
        self.btn_school4 = QtWidgets.QPushButton(Form)
        self.btn_school4.setGeometry(QtCore.QRect(450, 170, 41, 31))
        self.btn_school4.setText("")
        self.btn_school4.setIcon(icon3)
        self.btn_school4.setIconSize(QtCore.QSize(30, 30))
        self.btn_school4.setObjectName("btn_school4")
        self.btn_school15 = QtWidgets.QPushButton(Form)
        self.btn_school15.setGeometry(QtCore.QRect(680, 460, 31, 31))
        self.btn_school15.setText("")
        self.btn_school15.setIcon(icon3)
        self.btn_school15.setIconSize(QtCore.QSize(30, 30))
        self.btn_school15.setObjectName("btn_school15")
        self.btn_mines = QtWidgets.QPushButton(Form)
        self.btn_mines.setGeometry(QtCore.QRect(740, 630, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_mines.setFont(font)
        self.btn_mines.setIconSize(QtCore.QSize(25, 25))
        self.btn_mines.setObjectName("btn_mines")
        self.btn_museum = QtWidgets.QPushButton(Form)
        self.btn_museum.setGeometry(QtCore.QRect(730, 500, 31, 31))
        self.btn_museum.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Images/musem.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_museum.setIcon(icon7)
        self.btn_museum.setIconSize(QtCore.QSize(25, 25))
        self.btn_museum.setObjectName("btn_musem")
        self.btn_hrust = QtWidgets.QPushButton(Form)
        self.btn_hrust.setGeometry(QtCore.QRect(790, 570, 31, 31))
        self.btn_hrust.setText("")
        self.btn_hrust.setIcon(icon)
        self.btn_hrust.setIconSize(QtCore.QSize(25, 25))
        self.btn_hrust.setObjectName("btn_hrust")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному"))
        self.btn_mines.setText(_translate("Form", "-"))

    def mines(self):  # Метод который открывает главную карту
        self.close()
        self.openInterface = MainWindow()
        self.openInterface.show()

    def factory_sv(self):  # Открытие окна с информацией о заводе стекловолкно
        self.openInterface = FactorySV()
        self.openInterface.show()

    def factory_gusar(self):  # Открытие окна с информацией о заводе гусар
        self.openInterface = FactoryGusar()
        self.openInterface.show()

    def factory_khrust(self):  # Открытие окна с информацией о хрустальном заводе
        self.openInterface = FactoryKhrust()
        self.openInterface.show()

    def museum(self):  # Открытие окна с информацией о музее хрусталя
        self.openInterface = Museum()
        self.openInterface.show()

    def vodoley(self):  # Открытие окна с информацией об отеле водолей
        self.openInterface = Vodoley()
        self.openInterface.show()

    def undina(self):  # Открытие окна с информацией об отеле ундина
        self.openInterface = Undina()
        self.openInterface.show()

    def church(self):  # Открытие окна с информацией о храме
        self.openInterface = Church()
        self.openInterface.show()

    def school4(self):  # Открытие окна с информацией о школе №4
        self.openInterface = School4()
        self.openInterface.show()

    def azs(self):  # Открытие окна с информацией о АЗС
        self.openInterface = AZS_LionOil()
        self.openInterface.show()

    def school5(self):  # Открытие окна с информацией о школе №5
        self.openInterface = School5()
        self.openInterface.show()

    def school15(self):  # Открытие окна с информацией о школе №15
        self.openInterface = School15()
        self.openInterface.show()


class MapDownLeft(QWidget):  # Нижняя левая часть карты
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_mines.clicked.connect(self.mines)
        self.btn_childHospital.clicked.connect(self.childHospital)
        self.btn_cinema.clicked.connect(self.cinema)
        self.btn_school10.clicked.connect(self.school10)
        self.btn_school13.clicked.connect(self.school13)
        self.btn_five_2.clicked.connect(self.five)
        self.btn_five.clicked.connect(self.five_2)
        self.btn_azs.clicked.connect(self.azs)
        self.btn_childHospital1.clicked.connect(self.childHospital1)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(636, 708)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -20, 651, 741))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/map_down_left.jpg"))
        self.label.setObjectName("label")
        self.btn_childHospital = QtWidgets.QPushButton(Form)
        self.btn_childHospital.setGeometry(QtCore.QRect(240, 140, 31, 31))
        self.btn_childHospital.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_childHospital.setIcon(icon)
        self.btn_childHospital.setIconSize(QtCore.QSize(20, 20))
        self.btn_childHospital.setObjectName("btn_childHospital")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/gas station.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/shop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.btn_five = QtWidgets.QPushButton(Form)
        self.btn_five.setGeometry(QtCore.QRect(350, 80, 31, 31))
        self.btn_five.setText("")
        self.btn_five.setIcon(icon2)
        self.btn_five.setIconSize(QtCore.QSize(20, 20))
        self.btn_five.setObjectName("btn_five")
        self.btn_mines = QtWidgets.QPushButton(Form)
        self.btn_mines.setGeometry(QtCore.QRect(590, 660, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_mines.setFont(font)
        self.btn_mines.setIconSize(QtCore.QSize(25, 25))
        self.btn_mines.setObjectName("btn_mines")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/eat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cinema = QtWidgets.QPushButton(Form)
        self.btn_cinema.setGeometry(QtCore.QRect(550, 40, 51, 51))
        self.btn_cinema.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/cinema.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cinema.setIcon(icon4)
        self.btn_cinema.setIconSize(QtCore.QSize(30, 30))
        self.btn_cinema.setObjectName("btn_cinema")
        self.btn_five_2 = QtWidgets.QPushButton(Form)
        self.btn_five_2.setGeometry(QtCore.QRect(280, 360, 31, 31))
        self.btn_five_2.setText("")
        self.btn_five_2.setIcon(icon2)
        self.btn_five_2.setIconSize(QtCore.QSize(20, 20))
        self.btn_five_2.setObjectName("btn_five_2")
        self.btn_azs = QtWidgets.QPushButton(Form)
        self.btn_azs.setGeometry(QtCore.QRect(300, 560, 31, 41))
        self.btn_azs.setText("")
        self.btn_azs.setIcon(icon1)
        self.btn_azs.setIconSize(QtCore.QSize(20, 20))
        self.btn_azs.setObjectName("btn_azs_2")
        self.btn_school10 = QtWidgets.QPushButton(Form)
        self.btn_school10.setGeometry(QtCore.QRect(310, 110, 31, 31))
        self.btn_school10.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images/school.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_school10.setIcon(icon6)
        self.btn_school10.setIconSize(QtCore.QSize(30, 30))
        self.btn_school10.setObjectName("btn_school10")
        self.btn_school13 = QtWidgets.QPushButton(Form)
        self.btn_school13.setGeometry(QtCore.QRect(500, 190, 31, 31))
        self.btn_school13.setText("")
        self.btn_school13.setIcon(icon6)
        self.btn_school13.setIconSize(QtCore.QSize(30, 30))
        self.btn_school13.setObjectName("btn_school13")
        self.btn_childHospital1 = QtWidgets.QPushButton(Form)
        self.btn_childHospital1.setGeometry(QtCore.QRect(590, 150, 41, 41))
        self.btn_childHospital1.setText("")
        self.btn_childHospital1.setIcon(icon)
        self.btn_childHospital1.setIconSize(QtCore.QSize(25, 25))
        self.btn_childHospital1.setObjectName("btn_childHospital1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному"))
        self.btn_mines.setText(_translate("Form", "-"))

    def mines(self):  # Метод который открывает главную карту
        self.close()
        self.openInterface = MainWindow()
        self.openInterface.show()

    def childHospital(self):  # Открытие окна с информацией о детской больнице №1
        self.openInterface = ChildHospital_2()
        self.openInterface.show()

    def cinema(self):  # Открытие окна с информацией о кинотеатре
        self.openInterface = Cinema()
        self.openInterface.show()

    def school10(self):  # Открытие окна с информацией о школе №15
        self.openInterface = School10()
        self.openInterface.show()

    def school13(self):  # Открытие окна с информацией о школе №13
        self.openInterface = School13()
        self.openInterface.show()

    def five(self):  # Открытие окна с информацией о пятёрочке
        self.openInterface = Five2()
        self.openInterface.show()

    def five_2(self):  # Открытие окна с информацией о пятёрочке
        self.openInterface = Five3()
        self.openInterface.show()

    def azs(self):  # Открытие окна с информацией о лукоиле
        self.openInterface = AZS_lukoil()
        self.openInterface.show()

    def childHospital1(self):  # Открытие окна с информацией о больнице
        self.openInterface = ChildHospital()
        self.openInterface.show()


class MapDownRight(QWidget):  # Нижняя правая часть карты
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_mines.clicked.connect(self.mines)
        self.btn_childHospital1.clicked.connect(self.childHospital)
        self.btn_centerHospital.clicked.connect(self.centerHospital)
        self.btn_meschera.clicked.connect(self.meschera)
        self.btn_school2_1.clicked.connect(self.school2_1)
        self.btn_school2_2.clicked.connect(self.school2_2)
        self.btn_school7.clicked.connect(self.school7)
        self.btn_five.clicked.connect(self.five)
        self.btn_diksi.clicked.connect(self.diksi)
        self.btn_lider.clicked.connect(self.lider)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(549, 731)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -30, 621, 771))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/map_down_right.jpg"))
        self.label.setObjectName("label")
        self.btn_centerHospital = QtWidgets.QPushButton(Form)
        self.btn_centerHospital.setGeometry(QtCore.QRect(270, 200, 61, 51))
        self.btn_centerHospital.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_centerHospital.setIcon(icon)
        self.btn_centerHospital.setIconSize(QtCore.QSize(40, 40))
        self.btn_centerHospital.setObjectName("btn_centerHospital")
        self.btn_childHospital1 = QtWidgets.QPushButton(Form)
        self.btn_childHospital1.setGeometry(QtCore.QRect(60, 130, 61, 51))
        self.btn_childHospital1.setText("")
        self.btn_childHospital1.setIcon(icon)
        self.btn_childHospital1.setIconSize(QtCore.QSize(40, 40))
        self.btn_childHospital1.setObjectName("btn_childHospital1")
        self.btn_meschera = QtWidgets.QPushButton(Form)
        self.btn_meschera.setGeometry(QtCore.QRect(110, 40, 41, 41))
        self.btn_meschera.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/hotel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_meschera.setIcon(icon1)
        self.btn_meschera.setIconSize(QtCore.QSize(30, 30))
        self.btn_meschera.setObjectName("btn_meshera")
        self.btn_school2_2 = QtWidgets.QPushButton(Form)
        self.btn_school2_2.setGeometry(QtCore.QRect(220, 40, 31, 31))
        self.btn_school2_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/school.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_school2_2.setIcon(icon2)
        self.btn_school2_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_school2_2.setObjectName("btn_school2_2")
        self.btn_school7 = QtWidgets.QPushButton(Form)
        self.btn_school7.setGeometry(QtCore.QRect(160, 210, 31, 31))
        self.btn_school7.setText("")
        self.btn_school7.setIcon(icon2)
        self.btn_school7.setIconSize(QtCore.QSize(30, 30))
        self.btn_school7.setObjectName("btn_school7")
        self.btn_school2_1 = QtWidgets.QPushButton(Form)
        self.btn_school2_1.setGeometry(QtCore.QRect(400, 30, 31, 31))
        self.btn_school2_1.setText("")
        self.btn_school2_1.setIcon(icon2)
        self.btn_school2_1.setIconSize(QtCore.QSize(30, 30))
        self.btn_school2_1.setObjectName("btn_school2_1")
        self.btn_five = QtWidgets.QPushButton(Form)
        self.btn_five.setGeometry(QtCore.QRect(10, 50, 31, 31))
        self.btn_five.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/shop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_five.setIcon(icon3)
        self.btn_five.setIconSize(QtCore.QSize(20, 20))
        self.btn_five.setObjectName("btn_five")
        self.btn_lider = QtWidgets.QPushButton(Form)
        self.btn_lider.setGeometry(QtCore.QRect(180, 260, 31, 31))
        self.btn_lider.setText("")
        self.btn_lider.setIcon(icon3)
        self.btn_lider.setIconSize(QtCore.QSize(20, 20))
        self.btn_lider.setObjectName("btn_lider")
        self.btn_diksi = QtWidgets.QPushButton(Form)
        self.btn_diksi.setGeometry(QtCore.QRect(170, 160, 31, 31))
        self.btn_diksi.setText("")
        self.btn_diksi.setIcon(icon3)
        self.btn_diksi.setIconSize(QtCore.QSize(20, 20))
        self.btn_diksi.setObjectName("btn_diksi")
        self.btn_mines = QtWidgets.QPushButton(Form)
        self.btn_mines.setGeometry(QtCore.QRect(500, 680, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_mines.setFont(font)
        self.btn_mines.setIconSize(QtCore.QSize(25, 25))
        self.btn_mines.setObjectName("btn_mines")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному"))
        self.btn_mines.setText(_translate("Form", "-"))

    def mines(self):  # Метод который открывает главную карту
        self.close()
        self.openInterface = MainWindow()
        self.openInterface.show()

    def childHospital(self):  # Открытие окна с информацией о детской больнице №1
        self.openInterface = ChildHospital()
        self.openInterface.show()

    def centerHospital(self):  # Открытие окна с информацией о центральной больнице
        self.openInterface = CenterHospital()
        self.openInterface.show()

    def meschera(self):  # Открытие окна с информацией об отеле мещёра
        self.openInterface = Meschera()
        self.openInterface.show()

    def school2_1(self):  # Открытие окна с информацией о школе №2, корпус 1
        self.openInterface = School2_1()
        self.openInterface.show()

    def school2_2(self):  # Открытие окна с информацией о школе №2, корпус 2
        self.openInterface = School2_2()
        self.openInterface.show()

    def school7(self):  # Открытие окна с информацией о школе №7
        self.openInterface = School7()
        self.openInterface.show()

    def five(self):  # Открытие окна с информацией о пятёрочке
        self.openInterface = Five()
        self.openInterface.show()

    def diksi(self):  # Открытие окна с информацией о дикси
        self.openInterface = Diksi()
        self.openInterface.show()

    def lider(self):  # Открытие окна с информацией о лидере
        self.openInterface = Lider()
        self.openInterface.show()


class MapUpRight(QWidget):  # Верхняя правая часть карты
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_mines.clicked.connect(self.mines)
        self.btn_osz.clicked.connect(self.factory_osz)
        self.btn_um.clicked.connect(self.um)
        self.btn_beach.clicked.connect(self.beach)
        self.btn_hrust.clicked.connect(self.factory_khrust)
        self.btn_meschera.clicked.connect(self.meschera)
        self.btn_azs.clicked.connect(self.azs)
        self.btn_park.clicked.connect(self.park)
        self.btn_hospitalTown.clicked.connect(self.hospitalTown)
        self.btn_school3.clicked.connect(self.school3)
        self.btn_school1.clicked.connect(self.school1)
        self.btn_school2_1.clicked.connect(self.school2_1)
        self.btn_school2_2.clicked.connect(self.school2_2)
        self.btn_gimnazia.clicked.connect(self.gimnazia)
        self.btn_mendeleevsky.clicked.connect(self.mendeleevsky)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(776, 699)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, -10, 801, 721))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Images/map_up_right.jpg"))
        self.label.setObjectName("label")
        self.btn_gimnazia = QtWidgets.QPushButton(Form)
        self.btn_gimnazia.setGeometry(QtCore.QRect(150, 500, 41, 31))
        self.btn_gimnazia.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/school.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_gimnazia.setIcon(icon)
        self.btn_gimnazia.setIconSize(QtCore.QSize(30, 30))
        self.btn_gimnazia.setObjectName("btn_gimnazia")
        self.btn_school3 = QtWidgets.QPushButton(Form)
        self.btn_school3.setGeometry(QtCore.QRect(230, 420, 41, 31))
        self.btn_school3.setText("")
        self.btn_school3.setIcon(icon)
        self.btn_school3.setIconSize(QtCore.QSize(30, 30))
        self.btn_school3.setObjectName("btn_school13")
        self.btn_school2_2 = QtWidgets.QPushButton(Form)
        self.btn_school2_2.setGeometry(QtCore.QRect(200, 580, 31, 31))
        self.btn_school2_2.setText("")
        self.btn_school2_2.setIcon(icon)
        self.btn_school2_2.setIconSize(QtCore.QSize(30, 30))
        self.btn_school2_2.setObjectName("btn_school2_2")
        self.btn_school2_1 = QtWidgets.QPushButton(Form)
        self.btn_school2_1.setGeometry(QtCore.QRect(320, 590, 31, 31))
        self.btn_school2_1.setText("")
        self.btn_school2_1.setIcon(icon)
        self.btn_school2_1.setIconSize(QtCore.QSize(30, 30))
        self.btn_school2_1.setObjectName("btn_school2_1")
        self.btn_school1 = QtWidgets.QPushButton(Form)
        self.btn_school1.setGeometry(QtCore.QRect(380, 480, 31, 31))
        self.btn_school1.setText("")
        self.btn_school1.setIcon(icon)
        self.btn_school1.setIconSize(QtCore.QSize(30, 30))
        self.btn_school1.setObjectName("btn_school1BTN")
        self.btn_beach = QtWidgets.QPushButton(Form)
        self.btn_beach.setGeometry(QtCore.QRect(20, 360, 31, 31))
        self.btn_beach.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/beach.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_beach.setIcon(icon1)
        self.btn_beach.setIconSize(QtCore.QSize(25, 25))
        self.btn_beach.setObjectName("btn_beach")
        self.btn_hospitalTown = QtWidgets.QPushButton(Form)
        self.btn_hospitalTown.setGeometry(QtCore.QRect(120, 540, 41, 41))
        self.btn_hospitalTown.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_hospitalTown.setIcon(icon2)
        self.btn_hospitalTown.setIconSize(QtCore.QSize(25, 25))
        self.btn_hospitalTown.setObjectName("btn_childHospita1")
        self.btn_park = QtWidgets.QPushButton(Form)
        self.btn_park.setGeometry(QtCore.QRect(420, 370, 61, 61))
        self.btn_park.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/park.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_park.setIcon(icon3)
        self.btn_park.setIconSize(QtCore.QSize(40, 40))
        self.btn_park.setObjectName("btn_park")
        self.btn_azs = QtWidgets.QPushButton(Form)
        self.btn_azs.setGeometry(QtCore.QRect(580, 130, 31, 31))
        self.btn_azs.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Images/gas station.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btn_azs.setIcon(icon4)
        self.btn_azs.setIconSize(QtCore.QSize(20, 20))
        self.btn_azs.setObjectName("btn_azs")
        self.btn_um = QtWidgets.QPushButton(Form)
        self.btn_um.setGeometry(QtCore.QRect(320, 170, 41, 41))
        self.btn_um.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Images/hotel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_um.setIcon(icon5)
        self.btn_um.setIconSize(QtCore.QSize(25, 25))
        self.btn_um.setObjectName("btn_um")
        self.btn_mines = QtWidgets.QPushButton(Form)
        self.btn_mines.setGeometry(QtCore.QRect(720, 650, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_mines.setFont(font)
        self.btn_mines.setIconSize(QtCore.QSize(25, 25))
        self.btn_mines.setObjectName("btn_mines")
        self.btn_osz = QtWidgets.QPushButton(Form)
        self.btn_osz.setGeometry(QtCore.QRect(450, 170, 61, 61))
        self.btn_osz.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Images/factory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_osz.setIcon(icon6)
        self.btn_osz.setIconSize(QtCore.QSize(40, 40))
        self.btn_osz.setObjectName("btn_osz")
        self.btn_mendeleevsky = QtWidgets.QPushButton(Form)
        self.btn_mendeleevsky.setGeometry(QtCore.QRect(340, 460, 31, 31))
        self.btn_mendeleevsky.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Images/shop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_mendeleevsky.setIcon(icon7)
        self.btn_mendeleevsky.setIconSize(QtCore.QSize(20, 20))
        self.btn_mendeleevsky.setObjectName("btn_mendeleevsky")
        self.btn_meschera = QtWidgets.QPushButton(Form)
        self.btn_meschera.setGeometry(QtCore.QRect(170, 540, 31, 31))
        self.btn_meschera.setText("")
        self.btn_meschera.setIcon(icon5)
        self.btn_meschera.setIconSize(QtCore.QSize(25, 25))
        self.btn_meschera.setObjectName("btn_meschera")
        self.btn_hrust = QtWidgets.QPushButton(Form)
        self.btn_hrust.setGeometry(QtCore.QRect(10, 610, 31, 31))
        self.btn_hrust.setText("")
        self.btn_hrust.setIcon(icon6)
        self.btn_hrust.setIconSize(QtCore.QSize(25, 25))
        self.btn_hrust.setObjectName("btn_hrust")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному"))
        self.btn_mines.setText(_translate("Form", "-"))

    def meschera(self):  # Открытие окна с информацией об отеле мещёра
        self.openInterface = Meschera()
        self.openInterface.show()

    def mines(self):  # Метод который открывает главную карту
        self.close()
        self.openInterface = MainWindow()
        self.openInterface.show()

    def factory_osz(self):  # Открытие окна с информацией об ОСЗ
        self.openInterface = FactoryOSZ()
        self.openInterface.show()

    def um(self):  # Открытие окна с информацией об отеле усадьба мещёрская
        self.openInterface = UM()
        self.openInterface.show()

    def beach(self):  # Открытие окна с информацией о пляже
        self.openInterface = Beach()
        self.openInterface.show()

    def factory_khrust(self):  # Открытие окна с информацией о хрустальном заводе
        self.openInterface = FactoryKhrust()
        self.openInterface.show()

    def azs(self):  # Открытие окна с информацией о заправке
        self.openInterface = AZS()
        self.openInterface.show()

    def park(self):  # Открытие окна с информацией о парке
        self.openInterface = Park()
        self.openInterface.show()

    def hospitalTown(self):  # Открытие окна с информацией о больничном городке
        self.openInterface = HospitalTown()
        self.openInterface.show()

    def school3(self):  # Открытие окна с информацией о школе №3
        self.openInterface = School3()
        self.openInterface.show()

    def school1(self):  # Открытие окна с информацией о школе №1
        self.openInterface = School1()
        self.openInterface.show()

    def school2_1(self):  # Открытие окна с информацией о школе №2, корпус 1
        self.openInterface = School2_1()
        self.openInterface.show()

    def school2_2(self):  # Открытие окна с информацией о школе №2, корпус 2
        self.openInterface = School2_2()
        self.openInterface.show()

    def gimnazia(self):  # Открытие окна с информацией о гимназии
        self.openInterface = Gimnazia()
        self.openInterface.show()

    def mendeleevsky(self):  # Открытие окна с информацией о менделеевском
        self.openInterface = Mendeleevsky()
        self.openInterface.show()


class FactoryOSZ(QWidget):  # Окно с информацией об ОСЗ
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 692)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 30, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 291, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/osz/osz.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(320, 100, 211, 201))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/osz/osz_2.jpg"))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 610, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 490, 461, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 310, 461, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Опытный стекольный завод"))
        self.label.setText(_translate("Form", "Опытный стекольный завод"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_4.setText(_translate("Form", "АДРЕС\n"
                                                "г.Гусь-Хрустальный, ул. Интернациональная, д.114\n"
                                                "Тел.: (49241) 3-77-99, Факс: (49241) 2-53-04"))
        self.label_5.setText(_translate("Form", "Завод был построен в 1960 году.\n"
                                                "В 1997 году началось производство стаканов\n"
                                                "с утолщенным дном, в 2016 началось\n"
                                                "производство тарелок.\n"
                                                "Предприятие ООО «Опытный Стекольный Завод»\n"
                                                "является подразделением ARC, мирового\n"
                                                "лидера в производстве столовой посуды."))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://www.osz-glass.ru/"
        webbrowser.open(url)


class FactorySV(QWidget):  # Окно с информацией о заводе стекловолокно
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(608, 760)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 670, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(60, 330, 461, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 10, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(380, 60, 201, 261))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/Стекловолокно/img.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 291, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Стекловолокно/factory.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(
            _translate("Form", "Путеводитель по Гусь-Хрустальному | Завод стекловолокно"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_5.setText(_translate("Form", "ОАО \"Стекловолокно\" - крупнейшее\n"
                                                "российское предприятие по производству\n"
                                                "стекловолокна, лидер своей отрасли.\n"
                                                "Основанное в 1943 году,\n"
                                                " предприятие вот уже более полувека\n"
                                                "известно среди широкого круга\n"
                                                "потребителей в России\n"
                                                "и во многих странах мира\n"
                                                "с высоким качеством производимой\n"
                                                "продукции и постоянным\n"
                                                "стремлением к полному удовлетворению\n"
                                                "требований партнеров."))
        self.label.setText(_translate("Form", "Завод стекловолокно"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://www.steklovolokno.ru/"
        webbrowser.open(url)


class FactoryGusar(QWidget):  # Окно с информацией о заводе гусар
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(607, 701)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 311, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Гусар/fct.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(340, 70, 191, 271))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/Гусар/image.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 330, 461, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 10, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 610, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | Завод гусар"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label.setText('Завод Гусар')
        self.label_5.setText(
            'ООО «Гусевский арматурный завод «Гусар»\nоснован в 2002 году\nв городе Гусь-Хрустальный\nВладимирской области в создании\nкоторого приняли участие\nведущие специалисты предприятия\nс опытом работы в машиностроении\nболее десяти лет.')

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://gusarm.ru/"
        webbrowser.open(url)


class FactoryKhrust(QWidget):  # Окно с информацией о хрустальном заводе
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(603, 705)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 610, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(400, 120, 131, 161))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/Хрустальный завод/image.jpg"))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 310, 461, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 321, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Хрустальный завод/img.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Гусевской хрустальный завод имени Мальцова"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label.setText('Гусевской хрустальный завод имени Мальцова')
        self.label_5.setText(
            'Летом 1756 года орловский купец\nАким Мальцов основал во\n«Володимерском уезде» Московской\nгубернии при речке Гусь,\nв имении Никулино, в урочище Шиворово\nхрустальный завод.\nВ последние годы завод неоднократно\nстановился лауреатом международных\nи российских конкурсов, в том числе\n«100 лучших товаров России».')

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://ghz.ru/"
        webbrowser.open(url)


class Museum(QWidget):  # Окно с информацией о музее хрусталя
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(604, 704)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 130, 251, 191))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/Музей Хрусталя/img.jpg"))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 620, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 301, 221))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Музей Хрусталя/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 20, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(70, 510, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 370, 461, 121))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Музей Хрусталя им. Мальцовых"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label.setText('Музей Хрусталя им. Мальцовых')
        self.label_4.setText('Адрес:\nул. Калинина, 2А, Гусь-Хрустальный')
        self.label_5.setText(
            'Музей хрусталя располагается\nв здании Георгиевского собора с 1983 года.\nВ настоящее время экспозиция\nМузея Хрусталя состоит более,\nчем из 2 000 экспонатов.')

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://gus-hrustal.ru/"
        webbrowser.open(url)


class Beach(QWidget):  # Окно с информацией о городском пляже
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(597, 609)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 350, 461, 201))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 10, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 150, 191, 151))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/Пляж/img.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 301, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Пляж/image.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Городской пляж"))
        self.label.setText('Городской пляж')
        self.label_5.setText(
            'На пляже определена зона купания\nвзрослых и детей.\nПроведены специализированные работы\nпо обслуживанию дна.\nВ течение всего купального сезона \nбудет осуществляться отбор на исследования\nпроб воды из водоема.')


class UM(QWidget):  # Окно с информацией об отеле усадьба мещёрская
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(724, 731)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(350, 110, 351, 231))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/Усадьба мещёрская/hotel2.jpg"))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 620, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 40, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 301, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Усадьба мещёрская/hotel.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 310, 501, 201))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 500, 591, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Усадьба Мещёрская"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label.setText(_translate("Form", "Усадьба Мещерская"))
        self.label_4.setText(_translate("Form", "В окружении величественных сосен,\n"
                                                "в дали от шума и суеты есть место,\n"
                                                "дарящее Вам покой и отдых; место, где\n"
                                                "Вам всегда рады."))
        self.label_5.setText(_translate("Form", "Адрес\n"
                                                "Владимирская область, г. "
                                                "Гусь-Хрустальный, ул. Интернациональная, д. 105\n"
                                                "+7 (49241) 3-32-05"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://usadba-mescherskaya.ru/"
        webbrowser.open(url)


class Vodoley(QWidget):  # Окно с информацией об отеле водолей
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(722, 522)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, 10, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 301, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Водолей/hotel.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 350, 661, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(380, 100, 311, 211))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/Водолей/image.jpg"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Водолей"))
        self.label.setText(_translate("Form", "Водолей"))
        self.label_5.setText(_translate("Form", "Адрес\n"
                                                "601506, Гусь-Хрустальный район, г."
                                                " Гусь-Хрустальный, ул. Транспортная, д. 30\n"
                                                "Телефон:\n"
                                                "8 (49241) 3-54-17\n"
                                                "8 (920) 629-99-99\n"
                                                "8 (915) 794-39-00"))


class Undina(QWidget):  # Окно с информацией об отеле ундина
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(686, 698)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(340, 50, 321, 271))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/Ундина/hotel2.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 311, 141))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Ундина/hotel.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(310, 10, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 600, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 631, 201))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 500, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Ундина"))
        self.label.setText(_translate("Form", "Ундина"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_5.setText(_translate("Form", "Ундина - это настоящий банный комплекс\n"
                                                "с широким спектром услуг. В вашем распоряжении:\n"
                                                "баня с большой парной, хаммамом, купелью\n"
                                                "с проточной водой и уютными комнатами отдыха;\n"
                                                "сауна с  бассейном; vip сауна;\n"
                                                "гостевые номера и многое другое."))
        self.label_4.setText(_translate("Form", "Адрес: \n"
                                                "Владимирская область, г. Гусь-Хрустальный, ул. Транспортная, д. 2Б"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://www.undina33.ru/home"
        webbrowser.open(url)


class Meschera(QWidget):  # Окно с информацией об отеле мещёра
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 616)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(330, 10, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 510, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(410, 60, 301, 271))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Images/Мещёра/image.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 391, 211))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Мещёра/hotel.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 310, 631, 201))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Мещёра"))
        self.label.setText('Мещёра')
        self.label_4.setText('Адрес:\nГусь-Хрустальный, ул. Интернациональная, д. 22')
        self.label_5.setText(
            'К размещению гостей предоставляются комфортабельные\nномера различных категорий.\nКаждый отдыхающий найдет для себя\nнаиболее подходящий вариант.\nВ числе удобств - удобные спальные мечта,\nкачественная мебель, необходимая техника,\nа также собственная ванная комната.\nРеконструкция номерного фонда была произведена в 2008 году.')


class HospitalTown(QWidget):  # Окно с информацией о больничном городке
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(411, 545)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 321, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Больничный городок/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 20, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 320, 381, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 440, 331, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Больничный городок"))
        self.label.setText("Больничный городок")
        self.label_3.setText(
            'В больничном городке есть такие отделения как:\nХирургическое, Неврологическое, ГКБ,\nпсихиатрическое, офтальмологическое')
        self.label_4.setText('Адрес:\nУл. Октяборьская д. 39')


class ChildHospital(QWidget):  # Окно с информацией о детской больнице №1
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(744, 570)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 10, 511, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 450, 691, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 581, 401))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Детская городская больница_1/img.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Гусь-хрустальная детская городская больница № 1"))

        self.label.setText('Гусь-хрустальная детская городская больница № 1')
        self.label_5.setText(
            'Адрес\nРоссия, Владимирская область, Гусь-Хрустальный, Октябрьская ул., 3')


class ChildHospital_2(QWidget):  # Окно с информацией о детской больнице
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(733, 587)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 80, 491, 311))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Детская городская больница/img.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 20, 521, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 410, 651, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 520, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Детская Городская больница г. Гусь-Хрустальный"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_4.setText('Детская Городская больница г. Гусь-Хрустальный')
        self.label.setText('Адрес:\nул. Мира, 17')

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://gus-dgb.ru/"
        webbrowser.open(url)


class AZS(QWidget):  # Окно с информацией о заправке
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(505, 443)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 20, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 330, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 301, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/АЗС/line-oil_1.jpeg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Line-Oil"))
        self.label.setText(_translate("Form", "Line-Oil"))
        self.label_4.setText(_translate("Form", "Адрес: \n"
                                                "Россия, Владимирская область, Гусь-Хрустальный, 17Н-27"))


class Park(QWidget):  # Окно с информацией о парке
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(580, 668)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 380, 461, 281))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 60, 401, 331))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/парк Сказка/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 10, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Парк Сказка"))
        self.label_5.setText(_translate("Form", "Туда ходят все: от мала до велика,\n"
                                                "чтобы отдохнуть, подышать свежим воздухом,\n"
                                                "погулять и просто хорошо провести время.\n"
                                                "при заходе в сам парк начинает ощущаться\n"
                                                "сказочная атмосфера: практически на каждом углу\n"
                                                "находятся резные деревянные фигуры\n"
                                                "богатырей, щук, кощеев, сов и прочих\n"
                                                "существ из старославянских и древнерусских\n"
                                                "сказаний и мифов. "))
        self.label.setText(_translate("Form", "Парк Сказка"))


class School3(QWidget):  # Окно с информацией о школе №3
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(508, 597)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 331, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Школа №3/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 20, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 230, 461, 251))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 490, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Школа №3"))
        self.label.setText(_translate("Form", "Школа №3"))
        self.label_5.setText(_translate("Form", "Ранней весной 1990 года в Муромском переулке\n"
                                                "началось строительство школы, осуществляемое\n"
                                                "силами компании \"Стеклострой\".\n"
                                                "Директором строящейся школы\n"
                                                "назначили Боброва Евгения Александровича,\n"
                                                "руководившего в то время средней школой №1."))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://gusschool3.ucoz.ru/"
        webbrowser.open(url)


class School1(QWidget):  # Окно с информацией о детской больнице
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 773)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 110, 331, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Школа №1/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 511, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 10, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 680, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 590, 481, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Школа №1"))
        self.label_5.setText(_translate("Form", "В 1977 году средняя школа № 1\n"
                                                "впервые открыла двери для своих учеников.\n"
                                                "На краю города, в лесном массиве,\n"
                                                " в современном здании зазвучали голоса\n"
                                                "ребятишек. Здесь начиналась новая жизнь:\n"
                                                "первым директором Бобровым Е.А.\n"
                                                "сюда были приглашены учителя со всех школ города,\n"
                                                "молодые, перспективные; родители\n"
                                                "были рады за своих детей (наконец в этом микрорайоне\n"
                                                "появилась своя школа); Кварцевый завод\n"
                                                "стал шефским предприятием.\n"
                                                "Жизнь закипела ключом. Школа была\n"
                                                "рассчитана на  1200 человек, современно оборудована."))
        self.label.setText(_translate("Form", "Школа № 1"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_3.setText(_translate("Form", "Адрес:\n"
                                                "601500, Владимирская область,\n"
                                                "г. Гусь-Хрустальный, ул. Калинина, д. 1"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://gus-sch1.ucoz.ru/"
        webbrowser.open(url)


class School2_1(QWidget):  # Окно с информацией о школе № 2, корпус 1
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 780)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 20, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 481, 221))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Школа №2 корпус 1/img.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 310, 491, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 680, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Школа №2, корпус 1"))
        self.label.setText(_translate("Form", "Школа № 2 корпус 1"))
        self.label_5.setText(_translate("Form", "Средняя школа №2 г. Гусь-Хрустальный\n"
                                                "была заложена в Международный\n"
                                                "День Защиты детей - 1 июня 1966 г.\n"
                                                " 7 октября 1967 года школа\n"
                                                "была сдана в эксплуатацию и\n"
                                                "приняла учащихся 1-9 классов.\n"
                                                "Школа строилась по современному типовому проекту\n"
                                                "в три этажа. Кроме классов, она будет иметь\n"
                                                "специализированные лаборатории,\n"
                                                "актовый и спортивный залы, различные комнаты.\n"
                                                "Около школы разместится стадион,\n"
                                                "пришкольный участок. Перед входом будет\n"
                                                "разбит сквер."))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://gusschool2.ru/"
        webbrowser.open(url)


class School2_2(QWidget):  # Окно с информацией о школе № 2, корпус 2
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 784)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 680, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 20, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 120, 311, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Школа №2 корпус 2/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 310, 491, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Школа №2, корпус 2"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label.setText(_translate("Form", "Школа № 2 корпус 2"))
        self.label_5.setText(_translate("Form", "Средняя школа №2 г. Гусь-Хрустальный\n"
                                                "была заложена в Международный\n"
                                                "День Защиты детей - 1 июня 1966 г.\n"
                                                " 7 октября 1967 года школа\n"
                                                "была сдана в эксплуатацию и\n"
                                                "приняла учащихся 1-9 классов.\n"
                                                "Школа строилась по современному типовому проекту\n"
                                                "в три этажа. Кроме классов, она будет иметь\n"
                                                "специализированные лаборатории,\n"
                                                "актовый и спортивный залы, различные комнаты.\n"
                                                "Около школы разместится стадион,\n"
                                                "пришкольный участок. Перед входом будет\n"
                                                "разбит сквер."))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://gusschool2.ru/"
        webbrowser.open(url)


class Gimnazia(QWidget):  # Окно с информацией о школе № 2, корпус 2
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(565, 677)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 20, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 310, 491, 171))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 451, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Гимназия/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 570, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 460, 371, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Православная гимназия"))
        self.label.setText(_translate("Form", "Православная гимназия"))
        self.label_5.setText(_translate("Form", "Православная гимназия во имя преподобного\n"
                                                "Сергия Радонежского была открыта в\n"
                                                "г. Гусь-Хрустальный 1 сентября 1999 года по\n"
                                                "благословению архиепископа Владимирского\n"
                                                "и Суздальского Евлогия."))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_3.setText(_translate("Form", "Адрес\n"
                                                "Интернациональная ул., 52"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://www.prav-gymnasium.ru/"


class Mendeleevsky(QWidget):  # Окно с информацией о менделеевском
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(577, 489)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 0, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 360, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 100, 471, 261))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Менделеевский/image.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Менделеевский"))
        self.label.setText(_translate("Form", "Менделеевский"))
        self.label_5.setText(_translate("Form", "Адрес:\n"
                                                "ул. Менделеева, 23, Гусь-Хрустальный"))


class CenterHospital(QWidget):  # Окно с информацией о центральной больнице
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(561, 389)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 0, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 220, 491, 131))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 401, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Центральная больница/image.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Гусь хрустальная центральная городская больница"))
        self.label.setText(_translate("Form", "Гусь хрустальная центральная городская больница"))
        self.label_5.setText(_translate("Form", "Адрес:\n"
                                                "\n"
                                                "ул. Калинина, 61, Гусь-Хрустальный"))


class School7(QWidget):  # Окно с информацией о школе №7
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 669)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 501, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 550, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 70, 341, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Школа №7/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 420, 481, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 0, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Школа №7"))
        self.label_5.setText(_translate("Form", "Муниципальное бюджетное\n"
                                                "общеобразовательное учреждение\n"
                                                "«Основная общеобразовательная школа №7» была\n"
                                                "построена в 1936 году, о чем записано\n"
                                                "в техническом паспорте школы"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_3.setText(_translate("Form", "Адрес:\n"
                                                "\n"
                                                "2-я Народная ул., 5"))
        self.label.setText(_translate("Form", "Школа № 7"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://xn--7-7sbaa3cgkl1gb.xn--p1ai/"
        webbrowser.open(url)


class Five(QWidget):  # Окно с информацией о пятёрочке
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(517, 599)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 10, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 490, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 360, 371, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 331, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Пятёрочка/logo.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Пятёрочка"))
        self.label.setText(_translate("Form", "Пятёрочка"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_3.setText(_translate("Form", "Адрес:\n"
                                                "ул. Калинина, 28Б"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://5ka.ru/"
        webbrowser.open(url)


class Diksi(QWidget):  # Окно с информацией о дикси
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(472, 584)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 350, 371, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 401, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Дикси/logo.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 0, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 480, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Дикси"))
        self.label_3.setText(_translate("Form", "Адрес:\n"
                                                "ул. Свердлова, 9"))
        self.label.setText(_translate("Form", "Дикси"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://dixy.ru/"
        webbrowser.open(url)


class Lider(QWidget):  # Окно с информацией о лидере
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(497, 454)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 330, 371, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 0, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 451, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Лидер/image.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Лидер"))
        self.label_3.setText(_translate("Form", "Адрес:\n"
                                                "Теплицкий просп., 4"))
        self.label.setText(_translate("Form", "Лидер"))


class Cinema(QWidget):  # Окно с информацией о алмазе
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 766)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 660, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 290, 491, 361))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 0, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 291, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Алмаз/image.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Алмаз"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_5.setText(_translate("Form", "В самом центре города, напротив городского\n"
                                                "озера – ещё одной местной «достопримечательности», \n"
                                                "находится развлекательный центр «АлмаZ»,\n"
                                                "включающий в себя 2 кинозала на\n"
                                                "150 посадочных мест каждый – цифровой\n"
                                                "с экраном 6 х 3,2 м и 3 D c экраном\n"
                                                "7,65 х 3,2 м, летнее кафе, бар,\n"
                                                "пиццерию, игровые автоматы, боулинг\n"
                                                "(2 дорожки) со своим баром, караоке – кафе,\n"
                                                "детскую комнату с батутом, лабиринтом,\n"
                                                "горкой и различными игрушками и своим\n"
                                                "детским кафе, где часто устраиваются\n"
                                                "детские праздники."))
        self.label.setText(_translate("Form", "АлмаZ"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://almaz-cinema.ru/"
        webbrowser.open(url)


class School10(QWidget):  # Окно с информацией о школе №15
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(584, 659)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 560, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 320, 491, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 401, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Школа №10/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 20, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Школа №10"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_5.setText(_translate("Form", "С 1926 года начала свою историю школа № 10.\n"
                                                "Сначала это была начальная школа, которую\n"
                                                "построили для детей кирпичного завода.\n"
                                                "В ней было 6 классов, где\n"
                                                "обучались 227 учеников.\n"
                                                "В 1935 году было построено старое здание школы,\n"
                                                "в котором сейчас находятся кабинеты начальных классовn\n"
                                                "и школьная библиотека. "))
        self.label.setText(_translate("Form", "Школа № 10"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://school10gus.ru/"
        webbrowser.open(url)


class School13(QWidget):  # Окно с информацией о школе №13
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(544, 777)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 320, 491, 311))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 20, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 331, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Школа №13/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 670, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Школа №13"))
        self.label_5.setText(_translate("Form", "Здание школы является памятником XIX века,\n"
                                                "включён в реестр объектов культурного наследия\n"
                                                "(памятников истории и культуры)\n"
                                                "народов Российской Федерации.Открытие средней школы"
                                                " № 13 в сентябре 1938 года.\n"
                                                "\n"
                                                "Основание: Технический паспорт.\n"
                                                "\n"
                                                "С 01.09.1997 года средняя школа № 13\n"
                                                "переименована в Муниципальное образовательное\n"
                                                "учреждение «Средняя общеобразовательная"
                                                " школа № 13»."))
        self.label.setText(_translate("Form", "Школа № 13"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://gus-school13.ru/"
        webbrowser.open(url)


class Five2(QWidget):  # Окно с информацией о пятёрочке
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(531, 622)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 380, 501, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 100, 331, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Пятёрочка/logo.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 30, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 510, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному"
                                               "| Пятёрочка"))
        self.label_3.setText(_translate("Form", "Адрес:\n"
                                                "Россия, Владимирская область,"
                                                " Гусь-Хрустальный, Полевая улица, 1А"))
        self.label.setText(_translate("Form", "Пятёрочка"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://5ka.ru/"
        webbrowser.open(url)


class Five3(QWidget):  # Окно с информацией о пятёрочке
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(546, 585)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 0, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 480, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 350, 501, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 331, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Пятёрочка/logo.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Пятёрочка"))
        self.label.setText(_translate("Form", "Пятёрочка"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_3.setText(_translate("Form", "Адрес:\n"
                                                "Россия, Владимирская область,"
                                                " Гусь-Хрустальный, Полевая улица, 1А"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://5ka.ru/"
        webbrowser.open(url)


class AZS_lukoil(QWidget):  # Окно с информацией о лукоиле
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(583, 713)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 440, 461, 121))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 600, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 10, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 80, 281, 291))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/лукойл/image.jpg"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " АЗС"))
        self.label_4.setText(_translate("Form", "АДРЕС\n"
                                                "Владимирская обл., г. Гусь-Хрустальный, ул. Курловская"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label.setText(_translate("Form", "Лукойл"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://www.lukoil.ru/"
        webbrowser.open(url)


class Church(QWidget):  # Окно с информацией о храме
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(596, 857)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 70, 441, 281))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Храм/image.jpg"))
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 451, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 360, 441, 391))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Храм во имя святителя Николая Чудотворца"))
        self.label.setText(_translate("Form", "Храм во имя святителя Николая Чудотворца"))
        self.label_3.setText(_translate("Form", "22 мая 2018 года в Гусь-Хрустальном\n"
                                                "освятили новый храм во имя святителя\n"
                                                "Николая Чудотворца. Храм воздвигнут\n"
                                                "на средства учредителей завода\n"
                                                "«Гусар» и их семей, а также на\n"
                                                "пожертвования рабочих предприятия\n"
                                                "и прихожан. Главным меценатом\n"
                                                "строительства новой церкви,\n"
                                                "которую некоторые уже называют\n"
                                                "«архитектурным шедевром», стал генеральный\n"
                                                "директор \"Гусара\", депутат Законодательного\n"
                                                "Собрания Владимирской области\n"
                                                "Александр Берёзкин. Как говорили на закладке\n"
                                                "церкви, идея строительства принадлежит\n"
                                                "жене Березкина."))


class School4(QWidget):  # Окно с информацией о школе №4
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(655, 788)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 90, 371, 231))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Школа №4/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(230, 690, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 320, 491, 361))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 30, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному | "
                                               "Школа №4"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label_5.setText(_translate("Form", "В феврале 1987 года распахнула\n"
                                                "свои двери новая общеобразовательная\n"
                                                "школа №4. Именно с этого дня\n"
                                                "она ведёт отсчёт своих лет.\n"
                                                "И с этих пор каждый из нас\n"
                                                "с нетерпением ждёт волнующую трель\n"
                                                "школьного звонка. Каждый день мы,\n"
                                                "ученики и учителя, торопимся в этот дом и в нём\n"
                                                "проводим большую часть дня, значит\n"
                                                "и жизнь.К сентябрю 1986 года\n"
                                                "было принято около тысячи\n"
                                                "заявлений от родителей района Эстакада\n"
                                                "на обучение их детей в новой школе."))
        self.label.setText(_translate("Form", "Школа № 4"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://www.gus-school4.ru/"
        webbrowser.open(url)


class AZS_LionOil(QWidget):  # Окно с информацией о АЗС
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 478)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 401, 291))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Lion-Oil/img.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 20, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 390, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " АЗС"))
        self.label.setText(_translate("Form", "Line-Oil"))
        self.label_4.setText(_translate("Form", "Адрес: \n"
                                                "Транспортная ул., 51А, Гусь-Хрустальный"))


class School5(QWidget):  # Окно с информацией о школе №5
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(535, 719)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 421, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Школа №5/image.jpg"))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 610, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 10, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 330, 481, 261))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Школа №5"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))
        self.label.setText(_translate("Form", "Школа №5"))
        self.label_3.setText(_translate("Form", "МОУ «Основная общеобразовательная школа №5»\n"
                                                " г. Гусь-Хрустального открыта в 1936 г.,\n"
                                                "как начальная школа №7. Первым директором\n"
                                                "начальной школы стал А.Н. Борисов.\n"
                                                "В 1963 г. изменен номер школы с № 7 на № 5,\n"
                                                "в 1971 г. начальная школа № 5\n"
                                                "была реорганизована в восьмилетнюю №5,\n"
                                                "в 1989 – в неполную среднюю школы № 5,\n"
                                                "в 1997 г. – в муниципальное общеобразовательное\n"
                                                "учреждение «Основная общеобразовательная\n"
                                                "школа № 5»."))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "http://ekolan5.ru/news.php"
        webbrowser.open(url)


class School15(QWidget):  # Окно с информацией о школе №15
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushBTN)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(549, 584)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 260, 491, 211))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 471, 191))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Images/Школа №15/img.jpg"))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 0, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 470, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Путеводитель по Гусь-Хрустальному |"
                                               " Школа №15"))
        self.label_5.setText(
            _translate("Form", "Школа была основана в 196 году. С 1942 по 1945 гг\n"
                               "в в школе была госпиталь. В 2016 году прошло\n"
                               "открытие первого кадетского класса\n"
                               " В 2018 году школа стала лауреатом\n"
                               "выставки образовательных организаций."))
        self.label.setText(_translate("Form", "Школа № 15"))
        self.pushButton.setText(_translate("Form", "Перейти на сайт"))

    def pushBTN(self):
        # Переход на сайт объекта
        url = "https://stupeni15.edusite.ru/"
        webbrowser.open(url)


def ProgramOperation():
    global candycash
    global level, name_user, icon_user, translator
    global interface, sounds_and_voices
    info_database_resources = [0, 0]
    con = sqlite3.connect('CandyBase.db')
    cur = con.cursor()
    cur.execute('SELECT [CandyCash], [CandyLevel] FROM [resources] LIMIT 500')
    temp = cur.fetchall()
    for i in temp:
        candycash = int(i[0])
        level = int(i[1])
    cur.execute('SELECT [Nickname], [image] FROM [settings] LIMIT 500')
    temp = cur.fetchall()
    for i in temp:
        name_user = str(i[0])
        icon_user = str(i[1])
    con.commit()
    cur.execute('SELECT [interface], [sounds_and_voices], [translator] FROM [candymarket] LIMIT 500')
    temp = cur.fetchall()
    for i in temp:
        interface = i[0]
        sounds_and_voices = i[1]
        translator = i[2]
    con.commit()
    con.close()
    app = QtWidgets.QApplication([])
    if interface == 1:
        application = Interface1()
    elif interface == 2:
        application = Interface2()
    application.show()
    sys.exit(app.exec())


PO = ProgramOperation()
