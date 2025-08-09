#   Electricity Bill Formatter

customer_fullname = input("Kindly enter your fullname: ")

units_consumed = int(input("Enter the units consumed (kWh): "))

cost_per_unit = float(input("Kindly provide the amount per unit: "))

total_bill = units_consumed * cost_per_unit

print(f"The neatly formatted receipt:\nCustomer\'s full name:\t\t{customer_fullname}\nUnits consumed(kWh):\t\t{units_consumed}\nCost per unit:\t\t\t#{cost_per_unit}\n______________________________________________\nTotal bill:\t\t\t#{total_bill:,}.")