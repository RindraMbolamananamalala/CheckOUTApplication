# -*- coding: utf-8 -*-

"""
rework_check_out_application_mysql_dao_intf.py: The python file dedicated to the Abstract Base Class of the Data Access
Object (DAO) for any need of CRUD to MySQL Data Base by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from abc import ABC, abstractmethod


class ReworkCheckOUTApplicationMySQLDAOIntf(ABC):

    @abstractmethod
    def are_there_lines_wrong_routing(self, order_number: str) -> bool:
        """

        :param order_number: The Order Number from which all the Wrong Routing lines will be retrieved from DB
        :return: TRUE if there are Wrong Routine lines corresponding to the given Order Number in the DB,
        FALSE otherwise
        """
        return

    @abstractmethod
    def are_there_lines_open_connections(self, order_number: str) -> bool:
        """

        :param order_number: The Order Number from which all the Open Connections lines will be retrieved from DB
        :return: TRUE if there are Open Connections lines corresponding to the given Order Number in the DB,
        FALSE otherwise
        """
        return

    @abstractmethod
    def are_there_lines_extra_connections(self, order_number: str) -> bool:
        """

        :param order_number: The Order Number from which all the Extra Connections lines will be retrieved from DB
        :return: TRUE if there are Extra Connections lines corresponding to the given Order Number in the DB,
        FALSE otherwise
        """
        return

    @abstractmethod
    def are_there_lines_additional_information(self, order_number: str) -> bool:
        """

        :param order_number: The Order Number from which all the Additional Information lines will be retrieved from DB
        :return: TRUE if there are Additional Information lines corresponding to the given Order Number in the DB,
        FALSE otherwise
        """
        return