from typing import Dict
import sqlite3
from jsonload import *


def runsql(command: str) -> Dict:
    connection = sqlite3.connect("myDB.db")
    cursor = connection.cursor()
    cursor.execute(command)
    retval = cursor.fetchall()
    connection.commit()
    connection.close()
    return retval


def create_table():
    sql_command: str = ("CREATE TABLE IF NOT EXISTS tasks (  \n"
                   "    id INTEGER PRIMARY KEY,  \n"
                   "    task VARCHAR(50),  \n"
                   "    notes VARCHAR(100),  \n"
                   "    username VARCHAR(30),\n"
                   "    fullname VARCHAR(30),\n"
                   "    completed INTEGER,\n"
                   "    subtasks INTEGER)")
    runsql(sql_command)


def insert(values: dict):

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
    runsql(sql_command)


def delete(id: int):
    sql_command: str = "DELETE from tasks where id='{}'".format(id)
    runsql(sql_command)


def deleteall():
    sql_command: str = "DELETE from tasks"
    runsql(sql_command)


def mark_complete(id: int):
    sql_command: str = "UPDATE tasks SET completed = 1 where id='{}'".format(id)
    runsql(sql_command)


def showall():
    sql_command: str = "SELECT * FROM tasks"
    all = runsql(sql_command)
    for i in all:
        print(i)



def showall_incomp():
    sql_command: str = "SELECT * FROM tasks WHERE completed = 0"
    all = runsql(sql_command)
    for i in all:
        print(i)



