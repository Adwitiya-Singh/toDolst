from typing import Dict, Callable
import sqlite3
from jsonload import *
from functools import wraps


def uppermethod( message: str="working"):
    def _database_connector(func: Callable) -> object:
        @wraps(func)
        def connector(*args, **kwargs):
            connection = sqlite3.connect("myDB.db")
            print(message)
            cursor = connection.cursor()
            func(*args, **kwargs, cursor=cursor)
            connection.commit()
            connection.close()
        return connector
    return _database_connector

@uppermethod()
def create_table(cursor):
    sql_command: str = ("CREATE TABLE IF NOT EXISTS tasks (  \n"
                   "    id INTEGER PRIMARY KEY,  \n"
                   "    task VARCHAR(50),  \n"
                   "    notes VARCHAR(100),  \n"
                   "    username VARCHAR(30),\n"
                   "    fullname VARCHAR(30),\n"
                   "    completed INTEGER,\n"
                   "    subtasks INTEGER)")
    cursor.execute(sql_command)


@uppermethod()
def insert(values: Dict, *, cursor):
    flat_values: dict = {}
    flatten_dict(values, flat_values)
    if flat_values['completed'] == "True":
        flat_values['completed'] = 1
    else:
        flat_values['completed'] = 0
    if flat_values['subtasks'] is None:
        flat_values['subtasks'] = 0
    sql_command: str = """REPLACE INTO tasks VALUES (NULL, "{task}", "{notes}", "{username}", "{fullname}", 
    "{completed}", "{subtasks}")""".format(**flat_values)
    cursor.execute(sql_command)


@uppermethod(message="success")
def delete(id: int,  *, cursor):
    sql_command: str = "DELETE from tasks where id='{}'".format(id)
    cursor.execute(sql_command)


@uppermethod()
def deleteall(*, cursor):
    sql_command: str = "DELETE from tasks"
    cursor.execute(sql_command)


@uppermethod()
def mark_complete(id:int,  *, cursor):
    sql_command = "UPDATE tasks SET completed = 1 where id='{}'".format(id)
    cursor.execute(sql_command)


@uppermethod()
def showall(*, cursor):
    sql_command: str = "SELECT * FROM tasks"
    cursor.execute(sql_command)
    all = cursor.fetchall()
    for i in all:
        print(i)


@uppermethod()
def showall_incomp(*, cursor):
    sql_command: str = "SELECT * FROM tasks WHERE completed = 0"
    cursor.execute(sql_command)
    all = cursor.fetchall()
    for i in all:
        print(i)



