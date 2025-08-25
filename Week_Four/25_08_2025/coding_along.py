# #  range()
# for i in range(3):
#     print(i) 

# #  zip()
# names = ["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)

# # Lambda and map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)

# # filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)

# #  Student Performance & Feedback System
# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# print("\nStudent Data:")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# # Summary using buil-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score", highest)
# print("Lowest Score", lowest)

# # Ranking (Using sorted and zip)
# ranked = sorted(zip(scores, names), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# # Check data types
# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# # Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores ))
# print("\nPassing Scores:", passing)

# #  Map names to uppercase
# upper_names = list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upper_names)

# # Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)


# #  Defining a function
# def greet():
#     print("Hello, welcome to AI Fellowship!")

# # When you want to use a function, this is how to call it.
# greet()
# greet()
# greet()

# # Function Arguments and Parameters
# def greet(name):
#     print("Hello", name, "Welcome to Python learning!")

# # Calling with parameter - the actual name
# greet("Class rep")
# greet("Ridwan")

#  return print() and yield()
def greet(name):
    return f"Hello", name
    print("Hello", name)

#  Function call
result = greet("Esther")

print("Result:", result)