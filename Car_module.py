import random
import string
class Car:
    def __init__(self,name,year,color,mode,weight):
        self.name=name
        self.year=year
        self.color=color
        self.mode=mode
        self.number=self.randomizer()
        self.weight=weight
    def randomizer(self):
        letter = random.choice(string.ascii_letters)
        nomber=random.randint(1,10)
        lotter=random.choice(string.ascii_letters)
        nember=random.randint(1,10)
        latter=random.choice(string.ascii_letters)
        namber=random.randint(1,10)
        serial_number=(f"{letter}{nomber}{lotter}{nember}{latter}{namber}")
        return serial_number
    def info(self):
        print(f"The name of the car is {self.name}")
        print(f"The year the car was made in is {self.year}")
        print(f"The color of the car is {self.color}")
        print(f"The mode of the car is {self.mode}")
        print(f"The serial number of the car is {self.number}")
        print(f"The weight of the car is {self.weight}")
    def on(self):
        if self.mode=="on":
            print("You already turned on the car.")
        else:
            self.mode="on"
            print("You turned on the car")
    def off(self):
        if self.mode=="off":
            print("You already turned off the car")
        else:
            self.mode="off"
            print("You chose to not turn on the car")

    def showmode(self):
        print(f"The mode that the car is on is {self.mode}")

    def slowmode(self):
        slowmo="slow"
        print("You can also turn on the",slowmo,"mode")

