import csv
import sqlite3 as db
from random import randint, shuffle
from datetime import datetime, date, time


list_of_name_m = []
list_of_name_w = []
list_of_surname_m = []
list_of_surname_w = []


def create_name_m():
    global list_of_name_m
    with open('name_m.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            list_of_name_m.append(''.join(row))


def create_name_w():
    global list_of_name_w
    with open('name_w.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            list_of_name_w.append(''.join(row))


def create_surname_m():
    global list_of_surname_m
    with open('surname.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            list_of_surname_m.append(''.join(row))


def create_surname_w():
    global list_of_surname_w
    with open('surname.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            temp = ''.join(row) + 'а'
            list_of_surname_w.append(temp)


def create_stuff():
    connection = db.connect("scrum.db")
    cursor = connection.cursor()
    global list_of_name_m
    global list_of_name_w
    global list_of_surname_m
    global list_of_surname_w
    contacts_id = [i for i in range(1, 21)]
    shuffle(contacts_id)
    post_id = [i for i in range(1, 21)]
    shuffle(post_id)
    status_id = [i for i in range(1, 21)]
    shuffle(status_id)
    for i in range(1, 21):
        dt = date(randint(1975, 1999), randint(1, 12), randint(1, 28))
        choose = randint(0, 1)
        if choose == 0:
            name = list_of_name_m[randint(0, len(list_of_name_m) - 1)]
            surname = list_of_surname_m[randint(0, len(list_of_surname_m) - 1)]
        else:
            name = list_of_name_w[randint(0, len(list_of_name_w) - 1)]
            surname = list_of_surname_w[randint(0, len(list_of_surname_w) - 1)]
        sql = f'''
        INSERT INTO stuff
            (stuff_id, stuff_name, stuff_surname, stuff_date_birth, stuff_contacts_id, stuff_post_id, stuff_status_id)
        VALUES
            ({i}, '{name}', '{surname}', '{dt}', {contacts_id[i - 1]}, {post_id[i - 1]}, {status_id[i - 1]});
        '''
        cursor.execute(sql).fetchall()
    connection.commit()


create_name_m()
create_name_w()
create_surname_m()
create_surname_w()
create_stuff()
