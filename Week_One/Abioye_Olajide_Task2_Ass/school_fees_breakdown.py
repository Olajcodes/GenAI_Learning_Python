#   School Fees Breakdown

school_name = input("Kindly enter the school name: ")

tuition_fee = float(input("Enter your Tuition fee: "))

hostel_fee = float(input("Provide your hostel fee: "))

feeding_fee = float(input("How much is for your feeding?: "))

total_fee = tuition_fee + hostel_fee + feeding_fee

print(f"The School Fees Breakdown for {school_name} is as follows:\nTuition Fee:\t\t{tuition_fee}\nHostel Fee:\t\t{hostel_fee}\nFeeding Fee:\t\t{feeding_fee}\n___________________________________\nTotal Fee:\t\t{total_fee}")