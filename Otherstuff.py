# import os
#
# def agreement():
#     agree=input("Are you sure you want to shut down the computer? ")
#     if agree.lower()=="yes":
#         os.system("shutdown /s 5")
#     else:
#         print("Shutdown canceled.")
# agreement()

tries = 3
correct_answers = 0  # Variable to track the number of correct answers
wrong_answers = 0  # Variable to track the number of wrong answers
total_questions = 4  # Total number of true/false questions (not including the last one)

while True:
    # First true/false question
    print("This is a game, where I can see how good you know me, with using only true or false.")
    print("This is the first true or false question about me. Am I really smart?")
    answer = input("True or false? ")

    if answer.lower() == "true":
        print("Oh yeah.")
        correct_answers += 1  # Increment the correct answers
    else:
        print("No!!!!")
        wrong_answers += 1  # Increment the wrong answers

    # Second true/false question
    print("This is the next question, about me. I don't want to go somewhere.")
    reason = input("True or False? ")

    if reason.lower() == "false":
        print("You rock.")
        correct_answers += 1
    else:
        print("!No!")
        wrong_answers += 1

    # Pre-last true/false question
    print("This is the pre-last question about me. Is April Fools the best holiday for me?")
    finding = input("True or False? ")

    if finding.lower() == "false":
        print("On the way.")
        correct_answers += 1
    else:
        print("BOOOOOO")
        wrong_answers += 1

    # Last true/false question (after this, the game will stop)
    print("This is the last question but it is not true or false. Is Easter or Halloween my favorite holiday?")
    explain = input("Easter or Halloween?   ")
    print("WOw")

    if explain.lower() == "easter" or explain.lower()=="halloween":
        print("You didn't get it since it was a tricky question.")
        wrong_answers += 1
    elif explain.lower() == "birthday" or explain.lower()=="christmas":
        print("Great! But let's check if you won.")
        correct_answers += 1

    # Now, after all true/false questions are answered, we check the final condition
    if correct_answers == 3:
        print("Congratulations, you won the game!")
        break
    elif wrong_answers == total_questions:
        print("You didn't get any questions right. Better luck next time!")
        break
    else:
        print("You didn't get enough questions right. Better luck next time!")
        break
