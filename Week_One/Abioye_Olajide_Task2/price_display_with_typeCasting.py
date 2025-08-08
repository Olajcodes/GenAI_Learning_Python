#   Ask the user for the price of garri per paint in naira (as a string) and convert it to float. Display it with a message showing the amount in naira and kobo using print().

price_of_garri = input("How much is Garri per paint?: ")

conv_price_of_garri = float(price_of_garri)     #   Converted string to float

print(f"The price of Garri per paint is #{conv_price_of_garri}k")