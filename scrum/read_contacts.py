import sqlite3 as db
from scrum.find import find_worker as fw

contacts_list = []


def serial():
    try:
        item = int(input('Please select the serial number: '))

def read_contacts():
    index = serial()
    connection = db.connect("data/scrum.db")
    cursor = connection.cursor()
    contacts = {'contacts_id': '',
                'contacts_stuff_id': '',
                'main_tel': '',
                'second_tel': '',
                'e-mail': '',
                'telegram': ''}
    global contacts_list
    items = cursor.execute("SELECT stuff_name, stuff_surname, contacts_main_tel, "
                           "contacts_second_tel, contacts_mail, contacts_telegram FROM stuff INNER JOIN contacts "
                           "ON stuff_id = contacts_stuff_id WHERE "
                           f"contacts_main_tel = '{index}'").fetchall()
    for item in items:
        contacts_list.append(dict(zip(contacts, item)))

