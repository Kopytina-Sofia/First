class Human:
    def __init__(self, name = 'No name'):
        self.name = name

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passenger = []

    def add_passenger(self,*humans):
        for passenger in humans:
             self.passenger.append(passenger)


    def print_passengers(self):
        if self.passenger == []:
            print("Автівка зараз порожня.")
        else:
            print(f'Зараз на {self.brand} кудись їдуть:')
            for passenger in self.passenger:
                print(passenger.name)



human1 = Human("Сергій")
human2 = Human("Ала")
car = Car("BMV")
car.print_passengers()
car.add_passenger(human1,human2)
car.print_passengers()

