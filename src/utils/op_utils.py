import json

def load_json(file):
    with open(file, 'r') as f:
        a = json.load(f)
    return a

def save_json(obj, file, indent=4, sort_keys=True):
    with open(file, 'w') as f:
        json.dump(obj, f, sort_keys=sort_keys, indent=indent)