import sqlite3 as db

connection = db.connect("data/scrum.db")
cursor = connection.cursor()

stuff = {'stuff_id': '',
         'stuff_name': '',
         'stuff_surname': '',
         'stuff_date_birth': '',
         'stuff_contacts_id': '',
         'stuff_post_id': '',
         'stuff_status_id': ''}
stuff_list = []


def read_stuff():
    global stuff_list
    items = cursor.execute("SELECT stuff_name, stuff_surname, stuff_date_birth FROM stuff").fetchall()
    for item in items:
        stuff_list.append(dict(zip(stuff, item)))


read_stuff()
print(stuff_list)