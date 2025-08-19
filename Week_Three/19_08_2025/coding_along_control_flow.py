# #   Conditional Statements
# # if Statments
# age = 20
# if age >= 18:
#     print("You are eligible to vote")

# # if-else Statement
# wallet = 400
# price = 500

# if wallet >= price:
#     print("Purchase succcessful")
# else:
#     print("Insufficient balance")

# #  if-elif-else Statement
# score = 85
# if score >= 70:
#     print("Grade A")
# elif score >= 50:
#     print("Grade B")
# else:
#     print("Grade C")

# #  Nested if Statement
# age = 19
# citizen = True

# if age >= 18:
#     if citizen:
#         print("You can vote")
#     else:
#         print("You must be a citizen to vote")
# else:
#     print("Too young to vote")


# #  LOOPS
# # for loop
# # Iterates through each element in a LIST
# fruits = ["apple", "banana", "orange"]
# for fruits in fruits:
#     print(f"I like {fruits}")

# #  Iterates through each element in a TUPLE
# coordinates = (0.34654, -0.48585, 0.57477)
# for point in coordinates:
#     print(f"Point: {point}")

# # Iterates through each element in a DICTIONARY. Remember that dictionaries have key-value pairs.
# student ={"name": "Olajide", "age": 16, "grade": "A"}
# for key, value in student.items():
#     print(f"{key}: {value}")

# #  Iterates through each element in a STRING. Remember that strings are sequences of characters.
# word = "PYTHON"
# for c in word:
#     print(c, end=" ")


#  WHILE LOOP
# while condition:
'''
Let the loop start with count = 1
Let it keep printing until count is greater than 5
Let the loop terminate when the condition is no longer true
'''

# count = 1
# while count <= 5:
#     print("Number:", count)
#     count += 1

# #  Incrementing with "While"
# num = 1
# while num <= 10:
#     print(num, end=" ")
#     num += 1

# #  Decrementing with "While"
# timer = 10
# while timer > 0:
#     print("Countdown:", timer)
#     timer -= 1

# password = " "
# while password != "python123":
#     password = input("Enter the password: ")

# print("Access Granted")


# #  Understanding while True
# #  While True
# #  Keep asking the user for a name until they type "exit".

# while True:
#     name = input("Enter your name (type 'exit' to quit): ")
#     if name.lower() == "exit":
#         print("Goodbye!")
#         break
#     print(f"Hello, {name}")


# #  Loop Control Statements (break, continue, and pass)
# #  break 
# for num in range(1, 10):
#     if num == 5:
#         break
#     print(num)

#  continue
# for num in range(1, 6):
#     if num == 3:
#         continue
#     print(num)

# #  Pass
# for num in range(1, 6):
#     if num == 3:
#         pass
#     print(num)

# #  Lets try while True again
# while True:
#     print("\nMenu:")
#     print("1.  Say Hello")
#     print("2.  Say Goodbye")
#     print("3.  Exit")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         print("Hello")
#     elif choice == "2":
#         print("Goodbye")
#     elif choice == "3":
#         print("Exicting program...")
#         break
#     else:
#         print("Invalid choice. Try again.")

#  Try and use while True for validation
# while True:
#     age = input("Enter your age: ")
#     if age.isdigit():
#         print(f"Your age is {age}")
#         break
#     else:
#         print("Invalid input. Please enter a number.")

# Let's make a guess
secret = "python"

while True:
    guess = input("Guess the secret word: ")
    if guess.lower() == secret:
        print("Correct! You guessed the word.")
        break
    else:
        print("Wrong! Try again.")

#  Do you remeber this?

balance = 1000
