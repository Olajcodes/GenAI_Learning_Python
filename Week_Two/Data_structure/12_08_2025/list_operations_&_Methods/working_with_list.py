#   How to create a list

# Method 1: Using square brackets
empty_list = []
print(empty_list)

# Method 2: Using the list() constructor
empty_list2 = list()
print(empty_list2)

# creating a list with initial elements
# List of integers 
numbers = [1,2,3,4,5]
print(numbers)  # Output: [1, 2, 3, 4, 5]

# List of strings
fruits = ["apples", "banana", "cherry"]
print(fruits)

# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)

#  From a string (each character becomes an element)
chars = list("hello")
print(chars)

# From a Tuple
my_tuple = (10,20,30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

#  From a range
numbers_range = list(range(5))
print(numbers_range)

# Creating a list using list comprehension
# Squares of numbers 0 - 4
squares = [x**2 for x in range(5)]
print(squares)

#  Even numbers between 0 - 10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)

#  Even numbers between 0 - 10
numbers = int(input("Enter  whole number: "))
odd = [num for num in range(numbers) if num % 2 == 1]
print(odd)

# Matrix-like list
matrix = [[1,2], [3,4], [5,6]]
print(matrix)

#  Accessing elements in a nested list
print(matrix[0])
print(matrix[0][1])

# Ordered Collection
fruits = ["mango", "orange", "banana"]
print(fruits)
print(fruits[0])
print(fruits[2])

# Allows Duplicates
items = ["rice", "beans", "yam", "rice"]
print(items)

# Mutable (can be changed)
numbers = [1, 2, 3]
numbers[1] = 20  # Changing element at index 1
print(numbers)

#  Contain different data types
mixed = [10, "Nigeria", 3.14, True]
print(mixed)

#  Can be Nested
nested_list = [[1, 2], ["a", "b"]]
print(nested_list)
print(nested_list[0][1])

#  Dynamic Size
names = ["Olajide"]
names.append("Abdullateef")
names.append("Abioye")
names.remove("Olajide")
print(names)
