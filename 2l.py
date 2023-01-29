class Student:
    count_of_Student = 0
    def __init__(self, name=None , height = 160, mental_activity = 10,):
        self.mental_activity = mental_activity
        self.name = name
        self.height = height
        Student.count_of_Student += 1
        print('Привіт, я з`явився.')
    def grow (self,height=1):
        self.height += height
    def  mental_act (self, mental_activity = 0.5 ):
        self.mental_activity += mental_activity
        print('Я підвищив свій рівень знань.')

    def __str__(self):
        return f'Привіт, я {self.name}, мій зріст {self.height} cm. Мої розумові здібності дорівнюють\
        {self.mental_activity}.'

    def __del__(self):
        print(f'Привіт, я {self.name},і я пішов. ((')

Serg = Student(height=180)
print(Serg)
print(Serg.height)
#print(Serg.count_of_Student)

Artur = Student(name = 'Артур', height=165)
print(Artur)
Artur.grow(10)
print(Artur.height)
#print(Artur.count_of_Student)
#print(Student.count_of_Student)