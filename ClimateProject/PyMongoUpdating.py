import pymongo
import datetime
import sys

connection = pymongo.Connection("mongodb://localhost", safe=True)

def remove_review_date():
	db = connection.school
	scores = db.scores
	try:
		scores.update({}, {'$unset':{'review_date':1}}, multi=True)
	except:
		print 'Unexpected Error'

def using_save():
	db = connection.school
	scores = db.scores
	try:
		score = scores.findOne({'student_id':1, 'type':'homework'})
		print 'before', score
		score['review_date'] = datetime.datetime.utcnow()
		score.save(score)
		score = scores.findOne({'student_id':1, 'type':'homework'})
		print 'after', score
	except:
		print 'Unexpected Error', sys.exc_info()[0]

def using_update():
	db = connection.school
	scores = db.scores
	try:
		score = scores.findOne({'student_id':1, 'type':'homework'})
		print 'before', score
		score['review_date'] = datetime.datetime.utcnow()
		scores.update({'student_id':1, 'type':'homework'}, score)
		score = scores.findOne({'student_id':1, 'type':'homework'})
		print 'after', score
	except:
		print 'Unexpcected Error'

def using_set():
	db = connection.school
	scores = db.scores
	try:
		score = scores.findOne({'student_id':1, 'type':'homework'})
		print 'before', score
		scores.update({'student_id':1, 'type':'homework'}, {'$set':{'review_date':datetime.datetime.utcnow()}})
		score = scores.findOne({'student_id':1, 'type':'homework'})
		print 'after', score
	except:
		print 'Unexpcected Error'

print using_save
using_save()
remove_review_date()
print using_update
using_update()
remove_review_date()
print using_set
using_set()
remove_review_date()
