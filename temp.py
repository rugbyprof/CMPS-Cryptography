import collections
import sys
import fractions
import time
import pprint

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


def phi(n,return_list=False):
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

    #print(relatively_prime_generator(1024))
    #for n in relatively_prime_generator(1024,2,3):
    #    print(n)
    # start = time.time()
    # phi(303137)
    # end = time.time()
    # print(end-start)
    #
    # start = time.time()
    # phi(303137,True)
    # end = time.time()
    # print(end-start)

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
