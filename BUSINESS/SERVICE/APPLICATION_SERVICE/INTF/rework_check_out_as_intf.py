# -*- coding: utf-8 -*-

"""
rework_check_out_as_intf.py: The python file dedicated to the abstract class of the Application Service part
dedicated to any need of service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from abc import ABC, abstractmethod


class ReworkCheckOUTASIntf(ABC):

    @abstractmethod
    def is_barcode_valid(self, barcode_scanned):
        """
        Determine whether a given Barcode (being scanned) is a valid one or not
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
