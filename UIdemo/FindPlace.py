'''
	This is a program allowing users to search a particular place in China
	by inputing certain conditions :)
'''
import pymongo
from pymongo import MongoClient
import bottle

connection = MongoClient('localhost', 27017)
db = connection.weather

conditions = {}

# Initialize the home page
@bottle.route('/')
def make_home_page():
	return bottle.template('home_page')

# Called after user press the button
# Get the given conditions from text boxes in the homepage
@bottle.post('/')
def process_search():
	global conditions
	print('flag', bottle.request.forms.get('elevation'))
	if bottle.request.forms.get('elevation') != '':
		conditions['elevation'] = float(bottle.request.forms.get('elevation'))
	if bottle.request.forms.get('latitude') != '':
		conditions['latitude'] = float(bottle.request.forms.get('latitude'))
	if bottle.request.forms.get('longitude') != '':
		conditions['longitude'] = float(bottle.request.forms.get('longitude'))
	if bottle.request.forms.get('precipitation') != '':
		conditions['precipitation'] = float(bottle.request.forms.get('precipitation'))
	if bottle.request.forms.get('snowdepth') != '':
		conditions['snowdepth'] = float(bottle.request.forms.get('snowdepth'))
	if bottle.request.forms.get('tmax') != '':
		conditions['tmax'] = float(bottle.request.forms.get('tmax'))
	if bottle.request.forms.get('tmin') != '':
		conditions['tmin'] = float(bottle.request.forms.get('tmin'))
	
	print(conditions)
	bottle.redirect("/search")

# Use the given conditions to search in the database
def search_in_db():
	global conditions
	# for item in conditions:
	# 	if conditions[item] == '':
	# 		conditions.pop(item)
	conditions = modify_dic(conditions)
	items = db.condition.find(
		{

		})
	print('items=', items)
	return items

def modify_dic(conditions):
	new_conditions = {}
	if 'elevation' in conditions:
		new_conditions['ELEVATION'] = conditions['elevation']
	if 'latitude' in conditions:
		new_conditions['LATITUDE'] = conditions['latitude']
	if 'longitude' in conditions:
		new_conditions['LONGITUDE'] = conditions['longitude']
	if 'precipitation' in conditions:
		new_conditions['PRCP'] = conditions['precipitation']
	if 'snowdepth' in conditions:
		new_conditions['SNWD'] = conditions['snowdepth']
	if 'tmax' in conditions:
		new_conditions['TMAX'] = conditions['tmax']
	if 'tmin' in conditions:
		new_conditions['TMIN'] = conditions['tmin']
	return new_conditions


# Display the search result
@bottle.route('/search')
def show_result():
	return bottle.template('result', {"Items": search_in_db()})


bottle.debug(True)
bottle.run(host='localhost', port = 8082)

