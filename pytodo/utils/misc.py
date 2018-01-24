#!/usr/bin/env python

import sys
import os
import logging
from datetime import datetime
from pytodo.constants import DATE_FORMAT, LITE_DB_FILE

# check if database file exist
db_is_new = not os.path.exists(LITE_DB_FILE)


# The log.
log = logging.getLogger(__name__)

# Maps level names to their constant values.
LEVELS = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG,
}


def date(string):
    '''
    Converts a string parameter into a date and back again to validate it.
    '''
    # Parse and validate the date.
    date = datetime.strptime(string, DATE_FORMAT).date()
    #return date.strftime(DATE_FORMAT)
    return date


def set_log_level(level):
    '''
    Set the log level using a string.
    '''
    logging.basicConfig(level=LEVELS[level])
