import json
from typing import Dict


def flatten_dict(nested_dict: Dict, final_dict: Dict):
    for k, v in nested_dict.items():
        if isinstance(v, dict):
            flatten_dict(v, final_dict)
        else:
            final_dict[k] = v


def pop_temp(template: Dict, request_dict: Dict):
    for k, v in template.items():
        if isinstance(v, dict):
            pop_temp(v, request_dict)
        else:
            if isinstance(v, str):
                template[k] = v.format(**request_dict)


def jsonread(templatename: str, requestname: str) ->  Dict:
    with open(requestname, 'r') as myfile:
        data = myfile.read()
    obj: dict = json.loads(data)
    flat: dict = {}
    flatten_dict(obj, flat)
    data: dict = json.loads(open(templatename).read())
    pop_temp(data, flat)
    return data
