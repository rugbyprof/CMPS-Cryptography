___Prop___

1. For every _a_ ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/neq.gif) _0_, 
    - _a_ | _0_, 
    - _a_ | _a_, 
    - also _1_ | _b_ for every _b_
2. if _a_ | _b_ and _b_ | _c_ , then _a_ | _c_
3. If _a_ | _b_ and _a_ | _c_, then _a_ | _sb + tc_ for any _s,t_ that ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/in.gif) ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/integers.gif)

- A number `p > 1` that is divisible only by 1 and itself is called prime.
- An integer that is not prime is called composite, that `n=ab`, where `1 < a,b < n`

___Thm___
```
There are infinitely many prime numbers.
```

___Thm___
```
Let Pi(n) be the number of primes less than n. Then Pi(x) = x / log(x) (approx)

ratio Pi(x) / (x / ln(x)) -> 1 as x -> infinity

```

___Thm___
```
For every positive integer is a product of primes. The factorization is unique up to order.

```

___Thm___
```
If p is prime and `p | ab` then `p|a` or `p|b`

```

___Definition___ 

```
The greatest common divisor of a & b is the largest positive integer dividing both a & b.
We denote that as gcd(a,b) = ??
```

```
We say that a & b are relatively prime, if there gcd(a,b) == 1
```

___Division Algorithm___

```
Given a & b in integers, there exists a unique q,r such that a = ba + r where 0 <= r < b
```

___Euclidian Algorithm___

1728 = 12(135) + 108
135 = 108(1) + `27`(gcd)
108 = 27(4) + 0

gcd(482,1180)

1180 = 2(482) + 216
482 = 2(216) + 50
216 = 4(50) + 16
50 = 3(16) + `2`
16 = 8(2) + 0

`gcd(a,b) = gcd(b,r)`

___Def___

Let a,b,n integers and n != 0
we say that a is congruent to b % n , a (triple equal) b (mod n)

if n|a-b 

32 congruent 7 (mod 5)

32 - 7 = 25 => 25 / 5 == 0

-12 congruent 37 (mod 7)

-12 - 37 = -49 => -49 % 7 == 0

___Prop___

Let a,b,c,n be integers and n != 0
1. a congruent 0 (mod n) iff n | a
2. a congruent a (mod n)
3. a congruent b (mod n) iff b congruent a (mod n)
4. a congruent b (mod n) and b congruent c (mod n), then a congruent c (mod n)

___Thm___

Let a,b,c,c,n be integers and n != 0
and suppose a congruent b (mod n) and c congruent d (mod n)
then:
a + c congruent b + d (mod n)
a - c congruent b - d (mod n)
a * c congruent b * d (mod n)

___Prop___

Let a,b,c,n be integers and n != 0
and gcd(a,n) = 1

If ab congruent ac (mod n), then b congruent c (mod n)

