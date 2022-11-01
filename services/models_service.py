import csv
import os
import pandas as pd
import logging
from flask import Blueprint, jsonify, request
import pickle


loaded_model = pickle.load(open('repo/trained_model.sav', 'rb'))


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


# test inout dictionary values
# dict = {'accommodates':[2],'beds':[2],'smoke_alarm':[0],'oven':[1],'patio_balcony':[1],'fire_extinguisher':[0],'shower_gel':[1]}
# data2 = pd.DataFrame.from_dict(dict)
# az = loaded_model.predict(data2)
# print(az)


# here we can assign the values to the model and get the price
# dict = {'accommodates':[2],'beds':[2],'smoke_alarm':[0],'oven':[1],'patio_balcony':[1],'fire_extinguisher':[0],'shower_gel':[1]}

# assign the values to the neighborhoods dict
neighborhoods_dict = {"neighbourhood_cleansed_1Ο ΝΕΚΡΟΤΑΦΕΙΟ": [0],
                      "neighbourhood_cleansed_ΑΓΙΟΣ ΕΛΕΥΘΕΡΙΟΣ": [0],
                      "neighbourhood_cleansed_ΑΓΙΟΣ ΚΩΝΣΤΑΝΤΙΝΟΣ-ΠΛΑΤΕΙΑ ΒΑΘΗΣ": [0],
                      "neighbourhood_cleansed_ΑΓΙΟΣ ΝΙΚΟΛΑΟΣ": [0],
                      "neighbourhood_cleansed_ΑΚΑΔΗΜΙΑ ΠΛΑΤΩΝΟΣ": [0],
                      "neighbourhood_cleansed_ΑΚΡΟΠΟΛΗ": [0],
                      "neighbourhood_cleansed_ΑΜΠΕΛΟΚΗΠΟΙ": [0],
                      "neighbourhood_cleansed_ΑΝΩ ΚΥΨΕΛΗ": [0],
                      "neighbourhood_cleansed_ΑΝΩ ΠΑΤΗΣΙΑ": [0],
                      "neighbourhood_cleansed_ΒΟΤΑΝΙΚΟΣ": [0],
                      "neighbourhood_cleansed_ΓΚΑΖΙ": [0],
                      "neighbourhood_cleansed_ΓΚΥΖΗ": [0],
                      "neighbourhood_cleansed_ΓΟΥΒΑ": [0],
                      "neighbourhood_cleansed_ΓΟΥΔΙ": [0],
                      "neighbourhood_cleansed_ΕΛΛΗΝΟΡΩΣΩΝ": [0],
                      "neighbourhood_cleansed_ΕΜΠΟΡΙΚΟ ΤΡΙΓΩΝΟ-ΠΛΑΚΑ": [0],
                      "neighbourhood_cleansed_ΖΑΠΠΕΙΟ": [0],
                      "neighbourhood_cleansed_ΘΗΣΕΙΟ": [0],
                      "neighbourhood_cleansed_ΙΛΙΣΙΑ": [0],
                      "neighbourhood_cleansed_ΚΕΡΑΜΕΙΚΟΣ": [0],
                      "neighbourhood_cleansed_ΚΟΛΟΚΥΝΘΟΥ": [0],
                      "neighbourhood_cleansed_ΚΟΛΩΝΑΚΙ": [0],
                      "neighbourhood_cleansed_ΚΟΛΩΝΟΣ": [0],
                      "neighbourhood_cleansed_ΚΟΥΚΑΚΙ-ΜΑΚΡΥΓΙΑΝΝΗ": [0],
                      "neighbourhood_cleansed_ΚΥΨΕΛΗ": [0],
                      "neighbourhood_cleansed_ΛΥΚΑΒΗΤΤΟΣ": [0],
                      "neighbourhood_cleansed_ΜΟΥΣΕΙΟ-ΕΞΑΡΧΕΙΑ-ΝΕΑΠΟΛΗ": [0],
                      "neighbourhood_cleansed_ΝΕΑ ΚΥΨΕΛΗ": [0],
                      "neighbourhood_cleansed_ΝΕΟΣ ΚΟΣΜΟΣ": [0],
                      "neighbourhood_cleansed_ΝΙΡΒΑΝΑ": [0],
                      "neighbourhood_cleansed_ΠΑΓΚΡΑΤΙ": [0],
                      "neighbourhood_cleansed_ΠΑΤΗΣΙΑ": [0],
                      "neighbourhood_cleansed_ΠΕΔΙΟ ΑΡΕΩΣ": [0],
                      "neighbourhood_cleansed_ΠΕΝΤΑΓΩΝΟ": [0],
                      "neighbourhood_cleansed_ΠΕΤΡΑΛΩΝΑ": [0],
                      "neighbourhood_cleansed_ΠΛΑΤΕΙΑ ΑΜΕΡΙΚΗΣ": [0],
                      "neighbourhood_cleansed_ΠΛΑΤΕΙΑ ΑΤΤΙΚΗΣ": [0],
                      "neighbourhood_cleansed_ΠΟΛΥΓΩΝΟ": [0],
                      "neighbourhood_cleansed_ΠΡΟΜΠΟΝΑ": [0],
                      "neighbourhood_cleansed_ΡΗΓΙΛΛΗΣ": [0],
                      "neighbourhood_cleansed_ΡΙΖΟΥΠΟΛΗ": [0],
                      "neighbourhood_cleansed_ΣΕΠΟΛΙΑ": [0],
                      "neighbourhood_cleansed_ΣΤΑΔΙΟ": [0],
                      "neighbourhood_cleansed_ΣΤΑΘΜΟΣ ΛΑΡΙΣΗΣ": [0]}

