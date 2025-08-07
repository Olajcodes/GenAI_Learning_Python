# This is Creating an Imagination for Operations on BANK
#  Prompt for Password / Pin
#   Welcome Screen
#   Select Options (Transfer)
#   

name = input("Enter your Name: ")
pin_request = int(input("Kindly enter your Pin: "))
print(f"Welcome {name}!")

operation_request = input("What will you like to do? (Withdrawal / Deposit / Check Balance): ")
confirming_option = bool(input("Are you sure? (TRUE / FALSE): "))
print(f"The Option selected is {operation_request}")


