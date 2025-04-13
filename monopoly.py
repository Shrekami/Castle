import random
player1=0
player2=0
while True:
    print("Player1 throw the dice👨")
    answer=input("Type ok to for throwing the dice ")
    if answer.lower()=="ok":
        a = random.randrange(1, 7)
        print("The number on the dice that rolled is", a)
        player1+=a
        print("Player1 is on a", player1, "slot")
        if player1==20:
            player1-= random.randrange(1, 7)
            print("Oh oh looks like you landed on a disadvantage", "You now are on slot",player1)
        if player1==43:
            player1-=5
            print("You now go back 5 slots","Now you are on slot",player1)
        if player1==36:
            player1-=8
            print("Noo, you go back 8 slots","Now you are on slot",player1)
        if player1==15:
            player1-=2
            print("This is not so big of a disadvantage", "Now you are on slot",player1)
        if player1==24:
            player1+=random.randrange(1, 7)
        if player1==13:
            continue
    if player1>49:
        print("Player1 won")
        break
    print("Player2 throw the dice👩")
    answer = input("Type ok to for throwing the dice ")
    if answer.lower() == "ok":
        a = random.randrange(1, 7)
        print("The number on the dice that rolled is", a)
        player2 += a
        print("Player2 is on a", player2, "slot")
        if player2 == 19:
            player2 -= random.randrange(1, 7)
            print("Oh oh looks like you landed on a disadvantage", "You now are on slot", player2)
        if player2 == 39:
            player2 -= 3
            print("You now go back 5 slots", "Now you are on slot", player2)
        if player2 == 44:
            player2 -= 7
            print("Noo, you go back 8 slots", "Now you are on slot", player2)
        if player2 == 15:
            player2 -= 4
            print("Ouch", "Now you are on slot", player2)
        if player2 == 28:
            player2 += random.randrange(1, 7)
        if player2 ==26:
            continue
    if player2 > 49:
        print("Player2 won")
        break