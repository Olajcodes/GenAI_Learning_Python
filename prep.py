# # Use a list to collect numbers
# # Accept 20 numbers form users
# # Check for duplicate (not accepted)
# # Print using for statement
# # Sort the list
# # print the sorted list

# num_list = []

# # Assuming the numbers to be read wasn't specified
# n = int(input("Enter the amount of numbers to be read: "))

# # For loop - 
# for i in range(n):
#     num = int(input("Enter the unique numbers: "))
    
#     if num in num_list:
#         print(f"{num} is a duplicate, hence cannot be added!")
#     else:
#         num_list.append(num)
        
# # Printing out the items in the list
# for items in num_list:
#     print(items)
    

# print(f"Before sorting: {num_list}\n")  
  
# # Sorting the list
# num_list.sort()

# # Printing the sorted list
# print(f"The sorted list: {num_list}")

# Using for loop
# Odd numbers between 1 to n

# Specifying the value of n
n = int(input("Enter the value of n: "))

count = 0
# if n = 10 that means our range is 1 - 11 (20, 30 18)
for num in range(1, n+1):
    if num % 2 != 1:
        count = count + num

print(f"The total sum of the even numbers is {count}")
        
    
name = "AbaaaaBBBBBBUUYSTSFGSSBNSSxnsn"

count = 0
for ch in name:
       if ch == "A":
           count = count + ch