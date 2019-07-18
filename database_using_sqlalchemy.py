from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from jsonload import *
from typedef import *
from typing import Dict, List

Base: AlchemyEngine = declarative_base()


class Task(Base):
    def __init__(self, id: int, task: str, notes: str, username: str, fullname: str, completed: int, subtasks: int):
        self.id: int = id
        self.task: str = task
        self.notes: str = notes
        self.username: str = username
        self.fullname: str = fullname
        self.completed: int = completed
        self.subtasks: int = subtasks

    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    notes = Column(String)
    username = Column(String)
    fullname = Column(String)
    completed = Column(Integer)
    subtasks = Column(Integer)


engine: AlchemyEngine = create_engine("sqlite:///sqlalchemy.db")
session: AlchemyFactory = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
s = session()


def insert(values: Dict):
    flat_values: Dict = {}
    flatten_dict(values, flat_values)
    if flat_values['completed'] == "True":
        flat_values['completed'] = 1
    else:
        flat_values['completed'] = 0
    if flat_values['subtasks'] is None:
        flat_values['subtasks'] = 0
    task = Task(id=None, task=flat_values["task"], notes=flat_values["notes"], username=flat_values["username"],
                fullname=flat_values["fullname"], completed=flat_values["completed"], subtasks=flat_values["subtasks"])
    s.add(task)
    s.commit()


def delete(id: int):
    tbd = s.query(Task).filter(Task.id == id)
    tbd.delete()
    s.commit()


def deleteall():
    s.query(Task).delete()
    s.commit()


def mark_complete(id: int):
    user = s.query(Task).filter(Task.id == id).first()
    setattr(user, 'completed', 1)
    s.commit()


def showall():
    tasks: List[Task] = s.query(Task).all()
    for task in tasks:
        print_task(task)
    s.commit()


def showall_incomp():
    tasks = s.query(Task).all()
    for task in tasks:
        if task.completed == 0:
            print_task(task)
    s.commit()


def print_task(t: Task):
    print("Id: "+str(t.id)+"\nTask: "+t.task+"\nNotes: "+t.notes+"\nUsername: "+t.username+"\nFull Name: "+t.fullname)
    print("Completed: ", end="")
    if t.completed==0:
        print("No")
    else:
        print("Yes")

    print("Subtasks: ", end="")
    if t.subtasks == 0:
        print("None")
    else:
        print(t.subtasks)
    print("\n\n")
