import collections
import sys

def first_n_coprimes():
    N = 100

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
#    print('{} is coprime with {} others'.format(n, len(coprimes))
    print(n,' is coprime with ',len(coprimes),' others')
