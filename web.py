import os
from urllib.request import urlopen
import json
import pandas as pd
from pandas.io.json import json_normalize
from bottle import route, template, redirect, error, run
from operator import itemgetter


def get_appointments_data(location):
    jsonData = json.loads(urlopen(
        'https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json').read())['locations']
    locationData = json_normalize(jsonData)
    return locationData if location is None else locationData[locationData.city.str.lower() == location]


def get_location_appointments(location):
    locationData = get_appointments_data(location)
    locationData = locationData.sort_values(
        by='openTimeslots',  ascending=False)
    return locationData.to_dict('r')


def get_location_grouped():
    locationData = get_appointments_data(None)
    locationData = locationData.groupby(by='city', as_index=False)[
        'openTimeslots'].sum()
    locationData = locationData.sort_values(
        by='openTimeslots',  ascending=False)
    return locationData.to_dict('r')


@route('/')
def handle_root_url():
    redirect('/heb')


@route('/heb')
def make_request():
    return template('heb', data=get_location_grouped())


@route('/heb/<location>')
def make_request(location):
    location = location.lower()
    return template('city', data=get_location_appointments(location), loc=location)


@error(404)
def error404(error):
    return template('error', error_msg='404 error. Nothing to see here')


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8087, debug=True)
