import sqlite3 as db
from scrum.find import find_worker as fw

contacts_list = []


def serial():
    while True:
        if len(fw.serial) > 1:
            try:
                item = int(input('Please select the serial number: '))
                if item < len(fw.serial):
                    stuff_id = fw.serial[item]
                    break
                else:
                    print('Your input is incorrect!')
            except:
                print('Your input is incorrect!')
        else:
            stuff_id = fw.serial[0]
            break
    return stuff_id


def read_contacts():
    index = serial()
    connection = db.connect("data/scrum.db")
    cursor = connection.cursor()
    contacts = {'name': '',
                'surname': '',
                'main_tel': '',
                'second_tel': '',
                'e-mail': '',
                'telegram': ''}
    global contacts_list
    items = cursor.execute("SELECT stuff_name, stuff_surname, contacts_main_tel, "
                           "contacts_second_tel, contacts_mail, contacts_telegram FROM stuff INNER JOIN contacts "
                           "ON stuff_id = contacts_stuff_id WHERE "
                           f"stuff_id = '{index}'").fetchall()
    for item in items:
        contacts_list.append(dict(zip(contacts, item)))
    for row in contacts_list:
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
    print()
