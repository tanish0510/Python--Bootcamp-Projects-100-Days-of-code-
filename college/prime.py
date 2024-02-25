def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

number = int(input("Enter a number: "))
result = prime_factors(number)

print(f"Prime factors of {number}: {result}")


