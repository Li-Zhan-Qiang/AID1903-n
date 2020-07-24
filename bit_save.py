import pymysql
import sys

import string


print(sys.argv)

db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     passwd='mysql',
                     database='stu',
                     charset='utf8')
cur = db.cursor()

with open('mysql.jpg', 'rb') as fd:
    data = fd.read()
try:
    sql = "insert into Images values (1, 'mysql.jpg', _binary %s)"
    cur.execute(sql, [data])
    db.commit()
except Exception as e:
    db.rollback()
    print(e)
# sql = "select * from Images where filename='mysql.jpg';"
# cur.execute(sql)
# image = cur.fetchone()
# with open(image[1], 'wb') as fd:
#     fd.write(image[2])
cur.close()
db.close()