# This calculator project helps to split the total restrauant bill plus tip that each person should pay

print("Welcome to the tip calculator!")

bill = float(input(f"What was the total bill? £")) # total amount
tip = int(input(f"\nWhat percentage tip would you like to give? 10 12 15: ")) # What percentage of tip to give: 10%, 12% or 15%
people = int(input(f"\nHow many people to split the bill? ")) # between how many people? 

# calculation 
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: £{final_amount}") # output amount
