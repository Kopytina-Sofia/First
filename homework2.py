import random

name_list = {"Шарік", "Цятка", "Еверест", "Вуді", "Гаррі", "Арон"}


class Dogs:
    count_of_Dogs = 0

    def __init__(self, size=None, height=50, age=0, weight=0, breed=None, ):
        self.name = random.choice(list(name_list))
        self.size = size
        self.height = height
        self.age = age
        self.weight = weight
        self.breed = breed
        self.gladness = 10
        self.satiety = 10

        Dogs.count_of_Dogs += 1
        print('Гаф')

    def play(self):
        self.gladness += 30

    def grow(self, height=10):
        self.height += height

    def aging(self, age=1):
        self.age += age

    def weight_gain(self, weight=5):
        self.weight += weight

    def __str__(self):
        return f'Привіт, я найкращий пес у світі. Хочешь дізнатись мої параметри? Мене звуть {self.name},\b' \
               f' мені {self.age} років. Моя порода це {self.breed}, моя вага дорівнює {self.breed.weight} см і мій \b' \
               f'зріст це {self.breed.height} мій розмір {self.breed.size}. В цьому класі, нас всього {Dogs.count_of_Dogs}.' \

    def __del__(self):
        print(f'Привіт це {self.name} і я пішов :(')

    def get_food(self):
        self.satiety += 10

    def a_life(self, day_number):
        if self.is_alive() == False:
            return False
        if self.gladness < 10:
            self.play()
            print("Погрався")
        if self.satiety < 0:
            self.get_food()
        self.info_day(day_number)

    def is_alive(self):
        if self.gladness < 0:
            print("На жаль це депресія.")
            return False
        if self.satiety < 0:
            print("Він помер від голоду.")

    def info_day(self, day_number):
        day_str = f"День {day_number}-й з життя {self.name}-а"
        print(f"{day_str:=^50}")
        dog_str = f"Інформація про {self.name}-а:"
        print(f"{dog_str:=^50}")
        print(f"Задоволення:    {self.gladness}")
        print(f"Вік:            {self.age}")
        print(f"Ситість:        {self.satiety}", "\n")
        breed_str = f"Параметри {self.name}:"
        print(f"{breed_str:=^50}")
        print(f"Вага:         {self.breed.weight}")
        print(f"Висота:         {self.breed.height}")
        print(f"Розмір:           {self.breed.size}""\n")


types_of_breed = {"Німецька вівчарка": {"weight": 40, "height": 65, "size": 'big'},
                  "Ротвейлер": {"weight": 49, "height": 73, "size": 'medium'},
                  "Чихуа-хуа": {"weight": 1, "height": 21, "size": 'small'},
                  "Йоркширський тер'єр": {"weight": 3, "height": 23, "size": 'small'}}


class Breed:
    def __init__(self):
        self.breed = random.choice(list(types_of_breed))
        self.weight = types_of_breed[self.breed]["weight"]
        self.height = types_of_breed[self.breed]["height"]
        self.size = types_of_breed[self.breed]["size"]

    def get_weight(self):
        if self.breed.weight < 10:
            self.get_food()


Sharik = Dogs(size='medium', height=67, age=7, weight=59, breed='rottweiler')
for day in range(1, 366):
    if Sharik.a_life(day) == False:
        break
