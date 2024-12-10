from flask import Flask
import requests
import json
import sqlite3


app = Flask(__name__)

class BirdData(object):
    def __init__(self, state=None, bird=None, scientific_name=None, year=None, abbreviation=None):
        self.state = state
        self.bird = bird
        self.scientific_name = scientific_name
        self.year = year
        self.abbreviation = abbreviation
    def __str__(self):
        return "test" + self.state

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

def get_weather(state: str):
    r = requests.get(f'https://api.weather.gov/alerts/active?area={state}')
    return r.json()


@app.get('/')
def hello():
    return "Add a 2 letter state param to learn about birds and the weather challenges they face.", \
           200, \
           {'Content-Type': 'text/html; charset=utf-8'}


@app.get('/<state>')
def bird(state):
    state = state.upper()
    bird_json, bird_obj = get_bird(state)
    if len(bird_obj) < 1:
        raise ValueError(f"No birds found for abbreviation <{state}>")
        return out, 400, {'Content-Type': 'application/json'}
    print(f"State <{bird_obj[0].state}> has the following bird(s): ")
    for bird in bird_obj:
        print(f"\t{bird.bird} <{bird.scientific_name}>")
    weather = get_weather(state)
    if weather['title'] == 'Bad Request':
        raise ValueError(f"Bad Request for weather")
        return out, 400, {'Content-Type': 'application/json'}
    print(weather['title'])
    out = str([bird_json, weather])
    return out, 200, {'Content-Type': 'application/json'}

