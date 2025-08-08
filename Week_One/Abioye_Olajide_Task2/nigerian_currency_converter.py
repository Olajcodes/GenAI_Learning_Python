#   Nigerian Currency Converter

amount_naira = float(input("Enter the amount in Naira: ₦"))

rate_to_US_Dollars = float(input("Please provide the exchange rate to US Dollars: $"))

rate_to_British_Pounds = float(input("Please provide the exchange rate to British Pounds: £"))

conv_rate_to_US_Dollars = rate_to_US_Dollars * amount_naira     #   Converted rate to US Dollars

conv_rate_to_British_Pounds = rate_to_British_Pounds * amount_naira     #   Converted rate to British Pounds

print(f"Amount(₦)\t\tUS Dollars($)\t\tBritish Pounds(£)\n{amount_naira:,}\t\t   {conv_rate_to_US_Dollars:,}\t\t\t  {conv_rate_to_British_Pounds:,}")