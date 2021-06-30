import json

def db_loads():
    with open("pateshestvenik.json", encoding="UTF-8") as f:
        return json.load(f)
db = db_loads()