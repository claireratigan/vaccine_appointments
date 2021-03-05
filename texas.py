from time import sleep

import requests
import sys
import webbrowser


def open_appointments(cities=None):
    locations = requests.get('https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json').json()['locations']
    success = False
    for location in locations:
        if cities is not None and location['city'].lower() not in cities:
            continue
        if location['openTimeslots'] > 0:
            webbrowser.open(location['url'])
            success = True
    return success


if __name__ == '__main__':
    cities = None
    if len(sys.argv) > 1:
        cities = {city.lower() for city in sys.argv[1:]}
    while not open_appointments(cities):
        sleep(1)
