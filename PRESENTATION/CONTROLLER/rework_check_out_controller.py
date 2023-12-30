# -*- coding: utf-8 -*-

"""
rework_check_out_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented
within the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from PRESENTATION.VIEW.barcode_scan_view import BarcodeScanView
from PRESENTATION.VIEW.quality_inspector_code_scan_view import QualityInspectorCodeScanView
from PRESENTATION.VIEW.test_report_result_view import TestReportResultView


class ReworkCheckOUTController:

    def set_barcode_scan_view(self, barcode_scan_view: BarcodeScanView):
        """

        :param barcode_scan_view: The Barcode Scan View to be used by the current Controller
        :return: None
        """
        self.barcode_scan_view = barcode_scan_view

    def get_barcode_scan_view(self) -> BarcodeScanView:
        """

        :return: The Barcode Scan View used by the current Controller
        """
        return self.barcode_scan_view

    def set_quality_inspector_code_scan_view(self, quality_inspector_code_scan_view: QualityInspectorCodeScanView):
        """

        :param quality_inspector_code_scan_view: The Quality Inspector Code Scan View to be used by the current
        Controller
        :return: None
        """
        self.quality_inspector_code_scan_view = quality_inspector_code_scan_view

    def get_quality_inspector_code_scan_view(self) -> QualityInspectorCodeScanView:
        """

        :return: The Quality Inspector Code Scan View used by the current Controller
        """
        return self.quality_inspector_code_scan_view

    def set_test_report_result_view(self, test_report_result_view: TestReportResultView):
        """

        :param test_report_result_view: The Test Report View to be used by the current Controller
        :return: None
        """
        self.test_report_result_view = test_report_result_view

    def get_test_report_result_view(self) -> TestReportResultView:
        """

        :return: The Test Report View used by the current Controller
        """
        return self.test_report_result_view

    def __init__(self):
        # First, let's initialize all the View components to be used by the current Controller
        self.set_barcode_scan_view(BarcodeScanView())
        self.set_quality_inspector_code_scan_view(QualityInspectorCodeScanView())
        self.set_test_report_result_view(TestReportResultView())

        # The first window to display is that of the Barcode Scan...
        self.get_barcode_scan_view().show_window()
