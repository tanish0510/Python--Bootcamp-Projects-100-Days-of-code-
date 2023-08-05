size = input("Do you want small , medium or large pizza ? :: S  M  L")
type_1 = input("Do you want pepperoni? :: Y or N")
type_2 = input("Do you want extra cheese ? :: Y or N ")
bill = 0
if size == "S":
    bill = bill+10
elif size == "M":
    bill-bill+15
elif size == "L":
    bill = bill+20
if type_1 == "Y":
    if size == "S":
        bill = bill+3
    elif size == "M":
        bill = bill+4
    elif size == "L":
        bill = bill+5


else:
    bill = bill+0
if type_2 == "Y":
    bill = bill+1
else:
    bill = bill+0
print(f"Your bill is {bill} ")
