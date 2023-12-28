# -*- coding: utf-8 -*-

"""
ui_test_report_result.py: The python file dedicated to the graphical definition of the specific window for the
Test Result Report of the Check OUT
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PRESENTATION.HMI.ui_rework_check_out_window import Ui_ReworkCheckOUTWindow


def get_list_pft() -> list:
    """

    :return: The list of labels' texts corresponding to the PFT
    """
    return ["BCCT", "PreTest", "APC", "ROB", "TRQ1", "Prep1", "TRQ2", "Prep2", "VOSS", "Vision"]


def get_list_rework_processes() -> list:
    """
    
    :return: The list of label's texts corresponding to the Rework Processes
    """
    return ["Crimping", "Flat Board", "USW", "Part 1", "Part 2", "Part 3", "Part 4", "Part 5", "Part 6"]


class UITestReportResult(Ui_ReworkCheckOUTWindow):

    def get_stylesheet_process_element_not_concerned(self):
        """

        :return: The specific stylesheet for a Process Element (Label) not concerned by the current presentation
        """
        return "background-color: #808080;"\
               "color: white;" \
               "border-radius: 35px;"

    def get_stylesheet_process_element_concerned(self):
        """

        :return: The specific stylesheet for a Process Element (Label) concerned by the current presentation
        """
        return "background-color: #34393f;"\
               "color: white;" \
               "border-radius: 35px;"

    def get_stylesheet_process_ok(self):
        """

        :return: The specific stylesheet for a Process Element (Label) corresponding to a OK Harness Status
        """
        return "background-color: #008000;"\
               "color: white;"\
               "border-radius: 35px;"

    def get_stylesheet_process_nok(self):
        """

        :return: The specific stylesheet for a Process Element (Label) corresponding to a NOK Harness Status
        """
        return "background-color: #ff0000;"\
               "color: white;"\
               "border-radius: 35px;"

    def get_label_order_number(self) -> QLabel:
        """

        :return: The label dedicated to the Order Number
        """
        return self.label_oder_number

    def get_list_labels_rework_processes(self) -> list:
        """

        :return: The list of Labels (elements) corresponding to the Rework Processes
        """
        return self.list_labels_rework_processes

    def __init__(self, main_window: QMainWindow):
        """

        :param main_window: The main window to be used by the current window
        """
        # First, we have to call the constructor of the Superclass in order to initialize (to configure)
        # all of the behaviors and data defined in it
        super(UITestReportResult, self).__init__(main_window)

        # The area for the Rework Processes
        self.area_rework_processes = QWidget(self.column_checking)
        self.area_rework_processes.setObjectName("area_rework_processes")
        self.area_rework_processes.setGeometry(QRect(350, 0, 320, 890))
        self.area_rework_processes.setStyleSheet("background-color: None;"
                                                 "border-radius: 75px;")
        # the introductory label..
        self.label_introductory_rp = QLabel(self.area_rework_processes)  # RP stands for "Rework Processes"
        self.label_introductory_rp.setGeometry(QRect(35, 15, 240, 25))
        self.label_introductory_rp.setText("Rework Processes")
        font_rp = QFont()
        font_rp.setFamily(u"Calibri")
        font_rp.setPointSize(20)
        font_rp.setBold(False)
        self.label_introductory_rp.setFont(font_rp)
        self.label_introductory_rp.setStyleSheet("color: black;")
        # adding all the Rework Processes Labels...
        rp_label_counter = 0  # counter of Rework Process Labels initialized to 0
        rp_label_height = 75
        self.list_labels_rework_processes = []  # OOP-related part, Initializing the list of Rework Processes labels
        for rp_text in get_list_rework_processes():
            rp_label_text = rp_text
            rp_label = QLabel(self.area_rework_processes)
            rp_label.setGeometry(
                QRect(10
                      , 50 + (rp_label_counter * rp_label_height) + (rp_label_counter * 15)
                      , 300
                      , rp_label_height
                      )
            )
            rp_label.setObjectName("rp_" + rp_label_text)
            rp_label.setText(rp_label_text)
            font_rp = QFont()
            font_rp.setFamily(u"Calibri")
            font_rp.setPointSize(35)
            font_rp.setBold(False)
            rp_label.setFont(font_rp)
            rp_label.setStyleSheet(self.get_stylesheet_process_element_not_concerned()) # All labels are not yet
            # concerned at the beginning
            rp_label.setAlignment(Qt.AlignCenter)
            rp_label_counter = rp_label_counter + 1
            # OOP-related part...
            self.list_labels_rework_processes.append(rp_label)
        """VERY TEMPORARY"""
        self.get_list_labels_rework_processes()[0].setStyleSheet(self.get_stylesheet_process_element_concerned())
        self.get_list_labels_rework_processes()[1].setStyleSheet(self.get_stylesheet_process_element_concerned())
        self.get_list_labels_rework_processes()[3].setStyleSheet(self.get_stylesheet_process_nok())
        self.get_list_labels_rework_processes()[5].setStyleSheet(self.get_stylesheet_process_ok())
        """VERY TEMPORARY"""

        # The area for the Harness Status (OK or NOK)
        self.area_harness_status = QWidget(self.column_checking)
        self.area_harness_status.setObjectName("area_harness_status")
        self.area_harness_status.setGeometry(QRect(700, 0, 975, 890))
        self.area_harness_status.setStyleSheet("background-color: None;"
                                                     "border-radius: 75px;")
        # The label for the Harness Status (OK or NOK)
        self.label_harness_status = QLabel(self.area_harness_status)
        self.label_harness_status.setObjectName("label_harness_status")
        self.label_harness_status.setGeometry(QRect(300, 420, 350, 75))
        font_lhs = QFont()  # LHS stands for "Label Harness Status"
        font_lhs.setFamily(u"Calibri")
        font_lhs.setPointSize(37)
        font_lhs.setBold(True)
        self.label_harness_status.setFont(font_lhs)
        """VERY TEMPORARY"""
        self.label_harness_status.setText("Harness NOK")
        self.label_harness_status.setStyleSheet("color: #000000;"
                                                "background-color: None;"
                                                     "border-radius: 75px;")

        # The label for the Order Number
        self.label_oder_number = QLabel(self.column_checking)
        self.label_oder_number.setObjectName("label_oder_number")
        self.label_oder_number.setGeometry(QRect(92, 895, 930, 100))
        font_lon = QFont()  # LON stands for "Label Order Number"
        font_lon.setFamily(u"Calibri")
        font_lon.setBold(True)
        font_lon.setPointSize(80)
        font_lon.setBold(False)
        self.label_oder_number.setFont(font_lon)
        self.label_oder_number.setStyleSheet("color: white;"
                                             "background-color: None;")
        """VERY TEMPORARY"""
        self.label_oder_number.setText("B0008798077")
        """VERY TEMPORARY"""