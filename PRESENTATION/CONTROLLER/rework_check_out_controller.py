# -*- coding: utf-8 -*-

"""
rework_check_out_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented
within the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from CONFIGURATIONS.logger import LOGGER
from CONFIGURATIONS.settings_properties import get_settings_property

from PRESENTATION.VIEW.barcode_scan_view import BarcodeScanView
from PRESENTATION.VIEW.quality_inspector_code_scan_view import QualityInspectorCodeScanView
from PRESENTATION.VIEW.test_report_result_view import TestReportResultView

from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.rework_check_out_as_intf import ReworkCheckOUTASIntf
from BUSINESS.SERVICE.APPLICATION_SERVICE.IMPL.rework_check_out_as_impl import ReworkCheckOUTASImpl


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

    def set_rework_check_out_as(self, rework_check_out_as: ReworkCheckOUTASIntf):
        """

        :param rework_check_out_as: The Rework Check OUT Application Service component to be used by the current
        Controller
        :return: None
        """
        self.rework_check_out_as = rework_check_out_as

    def get_rework_check_out_as(self) -> ReworkCheckOUTASIntf:
        """

        :return: The Rework Check OUT Application Service component used by the current Controller
        """
        return self.rework_check_out_as

    def set_order_number_currently_treated(self, order_number_currently_treated: str):
        """

        :param order_number_currently_treated: The Order Number currently treated
        :return:
        """
        self.order_number_currently_treated = order_number_currently_treated

    def get_order_number_currently_treated(self) -> str:
        """

        :return: The Order Number currently treated
        """
        return self.order_number_currently_treated

    def set_pft_files_folder_path(self, pft_files_folder_path: str):
        """

        :param pft_files_folder_path: The path leading to the PFT Files
        :return: None
        """
        self.pft_files_folder_path  = pft_files_folder_path

    def get_pft_files_folder_path(self) -> str:
        """

        :return: The path leading to the PFT Files
        """
        return self.pft_files_folder_path

    def set_pft_test_reports_folder_path(self, pft_test_reports_folder_path: str):
        """

        :param pft_test_reports_folder_path: The path leading to the Folder dedicated to the Test Reports
        :return: None
        """
        self.pft_test_reports_folder_path = pft_test_reports_folder_path

    def get_pft_test_reports_folder_path(self) -> str:
        """

        :return: The path leading to the Folder dedicated to the Test Reports
        """
        return self.pft_test_reports_folder_path

    def set_list_pft_station_names(self, list_pft_station_names: list):
        """

        :param list_pft_station_names: The list of PFT Stations' names
        :return: None
        """
        self.list_pft_station_names = list_pft_station_names

    def get_list_pft_station_names(self) -> list:
        """

        :return: The list of PFT Stations' names
        """
        return self.list_pft_station_names

    def set_list_quality_inspector_codes(self, list_quality_inspector_codes: list):
        """

        :param list_quality_inspector_codes: The list of Quality Inspector Codes
        :return: None
        """
        self.list_quality_inspector_codes = list_quality_inspector_codes

    def get_list_quality_inspector_codes(self) -> list:
        """

        :return: The list of Quality Inspector Codes
        """
        return self.list_quality_inspector_codes

    def __init__(self):
        # First, let's initialize all the View components to be used by the current Controller
        self.set_barcode_scan_view(BarcodeScanView())
        self.set_quality_inspector_code_scan_view(QualityInspectorCodeScanView())
        self.set_test_report_result_view(TestReportResultView())

        # Then, let's load all the Settings' properties from the corresponding .INI file
        self.set_pft_files_folder_path(get_settings_property("pft_files_folder_path"))
        self.set_pft_test_reports_folder_path(get_settings_property("pft_test_reports_folder_path"))
        self.set_list_pft_station_names(get_settings_property("list_pft_station_names").split(","))
        self.set_list_quality_inspector_codes(get_settings_property("list_quality_inspector_codes").split(","))

        # Now, Let's initialize the Application Service component used by the same Controller
        self.set_rework_check_out_as(ReworkCheckOUTASImpl())

        # Let's manage all the events
        self.manage_events()

        # Now, let's start the Check OUT...
        self.start_check_out()

    def manage_events(self):
        barcode_scan_window = self.get_barcode_scan_view().get_ui_barcode_scan()

        # Events related to the Text Area dedicated to the Scan of a Barcode of Order Number
        barcode_scan_window.get_text_barcode().textChanged.connect(self.manage_scan_barcode)

    def start_check_out(self):
        """
        Starting the Check Out Process, let's remind that the first step is the scan of the Barcode
        :return: None
        """
        # The first window to display is that of the Barcode Scan...
        self.get_barcode_scan_view().show_window()

    def manage_scan_barcode(self):
        """
        Identifying if a complete string for an Order Number is present within the Barcode being scanned, and then
        launching the actual Check OUT Process
        :return: None
        """
        try:
            barcode_scan_window = self.get_barcode_scan_view().get_ui_barcode_scan()
            current_barcode_text = barcode_scan_window.get_text_barcode().toPlainText()
            if len(current_barcode_text) > 0:
                # First, reinitializing the appearance of the Barcode Scan Window
                self.get_barcode_scan_view().reinitialize_window_appearance()
                if "\n" in current_barcode_text:
                    # A complete string for an Order Number was found.. It's the Order Number to be treated
                    # ... and then, let's launch the actual check out process...
                    actual_barcode_scanned_raw = current_barcode_text.split("\n")[0]
                    self.set_order_number_currently_treated(actual_barcode_scanned_raw)
                    actual_barcode_scanned = actual_barcode_scanned_raw[1:]  # getting rid of the first character...
                    self.launch_actual_check_out_process(actual_barcode_scanned)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Barcode Management. "
            )
            raise

    def launch_actual_check_out_process(self, barcode_scanned: str):
        """
        Launching the actual process related to the checking out process.
        The first part of it is determining whether or not the Barcode being currently scanned is a valid one.
        Otherwise: Let's inform the User that the Barcode being scanned is a wrong one, so he/she needs to re-scan again
        :param barcode_scanned: The Barcode scanned corresponding to the Order Number concerned
        :return: None
        """
        try:
            barcode_scan_view = self.get_barcode_scan_view()
            barcode_validity = self.get_rework_check_out_as().is_barcode_valid(barcode_scanned)
            if not barcode_validity:
                # No line has been retrieved... let's notify the user that the Barcode Scanned is a wrong one
                barcode_scan_view.notify_wrong_barcode()
                LOGGER.info("The Barcode Scanned \"" + barcode_scanned + "\" is a wrong one")
            else:
                # Defect Line(s) have been retrieved...
                LOGGER.info(
                    "The Barcode Scanned \"" + barcode_scanned + "\" is a valid one"
                )
                # we're going to launch the Check Out treatment in function of the nature of the different processes
                """TEMPORARY, we'll work on it latter when the right time will come..."""
                # self.launch_defects_presentation(lines_retrieved)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Defects Lines Retrieval Process. "
            )
            raise