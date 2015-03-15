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
	return bottle.template('home_page')

# Called after user press the button
# Get the given conditions from text boxes in the homepage
@bottle.post('/')
def process_search():
	global conditions
	conditions.clear()
	conditions['elevation'] = (bottle.request.forms.get('elevation'))
	conditions['latitude'] = (bottle.request.forms.get('latitude'))
	conditions['longitude'] = (bottle.request.forms.get('longitude'))
	conditions['date'] = (bottle.request.forms.get('date'))
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
	new_conditions = modify_dic(conditions)
	items = db.condition.find(new_conditions)

	return items

def modify_dic(conditions):
	new_conditions = {}
	for item in conditions:
		new_conditions[item.upper()] = conditions[item]
	# For temperature range search 
	if new_conditions.has_key('TMAX'):
		new_conditions['TMAX'] = {'$lte': conditions['tmax']}
	if new_conditions.has_key('TMIN'):
		new_conditions['TMIN'] = {'$gte': conditions['tmin']}

	return new_conditions

# Display the search result
@bottle.route('/search')
def show_result():
	global conditions
	return bottle.template('result', {"Items": search_in_db()})

@bottle.post('/search')
def go_back():
	bottle.redirect('/')

bottle.debug(True)
bottle.run(host='localhost', port = 8082)

