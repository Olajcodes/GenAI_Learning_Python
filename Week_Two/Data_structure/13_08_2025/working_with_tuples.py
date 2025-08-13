#   TUPLES

# Creating Tuples using parentheses()
fruits = ("apple", "banana", "cherry")
print(fruits)

#   Creating without parentheses (tuple packing)
numbers = 1, 2, 3
print(numbers)

#   Creating single-item tuple (must include a comma)
single_item = ("apple",)
print(single_item)
print(type(single_item))

# Creating using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

#  Characteristics of Tuples
# 1. Ordered: Items have a fixed position
colors = ("red", "green", "blue")
print(colors[0])

# 2. Immutable : Cannot change after Creation (Trying to test if it is so, and it's going to cause ERROR)
# colors[1] = "yellow"        # Type Error

# 3. Allow Duplicates
numbers = (1, 2, 2, 3)
print(numbers)

# 4. Can contain mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)

# 5. Can be nested (tuples inside tuples)
nested = (("a", "b"), (1, 2))
print(nested)

# Tuple Operations
# 1. Indexing
fruits = ('apple', "banana", "cherry")
print(fruits[1])
print(fruits[-1])

# 2.  Slicing
print(fruits[0:2])
print(fruits[::-1])

# 3.   Concatenantion
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)

# 4.  Reptition
nums = (1, 2)
print(nums * 3)

# 5.  Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
print("grape" not in fruits)

# 6.  Iteration
for fruit in fruits:
    print(fruit)


# Unpacking Tuples
person = ("John", 25, "Nigeria")
name, age, country = person
print(name)
print(age)
print(country)

# Tuple Methods
# 1.  dot count() and dot index()
numbers = (1, 2, 2, 3, 4)
print(numbers.count(2))
print(numbers.index(3))

# 2.  Converting Between List and Tuple
# Tuple to List
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)

# List back to Tuple
t = tuple(lst)
print(t)

# 3. Built-in Functions with Tuples
nums = (4, 1, 7, 3)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
