import sqlite3 as db
import os

status = {'name': '',
          'surname': '',
          'status': '',
          'data': '',
          'id': ''}

status_list = []


def view_status(surname: str):
    connection = db.connect("data/scrum.db")
    cursor = connection.cursor()
    global status_list
    items = cursor.execute("SELECT "
                           "stuff_name, stuff_surname, status_status, status_date, status_stuff_id FROM "
                           "stuff INNER JOIN status "
                           "ON stuff_id = status_stuff_id WHERE stuff_surname LIKE "
                           f"'%{surname.lower().title()}%'").fetchall()
    for item in items:
        status_list.append(dict(zip(status, item)))
    for row in status_list:
        count = 1
        for key, value in row.items():
            if key != 'name' and key != 'surname':
                print(f'{key}: {value}', end='; ')
            else:
                if count < 2:
                    print(f'{value}', end=' ')
                    count += 1
                else:
                    print(f'{value}', end=' - ')
        print('')
    status_list.clear()

