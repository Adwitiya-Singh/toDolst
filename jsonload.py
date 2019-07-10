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

