from json_data import *

import json

def  get_information(message):
    with open("json_data/info_shikoyat.json", "r") as file:
        data = json.load(file)
    print(data)