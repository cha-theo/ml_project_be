import csv
import os
import pandas as pd
import logging 
from flask import Blueprint, jsonify, request
import pickle

loaded_model = pickle.load(open('repo/finalized_model.sav', 'rb'))



# find values for charts
a =1
b = [10,20,30,40]
df = pd.read_csv(os.getcwd() + '/repo/listings_preprocessed.csv', encoding="utf8")

max_price_per_room_type = []


#max price per room type
for x in df.groupby('room_type')['price'].max():
    max_price_per_room_type.append(x)


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
                    "value": x},
                    {"name": "Page A",
                    "value": x},
                    {"name": "Page A",
                    "value": x}],

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


# we get the data from the form as dictionary and we return the best price based on our model
# Form dictionary values are(we will change these):
# textField 
# textField2 
# selectField
# multiplSelectField 
# radioField
# switchField

#here we can set the model function
def test_second_function(a,b,c):
    if c == True:
        z = int(a)+int(b)
    else: 
        z = 10000
    return z


#test inout dictionary values
dict = {'accommodates':[2],'beds':[2],'smoke_alarm':[0],'oven':[1],'patio_balcony':[1],'fire_extinguisher':[0],'shower_gel':[1]}
data2 = pd.DataFrame.from_dict(dict)
az = loaded_model.predict(data2)
print(az)


def test_function_with_data(data):
    #here we can assign the prices to the model and get the price
    a = test_second_function(data["textField"], data["textField2"], data["switchField"]) 
    data["textField"] = [int(data["textField"])]
    return ("The best price for your home is: {}".format(az))

# input fields for model function
# accommodates, beds, smoke_alarm, oven, patio_balcony, fire_extinguisher, shower_gel


