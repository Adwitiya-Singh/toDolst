import json
import sqlite3


def flatten_dict(nested_dict: dict, final_dict: dict):
        for k, v in nested_dict.items():
            if isinstance(v, dict):
               flatten_dict(v, final_dict)
            else:
                final_dict[k] = v


def pop_temp(template: dict, request_dict: dict):
    for k, v in template.items():
        if isinstance(v, dict):
            pop_temp(v, request_dict)
        else:
            if isinstance(v, str):
                template[k] = v.format(**request_dict)


def get_cursor(name: str = "tasks.db"):
    connection = sqlite3.connect(name)
    cursor = connection.cursor()
    return cursor


def create_table():
    sql_command = ("CREATE TABLE tasks (  \n"
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
    flat_values = {}
    flatten_dict(values, flat_values)
    if flat_values['completed']:
        flat_values['completed'] = 1
    else:
        flat_values['completed'] = 0
    sql_command = """INSERT INTO tasks VALUES ("{id}", "{task}", "{notes}", "{username}", "{fullname}", 
    "{completed}", "{subtasks}");""".format(**flat_values)
    cursor = get_cursor()
    cursor.execute(sql_command)


def delete(id: int):
    sql_command = "DELETE from Student where id='{id}'".format(id)
    cursor = get_cursor()
    cursor.execute(sql_command)


def showall():
    cursor = get_cursor();
    cursor.execute("SELECT * FROM tasks")
    all = cursor.fetchall()
    for i in all:
        print(i)


def showall_incomp():
    cursor = get_cursor();
    cursor.execute("SELECT * FROM tasks WHERE completed = 0")
    all = cursor.fetchall()
    for i in all:
        print(i)


with open('sample_request.json', 'r') as myfile:
    data = myfile.read()

obj: dict = json.loads(data)

flat: dict = {}
flatten_dict(obj, flat)

data: dict = json.loads(open('sample_template.json').read())

pop_temp(data, flat)


with open('responseOther.json', 'w') as outfile:
    json.dump(data, outfile, indent='\t')


