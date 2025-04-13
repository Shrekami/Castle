# import random
# Question=int(input("What would be the smallest number"))
# question=int(input("What would be the largest number"))
# a=random.randint(Question,question)
# print(a)

# import random
# Question=int(input("Type a number"))
# for i in range(1,11):
#     print(random.random()*Question)

# import random
# a=random.randrange(10,99, 2)
# print(a)

import random
print("Type a number, you will have to guess a number but you have 3 guesses")
a=random.randrange(15,101)
tries=3
points=0
while True:
    if tries>0:
        if tries==1:
            print("You have", tries, "try to guess a number")
        else:
            print("You have", tries, "tries to guess a number")
        answer= input("Do you want to use a hint ")
        if answer.lower() =="yes":
            print("The answer range is" ,a-random.randint(1,4), "And" ,a+random.randint(1,5))
        number = int(input("Type a number"))
    else:
        print("All of you tries are gone, You lose")
        print("The number you didn't guess was", a)
        break
    if number==a:
        print("You guessed the number.YOU are GENIUS!!!")
        break
    else:
        print("You didn't guess, try again")
        tries -=1