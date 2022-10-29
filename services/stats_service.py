import csv
import os
import pandas as pd
import logging 
from flask import Blueprint, jsonify, request



# find values for charts

a = "test text"
b = [10,20,30,40]


#test chart to fill with values
charts = {
    "barChart": [{"pv": a,
                 "uv": b[0],
                  "amt": 2400,
                  "name": "Page AAAAavvvvvvaAA"},
                 {"pv": b[1],
                 "uv": 4000,
                  "amt": 2400,
                  "name": "Page AAAAaaAA"}],

    "pieChart": [{"pv": 2400,
                 "uv": 4000,
                  "amt": 2400,
                  "name": "Page A"}],

    "areaChart": [{"pv": 2400,
                  "uv": 4000,
                   "amt": 2400,
                   "name": "Page A"}],

    "lineChart": [{"pv": 2400,
                  "uv": 4000,
                   "amt": 2400,
                   "name": "Page A"}]
}

def get_all_data():
    with open(os.getcwd() + '/repo/listings_preprocessed.csv', encoding="utf8") as raw_data_file:

        reader = csv.DictReader(raw_data_file)
        data_to_return = list(reader)

        return {
            "data": data_to_return,
            "meta": {
                "count": len(data_to_return)
            }
        }


def max_host_id():
    df = pd.read_csv(os.getcwd() + '/repo/listings_preprocessed.csv', encoding="utf8")
    return charts



