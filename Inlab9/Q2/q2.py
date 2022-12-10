# AUTHOR: ASHWIN ABRAHAM

import sqlite3
import sys

sqliteConnection = sqlite3.connect('zipcodesDB.db')
sqlite_create_table_query = '''CREATE TABLE zipcodesInfo (
                                zip_code TEXT PRIMARY KEY,
                                latitude REAL NOT NULL,
                                longitude REAL NOT NULL,
                                city TEXT,
                                state TEXT,
                                county TEXT);'''
cursor = sqliteConnection.cursor()
cursor.execute(sqlite_create_table_query)
sqliteConnection.commit()

states = set()

with open('zipcodes.csv') as file:
    for line in file:
        if(line.split(',')[0] == 'zip_code'):
            continue
        t = line.split(',')
        states.add(t[4])
        insert_q = f"INSERT INTO zipcodesInfo (zip_code, latitude, longitude, city, state, county) VALUES (?, ?, ?, ?, ?, ?);"
        # print(insert_q)
        cursor.execute(insert_q, t)

state = sys.argv[1]
# if state in states:
state_q = f"SELECT city, county, MAX(latitude) FROM zipcodesInfo WHERE state='{state}';"
variab = cursor.execute(state_q)
records = variab.fetchall()
cit = (records[0][0], records[0][1])
new_q = f"SELECT zip_code FROM zipcodesInfo WHERE city='{cit[0]}' AND state='{state}' AND county='{cit[1]}';"
new_var = cursor.execute(new_q)
l = new_var.fetchall()
# for x in records:
#     l.append(x[0])
# print(l)
if l != []:
    l.sort()
    final_s = ''
    for t in l:
        final_s += t[0]+','
    print(final_s[:-1])
else:
    print('NOT FOUND')
cursor.close()
sqliteConnection.close()