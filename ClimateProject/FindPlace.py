import pymongo
from pymongo import MongoClient
import bottle

connection = MongoClient('localhost', 27017)
db = connection.weather

conditions = {}

def search_in_db():
	global conditions
	print(conditions)
	items = db.conditions.find({'ELEVATION':conditions['elevation'], 'LATITUDE':conditions['latitude'], 
		'LONGITUDE':conditions['longitude'], 'DATE':conditions['date'], 'PRCP':conditions['precipitation']})
	for item in items:
		print(item)

@bottle.route('/')
def make_home_page():
	return bottle.template('home_page')

@bottle.post('/')
def process_search():
	global conditions
	conditions['username'] = bottle.request.forms.get('username')
	conditions['elevation'] = bottle.request.forms.get('elevation')
	conditions['latitude'] = bottle.request.forms.get('latitude')
	conditions['longitude'] = bottle.request.forms.get('longitude')
	conditions['date'] = bottle.request.forms.get('date')
	conditions['precipitation'] = bottle.request.forms.get('precipitation')
	conditions['tmax'] = bottle.request.forms.get('tmax')
	conditions['tmini'] = bottle.request.forms.get('tmini')
	
	print(conditions)
	bottle.redirect("/search")

@bottle.route('/search')
def show_result():
	search_in_db()
	return bottle.template('result')


bottle.debug(True)
bottle.run(host='localhost', port = 8082)

