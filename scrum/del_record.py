import sqlite3 as db
from scrum.find import find_worker as fw


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


def del_record():
    index = serial()
    connection = db.connect("data/scrum.db")
    cursor = connection.cursor()
    sql = f"DELETE FROM stuff WHERE stuff_id = {index}"
    cursor.execute(sql).fetchall()
    connection.commit()
    sql = f"DELETE FROM status WHERE status_stuff_id = {index};"
    cursor.execute(sql).fetchall()
    connection.commit()
    sql = f"DELETE FROM post WHERE post_stuff_id = {index};"
    cursor.execute(sql).fetchall()
    connection.commit()
    sql = f"DELETE FROM contacts WHERE contacts_stuff_id = {index}"
    cursor.execute(sql).fetchall()
    connection.commit()
    print('Deletion completed successfully!')
