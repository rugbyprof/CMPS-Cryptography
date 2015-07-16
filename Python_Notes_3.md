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

The following snippet calculates phi(n), or the number of integers that are coprime (relatively prime) to n. This version will alternatively return the actual values that are coprime to n if wanted. Lets all agree that this would be insane for extremely large n :) 

```python
import fractions

def phi(n,return_list=False):
    amount = 0
    coprimes = []

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
            coprimes.append(k)

    if return_list:
        return coprimes
    else:
        return amount
        
print(phi(30,True))

#Output: [1, 7, 11, 13, 17, 19, 23, 29]

print(phi(30))

#Output: 8
```

#### Multiplicative Cipher

The caeser cipher uses addition as a function to map one letter to another. 

|Plaintext Symbol|Number|Shift 4|Ciphertext|
|:---:|:---:|:---:|:---:|
|A|0|0 + 4 % 26 = 4|E|
|B|1|1 + 4 % 26 = 5|F|
|C|2|2 + 4 % 26 = 6|G|
|D|3|3 + 4 % 26 = 7|H|
|E|4|4 + 4 % 26 = 8|I|
|F|5|5 + 4 % 26 = 9|J|
|G|6|6 + 4 % 26 = 10|K|
|H|7|7 + 4 % 26 = 11|L|
|I|8|8 + 4 % 26 = 12|M|
|J|9|9 + 4 % 26 = 13|N|
|K|10|10 + 4 % 26 = 14|O|
|L|11|11 + 4 % 26 = 15|P|
|M|12|12 + 4 % 26 = 16|Q|
|N|13|13 + 4 % 26 = 17|R|
|O|14|14 + 4 % 26 = 18|S|
|P|15|15 + 4 % 26 = 19|T|
|Q|16|16 + 4 % 26 = 20|U|
|R|17|17 + 4 % 26 = 21|V|
|S|18|18 + 4 % 26 = 22|W|
|T|19|19 + 4 % 26 = 23|X|
|U|20|20 + 4 % 26 = 24|Y|
|V|21|21 + 4 % 26 = 25|Z|
|W|22|22 + 4 % 26 = 0|A|
|X|23|23 + 4 % 26 = 1|B|
|Y|24|24 + 4 % 26 = 2|C|
|Z|25|25 + 4 % 26 = 3|D|

 We can do the same with multiplication.
 
 

Some of this material is based on: [Hacking Ciphers](https://inventwithpython.com/hackingciphers.pdf) Written by: [Al Sweigart](https://inventwithpython.com/about.html) 
