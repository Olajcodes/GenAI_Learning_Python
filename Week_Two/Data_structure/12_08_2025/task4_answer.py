#  TASK ONE: Your Favorite Life Quote
user_input = input("Kindly provide your favorite quote: ")
user_input_to_titleCase = user_input.title()
print(f'\"{user_input_to_titleCase}\"')

#  TASK TWO: Shopping List Manager
shopping_list = []
user_input_1 = input("Kindly input what you want to shop: ")
user_input_2 = input("Kindly input what you want to shop: ")
user_input_3 = input("Kindly input what you want to shop: ")
# Adding to cart
shopping_list.append(user_input_1)
shopping_list.append(user_input_2)
shopping_list.append(user_input_3)
print(shopping_list)

# TASK THREE: Word Counter
user = input("Type in a sentence: ")
splitted_sentence = user.split()
print(splitted_sentence)
num_of_words = len(splitted_sentence)
print(f"The number of words present in the sentence is: {num_of_words}")

#  TASK FOUR: Name Organizer
name_request = input("Kindly enter 5 names separated by spaces only: ")
conv_name_request = name_request.lower().split()    #   converting to lowercase
conv_name_request.sort()
print(*conv_name_request, sep='\n')

#  TASK FIVE: Student Score Tracker
student_names = []
student_score = []

student_names_request_1 = input("What is the student\'s name: ")
student_names.append(student_names_request_1)
student_score_request_1 = int(input("What is the corresponding Score?: "))
student_score.append(student_score_request_1)

student_names_request_2 = input("What is the student\'s name: ")
student_names.append(student_names_request_2)
student_score_request_2 = int(input("What is the corresponding Score?: "))
student_score.append(student_score_request_2)

student_names_request_3 = input("What is the student\'s name: ")
student_names.append(student_names_request_3)
student_score_request_3 = int(input("What is the corresponding Score?: "))
student_score.append(student_score_request_3)

print("The formatted score sheet is below: ")
for i in range(3):
    print(f"{student_names[i]}:\t{student_score[i]}")


# TASK SIX: Word Analyzer
user_input = input("Kindly enter a word: ")
print(len(user_input))
print(user_input.isupper())     # Check if it is Uppercase
print(user_input.islower())     # Check if it is lowercase
print(user_input.istitle())     # Check if it is title case

print(user_input[::-1])         # Slicing a word

# TASK SEVEN: List Manipulation
cities = ["Abuja", "Lagos", "Ibadan", "Kano", "Jos"]
user_city = input("Enter any city different from (Abuja, Lagos, Ibadan, Kano, Jos): ")
cities[2] = user_city
cities.pop()
cities.insert(0, "Akure")
print(cities)