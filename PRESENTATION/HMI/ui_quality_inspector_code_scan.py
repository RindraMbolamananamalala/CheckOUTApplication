# -*- coding: utf-8 -*-

"""
ui_quality_inspector_code_scan.py: The python file dedicated to the graphical definition of the specific window for the
Scan process of Quality Inspector Code of the Check OUT
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UIQualityInspectorCodeScan(object):

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
        # General Settings
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
            self.set_main_window(main_window)
        self.get_main_window().setWindowTitle("Scan")
        self.get_main_window().setFixedSize(400, 200)
        self.get_main_window().setGeometry(800, 500, 400, 200)
        # Thea area for the actual scanning of barcode
        self.area_actual_scanning = QWidget(self.get_main_window())
        self.area_actual_scanning.setGeometry(QRect(10, 50, 375, 75))
        self.area_actual_scanning.setStyleSheet("background-color: None;")
        # The text area for the Barcode...
        self.text_barcode = QPlainTextEdit(self.area_actual_scanning)
        self.text_barcode.setObjectName(u"text_comments")
        self.text_barcode.setGeometry(QRect(0, 0, 375, 75))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(13)
        self.text_barcode.setFont(font1)
        self.text_barcode.setStyleSheet(u"background-color: #34393f;"
                                        u" color: white;"
                                        u"border-radius: 37px;")
        self.text_barcode.setPlaceholderText("\n Scan Quality Inspector Code")

