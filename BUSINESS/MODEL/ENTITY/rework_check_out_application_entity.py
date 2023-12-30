# -*- coding: utf-8 -*-

"""
rework_check_out_application_entity.py: The python file dedicated to the super class of all the Project's Entities
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"


class ReworkCheckOUTEntity:

    def __str__(self) -> str:
        """

        :return:  a structure in which all Entity's attributes are presented besides their respective value(s)
        """
        return super.__str__(self) + " :" + str(vars(self))
