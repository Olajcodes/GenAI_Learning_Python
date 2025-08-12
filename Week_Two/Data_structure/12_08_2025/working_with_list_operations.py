#  List Operations in Python
# Concatenation(+)
list1 = [1, 2, 3]
list2 = [4, 5]
result = list1 + list2
print(result)

#  Repetiton
nums = [1, 2]
repeated = nums * 3 
print(repeated)

#  Indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[-1])

#  Slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[::2])

# Membership (in/not in)
colors = ["red", "green", "blue"]
print("green" in colors)
print("yellow" not in colors)

#  Length (len())
items = ["pen", "book", "laptop"]
print(len(items))

# Min and Max (min()/max())
nums = [5, 2, 9, 1]
print(min(nums))
print(max(nums))

# sum (sum())
numbers = [1, 2, 3, 4]
print(sum(numbers))

# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)

# Copying a duplicate list
a = [1, 2, 3]
b = a.copy()
b = list(a) #This can also be used.
print(b)