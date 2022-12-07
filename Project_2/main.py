#### ---------------------------------------------------------------- ###########
print("Welcome to the tip calculator")
total_cash = float(input("What was the total bill?\n"))
pg_like = int(input("What percentage tip would you like to give?\n"))
number_people = int(input("How many people to split the bill?\n"))

pg_total_final = pg_like / 100 
total_cash_final = total_cash * pg_total_final
total_billb= total_cash + total_cash_final
bill_per_person = total_billb / number_people
final_acont = round(bill_per_person, 2)

print(f"Each person should pay {final_acont:.2f}")
