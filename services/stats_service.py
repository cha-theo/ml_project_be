import csv
import os
import pandas as pd
import logging 
from flask import Blueprint, jsonify, request
import pickle

# loaded_model = pickle.load(open('repo/finalized_model.sav', 'rb'))



# find values for charts
a =1
b = [10,20,30,40]
df = pd.read_csv(os.getcwd() + '/repo/listings_preprocessed.csv', encoding="utf8")

max_price_per_room_type = []


#max price per room type
for x in df.groupby('room_type')['price'].max():
    max_price_per_room_type.append(x)


#dummy data chart

# charts = {
#         "barChart": [{"Max price": df.groupby('room_type')['price'].max()[0],
#                     "name": df.groupby('room_type')['price'].max().keys()[0],
#                     "Mean price": round(df.groupby('room_type')['price'].mean()[0],2)},
#                     {"Max price": df.groupby('room_type')['price'].max()[1],
#                     "name": df.groupby('room_type')['price'].max().keys()[1],
#                     "Mean price": round(df.groupby('room_type')['price'].mean()[1],2)},
#                     {"Max price": df.groupby('room_type')['price'].max()[2],
#                     "name": df.groupby('room_type')['price'].max().keys()[2],
#                     "Mean price": round(df.groupby('room_type')['price'].mean()[2],2)},
#                     {"Max price": df.groupby('room_type')['price'].max()[3],
#                     "name": df.groupby('room_type')['price'].max().keys()[3],
#                     "Mean price": round(df.groupby('room_type')['price'].mean()[3],2)},
#                     ],
#         "pieChart": [{"name": "Page A",
#                     "value": x},
#                     {"name": "Page A",
#                     "value": x},
#                     {"name": "Page A",
#                     "value": x}],

#         "areaChart": [{"pv": 2400,
#                     "uv": 4000,
#                     "amt": 2400,
#                     "name": "Page A"}],

#         "lineChart": [{"pv": 2400,
#                     "uv": 4000,
#                     "amt": 2400,
#                     "name": "Page A"}]
#     }


charts = {}

#bar chart max and mean price
barChart = []
for i in range(len(list(df['room_type'].unique()))):
    bar_chart = {"max price": df.groupby('room_type')['price'].max()[i],
    "mean price": round(df.groupby('room_type')['price'].mean()[i],2),
    "name": sorted(df['room_type'].unique())[i]}
    barChart.append(bar_chart)

#radar chart for top5 amenities
RadarChart = []

amenities_total_count = []
df['amenities'] = df['amenities'].apply(lambda x: x.replace("'",'').replace("[","").replace("]","").split(',  '))

for i in range(0, len(df)):
  for j in df['amenities'][i]:
    amenities_total_count.append(j.lower())

for i, k in enumerate(amenities_total_count):
  j = k.split(' ')
  if 'oven' in j:
    amenities_total_count[i] = 'oven'
  elif 'stove' in j:
    amenities_total_count[i] = 'stove'
  elif 'body' in j:
    amenities_total_count[i] = 'shower gel'
  elif 'shower' in j:
    amenities_total_count[i] = 'shower gel'
  elif 'shampoo' in j:
    amenities_total_count[i] = 'shampoo'
  elif 'conditioner' in j:
    amenities_total_count[i] = 'conditioner'
  elif 'heating' in j:
    amenities_total_count[i] = 'heating'
  elif 'netflix' in j:
    amenities_total_count[i] = 'netflix'
  elif 'amazon' in j:
    amenities_total_count[i] = 'amazon prime'
  elif 'wifi' in j:
    amenities_total_count[i] = 'wifi'
  elif 'game' in j:
    amenities_total_count[i] = 'game console'
  elif 'refrigerator' in j:
    amenities_total_count[i] = 'fridge'
  elif 'fridge' in j:
    amenities_total_count[i] = 'fridge'
  elif 'dedicated' in j:
    amenities_total_count[i] = 'dedicated workspace'
  elif 'sound' in j:
    amenities_total_count[i] = 'sound system'
  elif 'tv' in j:
    amenities_total_count[i] = 'tv'
  elif 'hdtv' in j:
    amenities_total_count[i] = 'tv'
  elif 'clothing' in j:
    amenities_total_count[i] = 'clothing storage'
  elif 'gym' in j:
    amenities_total_count[i] = 'gym'
  elif 'kitchen' in j:
    amenities_total_count[i] = 'kitchen'
  elif 'parking' in j:
    amenities_total_count[i] = 'parking'
  elif 'garage' in j:
    amenities_total_count[i] = 'parking'
  elif 'old' in j:
    amenities_total_count[i] = 'kids-friendly'
  elif 'baby' in j:
    amenities_total_count[i] = 'kids-friendly'
  elif 'toys' in j:
    amenities_total_count[i] = 'kids-friendly'
  elif 'fireplace' in j:
    amenities_total_count[i] = 'fireplace'
  elif ('pool' in j) and (len(j)<3):
    amenities_total_count[i] = 'pool'
  else:
    amenities_total_count[i] = k

amenities = pd.DataFrame(amenities_total_count, columns=['amenity'])
amenities_dict = amenities['amenity'].value_counts().to_frame().head()['amenity'].to_dict()


for i in range(len(amenities_dict)):
    radar_chart = {"frequency": list(amenities_dict.values())[i],
    "name": list(amenities_dict.keys())[i],
    "fullMark": max(amenities_dict.values())}
    RadarChart.append(radar_chart)

#radial bar chart for room type percentage
RadialBarChart = []

fill_colors = ['#8884d8','#83a6ed','#8dd1e1','#a4de6c']

room_type_total = len(df['room_type'])
room_type_dict = (df.groupby('room_type')['room_type'].count()*100/room_type_total).sort_values().to_dict()

i = 0
for key in room_type_dict:
    radial_bar_chart = {"uv": round(room_type_dict[key],2),
    "fill": fill_colors[i],
    "name": key}
    i += 1
    RadialBarChart.append(radial_bar_chart)

#scatter plot for top3 most expensive neighborhood visualization and their geographical boundaries with respect to the Acropolis
ScatterChart = []

neighborhoods_top3_dict = df.groupby('neighbourhood_cleansed')['price'].mean().sort_values(ascending=False).to_dict()

i = 1
data_1, data_2, data_3 = [], [], []

for key in neighborhoods_top3_dict:
  df_nei = df[df['neighbourhood_cleansed'] == key]
  df_nei.reset_index(inplace=True, drop=True)
  for i in range(len(df_nei)):
    d = {"x": df_nei['longitude'][i],
    "y": df_nei['longitude'][i]}
    if i == 1:
      data_1.append(d)
    elif i == 2:
      data_2.append(d)
    elif i == 3:
      data_3.append(d)

data_4 = [{"x": 37.9715, "y": 23.7257}] #Acropolis

ScatterChart.append([data_1, data_2, data_3, data_4])

#charts in json type
chart_types = ['barChart','radarChart','radialBarChart','scatterChart']

charts = dict.fromkeys(chart_types)
charts['barChart'] = barChart
charts['radarChart'] = RadarChart
charts['radialBarChart'] = RadialBarChart
charts['scatterChart'] = ScatterChart




# returns the stats for charts in json
def stat_for_charts():
    df = pd.read_csv(os.getcwd() + '/repo/listings_preprocessed.csv', encoding="utf8")
    return charts

# returns all the data from listings_preprocessed.csv in json
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