room_type_dict = {"room_type_Entire home/apt": [0],
                  "room_type_Hotel room": [0],
                  "room_type_Private room": [0],
                  "room_type_Shared room": [0]}



amenities_dict = {"amenities_high": [0],
                  "amenities_low": [0],
                  "amenities_medium": [0]}

def calculate_price(data):

# convert the data for the model
    data["accommodates"] = [int(data["accommodates"])]
    data["availability_365"] = [int(data["availability_365"])]
    data["bathroom"] = [int(data["bathroom"])]
    data["bathroom_type_private"] = [int(data["bathroom_type_private"])]
    data["beds"] = [int(data["beds"])]
    data["host_identity_verified"] = [int(data["host_identity_verified"])]
    data["host_is_superhost"] = [int(data["host_is_superhost"])]
    data["host_listings_count"] = [int(data["host_listings_count"])]
    data["instant_bookable"] = [int(data["instant_bookable"])]
    data["maximum_nights"] = [int(data["maximum_nights"])]
    data["minimum_nights"] = [int(data["minimum_nights"])]
    data["number_of_reviews"] = [int(data["number_of_reviews"])]
    data["reviews_per_month"] = [int(data["reviews_per_month"])]

    # assign value to multiple fiels    
    if data["room_type"] in room_type_dict:
        for key in room_type_dict.keys():
            room_type_dict[key] = [0]
        room_type_dict[data["room_type"]] = [1]
        
    if data["neighbourhood"] in neighborhoods_dict:
        for key in neighborhoods_dict.keys():
            neighborhoods_dict[key] = [0]
        neighborhoods_dict[data["neighbourhood"]] = [1]

    if data["amenities"] in amenities_dict:
        for key in amenities_dict.keys():
            amenities_dict[key] = [0]
        amenities_dict[data["amenities"]] = [1]

    # connect our main dict with room_type_dict and neighborhoods_dict
    data.update(room_type_dict)
    data.update(neighborhoods_dict)

    # remove the excess values(neighbourhood, room_type)
    del data["neighbourhood"]
    del data["room_type"]
    
    data2 = pd.DataFrame.from_dict(data)
    # data_input = pd.DataFrame.from_dict(data)

    # model_result = loaded_model.predict(data2)

    return ('The best price for your home is: {}€'.format(data))
