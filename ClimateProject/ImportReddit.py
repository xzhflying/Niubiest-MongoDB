import pymongo
import json
import urllib2

connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.school
students = db.students

def load():
	reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")

	parsed = json.loads(reddit_page.read())
	for item in parsed['data']['children']:
		#print(item)
		stories.insert(item['data'])

def find():
	#query = {'title':{'$regex':'Microsoft'}}
	query = {}
	selector = {'_id':0}

	try:
		iter = students.find(query, selector).sort([('student_id', pymongo.ASCENDING),('score', pymongo.DESCENDING)]).skip(2).limit(5)
	except:
		print 'Unexcepted Error'

	sanity = 1
	for item in iter:
		print(item)
		sanity += 1
		
find()