from flask import Flask
import requests
import json
import sqlite3


app = Flask(__name__)

# Class used to make processing the bird data easier
# Not used for return function
class BirdData(object):
    def __init__(self, state=None, bird=None, scientific_name=None, year=None, abbreviation=None):
        self.state = state
        self.bird = bird
        self.scientific_name = scientific_name
        self.year = year
        self.abbreviation = abbreviation
    def __str__(self):
        return "test" + self.state

# Function to get bird data; returns in both json and custom class object
def get_bird(state: str):
    conn = sqlite3.connect("./birds.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    print(f"select * from birds where abbreviation = '{state}';")
    row = cursor.execute(f"select * from birds where abbreviation = '{state}';")
    res = row.fetchall()
    list_accumulator = []
    result = []
    for item in res:
        list_accumulator.append({k: item[k] for k in item.keys()})
        result.append(BirdData(*item))
    return json.dumps(list_accumulator), result

# Function to get the weather data by connecting to api.weather.gov
def get_weather(state: str):
    r = requests.get(f'https://api.weather.gov/alerts/active?area={state}')
    return r.json()


@app.get('/')
def hello():
    return "Add a 2 letter state param to learn about birds and the weather challenges they face.", \
           200, \
           {'Content-Type': 'text/html; charset=utf-8'}

# Primary function
@app.get('/<state>')
def bird(state):
    state = state.upper()
    bird_json, bird_obj = get_bird(state)
    if len(bird_obj) < 1:
        print(f"Error: No birds found for abbreviation <{state}>")
        return bird_json, 404, {'Content-Type': 'application/json'}
    print(f"State <{bird_obj[0].state}> has the following bird(s): ")
    for bird in bird_obj:
        print(f"\t{bird.bird} <{bird.scientific_name}>")
    weather = get_weather(state)
    if weather['title'] == 'Bad Request':
        print(f"Error: Bad Request for weather")
        return weather, 400, {'Content-Type': 'application/json'}
    print(weather['title'] + ":")
    features = weather['features']
    if not isinstance(features, list):
        features = [features]
    for item in features:
        print("\t" + str(item['properties']['headline']))
    out = str([bird_json, weather])
    return out, 200, {'Content-Type': 'application/json'}