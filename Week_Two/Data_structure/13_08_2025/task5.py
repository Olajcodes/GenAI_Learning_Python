# Task1: Create and Display
print("Kindly enter your three favorite Nigerian dishes")
dishes = (input("Enter your favorite dish 1: "),
          input("Enter your favorite dish 2: "),
          input("Enter your favorite dish 3: ")
)
print(dishes)
print(*dishes, sep="\n")


# Task2: Tuple and Input
print("Kindly provide your 5 best friend's name")
best_friends = (input("Enter your best friend's name 1: "),
                input("Enter your best friend's name 2: "),
                input("Enter your best friend's name 3: "),
                input("Enter your best friend's name 4: "),
                input("Enter your best friend's name 5: "),
)
print(best_friends[::-1])


#  Task3: Tuple Operations
nigerian_state = (
    input("Enter the first Nigerian state: "),
    input("Enter the second Nigerian state: "),
    input("Enter the third Nigerian state: "),
    input("Enter the forth Nigerian state: "),
    input("Enter the fifth Nigerian state: ")
)
print(f"{nigerian_state[0]} and {nigerian_state[-1]}")
print("Lagos" in nigerian_state)
print("The number of states entered is: ", len(nigerian_state))

#  Task4: Tuple Unpacking
user_profile = (
    input("Enter your first name: "),
    int(input("Enter your age: ")),
    input("Enter your favorite color: "),
    input("Enter your home town: ")
)

first_name, age, favourite_color, home_town = user_profile      # Unpacking

print(f"Below is the {first_name}\'s profile:\nFirst Name:\t{first_name}\nAge:\t\t{age}\nColor:\t\t{favourite_color}\nHome town:\t{home_town}")


#  Task5: Modify Tuple Indirectly
shopping_list = (
    input("Enter the first item: "),
    input("Enter the second item: "),
    input("Enter the third item: ")
)
conv_shopping_list = list(shopping_list)
conv_shopping_list.append(input("Enter one more item: "))
conv_shopping_list.append(input("Enter another item: "))
updated_shopping_list = tuple(conv_shopping_list)
print('|'.join(updated_shopping_list))

#  Task6:  Attendance Tracker
days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

months_of_year = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" )

Student_name = input("Enter the Student\'s name: ")
Student_name = input("Enter the Gender: ")
Student_name = input("Enter the Course Track: ")
Student_name = int(input("Enter the Current month number (1-12): "))
Student_name = int(input("Enter the Current day number (1-7): "))