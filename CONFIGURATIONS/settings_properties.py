# -*- coding: utf-8 -*-

"""
settings_properties.py: The python file dedicated to the particular settings required by the Check OUT Application
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

import os
import configparser


# Fetching the path to the "settings.ini" file
project_root_folder_path = (os.path.abspath(".")).replace("/", "\\")
settings_ini_file_path = project_root_folder_path + "\\settings.ini"

# preparing the Configurations
config = configparser.RawConfigParser()
config.read(settings_ini_file_path)

# retrieving the chosen Profile
profile = config["PROFILE"]["value"]


def get_settings_property(property_key) -> str:
    """
    Getting an settings property from the latter's "property_key".

    :param property_key: The property key of the wanted property
    :return: The value of the wanted property
    """
    return config[profile][property_key]