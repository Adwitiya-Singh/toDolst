from jsonload import *
from database_using_sqlalchemy import *


def dbtes():
    # create_table()
    data = jsonread("/Users/as74855/Documents/toDolst/sample_template.json", "/Users/as74855/Documents/toDolst/sample_request.json")

    insert(data)
    data = jsonread("/Users/as74855/Documents/toDolst/sample_template.json", "/Users/as74855/Documents/toDolst/sample_request_two.json")
    insert(data)
    showall()
    # showall_incomp()
    # mark_complete(2)
    # showall_incomp()
    # showall()
    # showall_incomp()
    # deleteall()
    # showall()
    # delete(2)
    # showall()
if __name__ == "__main__":
    dbtes()
