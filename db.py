import urllib.parse as up

import psycopg2
from main import board
path_to_db_bot = "postgres://bdszdyaa:lTwBToBaKDLOcRfYf06i24H4V4okXH4w@trumpet.db.elephantsql.com/bdszdyaa"

up.uses_netloc.append("postgres")

url = up.urlparse(path_to_db_bot)

connection = psycopg2.connect(database=url.path[1:],

                              user=url.username,

                              password=url.password,

                              host=url.hostname,

                              port=url.port)

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS moves("
               "x1 INTEGER,"
               "y1 INTEGER,"
                "x2 INTEGER,"
                "y2 INTEGER,"
               "key BOOLEAN)")
cursor.execute("DELETE FROM moves")
connection.commit()
sql=''

def add(x1,y1,x2,y2):
    cursor.execute('insert into moves(x1,y1,x2,y2,key)values(%s,%s,%s,%s,%s)',(x1,y1,x2,y2,True))
    connection.commit()
def read():
    cursor.execute('SELECT * FROM moves')
    data=cursor.fetchall()
    print(data)

