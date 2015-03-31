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
	PlaceOptions = db.condition.distinct('STATION_NAME')
	return bottle.template('home_page', {'PlaceOptions': PlaceOptions})

# Called after user press the button
# Get the given conditions from text boxes in the homepage
@bottle.post('/')
def process_search():
	global conditions
	conditions.clear()
	conditions['elevation'] = (bottle.request.forms.get('minelevation'), bottle.request.forms.get('maxelevation'))
	conditions['latitude'] = (bottle.request.forms.get('minlatitude'), bottle.request.forms.get('maxlatitude'))
	conditions['longitude'] = (bottle.request.forms.get('minlongitude'), bottle.request.forms.get('maxlongitude'))
	conditions['date'] = (bottle.request.forms.get('mindate'),bottle.request.forms.get('maxdate'))
	conditions['prcp'] = (bottle.request.forms.get('minprcp'),bottle.request.forms.get('maxprcp'))
	conditions['snwd'] = (bottle.request.forms.get('minsnwd'),bottle.request.forms.get('maxsnwd'))
	conditions['tmax'] = ((bottle.request.forms.get('mintmax')),bottle.request.forms.get('maxtmax'))
	conditions['tmin'] = ((bottle.request.forms.get('mintmin')),bottle.request.forms.get('maxtmin'))

	# Determine the specific station_name
	place = (bottle.request.forms.get('station_name'))

	conditions = check_input(conditions)
	bottle.redirect("/search")

# Eliminate empty input and ensure valid conditions
def check_input(conditions):
	pprint.pprint(conditions)
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
	items = db.condition.find(conditions)

	return items

@bottle.post('/search')
def go_back():
	bottle.redirect('/')

bottle.debug(True)
bottle.run(host='localhost', port = 8082)

