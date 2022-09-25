import sqlite3 as db

connection = db.connect("data/scrum.db")
cursor = connection.cursor()

status = {'status_id': '',
         'status_stuff_id': '',
         'status': '',
         'date': ''}
status_list = []


def read_status():
    global status_list
    items = cursor.execute("SELECT * FROM status").fetchall()
    for item in items:
        status_list.append(dict(zip(status, item)))


read_status()
print(status_list)
