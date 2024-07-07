def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Example usage
a = 56
b = 98
print("GCD of", a, "and", b, "is", gcd(a, b))
