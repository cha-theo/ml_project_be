import csv
import os
import pandas as pd
import logging 
from flask import Blueprint, jsonify, request
import pickle


loaded_model = pickle.load(open('repo/finalized_model.sav', 'rb'))


# we get the data from the form as dictionary and we return the best price based on our model
# Form dictionary values are(we will change these):
# textField 
# textField2 
# selectField
# multiplSelectField 
# radioField
# switchField

# test: here we can set the model function
# def test_second_function(a,b,c):
#     if c == True:
#         z = int(a)+int(b)
#     else: 
#         z = 10000
#     return z


#test inout dictionary values
# dict = {'accommodates':[2],'beds':[2],'smoke_alarm':[0],'oven':[1],'patio_balcony':[1],'fire_extinguisher':[0],'shower_gel':[1]}
# data2 = pd.DataFrame.from_dict(dict)
# az = loaded_model.predict(data2)
# print(az)


def test_function_with_data(data):
    #here we can assign the values to the model and get the price
    dict = {'accommodates':[2],'beds':[2],'smoke_alarm':[0],'oven':[1],'patio_balcony':[1],'fire_extinguisher':[0],'shower_gel':[1]}
    
    
    data["accommodates"] = [int(data["accommodates"])]
    data["beds"] = [int(data["beds"])]
    data["smoke_alarm"] = [int(data["smoke_alarm"])]
    data["oven"] = [int(data["oven"])]
    data["patio_balcony"] = [int(data["patio_balcony"])]
    data["fire_extinguisher"] = [int(data["fire_extinguisher"])]
    data["shower_gel"] = [int(data["shower_gel"])]


    # data2 = pd.DataFrame.from_dict(dict)
    data_input = pd.DataFrame.from_dict(data)

    model_result = loaded_model.predict(data_input)

    return ('The best price for your home is: {:0.2f}€'.format((model_result[0])))


