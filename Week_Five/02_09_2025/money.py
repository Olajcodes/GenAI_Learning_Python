#  Send money to Victoria
balance = 10000

money_to_send = int(input("Kindly enter amount: "))

account_number = int(input("Enter the account number to send money to: "))

if money_to_send <= balance:
    print(f"#{money_to_send} has been successfully sent to {account_number} - Victoria Omoniyi")

else:
    print("Insufficient funds!")