# -*- coding: utf-8 -*-

"""
rework_check_out_controller.py: The python file dedicated to the "Controller" part of the MVC pattern implemented
within the "PRESENTATION" layer of the Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import datetime
import os
import sys

from PyQt5 import QtTest

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
                                                     ,
                                                     quality_inspector_code_verification_view: QualityInspectorCodeVerificationView):
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
        self.pft_files_folder_path = pft_files_folder_path

    def get_pft_files_folder_path(self) -> str:
        """

        :return: The path leading to the PFT Files
        """
        return self.pft_files_folder_path

    def set_list_pft_test_reports_folder_paths(self, list_pft_test_reports_folder_paths: list):
        """

        :param list_pft_test_reports_folder_paths: The list of paths leading to the Folders dedicated to the Test
        Reports, respectively specific to the PARTS 1-2-2-4-5-6
        :return: None
        """
        self.list_pft_test_reports_folder_paths = list_pft_test_reports_folder_paths

    def get_list_pft_test_reports_folder_paths(self) -> list:
        """

        :return: The list of paths leading to the Folders dedicated to the Test Reports, respectively specifici to the
        PARTS 1-2-2-4-5-6
        """
        return self.list_pft_test_reports_folder_paths

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

    def set_list_concerned_processes(self, list_concerned_processes: list):
        """

        :param list_concerned_processes: The list of the Processes Concerned by the current session
        :return: None
        """
        self.list_concerned_processes = list_concerned_processes

    def get_list_concerned_processes(self) -> list:
        """

        :return: The list of the Processes Concerned by the current session
        """
        return self.list_concerned_processes

    def set_list_processes_labels_stylesheets(self, list_processes_labels_stylesheets: list):
        """

        :param list_processes_labels_stylesheets: The list of stylesheets corresponding respectively to each Process
        Label of the Test Report Result window.
        Stylesheet [0] <-> "Crimping"
        , Stylesheet [1] <-> "Flat Board"
        , Stylesheet [2] <-> "USW"
        , Stylesheet [3] <-> "Part 1"
        , Stylesheet [4] <-> "Part 2"
        , Stylesheet [5] <-> "Part 3"
        , Stylesheet [6] <-> "Part 4"
        , Stylesheet [7] <-> "Part 5"
        , Stylesheet [8] <-> "Part 6"
        :return: None
        """
        self.list_processes_labels_stylesheets = list_processes_labels_stylesheets

    def get_list_processes_labels_stylesheets(self) -> list:
        """

        :return: The list of stylesheets corresponding respectively to each Process
        Label of the Test Report Result window.
        Stylesheet [0] <-> "Crimping"
        , Stylesheet [1] <-> "Flat Board"
        , Stylesheet [2] <-> "USW"
        , Stylesheet [3] <-> "Part 1"
        , Stylesheet [4] <-> "Part 2"
        , Stylesheet [5] <-> "Part 3"
        , Stylesheet [6] <-> "Part 4"
        , Stylesheet [7] <-> "Part 5"
        , Stylesheet [8] <-> "Part 6"
        """
        return self.list_processes_labels_stylesheets

    def __init__(self):
        # First, let's initialize all the View components to be used by the current Controller
        self.set_barcode_scan_view(BarcodeScanView())
        self.set_quality_inspector_code_scan_view(QualityInspectorCodeScanView())
        self.set_quality_inspector_code_verification_view(QualityInspectorCodeVerificationView())
        self.set_test_report_result_view(TestReportResultView())

        # Then, let's load all the Settings' properties from the corresponding .INI file
        self.set_pft_files_folder_path(get_settings_property("pft_files_folder_path"))
        self.set_list_pft_test_reports_folder_paths([])  # First, let's just initialize it with a blank list...
        for i in range(1, 6 + 1):
            # ... and then fill it with the different parts that concern respectively the PARTS 1-2-3-4-5-6
            self.get_list_pft_test_reports_folder_paths().append(
                get_settings_property("pft_test_reports_part_" + str(i) + "_folder_path")
            )
        self.set_list_pft_station_names(get_settings_property("list_pft_station_names").split(","))
        self.set_list_quality_inspector_codes(get_settings_property("list_quality_inspector_codes").split(","))

        # Now, Let's initialize the Application Service component used by the same Controller
        self.set_rework_check_out_as(ReworkCheckOUTASImpl())

        # Let's manage all the events
        self.manage_events()

        # Now, let's start the first App Cycle
        self.start_cycle()

    def manage_events(self):
        barcode_scan_window = self.get_barcode_scan_view().get_ui_barcode_scan()
        """QIC stands for "Quality Inspector Code" """
        qic_scan_window = self.get_quality_inspector_code_scan_view().get_ui_quality_inspector_code_scan()
        qic_verification_window = self.get_quality_inspector_code_verification_view() \
            .get_ui_quality_inspector_code_verification()

        # Events related to the Text Area dedicated to the Scan of a Barcode of Order Number
        barcode_scan_window.get_text_barcode().textChanged.connect(self.manage_scan_barcode)

        # Events related to the Text Area dedicated to the Scan of the Quality Inspector Code
        qic_scan_window.get_text_barcode().textChanged.connect(self.manage_scan_qic)

        # Events related to the "OK" button of the Quality Inspector Code Verification window
        qic_verification_window.get_button_ok().clicked.connect(self.manage_qic_verification_ok_chosen)

        # Events related to the "Abort" button of the Quality Inspector Code Verification window
        qic_verification_window.get_button_abort().clicked.connect(self.manage_qic_verification_abort_chosen)

    def start_cycle(self):
        """
        Starting a (new) cycle of the Application
        :return: None
        """
        LOGGER.info("A new cycle of the Application has started")
        # First, let's give default values to the Stylesheets of all the Processes' labels within the dedicated window
        self.set_list_processes_labels_stylesheets([])
        process_label_default_stylesheet = self.get_test_report_result_view().get_ui_test_report_result() \
            .get_stylesheet_process_element_not_concerned()
        for i in range(0, 8 + 1):
            self.get_list_processes_labels_stylesheets().append(process_label_default_stylesheet)

        # Then, let's start the Check OUT...
        self.start_check_out()

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
                        LOGGER.info("The scanned Quality Inspector Code " + actual_qic_scanned + " is a correct one")
                        # ... so, first, let's close the window...
                        self.get_quality_inspector_code_scan_view().close_window()
                        # ... and proceed to the launch of the PART processes Test Reports Analysis
                        self.launch_part_processes_test_reports_analysis()
                    else:
                        # The QIC is a wrong one...
                        LOGGER.info("The scanned Quality Inspector Code " + actual_qic_scanned + " is a wrong one")
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
        # Before anything, let's get the list of concerned processes, in function of the Order Number being currently
        # treated
        self.set_list_concerned_processes(
            self.get_rework_check_out_as().get_list_concerned_processes_within_dedicated_file(
                self.get_order_number_currently_treated()
            )
        )
        LOGGER.info(
            "The processes concerned with the "
            + self.get_order_number_currently_treated() + ".ini file :"
            + str(self.get_list_concerned_processes())
        )
        # The first step is to launch the specific Treatment related to the Quality Inspector code...
        if "Crimping" in self.get_list_concerned_processes() \
                or "Flat Board" in self.get_list_concerned_processes() \
                or "USW" in self.get_list_concerned_processes():
            # At least one of the "Non-part" processes is concerned, so we can start the treatment...
            self.launch_quality_inspector_code_treatment()
        else:
            # At least one of the "Non-part" processes is concerned, so let's jump directly to the PART Processes
            # Test Reports Analysis (after closing the current window of course)
            self.get_barcode_scan_view().close_window()
            self.launch_part_processes_test_reports_analysis()

    def launch_quality_inspector_code_treatment(self):
        """
        Launching the specific Treatment related to the Quality Inspector Code
        :return: None
        """
        test_reports_result_window = self.get_test_report_result_view().get_ui_test_report_result()
        stylesheet_process_element_not_concerned = test_reports_result_window \
            .get_stylesheet_process_element_not_concerned()
        stylesheet_process_element_concerned = test_reports_result_window.get_stylesheet_process_element_concerned()
        # Only if "Crimping" or "Flat Board" or "USW" is present within the list of concerned processes
        if "Crimping" in self.get_list_concerned_processes():
            # First, let us close the Window for the Order Number's barcode scan...
            self.get_barcode_scan_view().close_window()
            # ... and add the "Crimping" label's appropriate stylesheet within the dedicated list...
            self.get_list_processes_labels_stylesheets()[0] = stylesheet_process_element_concerned
            # Then, let's open that of the Quality Inspector Code scan...
            self.get_quality_inspector_code_scan_view().show_window()
        else:
            if "Flat Board" in self.get_list_concerned_processes():
                # First, let us close the Window for the Order Number's barcode scan
                self.get_barcode_scan_view().close_window()
                # ... and add the "Flat Board" label's appropriate stylesheet within the dedicated list...
                self.get_list_processes_labels_stylesheets()[1] = stylesheet_process_element_concerned
                # Then, let's open that of the Quality Inspector Code scan...
                self.get_quality_inspector_code_scan_view().show_window()
            else:
                if "USW" in self.get_list_concerned_processes():
                    # First, let us close the Window for the Order Number's barcode scan
                    self.get_barcode_scan_view().close_window()
                    # ... and add the "USW" label's appropriate stylesheet within the dedicated list...
                    self.get_list_processes_labels_stylesheets()[2] = stylesheet_process_element_concerned
                    # Then, let's open that of the Quality Inspector Code scan...
                    self.get_quality_inspector_code_scan_view().show_window()
                else:
                    # None of the 3 particular processes is present within the list, so, let's just pass..
                    pass

    def launch_part_processes_test_reports_analysis(self):
        """
        Launching the Analysis of the Part Processes' tests reports
        :return: None
        """
        try:
            # first of all, let's prepare the first bunch of information & values that we will need
            actual_order_number = self.get_order_number_currently_treated()[1:]
            test_reports_result_window = self.get_test_report_result_view().get_ui_test_report_result()
            stylesheet_process_element_nok = test_reports_result_window.get_stylesheet_process_nok()
            stylesheet_process_element_ok = test_reports_result_window.get_stylesheet_process_ok()
            for i in range(1, 6 + 1):
                if ("Part " + str(i)) in self.get_list_concerned_processes():
                    # Only the concerned PARTs will be taken for this...
                    test_reports_folder_path = get_settings_property("pft_test_reports_part_" + str(i) + "_folder_path")
                    actual_test_reports_file_name = self.get_actual_test_reports_file_name(
                        actual_order_number
                        , test_reports_folder_path
                    )
                    actual_test_reports_file_path = test_reports_folder_path \
                                                    + "\\\\" \
                                                    + actual_test_reports_file_name + ".txt"
                    LOGGER.info("The file path of the Test Report to be treated is : " + actual_test_reports_file_path)
                    part_i_status = self.get_rework_check_out_as().is_part_process_status_ok(
                        actual_test_reports_file_path
                    )
                    # Updating the Stylesheets of all the processes' labels in function of all the recently-determined
                    # status
                    if part_i_status:
                        # OK status, label in GREEN
                        self.get_list_processes_labels_stylesheets()[2 + i] = stylesheet_process_element_ok
                    else:
                        # NOK status, label in RED
                        self.get_list_processes_labels_stylesheets()[2 + i] = stylesheet_process_element_nok
            # After all of this, it's time to launch the processes' test reports visualization
            self.launch_processes_test_reports_visualization()
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Test Reports' file name Retrieval Process. "
            )
            raise

    def get_actual_test_reports_file_name(self, actual_order_number, test_reports_folder_path: str) -> str:
        """
        Determining the name of the actual Test Reports' file to be used for the Check OUT in function of a given PART
        folder
        :param actual_order_number: The Actual order number for the treatment
        :param test_reports_folder_path: The concerned PART folder's path
        :return: The name of the actual Test Reports' file to be used for the Check OUT corresponding to the PART
        specified within the arguments (its folder's path)
        """
        try:
            # First of all, let's get the date when the last Check IN was made
            date_check_in = self.get_rework_check_out_as().get_last_check_in_date(
                self.get_order_number_currently_treated()
            )
            LOGGER.info(
                "Treating the current Check OUT session for the order number "
                + actual_order_number
                + " with the .INI file of the Check IN of "
                + str(date_check_in)
            )
            # Now, it's time to chose which Test Report file (file's name) will be concerned by the Treatment
            most_recent_test_report_file_date = datetime.datetime.strptime("0001 01 01", "%Y %m %d")  # Initializing the
            most_recent_test_report_file = None
            # date se selector with an initial value
            for file_name in os.listdir(test_reports_folder_path):
                if file_name.startswith(actual_order_number + "_"):
                    # Only the files which names begin with the current order number are concerned

                    # Getting the part dedicated to the date within the file name and converting it into an actual Date
                    file_date_str = file_name.split("_")[1].replace(".txt", "")
                    file_date_year_str = file_date_str[0:4]
                    file_date_month_str = file_date_str[4:6]
                    file_date_day_str = file_date_str[6:8]
                    file_date_hour_str = file_date_str[8:10]
                    file_date_min_str = file_date_str[10:12]
                    file_date_str_formatted = file_date_year_str + " " + file_date_month_str + " " + file_date_day_str \
                                              + " " + file_date_hour_str + " " + file_date_min_str
                    file_date = datetime.datetime.strptime(file_date_str_formatted, "%Y %m %d %H %M")
                    if file_date > date_check_in:
                        # Only the Test Report file with a date more recent than that of the check IN will be
                        # concerned...
                        # ... and only the most recent one will be kept...
                        if file_date > most_recent_test_report_file_date:
                            most_recent_test_report_file_date = file_date
                            most_recent_test_report_file = file_name
            if most_recent_test_report_file is not None:
                return most_recent_test_report_file.replace(".txt", "")
            raise Exception(
                "No valid Test report file corresponding to the order number "
                + self.get_order_number_currently_treated()
                + "has been found"
            )
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Test Reports' file name Retrieval Process. "
            )
            raise

    def launch_processes_test_reports_visualization(self):
        """
        Launching the Visualization step of the Processes' Tests Reports
        :return: None
        """
        # First, let's update all the stylesheets that correspond to each of the Processes' labels...
        test_report_result_view = self.get_test_report_result_view()
        test_report_result_window = test_report_result_view.get_ui_test_report_result()
        i = 0
        are_all_part_processes_status_ok = True
        for process_label in test_report_result_window.get_list_labels_rework_processes():
            stylesheet_to_apply = self.get_list_processes_labels_stylesheets()[i]
            process_label.setStyleSheet(stylesheet_to_apply)
            if stylesheet_to_apply == test_report_result_window.get_stylesheet_process_nok():
                # The current Part Process has a NOK status...
                are_all_part_processes_status_ok = (are_all_part_processes_status_ok and False)
            i = i + 1
        # ... then, let's give the text value to the label for the Harness status
        if are_all_part_processes_status_ok:
            # All the parts Status are OK
            test_report_result_window.get_label_harness_status().setText("Harness OK")
        else:
            # At least one part Status is Not OK
            test_report_result_window.get_label_harness_status().setText("Harness NOK")
        # Then, let's show the window..
        test_report_result_view.show_window()
        if not are_all_part_processes_status_ok:
            # If the status is a "Harness NOK", the windows is only appearing during 5 seconds, and then a new App's
            # cycle begins
            QtTest.QTest.qWait(4000)
            test_report_result_view.close_window()
            # Re-starting the cycle...
            self.start_cycle()



