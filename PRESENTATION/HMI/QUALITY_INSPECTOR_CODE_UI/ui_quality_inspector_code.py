# -*- coding: utf-8 -*-

"""
ui_quality_inspector_code.py: The python file dedicated to the graphical definition of the Superclass of all the
specific windows for the Scan process of the Quality Inspector Code of the Check OUT
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtWidgets import *


class UIQualityInspectorCode(object):

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

        :param main_window: The main window to be used by the current window
        """
        # General Settings
        if not main_window.objectName():
            main_window.setObjectName(u"MainWindow")
            self.set_main_window(main_window)
        self.get_main_window().setFixedSize(400, 200)
        self.get_main_window().setGeometry(800, 500, 400, 200)
