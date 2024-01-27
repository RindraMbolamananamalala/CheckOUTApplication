# -*- coding: utf-8 -*-

"""
ui_asking_for_reprinting.py: The python file dedicated to the graphical definition of the specific window
for the questioning about making another reprinting after a wrong barcode scanned for the verification or not
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.QUALITY_INSPECTOR_CODE_UI.ui_quality_inspector_code import UIQualityInspectorCode


class UIAskingForReprinting(UIQualityInspectorCode):

    def get_button_ok(self) -> QPushButton:
        """

        :return: The Button dedicated to the option "OK"
        """
        return self.button_ok

    def get_button_abort(self) -> QPushButton:
        """

        :return: The Button dedicated to the option "Abort"
        """
        return self.button_abort

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
            main_window.setObjectName(u"ui_asking_for_reprinting")
            self.set_main_window(main_window)
        self.get_main_window().setFixedSize(400, 200)
        self.get_main_window().setGeometry(800, 500, 400, 200)

        # Customizing the Window's Title
        self.get_main_window().setWindowTitle("Wrong Barcode Scanned")
        # The area for the actual verification of the printing
        self.area_actual_verification = QWidget(self.get_main_window())
        self.area_actual_verification.setGeometry(QRect(10, 50, 375, 130))
        self.area_actual_verification.setStyleSheet("background-color: None;")
        # The text label for the Message announcing the (Re-)printing intention...
        self.label_announcement_reprinting = QLabel(self.area_actual_verification)  # QIC stands for
        # "Quality Inspector Code"
        self.label_announcement_reprinting.setObjectName(u"text_comments")
        self.label_announcement_reprinting.setGeometry(QRect(0, 0, 375, 40))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(13)
        self.label_announcement_reprinting.setFont(font1)
        self.label_announcement_reprinting.setAlignment(Qt.AlignCenter)
        self.label_announcement_reprinting.setStyleSheet(u"background-color: None;"
                                                                u" color: #34393f;")
        self.label_announcement_reprinting.setText("Do you want to reprint?")
        # The area for the buttons that will handle the redirection in function of the User's intention (Re-Printing or
        # not)
        self.area_buttons_for_redirections = QWidget(self.area_actual_verification)
        self.area_buttons_for_redirections.setGeometry(QRect(0, 60, 375, 90))
        self.area_buttons_for_redirections.setStyleSheet("background-color: None;")
        # OK Button
        self.button_ok = QPushButton(self.area_buttons_for_redirections)
        self.button_ok.setGeometry(QRect(55, 10, 100, 50))
        self.button_ok.setText("OK")
        self.button_ok.setFont(font1)
        self.button_ok.setStyleSheet("background-color: #34393f;"
                                        u" color: white;"
                                        u"border-radius: 20px;")
        self.button_ok.setCursor(Qt.PointingHandCursor)
        # Abort Button
        self.button_abort = QPushButton(self.area_buttons_for_redirections)
        self.button_abort.setGeometry(QRect(220, 10, 100, 50))
        self.button_abort.setText("Abort")
        self.button_abort.setFont(font1)
        self.button_abort.setStyleSheet("background-color: #34393f;"
                                     u" color: white;"
                                     u"border-radius: 20px;")
        self.button_abort.setCursor(Qt.PointingHandCursor)