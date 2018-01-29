#!/usr/bin/env python
import os
import sys
import logging
from sqlalchemy import Sequence, Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pytodo.constants import LITE_DB

# The log.
log = logging.getLogger(__name__)

 
Base = declarative_base()
 
class Project(Base):
    __tablename__ = 'project'
    # Here we define columns for the table project
    # Notice that each column is also a normal Python instance attribute.
    name = Column(String(30), primary_key=True)
    description = Column(String(250), nullable=False)
    deadline = Column(Date, nullable=False)

    tasks = relationship('Task', backref='project')

    def __repr__(self):
        return "<Project (name='%s', description='%s', deadline='%s')>" % (
        self.name, self.description, self.deadline)
 
class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    priority = Column(Integer, default=1)
    status = Column(String(12), nullable=False)
    details = Column(String(250), nullable=False)
    deadline = Column(Date, nullable=False)
    completed_on =  Column(Date, nullable=True)
    project_name = Column(String(30), ForeignKey('project.name'), nullable = False)
    sqlite_autoincrement=True

   # project = relationship(Project)

    def __repr__(self):
        return '''<Task (id='%d', priority='%d', status='%s', details='%s',
        deadline='%s', completed_on='%s', project_name='%s')>''' % (self.id, self.priority, self.status, self.details, self.deadline, self.completed_on, self.project_name)


def open_db_session():
    '''
    '''
    log.info('Opening database session')

    # Create an engine that stores data
    engine = create_engine(LITE_DB)

    # Bind the engine to the metadata of the Base class so that the
    # declaratives can be accessed through a DBSession instance
    # Base.metadata.bind = engine
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)

    # A DBSession() instance establishes all conversations with the database
    # and represents a "staging zone" for all the objects loaded into the
    # database session object. Any change made against the objects in the
    # session won't be persisted into the database until you call
    # session.commit(). If you're not happy about the changes, you can
    # revert all of them back to the last commit by calling
    # session.rollback()
    session = DBSession()
    return engine, session
