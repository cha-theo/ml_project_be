import csv
import os
import pandas as pd
import logging 
from flask import Blueprint, jsonify, request



# find values for charts

a =1
b = [10,20,30,40]
df = pd.read_csv(os.getcwd() + '/repo/listings_preprocessed.csv', encoding="utf8")

max_price_per_room_type = []


#max price per room type
for x in df.groupby('room_type')['price'].max():
    max_price_per_room_type.append(x)

print(df.groupby('room_type')['price'].max().keys()[0])
#test chart to fill with values
charts = {
    "barChart": [{"Max price": df.groupby('room_type')['price'].max()[0],
                  "name": df.groupby('room_type')['price'].max().keys()[0],
                  "Mean price": round(df.groupby('room_type')['price'].mean()[0],2)},
                  {"Max price": df.groupby('room_type')['price'].max()[1],
                  "name": df.groupby('room_type')['price'].max().keys()[1],
                  "Mean price": round(df.groupby('room_type')['price'].mean()[1],2)},
                  {"Max price": df.groupby('room_type')['price'].max()[2],
                  "name": df.groupby('room_type')['price'].max().keys()[2],
                  "Mean price": round(df.groupby('room_type')['price'].mean()[2],2)},
                  {"Max price": df.groupby('room_type')['price'].max()[3],
                  "name": df.groupby('room_type')['price'].max().keys()[3],
                  "Mean price": round(df.groupby('room_type')['price'].mean()[3],2)},
                  ],
    "pieChart": [{"name": "Page A",
                "value": 1000},
                {"name": "Page A",
                "value": 1000},
                {"name": "Page A",
                "value": 1000}],

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



