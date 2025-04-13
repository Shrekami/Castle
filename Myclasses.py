# class dad:
#     name="Serhii"
#     age="40"
#     house="white house"
#     def donkey(self):
#         print("Hello",self.name,'from',self.house)
#         print(f"Yay {self.name*2}")
# a=dad()
# a.donkey()

# class human:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def donkey(self):
#         print(f"Hi {self.name}, {self.age}")
# a=human(name="Shrekadomp",age=100)
# a.donkey()
# b=human(name="Fiona",age=99)
# b.age=15
# print(b.age)

# class cars:
#     def __init__(self,name,color,original):
#         self.name=name
#         self.color=color
#         self.original=original
#     def type(self):
#         print(f"This is the name of the car, {self.name}")
#         print(f"This is the color of the car, {self.color}")
#         print(f"This is what year {self.name} was made, {self.original}")
#
# c=cars(name="Lamborghini",color="orange",original="1963")
# c.type()
#
# d=cars(name="Audi",color="gray",original="1910")
# d.type()

# class soda:
#     def __init__(self,name,toppings=None):
#         self.name=name
#         self.toppings=toppings
#     def type(self):
#         print(f"This is what soda you get, {self.name}")
#         if self.toppings!=None:
#             print(f"These are the toppings you added, {self.toppings}")
#         else:
#             print("You didn't get any toppings 😭😭")
# f=soda(name="sprite",toppings="lime")
# f.type()

# class Triangle:
#     def __init__(self,side1,side2,side3):
#         self.side1=side1
#         self.side2=side2
#         self.side3=side3
#     def triangle(self):
#         if type(self.side1)==str or type(self.side2)==str or type(self.side3)==str:
#             print("You can't type letters")
#         else:
#             print("This statement approves that you didn't write any letters, which is good.")
#             if self.side1 > 0 and self.side2 > 0 and self.side3 > 0:
#                 print("Yay, you can build a triangle!")
#                 if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and self.side2 + self.side3 > self.side1:
#                     print("This formula confirms that you can build a triangle")
#                 else:
#                     print("This formula disregards that you can make a triangle")
#             else:
#                 print("Sorry, you can't make a triangle with negative numbers")
#
# lamb=Triangle(side1=3, side2=2, side3=3)
# lamb.triangle()

class People:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new_age):
        if new_age<0:
            print('Incorrect age')
        else:
            self.__age=new_age
    def info(self):
        print(f"Hi my name is {self.name}. And I am {self.__age} years old")
# human=People(name="Donkey",age=10)
# human.age = 1
# print(human.age)
# human.info()

class Sportsman(People):
    def sport(self):
        print("Baseball")

a=Sportsman(name='Boby',age="15")
print(a.name)
print(a.age)
a.sport()
