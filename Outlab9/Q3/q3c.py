# AUTHOR: ASHWIN ABRAHAM

import sqlite3

connection = sqlite3.connect('ipl.db')
cursor = connection.cursor()

q1 = '''SELECT runs_scored, striker FROM BALL_BY_BALL;'''
var = cursor.execute(q1)
records = var.fetchall()

runs = {}

for x in records:
    if x[1] not in runs:
        runs[x[1]] = 0
    runs[x[1]] += x[0]

id_to_name = {}

q2 = '''SELECT player_id, player_name FROM PLAYER;'''
var2 = cursor.execute(q2)
rec2 = var2.fetchall()

for x in rec2:
    id_to_name[x[0]] = x[1]

l = sorted([(-runs[id], id_to_name[id], id) for id in runs])[:20]
for t in l:
    print(f'{t[2]},{t[1]},{-t[0]}')

cursor.close()
connection.close()