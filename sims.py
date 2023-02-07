import random


class Human:
    def __init__(self, name, house = None, car = None, job= None):
        self.name = name
        self.house = house
        self.car = car
        self.job = job
        self.money = 100
        self. gladness = 50
        self.satiety = 50

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self, purchase):
        pass

    def cleaning(self):
        pass

    def to_repair(self):
        pass

    def chill(self):
        pass



    def get_house(self):
        self.house = House()

    def get_car(self):
        self.car = Car(brand_of_cars)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def is_alive(self):
        if self.gladness < 0:
            print("На жаль це депресія.")
            return False
        if self.satiety < 0:
            print("Він помер від голоду.")
            return False
        if self.money < - 200:
            print("Він банкрот.")
            return False

    def day_info(self,day_number):
        day_str = f"День {day_number}-й з життя {self.name}-а"
        print(f"{day_str:=^50}")
        human_str = f"Інформація про {self.name}-а:"
        print(f"{human_str:=^50}")
        print(f"Задоволення:    {self.gladness}")
        print(f"Ситість:        {self.satiety}")
        print(f"Гроші:          {self.money}","\n")
        house_str = f"Інформація про будинок:"
        print(f"{house_str:=^50}")
        print(f"Наявність їжі:  {self.house.food}")
        print(f"Порядок:        {self.house.mess}""\n")
        car_str = f"Інформація про автівку:"
        print(f"{car_str:=^50}")
        print(f"Пальне:         {self.car.fuel}")
        print(f"Стан:           {self.car.strength}""\n")



    def live(self, day_number):
        if self.is_alive() == False:
            return False
        if self.house is None:
            self.get_house()
            print("Оселився в будинку.")
        if self.car is None:
            self.get_car()
            print(f'Придбав автівку {self.car.brand}')
        if self.job is None:
            self.get_job()
            print(f'Влаштувався на роботу {self.job.job}, із зарплатнею {self.job.salary}$')
        self.day_info(day_number)
        if self.money <0:
            print("Час йти на роботу.")
            self.work()
        #elif




brand_of_cars = {"BMV":{"fuel":100, "strength":100, "consumption":6},
                 "Audi":{"fuel":80, "strength":80, "consumption":7},
                 "Mercedes":{"fuel":100, "strength":90, "consumption":5},
                 "Запорожець":{"fuel":50, "strength":50, "consumption":8}}

class Car:
    def __init__(self, brand_of_cars):
        self.brand = random.choice(list(brand_of_cars))
        #бренд
        self.fuel = brand_of_cars[self.brand]["fuel"]
        #пальне
        self.strength = brand_of_cars[self.brand]["strength"]
        #амортизація
        self.consumption = brand_of_cars[self.brand]["consumption"]
        #витрати пального

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("Немає пального або авто зломалося.")
            return False

class House:
    def __init__(self):
        #Наявність їжі
        self.food = 0
        #Забрудненість
        self.mess = 0

job_list = {"Розробник на Python": {"salary": 100, "gladness_less": 10},
                     "Викладач в Академії": {"salary": 80, "gladness_less": 2},
                     "Водій": {"salary": 60, "gladness_less": 5},
                     "Продавець": {"salary": 50, "gladness_less": 8}}


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

anton = Human("Антон")
for day in range(1, 366):
    if anton.live(day) == False:
        break


