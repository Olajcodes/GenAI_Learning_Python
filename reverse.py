word = "python world"
print(word[::4])

reverse_word = ""

for ch in word:
    reverse_word = ch + reverse_word
print(reverse_word)

print(word[::-1])

print(word.rfind("a"))

print(word.rindex("world"))

character = input("Enter a word: ")
character_length = character.find(character[-1]) + 1
print(character.find(character[-1]))
print(character_length)

fruits = ["apple", "banana"]
fruits.insert(2, "orange")
fruits.remove("watermelon")
print(fruits)  
Output: ['apple', 'orange', 'banana']

#  Calculator
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Zero division not allowed!"
    
def sqrt(num):
    return num ** 0.5

def exp(num1, num2):
    return num1 ** num2


def main():
    while True:
        try:
            print("\nWelcome to calculate operations!!!\n===================================================\nEnter the operation you want to perform from the options below:")
            print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Square root\n6. Exponential\n0. Exit.")
            
            choice = int(input("Enter the operation to perform: "))
            
            if choice == 0:
                print("Exiting the program...")
                break
            elif choice == 1:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(f"The addition of {num1} + {num2} is {add(num1, num2)}")
            elif choice == 2:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(f"The subtraction of {num1} - {num2} is {sub(num1, num2)}")
            elif choice == 3:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))    
                print(f"The multiplication of {num1} * {num2} is {mul(num1, num2)}")
            elif choice == 4:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(f"The division of {num1}/{num2} is {divide(num1, num2)}")
            elif choice == 5:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(f"The square root of {num1} is {sqrt(num1)}")
                print(f"The square root of {num2} is {sqrt(num2)}")
            elif choice == 6:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                print(f"The Exponent of {num1}^{num2} is {exp(num1, num2)}")
            else:
                print("Invalid options. Try again!\n")
        except ValueError:
            print("Oops! Kindly provide number instead.\n")
        except KeyboardInterrupt:
            print("\nThe program ended due to keyboard interrupt...\n")
            break
        except Exception as e:
            print("Unexpected error occurred: ", e)
            
main()

name = "olajideAbioye@gmail.com"
username, domain = name.split("@")
print(username,"\n",domain) 

#  Email Slicer
while True:
    try:
        user_email = input("Kindly enter your email address: ").lower().strip()
        
        if "@" in user_email and "." in user_email.split("@"[1]):
            username, domain = user_email.split("@") 
            print(f"Username: {username}")
            print(f"Domain: {domain}")
        else:
            print("Invalid email address. Try Again!")
    except Exception as e:
        print(f"Error: {e}")