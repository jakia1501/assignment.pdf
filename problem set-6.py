a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(f"Greatest Common Divisor of {a} and {b} is: {find_gcd(a, b)}")
