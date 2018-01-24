#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Used to build objects from args.
from pytodo.utils import misc


def _list(parser, projects, tasks):
    '''
    Add List subcomand to the parser
    '''
    # Add subcomands
    help = 'List all projects or tasks'
    subparsers = parser.add_subparsers(help=help)

    # Add sub-comand projects
    help = 'List all projects'
    parser_projects = subparsers.add_parser('projects', help=help)
    parser_projects.set_defaults(callback=projects)

    # Add sub-comand ptasks
    help = 'List tasks per project'
    parser_tasks = subparsers.add_parser('tasks', help=help)
   
    help = 'List all task for the target project'
    parser_tasks.add_argument('--project', type=str, help=help)
    parser_tasks.set_defaults(callback=tasks)

    # add subcommand tasks
    # help = 'List all tasks'
    # parser_tasks = subparsers.add_parser('tasks', help=help) 
    # parser_tasks.set_defaults(callback=all_tasks)


def _add_project(parser):
    '''
    Add Project specifier options to the parser.
    '''
    # Add project.
    help = 'project name'
    parser.add_argument('--name',  type=str, help=help)

    help = 'project description'
    parser.add_argument('--desc',  type=str, help=help)

    help = 'the project deadline'
    parser.add_argument('--deadline', type=misc.date, help=help)


def _add_task(parser):
    '''
    Add Task specifier options to the parser.
    '''
    # Add Task
    help = 'project name'
    parser.add_argument('--project',  type=str, help=help)

    help = 'task detail'
    parser.add_argument('--detail',  type=str, help=help)

    help = 'task status'
    parser.add_argument('--status',  type=str, help=help)

    help = 'the task deadline'
    parser.add_argument('--deadline', type=misc.date, help=help)

    help = 'task priority'
    parser.add_argument('--priority', type=int, help=help)


def _delete(parser):
    '''
    '''
    # delete Task
    help='a valid Task Id'
    parser.add_argument('--taskid', type=int, help=help)


def loglevel(parser, default='info'):
    '''
    Adds a log level to the parser.
    '''
    # Sanitize arguments.
    assert default in misc.LEVELS

    # Set the level.
    help = 'The log level.'
    choices = misc.LEVELS.keys()
    parser.add_argument('-L', '--loglevel', type=str, help=help,
                        choices=choices, default=default)

