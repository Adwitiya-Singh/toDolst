import sqlite3
from main import *


def get_cursor(name: str = "tasks.db"):
    connection = sqlite3.connect(name)
    cursor = connection.cursor()
    return cursor


def create_table():
    sql_command: str = ("CREATE TABLE tasks (  \n"
                   "    id INTEGER PRIMARY KEY,  \n"
                   "    task VARCHAR(50),  \n"
                   "    notes VARCHAR(100),  \n"
                   "    username VARCHAR(30),\n"
                   "    fullname VARCHAR(30),\n"
                   "    completed INTEGER,\n"
                   "    subtasks INTEGER;")
    cursor = get_cursor()
    cursor.execute(sql_command)


def insert(values: dict):
    flat_values: dict = {}
    flatten_dict(values, flat_values)
    if flat_values['completed']:
        flat_values['completed'] = 1
    else:
        flat_values['completed'] = 0
    sql_command: str = """INSERT INTO tasks VALUES ("{id}", "{task}", "{notes}", "{username}", "{fullname}", 
    "{completed}", "{subtasks}");""".format(**flat_values)
    cursor = get_cursor()
    cursor.execute(sql_command)


def delete(id: int):
    sql_command: str = "DELETE from Student where id='{id}'".format(id)
    cursor = get_cursor()
    cursor.execute(sql_command)

def mark_complete(id: int):
    sql_command = "UPDATE tasks SET completed = 1 where id='{id}'".format(id)
    cursor = get_cursor()
    cursor.execute(sql_command)


def showall():
    sql_command: str = "SELECT * FROM tasks"
    cursor = get_cursor();
    cursor.execute(sql_command)
    all = cursor.fetchall()
    for i in all:
        print(i)


def showall_incomp():
    sql_command: str = "SELECT * FROM tasks WHERE completed = 0"
    cursor = get_cursor(sql_command);
    cursor.execute()
    all = cursor.fetchall()
    for i in all:
        print(i)

