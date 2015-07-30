### A touch of Number Theory
(not proof read)

```
 ________________________________________
( When chuck Norris does division, there )
( are no remainders.                     )
 ----------------------------------------
        o   ^__^
         o  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
---------------------------------------------------------
```

___Prop___

>1. For every _a_ ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/neq.gif) _0_, 
    - _a_ | _0_, 
    - _a_ | _a_, 
    - also _1_ | _b_ for every _b_
2. if _a_ | _b_ and _b_ | _c_ , then _a_ | _c_
3. If _a_ | _b_ and _a_ | _c_, then _a_ | _sb + tc_ for any _s,t_ that ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/in.gif) ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/integers.gif)

- A number _p > 1_ that is divisible only by _1_ and itself is called prime.
- An integer that is not prime is called composite, that _n = ab_, where _1 < a,b < n_

___Thm___
>There are infinitely many prime numbers.

___Thm___
>Let ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/pi.gif)_(n)_ be the number of primes less than _n_. <br>
<br>
Then ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/pi.gif)_(x) ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/approx.gif) x / log(x)_ <br>
<br>
ratio ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/pi.gif)_(x) / (x / ln(x))_ -> _1_ as _x -> infinity_

___Thm___
>For every positive integer is a product of primes. The factorization is unique up to order.

___Thm___
>If _p_ is prime and _p | ab_ then _p|a_ or _p|b_

___Definition___ 
>The greatest common divisor of _a & b_ is the largest positive integer dividing both _a & b_.<br>
We denote that as _gcd(a,b) = x_
<br>
We say that _a & b_ are relatively prime, if there exists a _gcd(a,b) = 1_

___Division Algorithm___
>Given _a & b_ in integers, there exists a unique _q,r_ such that _a = ba + r_ where _0_ ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/leq.gif) _r < b_

___Euclidian Algorithm___
>1728 = 12(135) + 108<br>
135 = 108(1) + `27`(gcd)<br>
108 = 27(4) + 0<br>
<br>
gcd(482,1180)<br>
<br>
1180 = 2(482) + 216<br>
482 = 2(216) + 50<br>
216 = 4(50) + 16<br>
50 = 3(16) + `2`<br>
16 = 8(2) + 0<br>
<br>
`gcd(a,b) = gcd(b,r)`<br>

___Def___
>Let _a,b,n_ be integers and _n_ ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) _0_
we say that _a_ is congruent to _b % n_ , _a ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) b (mod n)_ , if _n | a-b_
<br>
32 ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) 7 (mod 5)<br>
<br>
32 - 7 = 25 => 25 / 5 == 0<br>
<br>
-12 ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) 37 (mod 7)<br>
<br>
-12 - 37 = -49 => -49 % 7 = 0<br>

___Prop___
>Let _a,b,c,n_ be integers and _n ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/neq.gif) 0_<br>
1. _a ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) 0 (mod n) iff n_ | _a_<br>
2. _a ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) a (mod n)_<br>
3. _a ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) b (mod n) iff b ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) a (mod n)_<br>
4. _a ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) b (mod n) and b ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) c (mod n), then a ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) c (mod n)_<br>

___Thm___
>Let _a,b,c,c,n_ be integers and _n ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/neq.gif) 0_
and suppose _a ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) b (mod n)_ and _c ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) d (mod n)_
then:<br>
_a + c ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) b + d (mod n)_<br>
_a - c ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) b - d (mod n)_<br>
_a * c ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) b * d (mod n)_<br>

___Prop___
>Let _a,b,c,n_ be integers and _n ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/neq.gif) 0_
and _gcd(a,n) = 1_
<br>
If _ab ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) ac (mod n)_, then _b ![](https://raw.githubusercontent.com/rugbyprof/CMPS-Cryptography/master/symbols/equiv.gif) c (mod n)_

___THM___
>Let _a_ , _b_ be integers, then there exists integers _x,y_ such that _ax + by = gcd(a,b_
<br>
`3x+2Y = 7`
