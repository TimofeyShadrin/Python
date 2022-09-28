import sqlite3 as db
from random import randint, shuffle
from datetime import datetime, date, time


posts = ['scrum-master', 'разработчик', 'тестировщик', 'дизайнер', 'аналитик']
result = []


stuff_id = [i for i in range(1, 21)]
shuffle(stuff_id)


def list_of_posts():
    global result
    global posts
    result.append(posts[0])
    for i in range(4):
        result.append(posts[2])
        result.append(posts[3])
        result.append(posts[4])
    while len(result) != 20:
        result.append(posts[1])
    shuffle(result)


list_of_posts()
print(result)
print(stuff_id)


def create_post():
    connection = db.connect("scrum.db")
    cursor = connection.cursor()
    for i in range(1, 21):
        dt = date(randint(2019, 2021), randint(1, 12), randint(1, 28))
        sql = f'''
                INSERT INTO post
                    (post_id, post_stuff_id, post_post, post_date)
                VALUES
                    ({i}, {stuff_id[i - 1]}, '{result[i - 1]}', '{dt}');
                '''
        cursor.execute(sql).fetchall()
    connection.commit()


create_post()
