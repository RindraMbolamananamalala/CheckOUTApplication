# -*- coding: utf-8 -*-

"""
rework_check_out_application_file_dao_intf.py: The python file dedicated to the Abstract Base Class of the Data Access
Object (DAO) for any need of CRUD to any classical File by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from abc import ABC, abstractmethod


class ReworkCheckOUTApplicationFileDAOIntf(ABC):

    @abstractmethod
    def get_list_concerned_processes_within_dedicated_file(self, ini_name: str) -> list:
        """

        :param ini_name: The name of the .ini file dedicated for the processes
        :return: The list of all the concerned processes contained within a given .ini file dedicated for them
        """
        return