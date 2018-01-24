#!/usr/bin/env python

from task import Task

class Project(object):
    """
    define a Todo project
    """

    def __init__(self, name, deadline):
            
            self.name = name
            self.deadline = deadline
            self.description = None
            self.tasks = [] 


    def set_name(self, name):
            self.name = name

    def set_deadline(self, deadline):
            self.deadline = deadline

    def set_description(self, description):
            self.description = description

    def add_task(self, priority, details, status, deadline):
            t_task = Task(priority, details, status, deadline, self)
            self.tasks.append(t_task)
