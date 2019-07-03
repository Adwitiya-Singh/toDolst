import json


def flattendict(nested_dict: dict, final_dict: dict):
        for k, v in nested_dict.items():
            if isinstance(v, dict):
               flattendict(v, final_dict)
            else:
                final_dict[k] = v


def poptemp(template: dict, request_dict: dict):
    for k, v in template.items():
        if isinstance(v, dict):
            poptemp(v, request_dict)
        else:
            if isinstance(v, str):
                template[k] = v.format(**request_dict)


with open('sample_request.json', 'r') as myfile:
    data = myfile.read()

obj: dict = json.loads(data)

flat: dict = {}
flattendict(obj, flat)

data: dict = json.loads(open('sample_template.json').read())

poptemp(data, flat)

with open('responseOther.json', 'w') as outfile:
    json.dump(data, outfile, indent='\t')

