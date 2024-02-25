def factorial(num):
    if num==1:
        return 1
    else:
        return (num*factorial(num-1))

num =4
print(f"the fact of {num} is ",factorial(num))