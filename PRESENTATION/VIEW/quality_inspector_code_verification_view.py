# -*- coding: utf-8 -*-

"""
quality_inspector_code_verification_view.py: The python file dedicated to the "View::QualityInspectorCodeVerification"
part of the MVC pattern implemented within the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtWidgets import *

from PRESENTATION.HMI.QUALITY_INSPECTOR_CODE_UI.ui_quality_inspector_code_verification import \
    UIQualityInspectorCodeVerification


class QualityInspectorCodeVerificationView:

    def set_ui_quality_inspector_code_verification(self
                                        ,ui_quality_inspector_code_verification: UIQualityInspectorCodeVerification):
        """

        :param ui_quality_inspector_code_verification: The Quality Inspector Code Verification UI component to be used
        by the current View
        :return: None
        """
        self.ui_quality_inspector_code_verification = ui_quality_inspector_code_verification

    def get_ui_quality_inspector_code_verification(self) -> UIQualityInspectorCodeVerification:
        """

        :return: The Quality Inspector Code Verification UI component used by the current View
        """
        return self.ui_quality_inspector_code_verification

    def __init__(self):
        # Instantiating the The Quality Inspector Code Verification UI component
        self.set_ui_quality_inspector_code_verification(UIQualityInspectorCodeVerification(QMainWindow()))

        # At the beginning, let's clear the Window..
        self.clear_window()

    def clear_window(self):
        """
        Clearing the content of the Window
        :return:
        """
        # For the moment, just pass..
        pass

    def show_window(self):
        """
        Displaying the Quality Inspector Code Verification window
        :return: None
        """
        self.get_ui_quality_inspector_code_verification().get_main_window().show()

    def close_window(self):
        """
        Closing the Quality Inspector Code Verification window
        :return:
        """
        # First, let's clear all the window's content
        self.clear_window()
        # Then, make the window not visible
        self.get_ui_quality_inspector_code_verification().get_main_window().setVisible(False)