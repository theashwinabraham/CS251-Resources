import sqlite3

connection = sqlite3.connect('ipl.db')
cursor = connection.cursor()
stad_sum = {}
stad_num = {}

q1 = '''SELECT match_id, venue_name FROM MATCH;'''
var = cursor.execute(q1)
records = var.fetchall()

for x in records:
    if x[1] not in stad_sum:
        stad_sum[x[1]] = 0
        stad_num[x[1]] = 0
    q2 = f"SELECT runs_scored, extra_runs FROM BALL_BY_BALL WHERE match_id='{x[0]}'"
    var2 = cursor.execute(q2)
    run_r = var2.fetchall()
    stad_num[x[1]] += 1
    for y in run_r:
        stad_sum[x[1]] += (y[0]+y[1])

# print(stad_sum)
# print('\n')
# print(stad_num)
# print('\n')
stad_avg = [(-stad_sum[stad]/stad_num[stad], stad) for stad in stad_num]
stad_avg.sort()
for x in stad_avg:
    if x[1] != 'NULL':
        print(f'{x[1]}, {"%.2f"%round(-x[0], 2)}')

cursor.close()
connection.close()