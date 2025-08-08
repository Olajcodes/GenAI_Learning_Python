#   Electricity Bill Formatter

customer_fullname = input("Kindly enter your fullname: ")

units_consumed = int(input("Enter the units consumed (kWh): "))

cost_per_unit = float(input("Kindly provide the amount per unit: "))

total_bill = units_consumed * cost_per_unit

print(f"The neatly formatted receipt:\nCustomer\'s full name: {customer_fullname}\nUnits consumed(kWh): {units_consumed}\nCost per unit: #{cost_per_unit}\nThe total bill: #{total_bill:,}.")