import sqlite3

connection = sqlite3.connect("database.sl3", 5)
cur = connection.cursor()

#cur.execute("create table users (id int primary key not null, login text, password text);")
cur.execute("select * from users;")
cur.execute("insert into users(id, login, password) values(4,'user2', 'pass8');")
cur.execute("insert into users(id, login, password) values(2,'user3', 'pass5');")
cur.execute("insert into users(id, login, password) values(3,'user4', 'pass7');")
cur.execute("insert into users(id, login, password) values(1,'user5', 'pass6');")
connection.commit()
res = cur.fetchall()
print(res)

#print(connection)
#print(cur)

connection.close()

