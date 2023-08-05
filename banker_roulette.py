import random
names=input("Enter the names of the persons (separayed with comma): ")
names=names.split(",")
items=(len(names))
random_choice=random.randint(0,items-1)
payee=names[random_choice]
print(payee+"is going to pay the bill...")
