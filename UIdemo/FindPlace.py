'''
	This is a program allowing users to search a particular place in China
	by inputing certain conditions
'''
import pymongo
from pymongo import MongoClient
import bottle
import pprint

connection = MongoClient('localhost', 27017)
db = connection.weather

conditions = {}

# Initialize the home page
@bottle.route('/')
def make_home_page():
	global conditions
	conditions.clear()
	return bottle.template('home_page')

# Called after user press the button
# Get the given conditions from text boxes in the homepage
@bottle.post('/')
def process_search():
	global conditions

	conditions['elevation'] = (bottle.request.forms.get('elevation'))
	conditions['latitude'] = (bottle.request.forms.get('latitude'))
	conditions['longitude'] = (bottle.request.forms.get('longitude'))
	conditions['prcp'] = (bottle.request.forms.get('prcp'))
	conditions['snwd'] = (bottle.request.forms.get('snwd'))
	conditions['tmax'] = (bottle.request.forms.get('tmax'))
	conditions['tmin'] = (bottle.request.forms.get('tmin'))

	conditions = check_input(conditions)
	pprint.pprint(conditions)
	bottle.redirect("/search")

# Eliminate empty input and ensure valid conditions
def check_input(conditions):
	new_conditions = {}
	for item in conditions:
		if conditions[str(item)] != '':
			try:
				new_conditions[str(item)] = float(conditions[str(item)])
			except:
				print('Error')
				bottle.redirect("/")
				pass
	return new_conditions

# Use the given conditions to search in the database
def search_in_db():
	global conditions
	print('search_in_db')
	pprint.pprint(conditions)
	conditions = modify_dic(conditions)
	items = db.temperature.find(conditions)

	return items

def modify_dic(conditions):
	new_conditions = {}
	for item in conditions:
		new_conditions[item.upper()] = conditions[item]
	# For temperature range search
	new_conditions['TMAX'] = {'$lt': conditions['tmax']}
	new_conditions['TMIN'] = {'$gt': conditions['tmin']}

	return new_conditions

# Display the search result
@bottle.route('/search')
def show_result():
	global conditions
	return bottle.template('result', {"Items": search_in_db()})

@bottle.post('/search')
def go_back():
	conditions.clear()
	bottle.redirect('/')
bottle.debug(True)
bottle.run(host='localhost', port = 8082)

