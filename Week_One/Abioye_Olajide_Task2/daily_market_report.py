#   Daily Market Report Ask the user to input: Market name Number of traders Daily revenue in naira Display the result using f-string formatting with commas for thousands separator.

market_name = input("Provide the market name: ")

number_of_traders = int(input("How many number of traders?: "))

daily_revenue_in_naira = int(input("What is the daily revenue in Naira?: #"))

print(f"The {market_name} market with {number_of_traders} traders generate #{daily_revenue_in_naira:,} revenue daily.")
