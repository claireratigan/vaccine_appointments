from time import sleep
from urllib.request import urlopen

import argparse
import json
import sys
from tqdm import tqdm
import webbrowser
import urllib.request
import winsound as sound

from geopy.geocoders import Nominatim
from geopy.distance import geodesic


store_name_to_distance = {}


def open_appointments(namespace, geolocator, reported_appointments):
    locations = json.loads(urlopen('https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json').read())['locations']
    success = False
    for location in locations:
        if namespace.cities is not None and location['city'].lower() not in namespace.cities:
            continue
        if namespace.zipcodes is not None and location['zip'] not in namespace.zipcodes:
            continue
        distance = None
        if namespace.distance is not None:
            if location['name'] in store_name_to_distance:
                distance = store_name_to_distance[location['name']]
            else:
                latlong = (location['latitude'], location['longitude'])
                if any(l is None for l in latlong):
                    geoloc = geolocator.geocode(', '.join(location[key] for key in ['street', 'city', 'state', 'zip']))
                    if geoloc is None:
                        geoloc = geolocator.geocode(location['zip'])
                    latlong = (geoloc.latitude, geoloc.longitude)
                distance = geodesic(ns.latlong, latlong)
                store_name_to_distance[location['name']] = distance
            if distance.miles > namespace.distance:
                continue
        if location['openTimeslots'] > 0 and location['url'] not in reported_appointments:
            contents = urllib.request.urlopen(location['url']).read().decode('utf-8')
            if 'Appointments are no longer available for this location' not in contents:
                webbrowser.open(location['url'])
                print('\n'.join(f'{k}={v}' for k, v in location.items() if k not in ['url', 'slotDetails'] and v is not None))
                if distance is not None:
                    print(f'Distance from home: {distance.miles} miles')
                if location['openTimeslots'] > 1:
                    success = True
                    for i in range(300):
                        sound.Beep(2500, 300)
                else:
                    sound.Beep(2500, 300)
                reported_appointments.append(location['url'])
    return success


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Program to ping HEB for vaccine appointments in your area")
    parser.add_argument('-c', '--cities', nargs='+', help='Cities to restrict the search to')
    parser.add_argument('-H', '--home',
                        help='Home location: can be in the form of a zipcode, address, latitude/longitude, city, etc. (requires distance)')
    parser.add_argument('-d', '--distance', type=float,
                        help='Maximum distance (in miles) from home (requires home)')
    parser.add_argument('-Z', '--zipcodes', nargs='+', help='Zipcodes to restrict the search to')
    # parser.add_argument('-V', '-v', '--vaccines', nargs='+', help = 'Vaccines to restrict (JJ, M, P)')

    ns = parser.parse_args(sys.argv[1:])

    assert (ns.distance is None) == (ns.home is None), 'Home location and distance should be supplied together'

    geolocator = Nominatim(user_agent='vaccine_appointments')

    if ns.cities:
        ns.cities = {city.lower() for city in ns.cities}
    if ns.distance:
        home = geolocator.geocode(ns.home)
        ns.latlong = (home.latitude, home.longitude)
        print(f'Looking for appointments {ns.distance} miles from {home}')
    reported_appointments = []
    with tqdm() as pbar:
        while not open_appointments(ns, geolocator, reported_appointments):
            sleep(1)
            pbar.update(1)
