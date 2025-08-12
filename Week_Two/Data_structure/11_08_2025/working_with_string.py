#   Strings in Python


# Single Quotes
name = 'Ada'
print(name)

# Double Quotes
greeting = "Hello"
print(greeting)

# Triple Quotes (for multiple-line strings)
story = '''Once upon a time, 
there was a coder named Ada.'''
print(story)

# String with numbers and symbols
password = "p@ssw0rd123"
print(password)

# STRING  OPERATIONS

#   Indexing
word = "My name is Abdullateef. I am an AI Engineer."
print(word[11])     # A
print(word[-9])     # E
# print(word[])

#   Slicing
word = "PythonS"
print(word[0:4])    # Pyth
print(word[2:])     # Start from index 2 to the end
print(word[:3])     #  Start from index 0 and stop at index 2
print(word[::2])    # Skipper: Steps on one character
print(word[::-1])   # Turns words backward

# String Concatenation & Repetition

a = "Hello"
b = "World"
print(a + " " + b)  #   Hello World

#  Repetition
word = "Hi! "
print(word * 3)

#   String Searching & Checking

# Membership
text = "Python programming"
print("Python" in text)     # True
print("Java" not in text)   # True

#   find() / rfind()
text = "Hello World"
print(text.find("o"))   # 4
print(text.rfind("o"))  # 7

#   index() / rindex()
text = "Hello World"
print(text.index("World"))

#   startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data"))
print(filename.endswith(".csv"))