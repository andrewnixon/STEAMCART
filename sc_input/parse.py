import json
import parameter

def open_json(file):
    with open(file) as json_path:
        try:
            json_d = json.load(json_path)
        except ValueError:
            raise Exception("File provided is not valid json")
        return json_d

def parse_json(json_d):
    parameter_list = [parameter.Parameter(key, json_d[key]) for key in json_d]

if __name__ == '__main__':
    parse_json(open_json('../examples/energy.json'))
