#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from contextlib import contextmanager


# The log.
_log = logging.getLogger(__name__)


class ExpectedException(Exception):
    '''
    A certain number of exceptions can happen when todo is running. These
    exceptions are logged without a traceback to prompt the user when
    something wrong has occurred.
    '''


@contextmanager
def log():
    '''
    Traps, logs and suppresses exceptions. This manager should be called at
    the top level of the app. Note that suppressing exceptions can be bad for
    control flow, so use with caution.
    '''
    global _log

    try:
        yield

    except ExpectedException, exception:
        # Log an error with the known exception message.
        _log.error(str(exception))

    except Exception, exception:
        # Log a full traceback with an unexpected exception.
        _log.exception(str(exception))
