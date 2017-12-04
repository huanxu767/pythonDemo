# coding: utf8

import mysql.connector

config = {
    'user': 'root',
    'password': '1234',
    'host': '127.0.0.1',
    'password':'1234',
    'database':'risk'
}

conn=mysql.connector.connect(**config)
cursor=conn.cursor()
cursor.execute("SELECT * FROM common_mobile_address WHERE status_type = '1' limit 5") #表查询
values =cursor.fetchall()
print(values)
cursor.close()