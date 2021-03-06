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
    
    # Insert some data into the Friends table
    with connection.cursor() as cursor:
        row = ("bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
        
    # Insert a bunch of rows at once!
    with connection.cursor() as cursor:
        rows = [("Albert", 25, "1990-02-06 23:04:56"),
                ("Jim", 56, "1955-05-09 13:12:45"),
                ("Fred", 100, "1911-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s,%s,%s);", rows)
        connection.commit()
        
    # Let's change Bob's age to 22
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = 22 WHERE name = 'bob';")
        connection.commit()
        
    # You could also use string interpolation to do that...
    with connection.cursor() as cursor:
        cursor.execute("UPDATE Friends SET age = %s WHERE name = %s;",
                       (23, 'bob'))
        connection.commit()
        
    # And you can update many rows at a time just like inserting:
    with connection.cursor() as cursor:
        rows = [(28, 'bob'),
                (24, 'jim'),
                (29, 'fred')]
        cursor.executemany("UPDATE Friends SET age = %s WHERE name = %s;",
                           rows)
        connection.commit()
        
    # Bob has betrayed us. Let's delete him!
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = 'bob';")
        connection.commit()
        
    # He's come back begging for forgiveness...we'll add him in again, but we've got an agenda
    with connection.cursor() as cursor:
        row = ("bob", 21, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
        
    # We never liked Bob anyway. Here's an alternative way to delete him
    with connection.cursor() as cursor:
        rows = cursor.execute("DELETE FROM Friends WHERE name = %s;", 'bob')
        connection.commit()
        
    # Looks like Jim and Fred are mad at us now. Luckily we can delete them both at once
    with connection.cursor() as cursor:
        rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Jim', 'Fred'])
        connection.commit()
        
    # Finally, you can delete with a list and string formatting
    with connection.cursor() as cursor:
        list_of_names = ['Jim', 'Bob', 'Albert', 'Fred']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)
        connection.commit()
finally: 
    # Close the connection regardless of whether the above was successful
    print('You have zero friends :( ... (Check it! select * from Friends;)')
    connection.close()
    
