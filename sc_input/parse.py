import json
from .Parameter import Parameter

def get_input_parameters(input_file):
    return _parse_json(_open_json(input_file))

def _open_json(file):
    with open(file) as json_path:
        try:
            json_d = json.load(json_path)
        except ValueError:
            raise Exception("File provided is not valid json")
        return json_d

def _parse_json(json_d):
    return [Parameter(key, json_d[key]) for key in json_d]

if __name__ == '__main__':
    _parse_json(_open_json('../examples/energy.json'))
