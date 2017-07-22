import pymysql

db = pymysql.connect(host='bdm259869163.my3w.com', port=3306, user='bdm259869163', passwd='********',
                     db='bdm259869163_db')

cursor = db.cursor()

cursor.execute('SELECT VERSION()')

data = cursor.fetchone();

print('Data version : %s' % data)

# cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

SQL_CREATE = '''CREATE TABLE IF NOT EXISTS EMPLOYEE(
                ID BIGINT(8) UNSIGNED PRIMARY KEY AUTO_INCREMENT,
                FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT )'''

cursor.execute(SQL_CREATE)

SQL_INSERT = '''INSERT INTO EMPLOYEE 
                (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
                VALUE 
                ('CAT', 'COOL', 18, '1', '2000')'''

try:
    cursor.execute(SQL_INSERT)
    db.commit()
except:
    db.rollback()

SQL_SELECT = '''SELECT * FROM EMPLOYEE'''

cursor.execute(SQL_SELECT)

results = cursor.fetchall()

for row in results:
    id_ = row[0]
    first_name = row[1]
    last_name = row[2]

    print('id:%d, first_name:%s, last_name:%s' % (id_, first_name, last_name))

SQL_DELETE = '''DELETE FROM EMPLOYEE WHERE ID = 1'''

try:
    cursor.execute(SQL_DELETE)
    db.commit()
except:
    db.rollback()

db.close()
