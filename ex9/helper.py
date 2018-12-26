############################################################
# FILE : helper.py
# WRITER : shay margolis , shaymar , 211831136
# EXERCISE : intro2cs1 ex9 2018-2019
# DESCRIPTION : helper functions
#############################################################

import json


def load_json(filename):
    json_file = filename
    with open(json_file, 'r') as file:
        car_config = json.load(file)
    # now car_config is a dictionary equivalent to the JSON file
    return car_config
