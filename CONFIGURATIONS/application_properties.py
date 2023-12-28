# -*- coding: utf-8 -*-

"""
application_properties.py: The python file dedicated to the particular process of retrieving
the current Profile & current Profile's properties of the Project
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import os
import configparser


# Fetching the path to the "application.ini" file
project_root_folder_path = (os.path.abspath(".")).replace("/", "\\")
application_ini_file_path = project_root_folder_path + "\\application.ini"

# preparing the Configurations
config = configparser.RawConfigParser()
config.read(application_ini_file_path)

# retrieving the chosen Profile
profile = config["PROFILE"]["value"]


def get_application_property(property_key) -> str:
    """
    Getting an application's property from the latter's "property_key".

    :param property_key: The property key of the wanted property
    :return: The value of the wanted property
    """
    return config[profile][property_key]



