import sqlite3 as db
from datetime import datetime, date, time


def change_status(stuff_id: int, text: str):
    connection = db.connect("data/scrum.db")
    cursor = connection.cursor()
    dt_now = str(date.today())
    print(dt_now)
    sql = f'''
                UPDATE status
                SET status_status = '{text}',
                status_date = '{dt_now}'
                WHERE status_stuff_id = '{stuff_id}'
                '''
    cursor.execute(sql).fetchall()
    connection.commit()

