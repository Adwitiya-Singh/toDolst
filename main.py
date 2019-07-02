import json


def getval(nested_dict: dict, key: str) -> str:
    vals = key.split()
    x = ""
    for val in vals:
        val.replace(" ", "")
        if(val[0]=='{'):
            val = val[1:len(val) - 1]
        for k, v in nested_dict.items():
            if k == val:
                x += v
            elif isinstance(v, dict):
                x += getval(v, val) + " "

    return x


def poptemp(template: dict, request_dict: dict):
    for k, v in template.items():
        if hasattr(v, 'items'):
            poptemp(v, request_dict)
        else:
            if isinstance(v, str):
                template[k] = getval(request_dict, v)


# read file
with open('sample_request.json', 'r') as myfile:
    data = myfile.read()

# parse file
obj = json.loads(data)

data = json.loads(open('sample_template.json').read())

poptemp(data, obj)

# print(data)


with open('response.json', 'w') as outfile:
    json.dump(data, outfile, indent='\t')
