import random

class Student:
    def __init__(self,name):
        self.name = name
        self.progress = 0.2
        self.gladness = 50
        self.alive = True
        self.money = 200

    def to_study(self):
        print("Я вчуся.")
        self.progress += 1
        self.gladness -= 5

    def to_sleep(self):
        print("Я пішла спати.")
        self.gladness += 3

    def to_have_fun(self):
        print("Я розважаюсь.")
        self.progress -= 1
        self.gladness += 6
        self.money -= 4

    def to_work(self):
        print("Я працюю.")
        self.gladness -= 10
        self.money +=12

    def is_alive(self):
        if self.progress < 0:
            print("Ви відраховані від навчального закладу.")
            self.alive == False

        if self.progress > 5:
            print("Ура я достроково завершила начальний заклад.")
            self.alive == False

        if self.gladness <0:
            print("Все пропало. В мене депресія.")
            self.alive == False




    def end_of_day(self):
        print(f'Задоволеність - {self.gladness}.')
        print(f'Прогресс - {round(self.progress)}.')

    def live(self,day):
        info = f'День номер {day} з життя {self.name}'
        print(f'{info:=^40}')
        if self.money < 30:
            self.to_work()
        elif self.progress < 1:
            self.to_study()
        elif self.gladness < 20:
            self.to_have_fun()
        elif self.money and self.progress and self.gladness == 5:
            choice = random.randint(1, 3)
            if choice == 1:
                self.to_study()
            elif choice == 2:
                self.to_sleep()
            elif choice == 3:
                self.to_have_fun()

        self.end_of_day()
        self.is_alive()



Sofia = Student(name='Софія')
for day in range(365):
    if Sofia.alive == False:
        break
    Sofia.live(day)
