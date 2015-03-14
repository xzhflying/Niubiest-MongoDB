import pymongo
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)

db = connection.school
people = db.people

def find_one():
	query = {'student_id': 10}
	try:
		doc = scores.find_one(query)
	except:
		print("Unexpected Error", sys.exc_info()[0])
	print(doc)


def find():
	query = {'type': 'exam', 'score':{'$gt':50, '$lt':80}} 
	selector = {'student_id':1, '_id':0}
	try:
	 	iter = scores.find(query, selector)
	except:
	 	print("Unexpected Error", sys.exc_info()[0])
	
	for doc in iter:
		print(doc)

def insert(person):
	try:
		people.insert(person)
	except:
		print('Unexpected Error', sys.exc_info()[0])

#find_one()
#find()
keyes = {'name':'Keyes', 'company':'10gen', 'interests':['running','swimming','hiking']}
insert(keyes)
cursor = people.find()
for item in cursor:
	print item