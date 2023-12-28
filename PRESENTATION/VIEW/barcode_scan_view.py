# -*- coding: utf-8 -*-

"""
barcode_scan_view_.py: The python file dedicated to the "View::BarcodeScan" part of the MVC pattern
implemented within the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_barcode_scan import UIBarcodeScan


class BarcodeScanView:

    def set_ui_barcode_scan(self, ui_barcode_scan: UIBarcodeScan):
        """

        :param ui_barcode_scan: The Barcode Scan UI component to be used by the current View
        :return: None
        """
        self.ui_barcode_scan = ui_barcode_scan

    def get_ui_barcode_scan(self) -> UIBarcodeScan:
        """

        :return: The Barcode Scan UI component used by the current View
        """
        return self.ui_barcode_scan

    def __init__(self):
        # Instantiating the Barcode Scan UI component
        self.set_ui_barcode_scan(UIBarcodeScan(QMainWindow()))

        # At the beginning, let's clear the Window..
        self.clear_window()

    def notify_wrong_barcode(self):
        """
        Notifying the User that he/she has scanned a wrong Barcode
        :return: None
        """
        text_area_barcode = self.get_ui_barcode_scan().get_text_barcode()
        # Turning the Barcode Scanning area's color into red
        text_area_barcode.setStyleSheet(u"background-color: red;"
                                        u" color: white;"
                                        u"border-radius: 55px;")
        text_area_barcode.setPlainText("")
        # Adapting the Placeholder of the Barcode Scanning area
        text_area_barcode.setPlaceholderText("Wrong Barcode Scanned")

    def reinitialize_window_appearance(self):
        """
        Re-initializing the appearance of the Barcode Scan window
        :return:
        """
        window = self.get_ui_barcode_scan()
        window.get_text_barcode().setStyleSheet(u"background-color: #34393f;"
                                                u" color: white;"
                                                u"border-radius: 55px;")
        window.get_text_barcode().setPlaceholderText("Scan Barcode")

    def clear_window(self):
        """
        Clearing the content of the Barcode Scan Window
        :return:
        """
        text_area_barcode = self.get_ui_barcode_scan().get_text_barcode()
        # No Barcode is being scanned at this stage...
        text_area_barcode.setPlainText("")
        self.reinitialize_window_appearance()

    def show_window(self):
        """
        Displaying the Barcode Scan window
        :return: None
        """
        self.get_ui_barcode_scan().get_main_window().showMaximized()

    def close_window(self):
        """
        Closing the Barcode Scan window
        :return:
        """
        # First, let's clear all the window's content
        self.clear_window()
        # Then, make the window not visible
        self.get_ui_barcode_scan().get_main_window().setVisible(False)
