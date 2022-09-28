import sqlite3 as db
from random import randint, shuffle
from datetime import datetime, date, time


status = ['уволен', 'работает', 'в отпуске', 'на больничном']
result = []


stuff_id = [i for i in range(1, 41)]
shuffle(stuff_id)


def list_of_status():
    global result
    global status
    for i in range(8):
        result.append(status[0])
        result.append(status[2])
        result.append(status[3])
    while len(result) != 40:
        result.append(status[1])
    shuffle(result)


list_of_status()
print(result)
print(stuff_id)


def create_status():
    connection = db.connect("scrum.db")
    cursor = connection.cursor()
    for i in range(1, 41):
        dt = date(2022, randint(1, 12), randint(1, 28))
        sql = f'''
                INSERT INTO status
                    (status_id, status_stuff_id, status_status, status_date)
                VALUES
                    ({i}, {stuff_id[i - 1]}, '{result[i - 1]}', '{dt}');
                '''
        cursor.execute(sql).fetchall()
    connection.commit()


create_status()
