import cgi;
from wsgiref.simple_server import make_server;
import MySQLdb;
import MySQLdb.cursors;

db = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db='assignment3', cursorclass=MySQLdb.cursors.DictCursor);
cursor = db.cursor( );

cursor.execute("SELECT * FROM registered_users");
data = cursor.fetchall();

last_name_array = [];


for row in data:
    lastName = row["lastname"];
    last_name_array.append(lastName);
    
x = sorted(last_name_array, key=str.casefold);

for i in range(len(x)):
    print(x[i])

cursor.close();
db.close();

import gc;
gc.collect();