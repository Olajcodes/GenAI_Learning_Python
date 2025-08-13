# Task1: Create and Display
print("Kindly enter your three favorite Nigerian dishes")
dishes = []     # Still in List
for food in range(3):
    dishes.append(input("Enter your favorite dish %d : " % food))    

dishes_tuple = tuple(dishes)        # List to Tuple
print(dishes_tuple)
print(*dishes_tuple, sep="\n")


# Task2: Tuple and Input
print("Kindly provide your 5 best friend's name")
best_friends = []
for name in range(5):
    best_friends.append(input("Enter your best friend's name %d : " % name))
    
best_friends_tuple = tuple(best_friends)        # List to Tuple
print(best_friends_tuple[::-1])


# 
