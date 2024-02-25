def find_largest(a, b, c):
    largest=[a,b,c]
    return max(largest)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

result = find_largest(num1, num2, num3)
print("The largest number is:", result)
