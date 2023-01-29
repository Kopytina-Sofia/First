class Dogs:
    count_of_Dogs = 0
    def __init__(self, name = None, size = None, height = 50, age = 0 , weight = 0, breed = None):
        self.name = name
        self.size = size
        self.height = height
        self.age = age
        self.weight = weight
        self.breed = breed
        Dogs.count_of_Dogs +=1
        print('Гаф')

    def grow(self,height=10):
        self.height += height

    def aging(self,age=1):
        self.age += age

    def weight_gain(self,weight=5):
        self.weight += weight

    def __str__(self):
        return f'Привіт, я найкращий пес у світі. Хочешь дізнатись мої параметри? Мене звуть {self.name},\b' \
               f' мені {self.age} років. Моя порода це {self.breed}, моя вага дорівнює {self.weight} см і мій \b' \
               f'зріст це {self.height}. В цьому класі, нас всього {Dogs.count_of_Dogs}.' \

    def __del__(self):
        print(f'Привіт це {self.name} і я пішов :(')


Sharik = Dogs(name='Sharik',size= 'medium',height = 67, age= 7, weight = 59,breed = 'rottweiler')
print(Sharik)
Boris = Dogs(name='Boris',size= 'medium',height = 50, age= 40, weight = 70,breed = 'staffordshire terrier')
print(Boris)

