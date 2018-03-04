import json

if __name__ == '__main__':
    with open('../examples/energy.json') as json_data:
        d = json.load(json_data)
        print(d['energy']['start'])
