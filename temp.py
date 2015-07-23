import fractions
import collections
import sys
import fractions
import time
import pprint

# Extended Euclidean algorithm
#   returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
def egcd_r(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Extended Euclidean algorithm
#   returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
def egcd_i(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

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
    g, x, y = egcd_r(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# Mod Inverse V2
#   returns the modular multiplicative inverse (x) of a and m.
#   where ax = 1 (mod m) (= means congruent here)
def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None # no mod inverse exists if a & m aren't relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

# Euler's totient function
#   returns some integer that represents the positive integers
#   less than or equal to n that are relatively prime to n.
def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount

# Euler's totient function (verbose)
#   returns some integer that represents the positive integers
#   less than or equal to n that are relatively prime to n.
#
#   Also returns the list of positive integers (not just the count)
#   if the return_list parameter is True
#   For Academic purposes
def phi_v(n,return_list=False):
    amount = 0
    if return_list:
        coprimes = []

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
            if return_list:
                coprimes.append(k)


    if return_list:
        return coprimes
    else:
        return amount

def prime_factors_less_n(N):

    factors = [set() for n in range(N)]
    factored = collections.defaultdict(set)

    print(len(factored))
    sys.exit()

    for n in range(2, N):
        if not factors[n]:           # no factors yet -> n is prime
            for m in range(n, N, n): # all multiples of n up to N
                factors[m].add(n)
                factored[n].add(m)

    for n in range(1, N):
        coprimes = set(range(1, N))  # start with all the numbers in the range
        for f in factors[n]:         # eliminate numbers that share a prime factor
            coprimes -= factored[f]
        print(n,' is coprime with ',len(coprimes),' others')


def relatively_prime_generator(n, a=1, b=1):
    ### generates all relatively prime pairs <= n.  The larger number comes first.
    #result = []

    yield (a,b)
    #result.append((a,b))
    k = 1
    while a*k+b <= n:
        for i in relatively_prime_generator(n, a*k+b, a):
            yield i
            #result.append(i)
        k += 1
    #return result

def print_md_table(data):
    table = []
    temp = []

    for v in data[0]:
        temp.append('|{}'.format(v))
    temp.append("|")
    table.append(''.join(temp))

    temp = []
    for v in data[0]:
        temp.append("|:---:")
    temp.append("|")
    table.append(''.join(temp))

    temp = []

    rows = len(data)
    cols = len(data[0])

    for row in range(1,rows):
        temp = []
        for col in range(cols):
            temp.append('|{}'.format(data[row][col]))
        temp.append("|")
        table.append(''.join(temp))


    for row in table:
        print(row)

if __name__ == '__main__':

    data = []
    data.append(['Plaintext Symbol', 'Number', 'Shift of 4', 'Ciphertext'])
    for i in range(26):
        encryption = '{} + 4 % 26 = {}'.format(i,(i+4)%26)
        symbol = '{}'.format(chr(((i+4)%26)+65))
        data.append([chr(i+65),i,encryption,symbol])
    print_md_table(data)

    data = []
    data.append(['Plaintext Symbol', 'Number', 'Encryption with Key 7', 'Ciphertext'])
    for i in range(26):
        encryption = '({} * 6) % 26 = {}'.format(i,(i*6)%26)
        symbol = '{}'.format(chr(((i*6)%26)+65))
        data.append([chr(i+65),i,encryption,symbol])
    print_md_table(data)
