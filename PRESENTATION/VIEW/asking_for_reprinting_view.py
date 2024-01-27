# -*- coding: utf-8 -*-

"""
barcode_scan_view_.py: The python file dedicated to the "View::AskingForReprinting" part of the MVC pattern
implemented within the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_asking_for_reprinting import UIAskingForReprinting


class AskingForReprintingView:

    def set_ui_asking_for_reprinting(self, ui_asking_for_reprinting: UIAskingForReprinting):
        """

        :param ui_asking_for_reprinting: The UI component to be linked to the current View
        :return:
        """
        self.ui_asking_for_reprinting = ui_asking_for_reprinting

    def get_ui_asking_for_reprinting(self) -> UIAskingForReprinting:
        """

        :return: The UI component linked to the current View
        """
        return self.ui_asking_for_reprinting

    def __init__(self):
        # Instantiating the UI linked to the current View
        self.set_ui_asking_for_reprinting(UIAskingForReprinting(QMainWindow()))

        # At the beginning, let's clear the Window..
        self.clear_window()

    def clear_window(self):
        """
        Clearing the content of the Barcode Scan Window
        :return:
        """
        # Just pass...
        pass

    def show_window(self):
        """
        Displaying the window
        :return: None
        """
        self.get_ui_asking_for_reprinting().get_main_window().show()

    def close_window(self):
        """
        Closing the window
        :return:
        """
        # First, let's clear all the window's content
        self.clear_window()
        # Then, make the window not visible
        self.get_ui_asking_for_reprinting().get_main_window().setVisible(False)

