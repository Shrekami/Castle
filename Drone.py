# Length=int(input("Type a length to your rectangle "))
# Width=int(input("Type a width to your rectangle "))
# answer=input("If you want to know the area of you rectangle, type area. But if you want to know the perimeter of your rectangle, type perimeter ")
# if answer.lower()=="area":
#     print("Your area is", Length*Width, "squares")
# if answer.lower()=="perimeter":
#     print("Your perimeter is", (Length+Width)*2, "squares")

# def module (number):
#     Mile = number//1.609
#     print(Mile)
# Kilometers=int(input("Type how much kilometers you want to be converted to miles "))
# module(number=Kilometers)

# Month=int(input("Type a number of month "))
# def module(number):
#     if number==12 or number==1 or number==2:
#         print("This is winter time")
#     elif number==3 or number==4 or number==5:
#         print("It is spring time")
#     elif number==6 or number==7 or number==8:
#         print("It is summer time")
#     elif number==9 or number==10 or number==11:
#         print("It is autumn time")
#     else:
#         print("There are no more months")
# module(number=Month)
number1=0
number2=0
def module(choice):
    global number1, number2
    if choice==1:
        number1 = int(input("Type number 1 "))
    elif choice==2:
        number1 = int(input("Type number 1 "))
        number2 = int(input("Type number 2 "))
    else:
        print("Incorrect choice")
while True:
    print("Available operations are")
    print("1-addition")
    print("2-subtraction")
    print("3-multiplying")
    print("4-division")
    print("5-factorial")
    print("6- 1/x")
    print("7-square")
    print("8-exit")
    number=int(input("Make your choice " ))
    if number==1:
        module(2)
        print("Your result is",number1+number2)
    elif number == 2:
        module(2)
        print("Your result is", number1 - number2)
    elif number == 3:
        module(2)
        print("Your result is", number1 * number2)
    elif number == 4:
        module(2)
        print("Your result is", number1 / number2)
    elif number == 5:
        result=1
        module(1)
        for i in range(1,number1+1):
            result*=i
        print("Your result is",result)
    elif number == 6:
        module(2)
        print("Your result is", 1/number1)
    elif number == 7:
        module(1)
        print("Your result is", number1**number1,)
    elif number == 8:
        break