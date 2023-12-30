# -*- coding: utf-8 -*-

"""
    line_additional_information.py: The python file dedicated to the
    "Model:Entity:LineAdditionalInformation" implemented within the "BUSINESS" layer of the Project,
    and at the same time one of the Project's Entity
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, Date

from CONFIGURATIONS.application_properties import get_application_property

from DATA_ACCESS.data_access_base import Data_Access_Base

from BUSINESS.MODEL.ENTITY.rework_check_out_application_entity import ReworkCheckOUTEntity


class LineAdditionalInformation(Data_Access_Base, ReworkCheckOUTEntity):
    __tablename__ = get_application_property("db_line_additional_information_table_name")
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    calendarWeek = Column(String)
    station_name = Column(String)
    orderNumber = Column(String)
    comment = Column(String)
    status = Column(Integer)
