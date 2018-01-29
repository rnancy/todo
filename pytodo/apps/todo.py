#!/usr/bin/env python

import argparse
import logging
import os
import sys
from pytodo.utils import options, database, misc, exceptions
from pytodo.utils.database import Base, Project

# The log.
log = logging.getLogger(__name__)

engine, session = database.open_db_session()

DESCRIPTION = "Add new project to todo"


def add_project(args):
    '''
    '''
    log.info('Creating new todo project')
    
    # If the database does not exist create one
    if misc.db_is_new:
        # Create all tables in the engine
        Base.metadata.create_all(engine)
    
    name = args.name
    desc = args.desc
    deadline = args.deadline
    new_project = Project(name=name, description=desc, deadline=deadline)
    session.add(new_project)
    session.commit()

def main():
    '''
    '''
    with exceptions.log():
        # create the parser
        parser = argparse.ArgumentParser(DESCRIPTION)
        options.loglevel(parser)
        options._add_project(parser)

        # parse the argument and add the project
        args=parser.parse_args()
        misc.set_log_level(args.loglevel)
        add_project(args)
