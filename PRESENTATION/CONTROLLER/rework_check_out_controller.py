# -*- coding: utf-8 -*-

"""
rework_check_out_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented
within the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import sys

from CONFIGURATIONS.logger import LOGGER
from CONFIGURATIONS.settings_properties import get_settings_property

from PRESENTATION.VIEW.barcode_scan_view import BarcodeScanView
from PRESENTATION.VIEW.quality_inspector_code_scan_view import QualityInspectorCodeScanView
from PRESENTATION.VIEW.quality_inspector_code_verification_view import QualityInspectorCodeVerificationView
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

    def set_quality_inspector_code_verification_view(self
                                    , quality_inspector_code_verification_view: QualityInspectorCodeVerificationView):
        """

        :param quality_inspector_code_verification_view: The Quality Inspector Code Verification View to be used by
        the current Controller
        :return: None
        """
        self.quality_inspector_code_verification_view = quality_inspector_code_verification_view

    def get_quality_inspector_code_verification_view(self) -> QualityInspectorCodeVerificationView:
        """

        :return: The Quality Inspector Code Verification View used by the current Controller
        """
        return self.quality_inspector_code_verification_view

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
        self.set_quality_inspector_code_verification_view(QualityInspectorCodeVerificationView())
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
        """QIC stands for "Quality Inspector Code" """
        qic_scan_window = self.get_quality_inspector_code_scan_view().get_ui_quality_inspector_code_scan()
        qic_verification_window = self.get_quality_inspector_code_verification_view()\
                                        .get_ui_quality_inspector_code_verification()

        # Events related to the Text Area dedicated to the Scan of a Barcode of Order Number
        barcode_scan_window.get_text_barcode().textChanged.connect(self.manage_scan_barcode)

        # Events related to the Text Area dedicated to the Scan of the Quality Inspector Code
        qic_scan_window.get_text_barcode().textChanged.connect(self.manage_scan_qic)

        # Events related to the "OK" button of the Quality Inspector Code Verification window
        qic_verification_window.get_button_ok().clicked.connect(self.manage_qic_verification_ok_chosen)

        # Events related to the "Abort" button of the Quality Inspector Code Verification window
        qic_verification_window.get_button_abort().clicked.connect(self.manage_qic_verification_abort_chosen)

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

    def manage_scan_qic(self):
        """
        Identifying if a complete string for an Quality Inspector Code is present within the Barcode being scanned,
        and then verifying if the latter is a correct one or not
        :return: None
        """
        try:
            """QIC stands for "Quality Inspector Code" """
            qic_scan_window = self.get_quality_inspector_code_scan_view().get_ui_quality_inspector_code_scan()
            current_qic_text = qic_scan_window.get_text_barcode().toPlainText()
            if len(current_qic_text) > 0:
                # First, reinitializing the appearance of the Quality Inspector Code Scan Window
                self.get_barcode_scan_view().reinitialize_window_appearance()
                if "\n" in current_qic_text:
                    # A complete string for a QIC was found.. It's the QIC to be treated...
                    # ... and after that, let's verify if the latter is a correct one or not...
                    actual_qic_scanned = current_qic_text.split("\n")[0]
                    if actual_qic_scanned in self.get_list_quality_inspector_codes():
                        # The QIC is a correct one...
                        """VERY TEMPORARY"""
                        print(actual_qic_scanned + " is CORRECT!!!")
                        """VERY TEMPORARY"""
                    else:
                        # Let's close the current window...
                        self.get_quality_inspector_code_scan_view().close_window()
                        # ... and open that of the QIC verification...
                        self.get_quality_inspector_code_verification_view().show_window()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Barcode Management. "
            )
            raise

    def manage_qic_verification_ok_chosen(self):
        """
        The Button "Ok" is the chosen one within the Quality Inspector Code Verification window, therefore, we have to
        re-open the Scan Window once again
        :return: None
        """
        """QIC stands for "Quality Inspector Code" """
        # Closing the currently opened QIC verification window...
        self.get_quality_inspector_code_verification_view().close_window()
        # ... and re-opening that of the QIC scan (after re-initializing the appearance of it of course...)
        self.get_quality_inspector_code_scan_view().reinitialize_window_appearance()
        self.get_quality_inspector_code_scan_view().show_window()

    def manage_qic_verification_abort_chosen(self):
        """
        The Button "Abort" is the chosen one within the Quality Inspector Code Verification window, therefore, we have
        to stop the entire Application
        :return: None
        """
        """QIC stands for "Quality Inspector Code" """
        # Stopping the entire App...
        sys.exit()

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
                self.launch_processes_treatment()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Defects Lines Retrieval Process. "
            )
            raise

    def launch_processes_treatment(self):
        """
        Launching the specific Treatment related to all the concerned Processes
        :return: None
        """
        # The first step is to launch the specific Treatment related to the Quality Inspector code
        self.launch_quality_inspector_code_treatment()

    def launch_quality_inspector_code_treatment(self):
        """
        Launching the specific Treatment related to the Quality Inspector Code
        :return: None
        """
        # First, let us close the Window for the Order Number's barcode scan
        self.get_barcode_scan_view().close_window()
        # Then, let's open that of the Quality Inspector Code scan...
        self.get_quality_inspector_code_scan_view().show_window()
