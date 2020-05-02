import json
import sqlite3

conn = sqlite3.connect('courseDB.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Course(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );

    CREATE TABLE Member(
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY(user_id, course_id)
    );
''')

fname = input("Enter a file Name: ")
file = open(fname).read()

js = json.loads(file)

for element in js:
    user = element[0]
    course = element[1]
    role = element[2]

    if user is None or course is None or role is None:
        continue

    print(user, course, role)

    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES (?)''', (user, ))
    cur.execute('''SELECT id FROM User WHERE name = ?''', (user, ))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES (?)''', (course,))
    cur.execute('''SELECT id FROM Course WHERE title = ?''', (course, ))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
        VALUES (?, ?, ?)''', (user_id, course_id, role))

    conn.commit()
