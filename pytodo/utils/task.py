#!/usr/bin/env python

class Task(object):
    """
    Define a todo list task per project
    """
    STATUS = ('doing','waiting','done')

    def __init__(self, priority, details, status, deadline, project):
             if status not in self.STATUS:
                 raise ValueError("%s is not a valid status." % status)

             self.priority = 1
             self.details = details
             self.status = status
             self.deadline = deadline
             self.completed_on = None
             self.project = project

    def set_priority(self, priority):
             self.priority = priority

    def set_details(self, details):
             self.details = details

    def set_deadline(self, deadline):
             self.deadline = deadline

    def set_completed_on(self, completed_on):
             self.completed_on = completed_on
