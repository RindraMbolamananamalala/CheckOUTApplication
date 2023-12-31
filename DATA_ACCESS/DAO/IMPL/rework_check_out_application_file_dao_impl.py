# -*- coding: utf-8 -*-

"""
rework_check_out_application_file_dao_impl.py: The python file dedicated to the Implementation Class of the Data Access
Object (DAO) for any need of CRUD to any classical File by the Application.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import configparser

from CONFIGURATIONS.logger import LOGGER
from CONFIGURATIONS.application_properties import get_application_property

from DATA_ACCESS.DAO.INTF.rework_check_out_application_file_dao_intf import ReworkCheckOUTApplicationFileDAOIntf


class ReworkCheckOUTApplicationFileDAOImpl(ReworkCheckOUTApplicationFileDAOIntf):

    def get_list_concerned_processes_within_dedicated_file(self, ini_name: str) -> list:
        """

        :param ini_name: The name of the .ini file dedicated for the processes
        :return: The list of all the concerned processes contained within a given .ini file dedicated for them
        """
        try:
            # first, let's get the entire path leading to the .ini file concerned
            ini_file_path = get_application_property("process_ini_file_folder_location") \
                            + "\\" \
                            + ini_name \
                            + ".ini"
            # then, let's read it...
            config = configparser.RawConfigParser()
            config.read(ini_file_path)
            # now, let's initialize the list to be returned...
            list_to_return = []
            # ...and fill it with the concerned processes
            # "Crimping"'s section
            try:
                if config["Crimping"] is not None:
                    list_to_return.append("Crimping")
                else:
                    # Normally it should not go here... but if so... just pass...
                    pass
            except:
                # The section needed is not within the .ini file... so... just pass
                pass
            # "Flat Board"'s section
            try:
                if config["Flat Board"] is not None:
                    list_to_return.append("Flat Board")
                else:
                    # Normally it should not go here... but if so... just pass...
                    pass
            except:
                # The section needed is not within the .ini file... so... just pass
                pass
            # "USW"'s section
            try:
                if config["USW"] is not None:
                    list_to_return.append("USW")
                else:
                    # Normally it should not go here... but if so... just pass...
                    pass
            except:
                # The section needed is not within the .ini file... so... just pass
                pass
            # "Part 1"'s section
            try:
                if config["Part 1"] is not None:
                    list_to_return.append("Part 1")
                else:
                    # Normally it should not go here... but if so... just pass...
                    pass
            except:
                # The section needed is not within the .ini file... so... just pass
                pass
            # "Part 2"'s section
            try:
                if config["Part 2"] is not None:
                    list_to_return.append("Part 2")
                else:
                    # Normally it should not go here... but if so... just pass...
                    pass
            except:
                # The section needed is not within the .ini file... so... just pass
                pass
            # "Part 3"'s section
            try:
                if config["Part 3"] is not None:
                    list_to_return.append("Part 3")
                else:
                    # Normally it should not go here... but if so... just pass...
                    pass
            except:
                # The section needed is not within the .ini file... so... just pass
                pass
            # "Part 4"'s section
            try:
                if config["Part 4"] is not None:
                    list_to_return.append("Part 4")
                else:
                    # Normally it should not go here... but if so... just pass...
                    pass
            except:
                # The section needed is not within the .ini file... so... just pass
                pass
            # "Part 5"'s section
            try:
                if config["Part 5"] is not None:
                    list_to_return.append("Part 5")
                else:
                    # Normally it should not go here... but if so... just pass...
                    pass
            except:
                # The section needed is not within the .ini file... so... just pass
                pass
            # "Part 6"'s section
            try:
                if config["Part 6"] is not None:
                    list_to_return.append("Part 6")
                else:
                    # Normally it should not go here... but if so... just pass...
                    pass
            except:
                # The section needed is not within the .ini file... so... just pass
                pass
            return list_to_return
        except Exception as exception:
            # At least one error has occurred, therefore, stop the process
            LOGGER.error(
                exception.__class__.__name__ + ": " + str(exception)
                + ". Can't go further with the Concerned Processes Retrieval Process. "
            )
            raise

