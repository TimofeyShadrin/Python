import random
import sqlite3 as db
from random import randint
from transliterate import translit
import read_stuff as rs


second_tel = ''
mail = ''


def create_second_tel():
    global second_tel
    choose = randint(0, 1)
    if choose == 0:
        second_tel = f'+7 ({randint(901, 999)}) ' \
                     + f'{randint(100, 999)}-' \
                     + f'{randint(10, 99)}-' \
                     + f'{randint(10, 99)} '
    else:
        second_tel = 'None'


def create_mail(name: str, surname: str):
    global mail
    choose = randint(0, 1)
    if choose == 0:
        eng_name = str(translit(name.lower(), language_code='ru', reversed=True)).replace('\'', '')
        eng_surname = str(translit(surname.lower(), language_code='ru', reversed=True)).replace('\'', '')
        web = random.choice(['mail', 'yandex'])
        mail = f'{eng_name}_{eng_surname}@{web}.ru'
    else:
        mail = 'None'


telegram = ''


def create_telegram(surname: str):
    global telegram
    eng_surname = str(translit(surname.lower(), language_code='ru', reversed=True)).replace('\'', '')
    telegram = f'@{eng_surname}'


def create_contacts():
    connection = db.connect("data/scrum.db")
    cursor = connection.cursor()
    rs.read_stuff()
    global mail
    global telegram
    global second_tel
    temp = [[] for _ in range(20)]
    for i in range(1, 21):
        under = []
        main_tel = f'+7 ({randint(901, 999)}) ' \
                   + f'{randint(100, 999)}-' \
                   + f'{randint(10, 99)}-' \
                   + f'{randint(10, 99)}'
        create_second_tel()
        create_mail(rs.stuff_list[i - 1]['stuff_name'], rs.stuff_list[i - 1]['stuff_surname'])
        create_telegram(rs.stuff_list[i - 1]['stuff_surname'])
        under.append(rs.stuff_list[i - 1]['stuff_id'])
        under.append(main_tel)
        under.append(second_tel)
        under.append(mail)
        under.append(telegram)
        index = int(rs.stuff_list[i - 1]['stuff_contacts_id']) - 1
        temp[index] = under
    print(temp)
    for j in range(1, 21):
        sql = f'''
                INSERT INTO contacts
                    (contacts_id,
                    contacts_stuff_id,
                    contacts_main_tel,
                    contacts_second_tel,
                    contacts_mail,
                    contacts_telegram)
                VALUES
                    ({j}, {temp[j - 1][0]}, '{temp[j - 1][1]}', '{temp[j - 1][2]}', 
                    '{temp[j - 1][3]}', '{temp[j - 1][4]}');
        '''
        cursor.execute(sql).fetchall()
    connection.commit()

create_contacts()
