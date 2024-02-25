def triangle(base,hyp,perp):
    try:

        if hyp*hyp==base*base+perp*perp:
            print("it is a right angled triangle")
        else:
            print("not right angled")


    except ValueError as e:
        print("Error:",e)

# base=int(input("enter the base:"))
# hyp=int(input("enter the hypotenuse:"))
# perp=int(input("enter the perpendicullar:"))
base = int(input("enter the base:"))
hyp = int(input("enter the hypotenuse:"))
perp = int(input("enter the perpendicullar:"))
result = triangle(base, hyp, perp)
print(result)

