#!/usr/bin/env python

import argparse
import logging
import os
import sys
from pytodo.utils import options, database, misc, exceptions
from pytodo.utils.database import Task

# The log.
log = logging.getLogger(__name__)

engine, session = database.open_db_session()

DESCRIPTION ='''
Delete entries (project, task) of todo'''


def delete(args):
    '''
    '''
    log.info('Deleting todo entries')

    session.query(Task).filter(Task.id == args.taskid).delete(synchronize_session=False)
    session.commit()

def main():
    '''
    '''
    with exceptions.log():
        # create the parser
        parser = argparse.ArgumentParser(DESCRIPTION)
        options.loglevel(parser)
        options._delete(parser)

        # parse the argument and add the project
        args=parser.parse_args()
        misc.set_log_level(args.loglevel)
        delete(args)
