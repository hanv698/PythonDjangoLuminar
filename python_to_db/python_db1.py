#step1: import mysql connector
import mysql.connector

#step2:establish a connection
db=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Password@123',
    auth_plugin='mysql_native_password'
)

#step3:create a cursor object(transporter/mediator)
cursor=db.cursor()

sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()


