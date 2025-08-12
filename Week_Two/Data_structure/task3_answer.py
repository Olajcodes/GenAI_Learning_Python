# # TASK 1

# 1. Program to accept a string input from user and display it in uppercase
string_input = input("Kindly provide your first name: ")
print(string_input.upper())

# 2. Given the string "python", print its first and last characters.
given_string = "python"
print(given_string[0], given_string[-1])

# 3. Ask the user for their name and print "Hello, ! the user name."
user_name = input("What\'s your name?: ")
print("Hello,!", user_name)

# 4. Write a program to count the number of characters in a string without using len().
character = input("Enter a word: ")
character_length = character.find(character[-1]) + 1
print(character_length)

# 5. Given "Hello World", replace "World" with "Python"
given_string = "Hello World"
print(given_string.replace("World","Python"))

# #   TASK 2

# 6. Check if a given string contains the substring "python" (case-insensitive)
given_string = input("Enter a word: ")
print("python" in given_string.lower())

# 7. Write a program to reverse a string without using slicing ([::-1])
given_string = "Python"
print(given_string[5], given_string[4], given_string[3], given_string[2], given_string[1], given_string[0])

# 8. Given a string with extra spaces, remove the leading and trailing spaces.
string_with_spaces = "     A String of words to test  "
print(string_with_spaces.strip())

# 9. Ask the user to enter a sentence and print the number of vowels in it
user_input_vowel = input("Kindly provide a sentence: ")
user_input = user_input_vowel.lower() 
print(user_input.count("i") + user_input.count("e") + user_input.count("a") + user_input.count("o") + user_input.count("u"))


# # 10. Convert a string "1234" to an integer and multiply it by 2
string = "1234"
string_to_int = int(string)
mul_string_to_int = string_to_int * 2
print(f"The multiplication is {mul_string_to_int}")

# # #  TASK 3

# # 11. Given "apple,banana,orange", split the string into a list of fruits
given_fruits_string = "apple,banana,orange"
print(given_fruits_string.split(","))

# # 12. Ask the user for a sentence and print each word on a new line
user_input = input("Enter a sentence: ")
input_splitted = user_input.split()
print(*input_splitted, sep='\n')

# 13. Replace all spaces in a string with underscores(_)
string_with_spaces = "I love Programming."
print(string_with_spaces.replace(" ", "_"))

# 14. Count how many times the letter "a" appears in "Banana".
string_1 = "Banana"
print(string_1.count("a"))

# 15. Check if a given string starts with "https://"
given_string = input("Enter your word: ")
print(given_string.startswith("https://"))
