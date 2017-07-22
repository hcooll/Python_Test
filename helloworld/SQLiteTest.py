import sqlite3

import sys

conn = sqlite3.connect('test.db')

cursor = conn.cursor()

try:
    cursor.execute('SELECT VERSION()')
    version = cursor.fetchone()
    print('SQLite version: %s' % version)
except sqlite3.OperationalError as ero:
    print('SQLite SELECT Version Error : %s  &  %s !' % (sys.exc_info()[0], ero))

try:
    SQL_DROP = '''DROP TABLE IF EXISTS STUDENT'''
    # cursor.execute(SQL_DROP)
    conn.commit()
except sqlite3.Error as ero:
    conn.rollback()
    print('DROP Error: %s!' % ero)

try:
    SQL_CREATE = '''CREATE TABLE IF NOT EXISTS STUDENT(
                    ID INTEGER NOT NULL PRIMARY KEY,
                    NAME CHAR(20),
                    GRADE CHAR(50),
                    CLASS CHAR(10),
                    SEX CHAR(1),
                    AGE INT)'''
    cursor.execute(SQL_CREATE)
    conn.commit()
except sqlite3.Error as ero:
    conn.rollback()
    print('CREATE Error: %s!' % ero)

try:
    SQL_INSERT = '''INSERT INTO STUDENT
                    (NAME, GRADE, CLASS, SEX, AGE)
                    VALUES
                    ('CATHCOOL', '高三', '三班','1',18)'''
    cursor.execute(SQL_INSERT)
    conn.commit()
except sqlite3.Error as ero:
    conn.rollback()
    print('INSERT Error: %s!' % ero)

try:
    SQL_SELECT = '''SELECT * FROM STUDENT'''
    cursor.execute(SQL_SELECT)
    for row in cursor.fetchall():
        print('id_:%s, name:%s, grade:%s, class:%s, sex:%s, age:%s' % (
            row[0], row[1], row[2], row[3], row[4], row[5]))
except sqlite3.Error as ero:
    print('SELECT Error: %s!' % ero)

conn.close()
