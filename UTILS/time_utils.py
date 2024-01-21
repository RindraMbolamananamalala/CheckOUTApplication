# -*- coding: utf-8 -*-

"""
time_utils.py: The python file dedicated to the implementation of any need of Time information anywhere in the
Project.
"""

__author__ = "Rindra Mbolamananamalala"
__email__ = "rindraibi@gmail.com"

from datetime import date, datetime, timedelta


def get_current_date(date_format: str):
    """

    :param date_format: The format in which the date is wanted to be written
    :return: the current date
    """
    current_date = date.today().strftime(date_format)
    return current_date


def get_current_time(time_format: str):
    """

    :param time_format: The format in which the time is wanted to be written
    :return: the current time
    """
    current_time = datetime.now().strftime(time_format)
    return current_time


def is_a_date_a_week_end_date(date_to_be_determined: datetime):
    """

    :param date_to_be_determined: The date do be determined (Weekend date or not?)
    :return: True if the given date is a Weekend date, False otherwise.
    """
    return date_to_be_determined.isoweekday() > 5


def get_first_non_weekend_date_backwards(starting_date: datetime):
    """
    Getting the first Non-Weekend date (backwards) from a given date
    :param starting_date: The date from which the determination process will start
    :return: The first Non-Weekend date (backwards) from a given date
    """
    if not is_a_date_a_week_end_date(starting_date):
        # The date itself is already a Non-Weekend date, so let's return it
        return starting_date
    else:
        # We have to find another date (backwards)
        date_1 = starting_date - timedelta(days=1)
        date_2 = date_1 - timedelta(days=1)
        if not is_a_date_a_week_end_date(date_1):
            # Starting Date minus one is already a Non-Weekend date..;
            return date_1
        else:
            # Date minus one not yet a Non-Weekend date, so Date minus two is logically the chosen one...
            return date_2


def get_date_day_name(date_concerned: datetime):
    """
    Getting the name of a given date.
    :param date_concerned: The date the name of which has to be determined
    :return: The name of the given date.
    """
    return date_concerned.strftime("%A")
