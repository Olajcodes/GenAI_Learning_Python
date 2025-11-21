# num_list = []
# num_range = int(input("How many unique numbers do you want to read: "))
# for _ in range(num_range):
#     num = int(input("Enter the unique numbers: "))
#     if num in num_list:
#         print(f"{num} is a duplicate in the list, hence it can't be added!")
#     else:
#         num_list.append(num)

# for i in num_list:
#     print(i)   

# num_list.sort()

# print(f"The sorted list is {num_list}")


given_value = int(input("Enter the the value of n: "))

count = 0
for num in range(1, given_value+1):
    if num % 2 == 1:
        count += num

print(count)
        