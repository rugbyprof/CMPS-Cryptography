

# Extended Euclidean algorithm
#   returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# GCD
#   returns the greatest common denominator. Thats it.
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

# Mod Inverse V1
#   returns the modular multiplicative inverse (x) of a and m.
#   where ax = 1 (mod m) (= means congruent here)
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        #raise Exception('modular inverse does not exist')
        return None
    else:
        return x % m

# Euler's totient function
#   returns some integer that represents the positive integers
#   less than or equal to n that are relatively prime to n.
def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1

    return amount
