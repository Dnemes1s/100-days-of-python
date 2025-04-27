print("Welcome top the tip calculator")

bill = float(input("What was the total bill ? "))
tip = int(input("How much would you like to tip ? 10, 12 or 15? "))
people = int(input("How many people to split the bill ?"))

tip_amm = tip / 100
bill_plus_tip = bill * tip_amm + bill
split_bill = bill_plus_tip / people

final_amm=(round(split_bill, 2))

print(f"Each person should pay: $ {final_amm}")