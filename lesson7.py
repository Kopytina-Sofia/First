
class MyException:
    def __init__(self,my_date):
        self.date = my_date

    def __str__(self):
        return f"{self.date} Це мій клас винятку"


a = int(input())
b = int(input())
try:
    try:
        if b==0 :
            raise MyException("15.02.2023")
        print(a/b)
except:
    print("Помилка")
print("Кінець програми")

