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

The caeser cipher uses addition with modulus as a function to map one letter to another. The same can be done using multiplication with modulus. However, a side effect of using multiplication is the possibility that we don't get a one-to-one function! To ensure we get a one-to-one function we must ensure that the number we multiply with is relatively prime to the number of characters we are mapping (e.g. gcd(26,7) = 1). 


|  Caeser Shift 4       | Multiplication 7             |   Multiplication 6           |
|-----------------------|------------------------------|------------------------------|
|![alt text][addition_4]|![alt text][multiplication_15] |![alt text][multiplication_6] |


Some of this material is based on: [Hacking Ciphers](https://inventwithpython.com/hackingciphers.pdf) Written by: [Al Sweigart](https://inventwithpython.com/about.html) 

Reference-style: 


[addition_4]: http://f.cl.ly/items/0F15332X3u3K3U2V2w0R/addition_shift4.png "Addition Shift 4"
[multiplication_7]: http://f.cl.ly/items/3M1y0o1q3K3r1E1Z2l41/multiplication_key_7.png "Multiplication 7"
[multiplication_6]: http://f.cl.ly/items/1x3N2s3l0l3K3X433Q3i/multiplication_key_6.png "Multiplication 6"
[multiplication_15]: http://f.cl.ly/items/2x3W1x222C3w40070k3o/multiplication_key_15.png "Multiplication 15"
