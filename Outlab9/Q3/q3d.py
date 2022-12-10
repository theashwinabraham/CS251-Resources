import sqlite3

connection = sqlite3.connect('ipl.db')
cursor = connection.cursor()

connection.execute('''CREATE TABLE POINTS_TABLE
         (team_id INT PRIMARY KEY,
         team_name TEXT,
         points INT,
         nrr REAL);''')

quer = '''SELECT team_id, team_name FROM TEAM;'''
var = cursor.execute(quer)
records = var.fetchall()

for x in records:
    quer0 = f"INSERT INTO POINTS_TABLE (team_id, team_name, points, nrr) VALUES (?, ?, ?, ?);"
    cursor.execute(quer0, [x[0], x[1], 0, 0])

quer1 = '''SELECT match_id, team1, team2, match_winner, win_type, win_margin FROM MATCH;'''
var1 = cursor.execute(quer1)
rec1 = var1.fetchall()

for x in rec1:
    if x[3] == 'NULL' or x[4] == 'Tie':
        quer2 = f"SELECT points, nrr FROM POINTS_TABLE WHERE team_id = {x[1]};"
        quer3 = f"SELECT points, nrr FROM POINTS_TABLE WHERE team_id = {x[2]};"
        var2 = cursor.execute(quer2)
        rec2 = cursor.fetchall()
        win_old_p = rec2[0][0]
        win_old_n = rec2[0][1]
        var3 = cursor.execute(quer3)
        rec3 = cursor.fetchall()
        los_old_p = rec3[0][0]
        los_old_n = rec3[0][1]
        Quer4 = f"UPDATE POINTS_TABLE SET points = {1+win_old_p} WHERE team_id = {x[1]};"
        cursor.execute(Quer4)
        Quer5 = f"UPDATE POINTS_TABLE SET points = {1+los_old_p} WHERE team_id = {x[2]};"
        cursor.execute(Quer5)
    else:
        win_id = int(x[3])
        quer2 = f"SELECT points, nrr FROM POINTS_TABLE WHERE team_id = {win_id};"
        quer3 = f"SELECT points, nrr FROM POINTS_TABLE WHERE team_id = {x[1]+x[2]-win_id};"
        var2 = cursor.execute(quer2)
        rec2 = cursor.fetchall()
        win_old_p = rec2[0][0]
        win_old_n = rec2[0][1]
        var3 = cursor.execute(quer3)
        rec3 = cursor.fetchall()
        los_old_p = rec3[0][0]
        los_old_n = rec3[0][1]
        Quer4 = f"UPDATE POINTS_TABLE SET points = {2+win_old_p} WHERE team_id = {win_id};"
        cursor.execute(Quer4)
        if x[4] == 'runs':
            margin = x[5]/20
        else:
            margin = x[5]/10
            Quer5 = f"UPDATE POINTS_TABLE SET nrr = {win_old_n+margin} WHERE team_id = {win_id};"
            Quer6 = f"UPDATE POINTS_TABLE SET nrr = {los_old_n-margin} WHERE team_id = {x[1]+x[2]-win_id};"
            cursor.execute(Quer5)
            cursor.execute(Quer6)
    connection.commit()

final_quer = '''SELECT team_id, team_name, points, nrr FROM POINTS_TABLE;'''
fvar = cursor.execute(final_quer)
frec = fvar.fetchall()

ffrec = sorted([(-x[2], -x[3], x[0], x[1]) for x in frec])
for x in ffrec:
    print(f'{x[2]},{x[3]},{-x[0]},{"%.2f"%round(-x[1], 2)}')