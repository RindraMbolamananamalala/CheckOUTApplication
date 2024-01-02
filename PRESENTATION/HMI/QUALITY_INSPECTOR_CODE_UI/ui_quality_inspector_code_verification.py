# -*- coding: utf-8 -*-

"""
ui_quality_inspector_code_verification.py: The python file dedicated to the graphical definition of the specific window
for the Verification process of the Quality Inspector Code of the Check OUT
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.QUALITY_INSPECTOR_CODE_UI.ui_quality_inspector_code import UIQualityInspectorCode


class UIQualityInspectorCodeVerification(UIQualityInspectorCode):

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: The main window to be used by the current window
        """
        # First, we have to call the constructor of the Superclass in order to initialize (to configure)
        # all of the behaviors and data defined in it
        super(UIQualityInspectorCodeVerification, self).__init__(main_window)
        # Customizing the Window's Title
        self.get_main_window().setWindowTitle("Wrong code scanned")
        # The area for the actual verification of the Code
        self.area_actual_verification = QWidget(self.get_main_window())
        self.area_actual_verification.setGeometry(QRect(10, 50, 375, 130))
        self.area_actual_verification.setStyleSheet("background-color: None;")
        # The text label for the Message announcing the Wrong Code scanned...
        self.label_announcement_wrong_qic_scanned = QLabel(self.area_actual_verification)  # QIC stands for
        # "Quality Inspector Code"
        self.label_announcement_wrong_qic_scanned.setObjectName(u"text_comments")
        self.label_announcement_wrong_qic_scanned.setGeometry(QRect(0, 0, 375, 40))
        font1 = QFont()
        font1.setFamily(u"Consolas")
        font1.setPointSize(13)
        self.label_announcement_wrong_qic_scanned.setFont(font1)
        self.label_announcement_wrong_qic_scanned.setAlignment(Qt.AlignCenter)
        self.label_announcement_wrong_qic_scanned.setStyleSheet(u"background-color: None;"
                                                                u" color: #34393f;")
        self.label_announcement_wrong_qic_scanned.setText("Repeat Code Scan?")
        # The area for the buttons that will handle the redirection in function of the User's intention (Re-scanning
        # the code or not)
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
        # Abort Button
        self.button_abort = QPushButton(self.area_buttons_for_redirections)
        self.button_abort.setGeometry(QRect(220, 10, 100, 50))
        self.button_abort.setText("Abort")
        self.button_abort.setFont(font1)
        self.button_abort.setStyleSheet("background-color: #34393f;"
                                     u" color: white;"
                                     u"border-radius: 20px;")