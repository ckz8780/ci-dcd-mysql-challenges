# Don't forget to run mysqld before running this so we have something to connect to!
# mysql-ctl start should work on Cloud 9

import os
import datetime
import pymysql

# Get username from Cloud9 Workspace
# Modify accordingly

username = os.getenv('C9_USER')

# Connect to the DB
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

# Try to run some queries!
try:
    # Print all results, no formatting
    with connection.cursor() as cursor:
        sql = 'select * from Artist;'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        
    # Print results row by row
    with connection.cursor() as cursor:
        sql = 'select * from Artist;'
        cursor.execute(sql)
        for row in cursor:
            print(row)
    
    # Use a dictionary cursor instead of default tuple cursor
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        sql = 'select * from Artist;'
        cursor.execute(sql)
        for row in cursor:
            print(row)
            
    # Create a table
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                          Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the table already exists
            
    
finally: 
    # Close the connection regardless of whether the above was successful
    connection.close()
    
