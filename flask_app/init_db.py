import pymysql

db_host = 'db'  
db_user = 'root'
db_password = 'Password'  
db_name = 'mysql'  

connection = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name)

with open('/docker-entrypoint-initdb.d/init.sql') as f:
    with connection.cursor() as cursor:
        cursor.execute(f.read())

with connection.cursor() as cursor:
    cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", ('First Post', 'Content for the first post'))
    cursor.execute("INSERT INTO posts (title, content) VALUES (%s, %s)", ('Second Post', 'Content for the second post'))

connection.commit()
connection.close()
