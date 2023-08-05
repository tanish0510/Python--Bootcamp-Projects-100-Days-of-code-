print("------------------------------")
print("|Welcome to love calculator...|")
print("------------------------------")
name_1=input("enter name 1\n")
name_2=input("enter name 2\n")

combined_string=name_1+name_2

lowercase_string=combined_string.lower()

t=lowercase_string.count("t")
r=lowercase_string.count("r")
u=lowercase_string.count("u")
e=lowercase_string.count("e")

true=t+r+u+e
l=lowercase_string.count("l")
o=lowercase_string.count("o")
v=lowercase_string.count("v")
e=lowercase_string.count("e")

love=l+o+v+e
love_score=true+love

if love_score<50:
    print("FAIR")
elif love_score>50:
    print("Good")

lovescore=str(love_score)
print(f"your love score is : {lovescore}")
