# -*- coding: utf-8 -*-

"""
test_report_result_view_.py: The python file dedicated to the "View::TestReportResultView" part of the MVC pattern
implemented within the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_test_report_result import UITestReportResult


class TestReportResultView:

    def set_ui_test_report_result(self, ui_test_report_result: UITestReportResult):
        """

        :param ui_test_report_result: The Test Report Result UI component to be used by the current View
        :return: None
        """
        self.ui_test_report_result = ui_test_report_result

    def get_ui_test_report_result(self) -> UITestReportResult:
        """

        :return: The Test Report Result UI component used by the current View
        """
        return self.ui_test_report_result

    def __init__(self):
        # Instantiating the Test Report Result UI component
        self.set_ui_test_report_result(UITestReportResult(QMainWindow()))

        # At the beginning, let's clear the Window..
        self.clear_window()

    def show_window(self):
        """
        Displaying the Test Report Result window
        :return: None
        """
        self.get_ui_test_report_result().get_main_window().showMaximized()

    def close_window(self):
        """
        Closing the Test Report Result window
        :return:
        """
        # First, let's clear all the window's content
        self.clear_window()
        # Then, make the window not visible
        self.get_ui_test_report_result().get_main_window().setVisible(False)
