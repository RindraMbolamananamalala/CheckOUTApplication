# -*- coding: utf-8 -*-

"""
ui_quality_inspector_code_scan.py: The python file dedicated to the graphical definition of the specific window for the
Scan process of the Quality Inspector Code of the Check OUT
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.QUALITY_INSPECTOR_CODE_UI.ui_quality_inspector_code import UIQualityInspectorCode


class UIQualityInspectorCodeScan(UIQualityInspectorCode):

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: The main window to be used by the current window
        """
        # First, we have to call the constructor of the Superclass in order to initialize (to configure)
        # all of the behaviors and data defined in it
        super(UIQualityInspectorCodeScan, self).__init__(main_window)
        # Customizing the Window's Title
        self.get_main_window().setWindowTitle("Scan")
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
