#   CREATING AND MANIPULATING STRINGS\

# Upper()
name = "Abioye Olajide"
print(name.upper())

# lower()
sentence = "Python is Amazing"
print(sentence.lower())

# title()
sentence = "chapter one is python programming"
print(sentence.title())

# strip()
text = "      Abuja   "
print(text.strip())

# replace()
message = "I love Java"
print(message.replace("Java", "Python"))

#  swapcase()
text = "Hello ABEOKUTA"
print(text.swapcase())

# lstrip()
text = "     Nigeria"
print(text.lstrip())

#  rstrip()
text = "Nigeria    "
print(text.rstrip())

#  split()
fruits = 'mango orange banana'
splited = fruits.split()
print(fruits.split())

#  rsplit()
text = "one,two,three,four"
print(text.rsplit(",",2))

# splitlines()
lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())

# join()
words = ["I", "love", "Python"]
print(" ".join(words))

# center()
text = "Python"
print(text.center(20, "-"))

# ljust()
text = "Python"
print(text.ljust(10, "*"))

# rjust()
text = "Python"
print(text.rjust(10,"*"))

# zfill()
num = "42"
print(num.zfill(5))

# isalpha()
print('Lagos'.isalpha())
print("Lagos123".isalpha())

# isdigit()
print("12345".isdigit())
print("123a".isdigit())

# isalnum()
print("Python3".isalnum())
print("Python 3".isalnum())