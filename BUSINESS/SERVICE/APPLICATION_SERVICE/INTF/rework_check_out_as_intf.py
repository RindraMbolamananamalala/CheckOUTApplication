# -*- coding: utf-8 -*-

"""
rework_check_out_as_intf.py: The python file dedicated to the abstract class of the Application Service part
dedicated to any need of service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import datetime
from abc import ABC, abstractmethod


class ReworkCheckOUTASIntf(ABC):

    @abstractmethod
    def is_barcode_valid(self, barcode_scanned):
        """
        Determining whether a given Barcode (being scanned) is a valid one or not
        :param barcode_scanned: The Barcode being scanned
        :return: TRUE if the given Barcode is a valid one,
        FALSE otherwise
        """
        pass

    @abstractmethod
    def get_list_concerned_processes_within_dedicated_file(self, ini_name: str) -> list:
        """

        :param ini_name: The name of the .ini file dedicated for the processes
        :return: The list of all the concerned processes contained within a given .ini file dedicated for them
        """
        return

    @abstractmethod
    def is_part_process_status_ok(self, part_test_reports_file_path: str) -> bool:
        """
        Determining whether the status of a PART process, which Test Reports file's path has benn given in the arguments,
        is OK or not (NOK)
        :param part_test_reports_file_path: The path leading to the Test Reports file corresponding to the concerned PART
        :return: TRUE if the so-called status is OK,
        Otherwise FALSE.
        """
        return

    @abstractmethod
    def get_last_check_in_date(self, raw_order_number: str) -> datetime.datetime:
        """
        Getting the Date when the last check IN corresponding to a given order number has be realized
        :param raw_order_number: The concerned order number (in a raw format)
        :return: The Date when the last check IN corresponding to a given order number has been done
        """
        return

    @abstractmethod
    def launch_print_process(self, raw_order_number: str) -> None:
        """
        Launching the printing process
        :param raw_order_number: The concerned order number (in a raw format) that will be concerned by the current
        printing process
        :return: None
        """
        pass

    @abstractmethod
    def archive_ini_file(self, raw_order_number: str) -> None:
        """
        Archiving the .ini file corresponding to the Order Number specified within the arguments
        :param: raw_order_number: The Order Number, in a raw format, corresponding to the .ini file to be archived
        :return: None
        """
        pass