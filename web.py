import os,requests
from bottle import route, template, redirect, error, run
from operator import itemgetter

def get_appointments_data(location) :
    locationData = requests.get('https://heb-ecom-covid-vaccine.hebdigital-prd.com/vaccine_locations.json').json()['locations']
    return [x for x in locationData if x['city'].lower() == location]


@route('/')
def handle_root_url():
    redirect('/heb/houston')


@route('/heb/<location>')
def make_request(location):
    location = location.lower()
    # API request
    locationData = get_appointments_data(location)
    locationData =  sorted(locationData, key=itemgetter('openTimeslots'), reverse=True)
    return template('heb', data=locationData,loc=location)
    
@error(404)
def error404(error):
    return template('error', error_msg='404 error. Nothing to see here')


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8087, debug=True)