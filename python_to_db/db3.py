import mysql.connector

db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password',
    database='pythondecember'
)

cursor=db.cursor()
sql="insert into movie values(101,'Pirates of Carribean 2','2006',7.5)"
try:
    cursor.execute(sql)
    print("Value inserted")
    db.commit()
except Exception as e:
    print(e.args)
    db.rollback()
db.close()
