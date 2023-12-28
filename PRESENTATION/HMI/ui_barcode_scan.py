# -*- coding: utf-8 -*-

"""
ui_barcode_scan.py: The python file dedicated to the graphical definition of the specific window for the Scan of
PFT Barcode (OUT)
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_rework_check_out_window import Ui_ReworkCheckOUTWindow


class UIBarcodeScan(Ui_ReworkCheckOUTWindow):

    def get_text_barcode(self) -> QPlainTextEdit:
        """

        :return: The text area dedicated to the Barcode to be scanned
        """
        return self.text_barcode

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: The main window to be used by the current window
        """
        # First, we have to call the constructor of the Superclass in order to initialize (to configure)
        # all of the behaviors and data defined in it
        super(UIBarcodeScan, self).__init__(main_window)

        # Thea area for the actual scanning of barcode
        self.area_actual_scanning = QWidget(self.column_checking)
        self.area_actual_scanning.setGeometry(QRect(0, 160, 1760, 200))
        self.area_actual_scanning.setStyleSheet("background-color: None;")
        # The label...
        self.label_scan_barcode = QLabel(self.area_actual_scanning)
        self.label_scan_barcode.setGeometry(QRect(630, 10, 475, 30))
        font_label_scan_barcode = QFont()
        font_label_scan_barcode.setBold(False)
        font_label_scan_barcode.setFamily(u"Calibri")
        font_label_scan_barcode.setPointSize(22)
        font_label_scan_barcode.setFamily(u"Consolas")
        self.label_scan_barcode.setFont(font_label_scan_barcode)
        self.label_scan_barcode.setStyleSheet("color: black;")
        self.label_scan_barcode.setText("Please Scan PFT Barcode")
        # The text area for the Barcode...
        self.text_barcode = QPlainTextEdit(self.area_actual_scanning)
        self.text_barcode.setObjectName(u"text_comments")
        self.text_barcode.setGeometry(QRect(120, 60, 1450, 110))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(50)
        self.text_barcode.setFont(font1)
        self.text_barcode.setStyleSheet(u"background-color: #34393f;"
                                         u" color: white;"
                                         u"border-radius: 55px;")
        self.text_barcode.setPlaceholderText("Scan Barcode")