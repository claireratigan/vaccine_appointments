# Vaccine Appointments
**[Automatically searching for vaccine appointments](https://vaccine-appointments.herokuapp.com/heb)**

# Usage

To copy this package, run:

`git clone https://github.com/TheIronicCurtain/vaccine_appointments`

## Texas

### Using Python (simplified)

Run the following in the command line:

` python texas.py [cities] `

Where `cities` are the cities you want to restrict your search to. If none are provided it will open all available appointments. e.g. if you're in the San Antonio area you might put: 

`python texas.py "San Antonio" Jourdanton Pleasanton Leming Poteet`

Once it starts running, it will ping HEB periodically until an appointment in one of those cities shows up, and then open it in your web browser. You still have to be quick from there!

The loop will stop running once it finds a page to open, so if you don't get the appointment on the first try just run it again!

### Using Python (fancy)

If you feel comfortable installing a few Python packages, the required packages are in `requirements.txt`

All you need to do to install the required packages is navigate to the repository and run the following line in the command line (assuming you have Python installed):

`python -m pip install -r requirements.txt`

Run `python texas_fancy.py --help` for usage:

```
usage: texas_fancy.py [-h] [-c CITIES [CITIES ...]] [-H HOME] [-d DISTANCE] [-Z ZIPCODES [ZIPCODES ...]]

Program to ping HEB for vaccine appointments in your area

optional arguments:
  -h, --help            show this help message and exit
  -c CITIES [CITIES ...], --cities CITIES [CITIES ...]
                        Cities to restrict the search to
  -H HOME, --home HOME  Home location: can be in the form of a zipcode, address, latitude/longitude, city, etc. (requires distance)
  -d DISTANCE, --distance DISTANCE
                        Maximum distance (in miles) from home (requires home)
  -Z ZIPCODES [ZIPCODES ...], --zipcodes ZIPCODES [ZIPCODES ...]
                        Zipcodes to restrict the search to

```

Examples:

 - `python texas_fancy.py -c "San Antonio" Jourdanton Pleasanton Leming Poteet` would do the same as the simple example
 - `python texas_fancy.py -H "San Antonio, TX" -d 50` would look for appointments 50 miles from San Antonio
 - `python texas_fancy.py -H 78023 -d 30` would look for appointments 30 miles from zip code 78023
 - `python texas_fancy.py -z 76028 75165` would look for appointments only in the zip codes 76028 and 75165

### On Windows

_Note: You probably shouldn't be trusting me with random executables. The Python version is recommended if you can work out how to run it._

Under the `dist` folder there's a `.exe` file corresponding to each of the Python files. Both of them can be run from the command line out of the box on a Windows machine using the same commands. For example, if you wanted to run the first `texas_fancy.py` example, you would open your command prompt (search for "cmd" on your computer) and then run `texas_fancy.exe -c "San Antonio" Jourdanton Pleasanton Leming Poteet` after downloading the file to your home directory.
