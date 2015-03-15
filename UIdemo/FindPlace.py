'''
	This is a program allowing users to search a particular place in China
	by inputing certain conditions :)
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

	#	这里你只考虑为空的情况，没有考虑错误输入，我的demo有错误检测的内容哈，你要想想怎么办
	#	并且这段代码我总觉得还能精炼，不过先这么写吧

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
	# for item in conditions:
	# 	if conditions[item] == '':
	# 		conditions.pop(item)
	conditions = modify_dic(conditions)

	#	呃，你这里面的find条件是怎么回事
	items = db.condition.find(conditions)

	return items

def modify_dic(conditions):
	new_conditions = {}

	#这一行应该能代替上面的所有了吧
	for item in conditions:
		new_conditions[item.upper()] = conditions[item]
		
	# For temperature range search
	new_conditions['TMAX'] = {'$lt': conditions['tmax']}
	new_conditions['TMIN'] = {'$gt': conditions['tmin']}

	return new_conditions


#	至于你说的不能范围查找，你还是没搞清楚JSON文件和字典的关系
#	"DATE" : {'$gt': earliest, '$lt': latest}
#	上面这句话能范围查找DATE吧，首先说明DATE关键字内容对应{'$gt': earliest, '$lt': latest}吧
#	那么DATE关键字对应的是不是又是一个字典，其中'$gt'字段对应earliest
#   温度不也一样吗，你 dic['Temperature']['$gt'] ＝ Tmax  难道不行吗？  意思是这个意思，再琢磨琢磨
#	还有，既然是提交了。。。就把没用的注释乱七八糟的删了，到时候直接提交到那边去的，注释什么的，都规范点呐


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

