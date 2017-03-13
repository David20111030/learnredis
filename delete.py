#!/usr/bin/python3

import pymysql

db = pymysql.connect('localhost','peng','1234','python3')

cursor = db.cursor()

sql = "delete from employee where age > '%d'" % (2)

try:
	cursor.execute(sql)
	db.commit()

except:
	db.rollback()

db.close()
