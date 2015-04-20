'''
	This is a program allowing users to search a particular place in China
	by inputing certain conditions
'''
import pymongo
from pymongo import MongoClient
import bottle
from bottle import *
import pprint
import copy
import math
import json

connection = MongoClient('localhost', 27017)
db = connection.weather
collection = db.condition

conditions = {}

user_info = [False,"None"]

@bottle.route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./assets/')

# Initialize the search page
@bottle.route('/conditional_search.html')
def conditional_search_page():
    global conditions
    Places = collection.distinct('STATION_NAME')
    PlaceOptions = []
    row = {}
    for item in Places:
        temp_lat_and_lon = getLAT_AND_LON(item)
        row['city'] = item
        row['lon_and_lat'] = str(temp_lat_and_lon[0]) + "," + str(temp_lat_and_lon[1])
        PlaceOptions.append(copy.copy(row))
    return bottle.template('conditional_search', {'PlaceOptions': PlaceOptions,'user_info': user_info})

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
@bottle.post('/conditional_search.html')
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
	return bottle.template('result', {"Items": search_in_db(),'user_info': user_info})

# Use the given conditions to search in the database
def search_in_db():
	global conditions
	items = collection.find(conditions)
	return items

@bottle.post('/search')
def go_back():
	bottle.redirect('/conditional_search.html')

@bottle.route('/search2')
def draw_point():
    source = search_in_db()
    station = []
    target = []
    for item in source:
        temp = {}
        if item['STATION_NAME'] not in station:
            for k,v in item.iteritems():
                if(k!="_id"):
                    temp[k]=v
            target.append(temp)
            station.append(item['STATION_NAME'])
    return json.dumps(target)

@bottle.route('/')
@bottle.view('index')
def index():
    return dict(user_info = user_info)

@bottle.post('/login')
@bottle.view('index')
def login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username == 'xzhflying' and password == '930619':
        user_info[0] = True
        user_info[1] = 'Xu Zihuan'
    return dict(user_info = user_info)


##################  graph   #####################
conditions1 = {}
conditions2 = {}

@bottle.route('/<filename>')
def server_static(filename):
    return bottle.static_file(filename, root='');

@bottle.route('/graph')
def do_search():
    PlaceOptions = db.condition.distinct('STATION_NAME')
    return bottle.template('graph', {'PlaceOptions': PlaceOptions,'user_info': user_info})

@bottle.post('/graph')
def go_to_result():
    PlaceOptions = db.condition.distinct('STATION_NAME')
        
    conditions1['place_name'] = bottle.request.forms.get('place_name1')
    conditions1['start_date'] = bottle.request.forms.get('start_date1')
    conditions1['end_date'] = bottle.request.forms.get('end_date1')
    conditions1['data_type'] = bottle.request.forms.get('data_type')
    conditions2['place_name'] = bottle.request.forms.get('place_name2')
    conditions2['start_date'] = bottle.request.forms.get('start_date2')
    conditions2['end_date'] = bottle.request.forms.get('end_date2')
    conditions2['data_type'] = bottle.request.forms.get('data_type')
        
    print conditions1
    print conditions2
        
    return bottle.template('graph', {'PlaceOptions': PlaceOptions,'user_info': user_info})

@bottle.route('/fetch')
def fetch():
    
    return json.dumps(search_graph())


# search data in the database according to the given conditions
def search_graph():
    parameters = []
    print "search in db"
    search_strategy1 = {}
    search_strategy2 = {}
    results1 = []
    results2 = []
    print "conditions:"
    print conditions1
    print conditions2
    print "conditions over"
    if len(conditions1) != 0:
        search_strategy1['STATION_NAME'] = conditions1['place_name']
        search_strategy1['DATE'] = {}
        search_strategy1['DATE']['$gte'] = int(conditions1['start_date'])
        search_strategy1['DATE']['$lte'] = int(conditions1['end_date'])
        try:
            print "this is strategy"
            print search_strategy1
            results1 =  collection.find(search_strategy1)
            print results1
        except:
            print("Search Error")
    if  len(conditions2) != 0:
        search_strategy2['STATION_NAME'] = conditions2['place_name']
        search_strategy2['DATE'] = {}
        search_strategy2['DATE']['$gte'] = int(conditions2['start_date'])
        search_strategy2['DATE']['$lte'] = int(conditions2['end_date'])
        try:
            print search_strategy2
            results2 = collection.find(search_strategy2)
        except:
            print("Search Error")
    placeOne = {}
    placeOne['label'] = conditions1['place_name']
    placeOne['data'] = construct_parameters(results1,1)
    placeTwo = {}
    placeTwo['label'] = conditions2['place_name']
    placeTwo['data'] = construct_parameters(results2,2)
    parameters.append(placeOne)
    parameters.append(placeTwo)
    return parameters


# Construct the line for one data set
def construct_parameters(results, num):
    parameters_for_one = []
    
    for i in results:
        temp = []
        temp.append(i['DATE'])
        if num ==1:
            if (i[conditions1['data_type']]!=-9999):
                if conditions1['data_type'] in ['TMAX', 'TMIN']:
                    i[conditions1['data_type']] = i[conditions1['data_type']] / 10
                    temp.append(i[conditions1['data_type']])

        elif num ==2:
            if (i[conditions2['data_type']]!=-9999):
                if conditions2['data_type'] in ['TMAX', 'TMIN']:
                    i[conditions2['data_type']] = i[conditions2['data_type']] / 10
                temp.append(i[conditions2['data_type']])

        parameters_for_one.append(temp)      

    return parameters_for_one


bottle.debug(True)
bottle.run(host='localhost', port = 8082)

