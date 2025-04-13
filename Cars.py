from Car_module import Car
my_car=Car(name="Audi",year=1910,color="Gray", mode="Fast",weight="2 tons")
other_car=Car(name="BMW",year=1916,color="Black",mode="Fast",weight="2.5 tons")
different_car=Car(name="Ford",year=1903,color="White",mode="Normal",weight="1.8 tons")
batmobile_car=[my_car, other_car, different_car]
print(batmobile_car[0].name)
b=0
car_number=0
while True:
    print("1) Create a car")
    print("2) Show info about car")
    print("3) Choose a car")
    print("4) Turn on the car")
    print("5) Turn off the car")
    print("6) Mode")
    print("7) Info about the cars")
    print("8) Exit")
    act=int(input("Pick an action "))
    if act==1:
        print("You are making a car")
        door = input("The color your car is going to be is ")
        if door.lower() in ["red", "orange", "yellow", "blue", "green", "pink", "purple", "brown","gray", "black"]:
            color = door.lower()
        else:
            color = 'black'
        print(f"You chose {color} as the color of your car.")

        nime=input("Choose the name of your car ")

        loop=input("Choose what year your car is going to be made in ")

        mide=input("Choose what mode your car is going to have ")

        wight=input("Choose how much tons your car is going to weigh ")
        my_new_car = Car(color=color,year=loop,mode=mide,weight=wight,name=nime)
        batmobile_car.append(my_new_car)
        my_new_car.info()

    elif act==2:
        batmobile_car[car_number].info()
    elif act==8:
        break
    elif act==4:
        batmobile_car[car_number].on()
    elif act==5:
        batmobile_car[car_number].off()
    elif act==6:
        batmobile_car[car_number].showmode()
    elif act==7:
        for i in batmobile_car:
            i.info()
            print("\n")

    elif act==3:
        a=1
        for i in batmobile_car:
            print(a,i.name,"\n")
            a+=1
        b=int(input("Choose what number you want that makes up your car "))
        car_number=b-1
        print(car_number)