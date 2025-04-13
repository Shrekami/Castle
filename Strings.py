# phone="45-02-11-1-28-38-7"
# newphone=phone.replace("-",'_')
# print(newphone)

# sentence='I love donkeys'
# dog=sentence.split("o")
# print(dog)

# floor='12345'
# if floor.isnumeric():
#     print("This is all numbers")
# elif floor.isalpha():
#     if floor.islower():
#         print("This sentence has lowercase letters")
#     elif floor.isupper():
#         print("This sentence has uppercase letters")

# fire="abacdafabaccooabacabacqabac"
# while True:
#     a = fire.find('abac')
#     if a==-1:
#         break
#     fire = fire[a + len('abac'):len(fire)]
#     print(fire)
#
# s="avfvhfukfofnbbnfffbmf"
# b=""
# for i in s:
#     if i=="f":
#         b+="f"*2
#     else:
#         b+=i
# print(b)

# al = "arRoW"
# c=""
# b=0
# for i in al:
#     if i.islower():
#         b+=1
# print("Number of lowercase letters is", b)
# for i in al:
#     if i=="a":
#         c+="Shrek"
#     else:
#         c+=i
# print("New string is",c)

# flomp="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent et bibendum quam. Morbi vitae sem eget risus consectetur fermentum vel sed urna. Ut vel ornare ante. Praesent semper tortor in"
# flomp2=flomp.split("i")
# print(flomp2)
# for i in flomp2:
#     if len(i)<4:
#         print(i)

# phone="+1-234-567-89-10"
# phen=phone.replace("-","*")
# print(phen)

# words="ox pneumonia anniversary floor lavender fire"
# max_bird=0
# wirds=words.split(" ")
# print(wirds)
# for i in wirds:
#     if len(i)>max_bird:
#         max_bird=len(i)
# min_bird = max_bird
# for i in wirds:
#     if len(i)<min_bird:
#         min_bird=len(i)
# print(min_bird)

# bomp="allies flare pearl lemp lays bam ham"
# c=0
# derts=bomp.split(" ")
# print(derts)
# b=bomp.replace("e","a")
# print(b)
# for i in derts:
#     if len(i)<5:
#         c+=1
# print(c)

# import random
# a="bromine lamp turtles noodles poodles"
# b=a.split(" ")
# (random.shuffle(b))
# print(b)

# import random
# gallows = [
#     "",
#     """
#     |
#     |
#     |
#     |
#     |
#     |
#     ---
#     """,
#     """
#     ------
#     |    |
#     |
#     |
#     |
#     |
#     |
#     ---
#     """,
#     """
#     ------
#     |    |
#     |    O
#     |
#     |
#     |
#     |
#     ---
#     """,
#     """
#     ------
#     |    O
#     |   /|\\
#     |
#     |
#     |
#     ---
#     """,
#     """
#     ------
#     |    |
#     |    O
#     |   /|\\
#     |   / \\
#     |
#     |
#     ---
#     """
# ]
# word=random.choice(["milk","floor","donkey","sushi","bromine","calibrating"])
# string="_"*len(word)
# tries=1
# print(word)
# print(string)
# while tries<5 and string!=word:
#     print("This is your word", string)
#     d=input("Type a letter")
#
#     if d in word:
#         newstring=""
#         for i in range (len(word)):
#             if d==word[i]:
#                 newstring+=d
#             else:
#                 newstring+=string[i]
#         string=newstring
#         print("That letter is on the right spot")
#     else:
#         tries+=1
#         print(gallows[tries])
# if tries==5:
#     print("You lose")
# else:
#     print("You win")
# print("Your word was",word)

nma="10"
print(type(nma)==str)