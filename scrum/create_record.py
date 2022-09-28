import sqlite3 as db
from datetime import date


def create_record():
    add_dict = {'name': '',
                'surname': '',
                'date birth': '',
                'main tel': '',
                'second tel': '',
                'e-mail': '',
                'telegram': '',
                'post': ''}
    for key, value in add_dict.items():
        add_dict[key] = input(f'Please enter {key}: ')

    connection = db.connect("data/scrum.db")
    cursor = connection.cursor()

    stuff_id = cursor.execute("SELECT max(stuff_id) FROM stuff").fetchall()
    new_stuff_id = int(*stuff_id[0]) + 1

    status_id = cursor.execute("SELECT max(status_id) FROM status").fetchall()
    new_status_id = int(*status_id[0]) + 1

    post_id = cursor.execute("SELECT max(post_id) FROM post").fetchall()
    new_post_id = int(*post_id[0]) + 1

    contacts_id = cursor.execute("SELECT max(contacts_id) FROM contacts").fetchall()
    new_contacts_id = int(*contacts_id[0]) + 1

    sql = f'''
            INSERT INTO stuff
                (stuff_id, stuff_name, stuff_surname, stuff_date_birth, stuff_contacts_id, 
                stuff_post_id, stuff_status_id)
            VALUES
                ({new_stuff_id}, '{add_dict['name']}', '{add_dict['surname']}', '{add_dict['date birth']}', 
                {new_contacts_id}, {new_post_id}, {new_status_id});
            '''
    cursor.execute(sql).fetchall()
    connection.commit()

    dt = date.today()

    sql = f'''
                INSERT INTO status
                    (status_id, status_stuff_id, status_status, status_date)
                VALUES
                    ({new_status_id}, {new_stuff_id}, 'работает', '{dt}');
                '''
    cursor.execute(sql).fetchall()
    connection.commit()

    sql = f'''
                INSERT INTO post
                    (post_id, post_stuff_id, post_post, post_date)
                VALUES
                    ({new_post_id}, {new_stuff_id}, '{add_dict['post']}', '{dt}');
                '''
    cursor.execute(sql).fetchall()
    connection.commit()

    sql = f'''
                INSERT INTO contacts
                    (contacts_id, contacts_stuff_id, contacts_main_tel, contacts_second_tel, 
                    contacts_mail, contacts_telegram)
                VALUES
                    ({new_contacts_id}, {new_stuff_id}, '{add_dict['main tel']}', '{add_dict['second tel']}', 
                    '{add_dict['e-mail']}', '{add_dict['telegram']}');
                '''
    cursor.execute(sql).fetchall()
    connection.commit()
    print('Record successfully added!')
