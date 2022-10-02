import sqlite3 as db

all_list = []
serial = []


def find_worker(phrase: str):
    connection = db.connect("C:/Users/tshad/OneDrive/Documents/Python/scrum/data/scrum.db")
    cursor = connection.cursor()
    global all_list
    workers = {'name': '',
               'surname': '',
               'date birth': '',
               'main tel': '',
               'e-mail': '',
               'post': '',
               'status': ''}

    if phrase == '':
        items = cursor.execute("SELECT "
                               "stuff_id, stuff_name, stuff_surname, stuff_date_birth, contacts_main_tel, "
                               "contacts_mail, post_post, status_status FROM "
                               "stuff INNER JOIN "
                               "(contacts INNER JOIN "
                               "(status INNER JOIN post ON status_stuff_id = post_stuff_id) "
                               "ON contacts_stuff_id = status_stuff_id) "
                               f"ON stuff_id = contacts_stuff_id").fetchall()
    else:
        items = cursor.execute("SELECT "
                               "stuff_id, stuff_name, stuff_surname, stuff_date_birth, contacts_main_tel, "
                               "contacts_mail, post_post, status_status FROM "
                               "stuff INNER JOIN "
                               "(contacts INNER JOIN "
                               "(status INNER JOIN post ON status_stuff_id = post_stuff_id) "
                               "ON contacts_stuff_id = status_stuff_id) "
                               f"ON stuff_id = contacts_stuff_id WHERE stuff_surname LIKE "
                               f"'{phrase.lower().title()}%' OR "
                               f"stuff_name LIKE '{phrase.lower().title()}%' "
                               f"OR contacts_main_tel LIKE '%{phrase}%' "
                               f"OR post_post LIKE '%{phrase}%' "
                               f"OR status_status LIKE '%{phrase}%'").fetchall()
    for item in items:
        all_list.append(dict(zip(workers, item[1::])))
        serial.append(item[0])
    for row in all_list:
        count = 1
        print(all_list.index(row), end=': ')
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
