#### Multiple Assignment

- Assigns a comma delimited set of values (with n values) or a list (of size n) to n individual variables.
- Not n+1 or n-1 variables.

```python
first, middle, last , age = 'Joe', 'Lee', 'Smith', 42
print(first, middle, last , age)
#output: Joe Lee Smith 42

a, b, c, d = ['Alice', 'Bob', 'Carol', 'David']
print(a,b,c,d)
#output: Alice Bob Carol David
```

#### Swapping Values

- Leveraging the multiple assignment statement, we can swap values:
```python

i , j = 13 , 11
j , i = i , j
print(i , j)
#output: 11 13
```

#### Euclid's Algorithm

- Euclid’s Algorithm for Finding the GCD of Two Numbers

```python
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
```
#### Relatively Prime

Relatively prime numbers are used for the multiplicative and affine ciphers. We say that two numbers are relatively prime if their greatest common divisor is 1. That is, the numbers a and b are relatively prime to each other if the gcd(a, b) == 1.

The following snippet will print out `n` integers `1 <= n <= 99` along with how many other integers that are also `1 <= n <= 99` that it is coprime (relatively prime) with.

```python
import collections
N = 100

factors = [set() for n in range(N)]
factored = collections.defaultdict(set)

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
```
Source: [StackOverflow](http://stackoverflow.com/questions/23922371/optimizing-list-comprehension-to-find-pairs-of-co-prime-numbers)

Example:

```
1  is coprime with  99  others
2  is coprime with  50  others
3  is coprime with  66  others
4  is coprime with  50  others
5  is coprime with  80  others
6  is coprime with  33  others
7  is coprime with  85  others
8  is coprime with  50  others
9  is coprime with  66  others
10  is coprime with  40  others
11  is coprime with  90  others
12  is coprime with  33  others
13  is coprime with  92  others
...
```

Source: [Hacking Ciphers](https://inventwithpython.com/hackingciphers.pdf) Written by: [Al Sweigart](https://inventwithpython.com/about.html)
