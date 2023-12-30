# -*- coding: utf-8 -*-

"""
rework_check_out_application_mysql_dao_impl.py: The python file dedicated to the Implementation Class of the Data Access
Object (DAO) for any need of CRUD to MySQL Data Base by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from sqlalchemy import and_

from CONFIGURATIONS.logger import LOGGER

from BUSINESS.MODEL.ENTITY.LINE.line_wrong_routing import LineWrongRouting
from BUSINESS.MODEL.ENTITY.LINE.line_open_connections import LineOpenConnections
from BUSINESS.MODEL.ENTITY.LINE.line_extra_connections import LineExtraConnections
from BUSINESS.MODEL.ENTITY.LINE.line_additional_information import LineAdditionalInformation

from DATA_ACCESS.data_access_base import Session
from DATA_ACCESS.DAO.INTF.rework_check_out_application_mysql_dao_intf import ReworkCheckOUTApplicationMySQLDAOIntf


class ReworkCheckOUTApplicationMySQLDAOImpl(ReworkCheckOUTApplicationMySQLDAOIntf):

    def are_there_lines_wrong_routing(self, order_number: str) -> bool:
        """

        :param order_number: The Order Number from which all the Wrong Routing lines will be retrieved from DB
        :return: TRUE if there are Wrong Routine lines corresponding to the given Order Number in the DB,
        FALSE otherwise
        """
        try:
            with Session() as session:
                results = session.query(LineWrongRouting).filter(
                    and_(
                        LineWrongRouting.orderNumber == order_number,
                        # Only the Old | Not yet Reworked lines will be fetched...
                        LineWrongRouting.status < 2
                    )
                )
                return results.count() > 0
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Defects Lines Retrieval Process. "
            )
            raise

    def are_there_lines_open_connections(self, order_number: str) -> bool:
        """

        :param order_number: The Order Number from which all the Open Connections lines will be retrieved from DB
        :return: TRUE if there are Open Connections lines corresponding to the given Order Number in the DB,
        FALSE otherwise
        """
        try:
            with Session() as session:
                results = session.query(LineOpenConnections).filter(
                    and_(
                        LineOpenConnections.orderNumber == order_number,
                        # Only the Old | Not yet Reworked lines will be fetched...
                        LineOpenConnections.status < 2
                    )
                )
                return results.count() > 0
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Defects Lines Retrieval Process. "
            )
            raise

    def are_there_lines_extra_connections(self, order_number: str) -> bool:
        """

        :param order_number: The Order Number from which all the Extra Connections lines will be retrieved from DB
        :return: TRUE if there are Extra Connections lines corresponding to the given Order Number in the DB,
        FALSE otherwise
        """
        try:
            with Session() as session:
                results = session.query(LineExtraConnections).filter(
                    and_(
                        LineExtraConnections.orderNumber == order_number,
                        # Only the Old | Not yet Reworked lines will be fetched...
                        LineExtraConnections.status < 2
                    )
                )
                return results.count() > 0
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Defects Lines Retrieval Process. "
            )
            raise

    def are_there_lines_additional_information(self, order_number: str) -> bool:
        """

        :param order_number: The Order Number from which all the Additional Information lines will be retrieved from DB
        :return: TRUE if there are Additional Information lines corresponding to the given Order Number in the DB,
        FALSE otherwise
        """
        try:
            with Session() as session:
                results = session.query(LineAdditionalInformation).filter(
                    and_(
                        LineAdditionalInformation.orderNumber == order_number,
                        # Only the Old | Not yet Reworked lines will be fetched...
                        LineAdditionalInformation.status < 2
                    )
                )
                return results.count() > 0
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Defects Lines Retrieval Process. "
            )
            raise

