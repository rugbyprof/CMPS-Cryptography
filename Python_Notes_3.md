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
|![alt text][addition_4]|![alt text][multiplication_7] |![alt text][multiplication_6] |

|Plaintext|Number|Key 15|Ciphertext|
|:---:|:---:|:---:|:---:|
|A|0|(0 * 15) % 26 = 0|A|
|B|1|(1 * 15) % 26 = 15|P|
|C|2|(2 * 15) % 26 = 4|E|
|D|3|(3 * 15) % 26 = 19|T|
|E|4|(4 * 15) % 26 = 8|I|
|F|5|(5 * 15) % 26 = 23|X|
|G|6|(6 * 15) % 26 = 12|M|
|H|7|(7 * 15) % 26 = 1|B|
|I|8|(8 * 15) % 26 = 16|Q|
|J|9|(9 * 15) % 26 = 5|F|
|K|10|(10 * 15) % 26 = 20|U|
|L|11|(11 * 15) % 26 = 9|J|
|M|12|(12 * 15) % 26 = 24|Y|
|N|13|(13 * 15) % 26 = 13|N|
|O|14|(14 * 15) % 26 = 2|C|
|P|15|(15 * 15) % 26 = 17|R|
|Q|16|(16 * 15) % 26 = 6|G|
|R|17|(17 * 15) % 26 = 21|V|
|S|18|(18 * 15) % 26 = 10|K|
|T|19|(19 * 15) % 26 = 25|Z|
|U|20|(20 * 15) % 26 = 14|O|
|V|21|(21 * 15) % 26 = 3|D|
|W|22|(22 * 15) % 26 = 18|S|
|X|23|(23 * 15) % 26 = 7|H|
|Y|24|(24 * 15) % 26 = 22|W|
|Z|25|(25 * 15) % 26 = 11|L|


Some of this material is based on: [Hacking Ciphers](https://inventwithpython.com/hackingciphers.pdf) Written by: [Al Sweigart](https://inventwithpython.com/about.html) 

Reference-style: 


[addition_4]: http://f.cl.ly/items/0F15332X3u3K3U2V2w0R/addition_shift4.png "Addition Shift 4"
[multiplication_7]: http://f.cl.ly/items/3M1y0o1q3K3r1E1Z2l41/multiplication_key_7.png "Multiplication 7"
[multiplication_6]: http://f.cl.ly/items/1x3N2s3l0l3K3X433Q3i/multiplication_key_6.png "Multiplication 6"
