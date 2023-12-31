# -*- coding: utf-8 -*-

"""
rework_check_out_as_impl.py: The python file dedicated to the implementation class of the Application Service part
dedicated to any need of service by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from CONFIGURATIONS.logger import LOGGER

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