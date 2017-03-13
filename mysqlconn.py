#!/usr/bin/python3

import pymysql


db = pymysql.connect("localhost","peng","1234","python3")

cursor = db.cursor()

cursor.execute("show variables like \"max_connections\"")

data = cursor.fetchone()

print (data[0],data[1])


db.close()
