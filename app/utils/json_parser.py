import json

def parse_json(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    if isinstance(data, list):
        return data
    elif isinstance(data, dict):
        return [data] 
    else:
        raise ValueError("Invalid JSON data format")
