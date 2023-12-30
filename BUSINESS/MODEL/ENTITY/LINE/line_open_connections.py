# -*- coding: utf-8 -*-

"""
line_open_connections.py: The python file dedicated to the "Model:Entity:LineOpenConnections"  implemented
within the "BUSINESS" layer of the Project, and at the same time one of the Project's Entity
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, Date

from CONFIGURATIONS.application_properties import get_application_property

from DATA_ACCESS.data_access_base import Data_Access_Base

from BUSINESS.MODEL.ENTITY.rework_check_out_application_entity import ReworkCheckOUTEntity


class LineOpenConnections(Data_Access_Base, ReworkCheckOUTEntity):
    __tablename__ = get_application_property("db_line_open_connections_table_name")
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    calendarWeek = Column(String)
    station_name = Column(String)
    orderNumber = Column(String)
    module = Column(String)
    wire_name = Column(String)
    cross_section = Column(DECIMAL(10, 2))
    position1 = Column(String)
    cavity1 = Column(String)
    position2 = Column(String)
    cavity2 = Column(String)
    color = Column(String)
    defect_code = Column(String)
    nok_position = Column(String)
    comment = Column(String)
    status = Column(Integer)
