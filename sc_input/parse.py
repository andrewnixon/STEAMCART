import json

def open_json(file):
    with open(file) as json_path:
        try:
            json_d = json.load(json_path)
        except ValueError:
            raise Exception("File provided is not valid json")
        return json_d

def parse_json(json_d):
    for key in json_d:
        if not isinstance(json_d[key], dict):
            raise Exception("Likely that the JSON is not correct")

        print(key)
        #print("{}: {}".format(key, json_d[key]))

if __name__ == '__main__':
    parse_json(open_json('../examples/energy.json'))
