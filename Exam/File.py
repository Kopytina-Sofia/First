import sqlite3

connection = sqlite3.connect("database.sl4", 5)
cur = connection.cursor()

print("Щоб зареєтруватися введіть 1, а щоб увійти введіть 2 ")
choice = int(input("Введіть свій вибір:  "))
login = ""
password = ""

if choice == 1:
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")
    print("Ви успішно зареєструвалися!")




if choice ==2:
    login = input("Введіть свій логін: ")
    password = input("Введіть свій пароль: ")

#cur.execute("create table user (login text, password text);")
#cur.execute("select login from user;")
cur.execute(f"insert into user(login, password) values('{login}', '{password}');")
cur.execute(f"select * from user where login='{login}';")
cur.execute(f"select * from user where password='{password}';")
res = cur.fetchall()
log , pas = res[0]

if login and password == res:
    print("Ви успішно увійшли!")
else:
    print("Вам не вдалося увійти")



connection.commit()
connection.close()


