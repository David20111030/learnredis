#!/usr/bin/python3

import pymysql

db = pymysql.connect("localhost","peng","1234","python3")

cursor = db.cursor()
dropExists ="drop table if exists employee"
create="""create table employee(
	FIRST_NAME CHAR(20) NOT NULL,
	LAST_NAME CHAR(20),
	AGE INT,
	SEX CHAR(1),
	INCOME FLOAT
)"""
cursor.execute(dropExists)
cursor.execute(create)

db.close()
