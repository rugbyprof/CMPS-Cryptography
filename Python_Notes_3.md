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

The caeser cipher uses addition as a function to map one letter to another. We can do the same with multiplication. 

|   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|

Some of this material is based on: [Hacking Ciphers](https://inventwithpython.com/hackingciphers.pdf) Written by: [Al Sweigart](https://inventwithpython.com/about.html) 
