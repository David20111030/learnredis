#!/usr/bin/python3

import pymysql

db = pymysql.connect('localhost','peng','1234','python3')

cursor = db.cursor()

sql = "select * from employee where income > '%d'" % (1000)

try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		fname = row [0]
		lname = row [1]
		age = row [2]
		sex = row [3]
		income = row[4]
		print ("fname=%s,fname=%s,fname=%d,fname=%s,fname=%d"  
			% (fname,lname,age,sex,income))
except:
	print ("ERROR:unable to fetch data")

db.close()