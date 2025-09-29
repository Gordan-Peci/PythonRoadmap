gradebook = {"Marko": 2, "Ivan": 5}

while True:
    choice = int(input("Choose an action you want to preform: 1 - Add student; 2 - Update Student; 3 - Show all students; 0 - exit program "))
    if choice == 1:
        add_name = input("Please enter the name of the student: ")
        add_grade = int(input("Please enter the grade of the set student: "))
        if add_grade > 5 or add_grade < 1:
            print("You can't enter a number bigger than 5 or smaller than 1!")
            continue
        else:
            gradebook[add_name] = add_grade
            continue
    
    elif choice == 2:
        find_student = input("Enter the name of the student you want the change the grade of: ")
        if find_student in gradebook:
            change_grade = int(input("Enter the grade you want to change to: "))
            gradebook[find_student] = change_grade
            continue
        else:
            print("The student you searched for doesn't exist")
            continue
    
    elif choice == 3:
        print(gradebook)

    elif choice == 0:
        break

    else:
        print("Invalid input, try again!")
        continue