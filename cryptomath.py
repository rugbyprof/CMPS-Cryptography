# Cryptomath Module
# http://inventwithpython.com/hacking (BSD Licensed)

def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b

def succesiveSquaring(base, exp, mod):
    if exp == 0:
        x = 1
    else:
        half = succesiveSquaring(base, exp // 2, mod)  # just / in Python 2
        x = half * half
        if exp % 2 == 1:
            x *= base
    return x % mod

def gcdr(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    k=0
    while a != 0:
        q = b // a
        r = b % a
        d = b
        a, b = b % a, a
        if k > 0:
            print('{} = {} x {} + {}'.format(d,q,b,r))
        k+=1
    return b

def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcdr(a, m) != 1:
        assert "Not relatively prime!"
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

if __name__ == '__main__':
    print(findModInverse(1051,17))
    print(succesiveSquaring(2,1234,789))
