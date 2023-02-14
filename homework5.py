import random

model_list = {"APPLE MacBook Air M1" , "Acer Swift 3", "Lenovo ThinkPad X1 Carbon", "Microsoft Surface Laptop 4"}

class Video_card:
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.video_memory_size = "1GB"
        self.video_memory_type = "GDDR4"

class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__()
        self.model = random.choice(list(model_list))
        self.RAM = " 30 GB"
        self.CPU = "Intel Core i5-1135G7"

    def calcu(self):
        print("Calculate...")

class Monitor(Video_card):
    def __init__(self , *args, **kwargs):
        super().__init__()
        self.screen_resolution = "8K"
    def display(self):
        print("Result...")


class Laptop(Computer, Monitor):
    def character(self):
        print(self.model)
        print(self.RAM)
        print(self.CPU)
        print(self.screen_resolution)
        print(self.video_memory_size)
        print(self.video_memory_type)

lap = Laptop(Computer,Monitor)
lap.character()


