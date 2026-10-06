import json

def readjson():
   with open("tracker.json", "r") as file:
    return json.load(file)