print("Welcome to the tip calculator!")

# Get user inputs
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate total per person
total_per_person = round(bill * (1 + (tip / 100)) / people, 2)

# Format to always show two decimal places
formatted_total = "{:.2f}".format(total_per_person)

print(f"Each person should pay: ${formatted_total}")
