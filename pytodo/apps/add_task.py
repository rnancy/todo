#!/usr/bin/env python

import argparse
import logging
import os
import sys
from pytodo.utils import options, database, misc, exceptions
from pytodo.utils.database import Base, Task, Project

# The log.
log = logging.getLogger(__name__)

engine, session = database.open_db_session()

DESCRIPTION = "Add new task to todo"


def add_task(args):
    '''
    '''
    log.info('Adding new task in project: %s', args.project)

    detail = args.detail
    status = args.status
    priority = args.priority
    project = session.query(Project).filter_by(name=args.project).first()
    deadline = args.deadline
    new_task = Task(details=detail, status=status, deadline=deadline,
            priority=priority, project=project)
    session.add(new_task)
    session.commit()

def main():
    '''
    '''
    with exceptions.log():
        # create the parser
        parser = argparse.ArgumentParser(DESCRIPTION)
        options.loglevel(parser)
        options._add_task(parser)

        # add the task
        args=parser.parse_args()
        misc.set_log_level(args.loglevel)
        add_task(args)
