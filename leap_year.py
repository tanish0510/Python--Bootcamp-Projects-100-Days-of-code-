year=int(input("Enter the year : "))
if year%4==0:
    print("It is a leap year")
elif year%100==0:
    print("It is not a leap year")
elif year%400==0:
    print("It is a leap year")
else :
    print("Not a leap year")