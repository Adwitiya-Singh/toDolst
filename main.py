
import json
from database import *
from jsonload import *



with open('sample_request.json', 'r') as myfile:
    data = myfile.read()

obj: dict = json.loads(data)

flat: dict = {}
flatten_dict(obj, flat)

data: dict = json.loads(open('sample_template.json').read())

pop_temp(data, flat)

create_table()
insert(data)
showall_incomp()
with open('responseOther.json', 'w') as outfile:
    json.dump(data, outfile, indent='\t')


