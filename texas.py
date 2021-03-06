from time import sleep
from urllib.request import urlopen

import json
import sys
import webbrowser


def open_appointments(cities=None):
    locations = json.loads(urlopen('https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json').read())['locations']
    success = False
    for location in locations:
        if cities is not None and location['city'].lower() not in cities:
            continue
        if location['openTimeslots'] > 0:
            contents = urlopen(location['url']).read().decode('utf-8')
            if 'Appointments are no longer available for this location' not in contents:
                webbrowser.open(location['url'])
                print('\n'.join(f'{k}={v}' for k, v in location.items() if k not in ['url', 'slotDetails'] and v is not None))
                success = True
    return success


if __name__ == '__main__':
    cities = None
    if len(sys.argv) > 1:
        cities = {city.lower() for city in sys.argv[1:]}
        print("Looking for appointments in the following cities: {}".format(sys.argv[1:]))
    else:
        print("Looking for appointments...")
    while not open_appointments(cities):
        sleep(1)
