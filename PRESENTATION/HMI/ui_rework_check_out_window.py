# -*- coding: utf-8 -*-

"""
ui_rework_check_out_window.py: The python file dedicated to the graphical definition of the abstract specific Window
of the  application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ReworkCheckOUTWindow(object):

    def set_main_window(self, main_window: QMainWindow):
        """

        :param main_window: The Qt Main Window to be used by the the current Main Window.
        :return:
        """
        self.main_window = main_window

    def get_main_window(self) -> QMainWindow:
        """

        :return: The Qt Main Window used by the the current Main Window.
        """
        return self.main_window

    def __init__(self, main_window: QMainWindow):
        """
        Setting up the UI.

        :param main_window: a blank main window to be associated with the set of settings.
        """
        # General Settings Part I
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
            self.set_main_window(main_window)
        self.get_main_window().setFixedSize(1920, 1080)
        self.get_main_window().setStyleSheet(u"background-color : #34393f;")

        self.get_main_window().setAutoFillBackground(False)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")

        # The column for the Navigation
        self.column_general_information = QWidget(self.centralwidget)
        self.column_general_information.setObjectName(u"column_navigation")
        self.column_general_information.setGeometry(QRect(0, 0, 290, 1080))
        self.column_general_information.setStyleSheet(u"background-color : #34393f;")

        # The label dedicated to the fixed Strings
        self.label_fixed_strings = QLabel(self.column_general_information)
        self.label_fixed_strings.setObjectName(u"label_fixed_strings")
        self.label_fixed_strings.setGeometry(QRect(30, 20, 190, 100))
        font = QFont()
        font.setFamily(u"Consolas")
        font.setPointSize(18)
        font.setBold(False)
        self.label_fixed_strings.setFont(font)
        self.label_fixed_strings.setAlignment(Qt.AlignTop)
        self.label_fixed_strings.setStyleSheet(u"color: white; "
                                               u"background-color: None;"
                                               u"border: None;")
        self.label_fixed_strings.setTextFormat(Qt.AutoText)
        self.label_fixed_strings.setWordWrap(True)

        # The button dedicated to the "Settings"
        self.button_settings = QPushButton(self.column_general_information)
        self.button_settings.setText("Settings")
        self.button_settings.setCursor(Qt.PointingHandCursor)
        self.button_settings.setObjectName(u"button_settings")
        self.button_settings.setGeometry(QRect(30, 900, 175, 50))
        self.button_settings.setStyleSheet(u"background-color: #eeeefa;"
                                           "border-radius: 25px;"
                                           "color: #34393f;"
                                           "font-family: Century Gothic;"
                                           "font-size: 30px;")

        # The Logo box area
        self.widget_logo_box = QWidget(self.column_general_information)
        self.widget_logo_box.setObjectName(u"widget_logo_box")
        self.widget_logo_box.setGeometry(QRect(20, 950, 205, 60))
        self.widget_logo_box.setStyleSheet(u"background-color: None;")
        self.label_logo_box = QLabel(self.widget_logo_box)
        self.label_logo_box.setGeometry(QRect(0, 0, 205, 60))
        self.label_logo_box.setPixmap(QPixmap("RESOURCES\\IMAGES\\aptiv-logo_white_m25.png"))

        self.label_logo_box.setObjectName(u"label_logo_box")
        self.label_logo_box.setStyleSheet(u"background-color: None;")

        # The column for the actual checking
        self.column_checking = QWidget(self.centralwidget)
        self.column_checking.setObjectName(u"column_treatment")
        self.column_checking.setGeometry(QRect(225, 0, 1760, 1001))
        self.column_checking.setStyleSheet(u"QWidget#column_treatment{"
                                            u"background-color: #eeeefa;"
                                            u"border-radius: 75px;\n"
                                            u"}")

        # General Settings Part II
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 26))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_fixed_strings.setText("Rework Out Station")
