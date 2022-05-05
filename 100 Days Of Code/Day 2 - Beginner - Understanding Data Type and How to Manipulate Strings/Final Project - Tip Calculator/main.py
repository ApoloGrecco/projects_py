print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")

percentage_tip = input("What percentage tip would you like to give?"
                        "10, 12 or 15? ")

split_bill = input("How many people to split the bill? ")

total_bill_float = float(total_bill)
split_bill_int = int(split_bill)
percentage_tip_float = (float(percentage_tip) / 100) + 1

bill_by_person = (total_bill_float / split_bill_int) * percentage_tip_float

rounding_bill = round(bill_by_person, 2)

print(f"Each person should pay: ${rounding_bill}")
