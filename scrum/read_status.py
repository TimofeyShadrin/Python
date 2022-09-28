import sqlite3 as db
from scrum.find import find_worker as fw

status_list = []


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


def read_status():
    global status_list
    index = serial()
    connection = db.connect("data/scrum.db")
    cursor = connection.cursor()
    status = {'name': '',
              'surname': '',
              'status': '',
              'status_date': ''
              }
    items = cursor.execute("SELECT stuff_name, stuff_surname, "
                           "status_status, status_date FROM stuff INNER JOIN status "
                           "ON stuff_id = status_stuff_id WHERE "
                           f"stuff_id = '{index}'").fetchall()
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
    print()

