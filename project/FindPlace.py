'''
	This is a program allowing users to search a particular place in China
	by inputing certain conditions
'''
import pymongo
from pymongo import MongoClient
import bottle
import pprint
import copy
import math

connection = MongoClient('localhost', 27017)
db = connection.weather
collection = db.condition

conditions = {}

# Initialize the home page
@bottle.route('/')
def make_home_page():
    global conditions
    Places = collection.distinct('STATION_NAME')
    PlaceOptions = []
    row = {}
    for item in Places:
        temp_lat_and_lon = getLAT_AND_LON(item)
        row['city'] = item
        row['lon_and_lat'] = str(temp_lat_and_lon[0]) + "," + str(temp_lat_and_lon[1])
        PlaceOptions.append(copy.copy(row))
    return bottle.template('home_page', {'PlaceOptions': PlaceOptions})

def getLAT_AND_LON(city):
    
    result = collection.find_one({"STATION_NAME":city})
    if result is not None:
        latitude = result["LATITUDE"]
        longitude = result["LONGITUDE"]
    else:
        return None
    return (latitude,longitude)


# Called after user press the button
# Get the given conditions from text boxes in the homepage
@bottle.post('/')
def process_search():
    global conditions
    conditions.clear()
    conditions['date'] = (bottle.request.forms.get('mindate'),bottle.request.forms.get('maxdate'))
    conditions['prcp'] = (bottle.request.forms.get('minprcp'),bottle.request.forms.get('maxprcp'))
    conditions['snwd'] = (bottle.request.forms.get('minsnwd'),bottle.request.forms.get('maxsnwd'))
    conditions['tmax'] = (bottle.request.forms.get('mintmax'),bottle.request.forms.get('maxtmax'))
    conditions['tmin'] = (bottle.request.forms.get('mintmin'),bottle.request.forms.get('maxtmin'))
    
    # Determine the specific station_name
    lat_and_lon = bottle.request.forms.get('station_name').split(",",1)
    if bottle.request.forms.get('distance') != "":
        distance = float(bottle.request.forms.get('distance'))
    else:
        distance = 0
    ranges = getRange(float(lat_and_lon[0]), float(lat_and_lon[1]), distance)
    conditions['latitude'] = (ranges[1], ranges[0])
    conditions['longitude'] = (ranges[3], ranges[2])    
    conditions = check_input(conditions)
    bottle.redirect("/search")

# Eliminate empty input and ensure valid conditions
def check_input(conditions):
	new_conditions = {}
	for item in conditions:
		if conditions[str(item)][0] != '' or conditions[str(item)][1] != '':
			new_conditions[item.upper()] = {}
		if conditions[str(item)][0] != '':
			try:
				#print(str(item), 'conditions[str(item)][0]', conditions[str(item)][0])
				new_conditions[item.upper()]['$gte'] = float(conditions[str(item)][0])
			except:
				print str(item)
				bottle.redirect("/")
		if conditions[str(item)][1] != '':
			try:				
				#print('conditions[str(item)][1]', conditions[str(item)][1])
				new_conditions[item.upper()]['$lte'] = float(conditions[str(item)][1])
			except:
				print str(item)
				bottle.redirect("/")

	pprint.pprint(new_conditions)
	return new_conditions

# get the range of latitude and longitude by a given point and a distance range
def getRange(lat , lon , distance):
    PI = 3.14159265359
    DEF_R = 6370693.5
    lat = lat * PI /180
    lon = lon * PI /180
    rad_dist = distance / DEF_R
    lat_min = lat - rad_dist
    lat_max = lat + rad_dist
    if(lat_min > -PI/2 and lat_max < PI/2):
        lon_t = math.asin( math.sin(rad_dist) / math.cos(lat) )
        lon_min = lon - lon_t
        if lon_min < -PI:
            lon_min = 2 * PI +lon_min
        lon_max = lon + lon_t
        if lon_max > PI:
            lon_max = 2 * PI - lon_max
    else:
        lat_min = max (lat_min , -PI/2)
        lat_max = min (lat_max, PI/2)
        lon_min = -PI
        lon_max = PI
    lat_min = lat_min * 180 / PI
    lat_max = lat_max * 180 / PI
    lon_min = lon_min * 180 / PI
    lon_max = lon_max *180 / PI
    result = (lat_max, lat_min, lon_max, lon_min)
    return result


# Display the search result
@bottle.route('/search')
def show_result():
	global conditions
	return bottle.template('result', {"Items": search_in_db()})

# Use the given conditions to search in the database
def search_in_db():
	global conditions
	print('search_in_db')
	pprint.pprint(conditions)
	#new_conditions = modify_dic(conditions)
	items = collection.find(conditions)

	return items

@bottle.post('/search')
def go_back():
	bottle.redirect('/')

bottle.debug(True)
bottle.run(host='localhost', port = 8082)

