# -*- coding: utf-8 -*-

"""
quality_inspector_code_scan_view_.py: The python file dedicated to the "View::QualityInspectorCodeScan" part of the MVC
pattern implemented within the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_quality_inspector_code_scan import UIQualityInspectorCodeScan


class QualityInspectorCodeScanView:

    def set_ui_quality_inspector_code_scan(self, ui_quality_inspector_code_scan: UIQualityInspectorCodeScan):
        """

        :param ui_quality_inspector_code_scan: The Quality Inspector Code Scan UI component to be used by the current
        View
        :return: None
        """
        self.ui_quality_inspector_code_scan = ui_quality_inspector_code_scan

    def get_ui_quality_inspector_code_scan(self) -> UIQualityInspectorCodeScan:
        """

        :return: The Quality Inspector Code Scan UI component used by the current View
        """
        return self.ui_quality_inspector_code_scan

    def __init__(self):
        # Instantiating the The Quality Inspector Code Scan UI component
        self.set_ui_quality_inspector_code_scan(UIQualityInspectorCodeScan(QMainWindow()))

        # At the beginning, let's clear the Window..
        self.clear_window()

    def show_window(self):
        """
        Displaying the Quality Inspector Code Scan window
        :return: None
        """
        self.get_ui_quality_inspector_code_scan().get_main_window().showMaximized()

    def close_window(self):
        """
        Closing the Quality Inspector Code Scan window
        :return:
        """
        # First, let's clear all the window's content
        self.clear_window()
        # Then, make the window not visible
        self.get_ui_quality_inspector_code_scan().get_main_window().setVisible(False)