import sqlite3 as db

connection = db.connect("data/scrum.db")
cursor = connection.cursor()

all = {'name': '',
         'surname': '',
         'date birth': '',
         'main tel': '',
         'e-mail': '',
         'post': '',
         'status': ''}
all_list = []


def view_one(surname: str):
    global all_list
    items = cursor.execute("SELECT "
                           "stuff_name, stuff_surname, stuff_date_birth, contacts_main_tel, "
                           "contacts_mail, post_post, status_status FROM "
                           "stuff INNER JOIN "
                           "(contacts INNER JOIN "
                           "(status INNER JOIN post ON status_stuff_id = post_stuff_id) "
                           "ON contacts_stuff_id = status_stuff_id) "
                           f"ON stuff_id = contacts_stuff_id WHERE stuff_surname = "
                           f"'{surname.lower().title()}'").fetchall()
    for item in items:
        all_list.append(dict(zip(all, item)))
    for row in all_list:
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


def view_all(surname = '*'):
    if surname == '*':
        global all_list
        items = cursor.execute("SELECT "
                               "stuff_name, stuff_surname, stuff_date_birth, contacts_main_tel, "
                               "contacts_mail, post_post, status_status FROM "
                               "stuff INNER JOIN "
                               "(contacts INNER JOIN "
                               "(status INNER JOIN post ON status_stuff_id = post_stuff_id) "
                               "ON contacts_stuff_id = status_stuff_id) "
                               f"ON stuff_id = contacts_stuff_id").fetchall()
        for item in items:
            all_list.append(dict(zip(all, item)))
        for row in all_list:
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
    else:
        view_one(surname)
