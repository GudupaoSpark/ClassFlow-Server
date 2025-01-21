import json

def read(file_path = "data/config.json"):
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def write(data,file_path="data/config.json"):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        pass

