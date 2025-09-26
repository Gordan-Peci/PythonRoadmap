import random

usr_score = 0
computer_score = 0

while usr_score < 5 and computer_score < 5:
    usr_input = int(input('Enter a number: 1 - Rock; 2 - Paper; 3 - Scissors \n '))

    computer_choice = random.randint(1, 3)
    print("Computer choose option: " + str(computer_choice))

    if usr_input > 3 or usr_input < 1:
        print("You did not enter a walid choice!")
    elif usr_input == 1:
        if computer_choice == 1:
            print("Same choice noone scored!")
            continue
        elif computer_choice == 2: 
            print("Computer scored!")
            computer_score += 1
            continue
        elif computer_choice == 3:
            print("You scored against computer!")
            usr_score += 1
            continue
    elif usr_input == 2:
        if computer_choice == 1:
            print("You scored against computer!")
            usr_score += 1
            continue
        elif computer_choice == 2: 
            print("Same choice noone scored!")
            continue
        elif computer_choice == 3:
            print("Computer scored!")
            computer_score += 1
            continue
    elif usr_input == 3:
        if computer_choice == 1:
            print("Computer scored!")
            computer_score += 1
            continue
        elif computer_choice == 2: 
            print("You scored against computer!")
            usr_score += 1
            continue
        elif computer_choice == 3:
            print("Same choice noone scored!")
            continue
    else:
        print("Invalid data type!")

if computer_score > usr_score:
    print(f"Computer won by {computer_score - usr_score} points! It was first to 5 points!")
else: 
    print(f"You won by {usr_score - computer_score} points! It was first to 5 points!")
