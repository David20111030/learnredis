#!/usr/bin/python3

import pymysql

db = pymysql.connect('localhost','peng','1234','python3')

cursor = db.cursor()

sql = "update employee set age = age+1 where sex='%c'" % ('M')

try:
	cursor.execute(sql)
	db.commit()

except:
	db.rollback()

db.close()
