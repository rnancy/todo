#!/usr/bin/env python

import argparse
import logging
import os
import sys
from pytodo.utils import options, database, misc, exceptions
from pytodo.utils.database import Base, Project, Task

# The log.
log = logging.getLogger(__name__)

engine, session = database.open_db_session()

DESCRIPTION = "Add new project and task to todo"


def add_project(args):
    '''
    '''
    log.info('Creating new todo project')
    
    # If the database does not exist create one
    if misc.db_is_new:
        # Create all tables in the engine
        Base.metadata.create_all(engine)
    
    new_project = Project(name=args.name, description=args.desc, deadline=args.deadline)
    session.add(new_project)
    session.commit()


def add_task(args):
        '''
        '''
        log.info('Adding new task in project: %s', args.project)

        project = session.query(Project).filter_by(name=args.project).first()
        new_task = Task(details=args.detail, status=args.status, deadline=args.deadline, 
                priority=args.priority, project=project)
        session.add(new_task)
        session.commit()


def main():
    '''
    '''
    with exceptions.log():
        # create the parser
        parser = argparse.ArgumentParser(DESCRIPTION)
        options.loglevel(parser)
        options._add(parser, add_project, add_task)

        # parse the argument and run the add command
        # callback can be either add_project or add_task
        args=parser.parse_args()
        misc.set_log_level(args.loglevel)
        args.callback(args)
