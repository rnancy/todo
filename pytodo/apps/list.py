#!/usr/bin/env python

import argparse
import logging
import os
import sys
from pytodo.utils import options, database, misc, exceptions
from pytodo.utils.database import Task, Project, Base
from prettytable import PrettyTable

# The log.
log = logging.getLogger(__name__)

DESCRIPTION = '''
List projects, tasks per project
'''

engine, session = database.open_db_session()

def list_projects(args):
    '''
    '''
    log.info('Listing all projects')
    
    project_list = PrettyTable()
    project_list.field_names = ['Name', 'Description', 'Deadline']
    
    for project in session.query(Project):
        project_list.add_row((project.name, project.description,
            project.deadline))
    print project_list
    
def list_project_tasks(args):
    '''
    '''
    log.info('Display the list of task for project: %s', args.project)
    
    list_doing = PrettyTable()
    list_todo = PrettyTable()
    list_done = PrettyTable()
    doing = []
    todo = []
    done = []
    project = session.query(Project).filter_by(name=args.project).first()
    for task in session.query(Task).filter(Task.project == project):
        if task.status == 'doing':
            doing.append(task.details)
        elif task.status == 'waiting':
            todo.append(task.details)
        else: done.append(task.details)

    # Display the list per status 
    if len(doing) > 0:
        list_doing.add_column('Doing', doing)
        print list_doing
    if len(todo) > 0:
        list_todo.add_column('Todo', todo)
        print list_todo
    if len(done) > 0: 
        list_done.add_column('Done', done)
        print list_done

def list_all_tasks(args):
    '''
    '''
    log.info('Listing all Tasks')

    tasks = PrettyTable(['TaskId','Project_name', 'Description',
        'Status', 'Deadline','Priority'])
    for task in session.query(Task).all():
        tasks.add_row((task.id, task.project.name, task.details, task.status,task.deadline, task.priority))
    
    print tasks
    

def list_tasks(args):
    '''
    '''
    log.info('Listing tasks')
    if args.project: list_project_tasks(args)
    else: list_all_tasks(args)


def main():
    '''
    '''
    with exceptions.log():
        # create the parser
        parser = argparse.ArgumentParser(DESCRIPTION)
        options.loglevel(parser)
        options._list(parser, list_projects, list_tasks)

        # process the argument and run the 
        # list commands
        # callback can be either list_projects or 
        # list_tasks
        args=parser.parse_args()
        misc.set_log_level(args.loglevel)
        args.callback(args)
