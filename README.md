# Flask-RESTful API project

<span style="display:block;text-align:center">![Logo](logo.png)</span>

## App details

The goal of this API is to get access to AirBnB data and expose the processed data to the world via a RESTful API.

- The API was created with [Flask](https://flask.palletsprojects.com/en/2.2.x/).

```
Package Version
---
autopep8 1.7.0
certifi 2022.9.24
charset-normalizer 2.1.1
click 8.1.3
colorama 0.4.5
contourpy 1.0.5
cycler 0.11.0
Flask 2.2.2
Flask-Cors 3.0.10
Flask-HTTPAuth 4.7.0
fonttools 4.38.0
idna 3.4
itsdangerous 2.1.2
Jinja2 3.1.2
joblib 1.2.0
kiwisolver 1.4.4
MarkupSafe 2.1.1
matplotlib 3.6.1
numpy 1.23.4
packaging 21.3
pandas 1.5.0
Pillow 9.2.0
pip 22.2.2
pycodestyle 2.9.1
pyparsing 3.0.9
python-dateutil 2.8.2
pytz 2022.4
requests 2.28.1
scikit-learn 1.1.3
scipy 1.9.3
setuptools 63.2.0
six 1.16.0
threadpoolctl 3.1.0
toml 0.10.2
urllib3 1.26.12
Werkzeug 2.2.2
xgboost 1.6.2
```

## Flask Application Structure

```
.
|──────controllers/
| |──────models_controller.py
| |──────ping_controller.py
| |──────stats_controller.py
|──────repo/
| |──────listings_preprocessed.csv
| |──────trained_model.sav
|──────services/
| |──────models_service.py
| |──────stats_service.py
| |────app.py
| |────bnb2022-11-02.log
| |────bnb_base_logger.py

```

## Usage

### Stats endpoint

GET http://127.0.0.1:5001/bnb/api/v1/stats/

RESPONSE

```json
{
  "barChart": [
    {
      "max price": 8240,
      "mean price": 82.33,
      "name": "Entire home/apt"
    }
  ]
}
```

GET http://127.0.0.1:5001/bnb/api/v1/stats/raw_data

RESPONSE

```json
{
  "data": [
    {
      "accommodates": "8",
      "amenities": "['Kitchen', ' Free street parking', ' Crib', ' Patio or balcony', ' Ethernet connection', ' Dishwasher', ' Host greets you', ' Dishes and silverware', ' Long term stays allowed', ' Iron', ' Air conditioning', ' Cooking basics', ' Washer', ' Refrigerator', ' Laundromat nearby', ' Wifi \\\\u2013 50 Mbps', ' Coffee maker', ' Microwave', ' Electric stove', ' Hangers', ' Essentials', ' High chair', ' Hair dryer', ' 43\\\\ HDTV', ' Extra pillows and blankets', ' Shower gel', ' Dedicated workspace', ' Oven', ' Single level home', ' Bed linens', ' Hot water', ' Central heating', ' Shampoo']",
      "amenities_category": "medium",
      "availability_365": "170",
      "bathroom": "2.0",
      "bathroom_type": "private",
      "bathrooms_text": "2 baths",
      "bedrooms": "3.0",
      "beds": "5.0",
      "description": "Athens Furnished Apartment No6 is 3-bedroom apartment with 2-bathrooms<br />-excellent located <br />-close to metro station, <br />-lovely, <br />-very clean <br />with all the facilities that you will need, nice balcony, excellent Wi-Fi, cable tv, fully air conditioned\u2026<br /><br /><b>The space</b><br />Athens Furnished Apartment No6 is an excellent located, close to metro, lovely, very clean 3-bedroom apartment with 2-bathrooms with all the facilities that you will need and balcony. It is on the 2nd floor but do not worry because there is elevator in the building. Fully equipped kitchen with everything you need to prepare your lunch/dinner. Living room to relax and enjoy a movie or a sport event. 2 Clean nice bathrooms. For more than 6 people there is a sofa/bed. <br />Apartment No6 has everything you will need.<br />1st Bedroom \u2013 Double bed<br />2nd Bedroom \u2013 2 single beds<br />3rd Bedroom \u2013 2 single beds<br />-Telephone line for incoming calls or to call us if you need something.<b",
      "has_availability": "t",
      "host_id": "37177",
      "host_identity_verified": "t",
      "host_is_superhost": "t",
      "host_listings_count": "6.0",
      "host_since": "2009-09-08",
      "id": "10595",
      "instant_bookable": "t",
      "last_review": "2019-04-04",
      "latitude": "37.98863",
      "longitude": "23.76527",
      "maximum_nights": "1125",
      "minimum_nights": "1",
      "neighbourhood_cleansed": "\u0391\u039c\u03a0\u0395\u039b\u039f\u039a\u0397\u03a0\u039f\u0399",
      "number_of_reviews": "32",
      "price": "81.37",
      "property_type": "Entire rental unit",
      "reviews_per_month": "0.41",
      "room_type": "Entire home/apt"
    }
  ]
}
```

POST http://127.0.0.1:5001/bnb/api/v1/models/

REQUEST

```json
{
  "host_listings_count": [5],
  "host_identity_verified": [1],
  "host_is_superhost": [1],
  "accommodates": [6],
  "beds": [4],
  "minimum_nights": [3],
  "maximum_nights": [30],
  "availability_365": [287],
  "number_of_reviews": [3],
  "reviews_per_month": [0],
  "instant_bookable": [0],
  "bathroom": [2],
  "bathroom_type_private": [1],
  "room_type_Entire home/apt": [1],
  "room_type_Hotel room": [0],
  "room_type_Private room": [0],
  "room_type_Shared room": [0],
  "neighbourhood_cleansed_1Ο ΝΕΚΡΟΤΑΦΕΙΟ": [0],
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
  "neighbourhood_cleansed_ΘΗΣΕΙΟ": [1],
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
  "neighbourhood_cleansed_ΣΤΑΘΜΟΣ ΛΑΡΙΣΗΣ": [0],
  "amenities_high": [0],
  "amenities_low": [1],
  "amenities_medium": [0]
}
```

RESPONSE

```
[161.0997]
```


GET http://127.0.0.1:5001/bnb/api/v1/ping/

RESPONSE

```
Pong
```