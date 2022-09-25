import sqlite3 as db

connection = db.connect("data/scrum.db")
cursor = connection.cursor()

contacts = {'contacts_id': '',
         'contacts_stuff_id': '',
         'contacts_main_tel': '',
         'contacts_second_tel': '',
         'contacts_mail': '',
         'contacts_telegram': ''}
contacts_list = []


def read_contacts():
    global contacts_list
    items = cursor.execute("SELECT * FROM contacts").fetchall()
    for item in items:
        contacts_list.append(dict(zip(contacts, item)))


read_contacts()
print(contacts_list)