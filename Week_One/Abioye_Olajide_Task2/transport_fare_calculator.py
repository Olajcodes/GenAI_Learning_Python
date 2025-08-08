#   Transport Fare Calculator

distance = float(input("Provide the distance in km: "))

fare = float(input("Enter the fare per km: "))

total_fare = distance * fare

print(f"The total fare is {total_fare:.2f}")