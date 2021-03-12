import cgi;
from wsgiref.simple_server import make_server;
import MySQLdb;
import MySQLdb.cursors;

db = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db='assignment3', cursorclass=MySQLdb.cursors.DictCursor);
cursor = db.cursor( );

cursor.execute("SELECT * FROM registered_users");
data = cursor.fetchall();

user_array = [];
all_users = [];

for row in data:
    id = row["user_id"];
    firstName = row["firstname"];
    lastName = row["lastname"];
    user_array.append(id);
    user_array.append(firstName);
    user_array.append(lastName);

    all_users.append(user_array);
    user_array = [];
    
for i in range(len(all_users)):
    print(all_users[i]);

cursor.close();
db.close();

import gc;
gc.collect();