import sqlite3 as db

connection = db.connect("data/scrum.db")
cursor = connection.cursor()

post = {'post_id': '',
         'post_stuff_id': '',
         'post': '',
         'date': ''}
post_list = []


def read_post():
    global post_list
    items = cursor.execute("SELECT * FROM post").fetchall()
    for item in items:
        post_list.append(dict(zip(post, item)))


read_post()
print(post_list)
