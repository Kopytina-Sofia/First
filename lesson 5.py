class Human:
    height = 170
    age = 30
    gladness = 50


class Student(Human):
    age = 17


class Aspirant(Student):
    height=180
    def __init__(self):
        print(self.height)
        print(self.age)
        print(self.gladness)

    def _hello(self):
        print("_Hello!")

    def __hello(self):
        print("__Hello!")



class Worker(Human):
    age = 50


class Hello_Kitty:
    hello = "Hello"
    _hello = "_Hello"
    __hello = "__Hello"
    def __init__(self):
        self.kitty = "Kitty"
        self._kitty = "_Kitty"
        self.__kitty = "__Kitty"

    def print(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.kitty)
        print(self._kitty)
        print(self.__kitty)

    def __method(self):
        print("Method")


class Hi(Hello_Kitty):
    def hi_print(self):
        super().__method()
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.kitty)
        print(self._kitty)
        print(self.__kitty)


class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__()
        self.model = model
        self.RAM = "16 GB"

    def calc(self):
        print("Calculate.....")

class Monitor:
    def __init__(self,*args, **kwargs):
        super().__init__()
        self.resolution = "8K"

    def display(self):
        print("Result....")

class Smartphone(Computer,Monitor):
    def info(self):
        print(self.RAM)
        print(self.resolution)
        print(self.model)


phone = Smartphone(model = "Apple 37")
phone.info()


'''hello = Hello_Kitty()
hello.print()'''
'''hi = Hi()
hi.hi_print()'''


'''asp = Aspirant()
asp._hello()
#asp.__hello()'''

'''st = Student()

wr = Worker()
print(st.age)
print(wr.age)'''