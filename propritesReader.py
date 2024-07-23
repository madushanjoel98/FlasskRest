import json


def loadFilers():
    data = None
    with open('setting.json') as json_file:
        data = json.load(json_file)
    print(data)
    return data


def isSeucre():
    return loadFilers()["secure"]
