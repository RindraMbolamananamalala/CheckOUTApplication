# -*- coding: utf-8 -*-

"""
rework_check_out_application_file_dao_intf.py: The python file dedicated to the Abstract Base Class of the Data Access
Object (DAO) for any need of CRUD to any classical File by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import datetime
from abc import ABC, abstractmethod


class ReworkCheckOUTApplicationFileDAOIntf(ABC):

    @abstractmethod
    def get_list_concerned_processes_within_dedicated_file(self, ini_name: str) -> list:
        """

        :param ini_name: The name of the .ini file dedicated for the processes
        :return: The list of all the concerned processes contained within a given .ini file dedicated for them
        """
        return

    @abstractmethod
    def get_part_process_status(self, part_test_reports_file_path: str) -> str:
        """
        Determining the status of a PART process, which Test Reports file's path has been given in the arguments
        :param part_test_reports_file_path: The path leading to the Test Reports file corresponding to the concerned
        PART
        :return: the status of a so-called PART process within its corresponding file
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
    def read_prn_file_content(self, prn_file_path: str) -> str:
        """
        Reading and returning the whole content of a given .prn file
        :param: prn_file_path : The path leading to the .prn file
        :return: None
        """
        return

    @abstractmethod
    def write_inside_prn_file(self, prn_file_path: str, content: str) -> None:
        """
        Writing a text inside a given .prn file
        :param: prn_file_path : The path leading to the .prn file
        :param: content: The content to be written
        :return: None
        """
        pass