import sqlite3
from jsonload import *





def create_table():
    connection = sqlite3.connect("myDB.db")
    cursor = connection.cursor()
    sql_command: str = ("CREATE TABLE IF NOT EXISTS tasks (  \n"
                   "    id INTEGER PRIMARY KEY,  \n"
                   "    task VARCHAR(50),  \n"
                   "    notes VARCHAR(100),  \n"
                   "    username VARCHAR(30),\n"
                   "    fullname VARCHAR(30),\n"
                   "    completed INTEGER,\n"
                   "    subtasks INTEGER)")
    cursor.execute(sql_command)
    connection.commit()
    connection.close()

def insert(values: dict):
    connection = sqlite3.connect("myDB.db")
    cursor = connection.cursor()
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
    connection.commit()
    connection.close()


def delete(id: int):
    connection = sqlite3.connect("myDB.db")
    cursor = connection.cursor()
    sql_command: str = "DELETE from tasks where id='{}'".format(id)
    cursor.execute(sql_command)
    connection.commit()
    connection.close()

def deleteall():
    connection = sqlite3.connect("myDB.db")
    cursor = connection.cursor()
    sql_command: str = "DELETE from tasks"
    cursor.execute(sql_command)
    connection.commit()
    connection.close()

def mark_complete(id: int):
    connection = sqlite3.connect("myDB.db")
    cursor = connection.cursor()
    sql_command = "UPDATE tasks SET completed = 1 where id='{}'".format(id)
    cursor.execute(sql_command)
    connection.commit()
    connection.close()


def showall():
    connection = sqlite3.connect("myDB.db")
    cursor = connection.cursor()
    sql_command: str = "SELECT * FROM tasks"
    cursor.execute(sql_command)
    all = cursor.fetchall()
    for i in all:
        print(i)
    connection.commit()
    connection.close()


def showall_incomp():
    connection = sqlite3.connect("myDB.db")
    cursor = connection.cursor()
    sql_command: str = "SELECT * FROM tasks WHERE completed = 0"
    cursor.execute(sql_command)
    all = cursor.fetchall()
    for i in all:
        print(i)
    connection.commit()
    connection.close()


