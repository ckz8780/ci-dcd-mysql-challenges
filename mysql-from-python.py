# Don't forget to run mysqld before running this so we have something to connect to!
# mysql-ctl start should work on Cloud 9

import os
import pymysql

# Get username from Cloud9 Workspace
# Modify accordingly

username = os.getenv('C9_USER')

# Connect to the DB
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

# Try to run a query:
try:
    with connection.cursor() as cursor:
        sql = 'select * from Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally: 
    # Close the connection regardless of whether the above was successful
    connection.close()
    
