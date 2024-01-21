# -*- coding: utf-8 -*-

"""
rework_check_out_as_impl.py: The python file dedicated to the implementation class of the Application Service part
dedicated to any need of service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import datetime

from UTILS.time_utils import get_current_date, get_current_time

from CONFIGURATIONS.logger import LOGGER
from CONFIGURATIONS.application_properties import get_application_property

from BUSINESS.SERVICE.APPLICATION_SERVICE.INTF.rework_check_out_as_intf import ReworkCheckOUTASIntf

from DATA_ACCESS.DAO.INTF.rework_check_out_application_mysql_dao_intf import ReworkCheckOUTApplicationMySQLDAOIntf
from DATA_ACCESS.DAO.INTF.rework_check_out_application_file_dao_intf import ReworkCheckOUTApplicationFileDAOIntf

from DATA_ACCESS.DAO.IMPL.rework_check_out_application_mysql_dao_impl import ReworkCheckOUTApplicationMySQLDAOImpl
from DATA_ACCESS.DAO.IMPL.rework_check_out_application_file_dao_impl import ReworkCheckOUTApplicationFileDAOImpl


class ReworkCheckOUTASImpl(ReworkCheckOUTASIntf):

    def set_mysql_dao(self, mysql_dao: ReworkCheckOUTApplicationMySQLDAOIntf):
        """

        :param mysql_dao: The MySQL DAO component to be used by the current Application Service
        :return: None
        """
        self.mysql_dao = mysql_dao

    def get_mysql_dao(self) -> ReworkCheckOUTApplicationMySQLDAOIntf:
        """

        :return: The MySQL DAO component used by the current Application Service
        """
        return self.mysql_dao

    def set_file_dao(self, file_dao: ReworkCheckOUTApplicationFileDAOIntf):
        """

        :param file_dao: The File DAO component to be used by the current Application Service
        :return: None
        """
        self.file_dao = file_dao

    def get_file_dao(self) -> ReworkCheckOUTApplicationFileDAOIntf:
        """

        :return: The File DAO component used by the current Application Service
        """
        return self.file_dao

    def __init__(self):
        # Initializing the DAO components to be used by the Application Service
        self.set_mysql_dao(ReworkCheckOUTApplicationMySQLDAOImpl())
        self.set_file_dao(ReworkCheckOUTApplicationFileDAOImpl())

    def is_barcode_valid(self, barcode_scanned):
        """
        Determine whether a given Barcode (being scanned) is a valid one or not
        :param barcode_scanned: The Barcode being scanned
        :return: TRUE if the given Barcode is a valid one,
        FALSE otherwise
        """
        try:
            # A Barcode (Order Number) is valid when at least one line corresponding to it has been found
            # within the DB
            mysql_dao = self.get_mysql_dao()
            validity_wrong_routing = mysql_dao.are_there_lines_wrong_routing(barcode_scanned)
            validity_open_connections = mysql_dao.are_there_lines_open_connections(barcode_scanned)
            validity_extra_connections = mysql_dao.are_there_lines_extra_connections(barcode_scanned)
            validity_additional_information = mysql_dao.are_there_lines_additional_information(barcode_scanned)
            return validity_wrong_routing \
                   or validity_open_connections \
                   or validity_extra_connections \
                   or validity_additional_information
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Barcode's Validity determination process."
            )
            raise

    def get_list_concerned_processes_within_dedicated_file(self, ini_name: str) -> list:
        """

        :param ini_name: The name of the .ini file dedicated for the processes
        :return: The list of all the concerned processes contained within a given .ini file dedicated for them
        """
        return self.get_file_dao().get_list_concerned_processes_within_dedicated_file(ini_name)

    def is_part_process_status_ok(self, part_test_reports_file_path: str) -> bool:
        """
        Determining whether the status of a PART process, which Test Reports file's path has benn given in the arguments,
        is OK or not (NOK)
        :param part_test_reports_file_path: The path leading to the Test Reports file corresponding to the concerned PART
        :return: TRUE if the so-called status is OK,
        Otherwise FALSE.
        """
        part_process_status = self.get_file_dao().get_part_process_status(part_test_reports_file_path)
        return part_process_status == "OK"

    def get_last_check_in_date(self, raw_order_number: str) -> datetime.datetime:
        """
        Getting the Date when the last check IN corresponding to a given order number has be realized
        :param raw_order_number: The concerned order number (in a raw format)
        :return: The Date when the last check IN corresponding to a given order number has been done
        """
        try:
            # Fetching the value from the DAO
            return self.get_file_dao().get_last_check_in_date(raw_order_number)
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Last Check IN's Date fetching Process. "
            )
            raise

    def launch_print_process(self, raw_order_number: str) -> None:
        """
        Launching the printing process
        :param raw_order_number: The concerned order number (in a raw format) that will be concerned by the current
        printing process
        :return: None
        """
        try:
            # First, let's load the content of the .prn file's template for the print ...
            prn_file_template_path = get_application_property("prn_file_template_path")
            prn_file_template_content = self.get_file_dao().read_prn_file_content(prn_file_template_path)
            # Then, let's fill each variables inside it with their respective values
            prn_file_new_content = prn_file_template_content.replace("@VAR1@", raw_order_number)
            prn_file_new_content = prn_file_new_content.replace("@VAR2@", raw_order_number)
            current_date = get_current_date("%Y-%m-%d")
            current_time = get_current_time("%H:%M:%S")
            prn_file_new_content = prn_file_new_content.replace("@VAR3@", current_time)
            prn_file_new_content = prn_file_new_content.replace("@VAR4@", current_date)
            # After that, we have to create a copy of this template, and inside it we put the new version of the content
            self.get_file_dao().write_inside_prn_file(
                prn_file_template_path.replace(".prn", "_copy.prn"), prn_file_new_content
            )
            # Then, we have to call for the App.exe that will print this copy above
            """WE'LL work on it seriously later..."""
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the PRN file Printing Process. "
            )
            raise
