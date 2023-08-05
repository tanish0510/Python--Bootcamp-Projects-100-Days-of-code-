# It will calculate the number of remaining days weeks and months of your life if you were to live 90 years old.....
print("Welcome to Death Countdown......")
age=input("Enter your age : ")
years_left=90-int(age)
months_left=years_left*12
days_left=years_left*365
print(f"You have {years_left} years {months_left} months and {days_left} days remaining")