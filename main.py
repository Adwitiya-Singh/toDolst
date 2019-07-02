import json


def getpath(nested_dict, key):
    for k, v in nested_dict.items():
        if k == key:
            return v
        elif hasattr(v, 'items'):
            p = getpath(v, key)
            if p is not None:
                return p


# read file
with open('sample_request.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)


id = 1
data = json.loads(open('sample_template.json').read())

print(getpath(obj,'last'))

with open('response.json', 'w') as outfile:
        json.dump(data,outfile, indent='\t')
