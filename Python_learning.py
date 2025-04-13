
print("Game\"Who wants to be a millionare\"")
pod50=True
podzn=True
summa=0
n_summa=0
def dost_podskazki():
    print("\t\t\t\t current sum:",summa)
    print("\t\t\t\t available hints:")
    if pod50 == True and podzn == True:
        print ("\t\t\t\t*****")
        print("\t\t\t\t* 50 over 50")
        print("\t\t\t\t*****")
        print("\t\t\t\t* Help from a player")
        print("\t\t\t\t*****")
    if pod50 == True and podzn == False:
        print("\t\t\t\t*****")
        print("\t\t\t\t*50 over 50*")
        print("\t\t\t\t*****")
    if pod50 == False and podzn ==True:
        print("\t\t\t\t*****")
        print("\t\t\t\t* Help from a player")
        print("\t\t\t\t*****")
    if pod50 ==False and podzn == False:
        print("\t\t\t\t*****")
        print("\t\t\t\t*There are no more hints*")
        print("\t\t\t\t*****")
def podskazki(a, b):
    global pod50
    global podzn
    question= input("Do you want a hint?")
    if question =="Yes" or question =="Yes" or question =="Yes":
        if pod50 ==False and podzn == False:
            print("There are no more hints")
    elif pod50 ==True and podzn == True:
        pods =input("50 over 50 or help from a player?")
    elif pod50 ==True and podzn == False:
        pods = input("50 over 50?")
    elif pod50 ==False and podzn ==True:
        pods =input("Help from a player?")
    if pods == "50 over 50":
        print("1.", a, "\t)2.", b)
        pod50 =False
    elif pods =="Help from a player":
        print("1.", b)
        podzn = False
    else:
        print("Incorrect choice!")
def question(a, b, a1, a2, a3, a4):
    print("Answer No" + str(a))
    print(b)
    print("1.", a1, "\t2.",a2)
    print("3.", a3, "\t4.", a4)
def loose(a):
    print("Sorry, but you lost!")
    print("Your prise has", n_summa, "Dollars")
Continue = True
Number = 0
begin = input("Do you want to start the game?")
if begin == "Yes" or begin =="yes" or begin == "YES":
    dost_podskazki()
    ques ="What continent has only 1 country?"
    question(1, question, "Europe", "Asia", "Africa", "Australia")
    podskazki("Europe", "Australia")
    answer =input("Type your answer:")
    if answer == "Australia":
        print("Nice! You had the right answer")
        summa = 500
else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques ="Where do sunflowers grow?"
    question(2, ques, "On the ground", "On the Sun", "On the clouds", "On water")
    podskazki("On the sun", "On the ground")
    answer = input("Type an answer:")
    if answer == "On the ground":
        print("Good job!You gave the right answer")
        summa = 1000
    else:
        Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques = "What currency doesn't exist"
    question(3,ques, "Grivni", "Leye", "Dollars", "Liru")
    podskazki("Leye", "Liru")
    answer = input("Type an answer:")
if answer =="Leye":
    print("Wonderful!You have the right answer!")
    summa = 2000
else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques = ("How is portrait called, when it is written by yourself?")
    question(4,ques,"Samoslaw","Self-recording", "Zerkalnik","Auto portrait")
    podskazki("Self-recording", "Auto portrait")
    answer = input("Type an answer:")
if answer =="Auto portrait":
    print("Astonishing!You gave the right answer!")
    summa = 5000
else:
    Continue = False
if Continue == False:
    loose (n_summa)
else:
    dost_podskazki()
    ques ="What is the name of an unmanned aerial vehicle"
    question(5,ques, "Drone", "Machaon", "Decepticon","Anion")
    podskazki("Anion", "Drone")
    answer = input("Type an answer:")
if answer == "Drone":
    print("Wow!You gave the right answer!")
    summa =10000
else:
    Continue =False
if Continue ==False:
    loose(n_summa)
else:
    dost_podskazki()
    ques= "In what game is the ball not involved"
    question(6,ques, "Basketball", "Tennis", "Baseball", "Kerling")
    podskazki("Tennis", "Kerling")
    answer = input("Type an answer:")
if answer == "Kerling":
    print("Unbelievable!You gave the right answer")
    summa=25000
else:
    Continue =False
if Continue ==False:
    loose(n_summa)
else:
    dost_podskazki()
    ques ="Which one of these bridges is in Kiev?"
    question(7,ques, "Krumskiy", "Darnicky", "Newskei","Slavotyckuy")
    podskazki("Newskei", "Darnicky")
    answer = input("Type an answer:")
if answer =="Darnicky":
    print("7th in a row!You gave the right answer")
    summa =100000
else:
    Continue = False
if Continue ==False:
    loose(n_summa)
else:
    dost_podskazki()
    ques= "Who is a writer out of these people"
    question(8,ques,"Jean-Claude Van Damme", "Claude Monet", "Usain Bolt", "Edgar Po")
    podskazki("Claude Monet", "Edgar Po")
    answer =input("Type an answer:")
if answer =="Edgar Po":
    print ("Coming in hot!You gave the right answer")
    summa =250000
else:
    Continue = False
if Continue == False:
    loose(n_summa)
else:
    dost_podskazki()
    ques= "Which one of these sailors created Mis Good Hope?"
    question(9,ques, "Bartolomeu Dias","John Bruce","Vaska Dagama", "Christopher Columb")
    podskazki("Christopher Columb", "Bartolomeu Dias")
    answer = input("Type an answer:")
if answer == "Bartolomeu Dias":
    print("Fabulous!You had given the right answer")
    summa = 500000
else:
    Continue = False
if Continue ==False:
    loose(n_summa)
else:
    dost_podskazki()
    ques ="What chemical element has gotten its name because of blue line in its spectrum?"
    question(10,ques, "Rhodium", "Indium", "Cerium", "Neptunium")
    podskazki("Rhodium", "Indium")
    answer =input("Type a last answer:")
if answer == "Indium":
    print("You rocketed through the questions!You also gave the right answer!")
    summa = 1000000
    print("You won the super prize!!!!!!Congratulations!!!!!!!!")
    print("Your win contains", n_summa,"Dollars")
else:
    Continue = False
    loose(n_summa)