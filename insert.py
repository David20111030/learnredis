#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost","peng","1234","python3")

cursor = db.cursor()

insert="""insert into employee(
        first_name,
        last_name,
        age,
        sex,
        income)
        values('tangkun','peng','24','M','2000')"""

try:
	cursor.execute(insert)
except:
	db.rollback()

db.close()
