## Not Done

## Randomized Vigenère

#### Overview:

This slight alteration of the original Vigenère cipher that was originally described by Giovan Battista Bellaso in 1553 will allow us to create a more secure version of the cipher, leveraging the power of computers and random number generation. The original version of the Vigenère cipher used a tableau that contained 26 alphabets, each differing by a shift of one. In my opinion the tableau was generated in this fashion because it was easily duplicated, and sufficiently secure at the time. 

#### Original

![](http://f.cl.ly/items/3K011s3A2y3d1R2z2t1m/Screen%20Shot%202015-07-22%20at%205.39.26%20PM.png)

The randomized version contains randomly generated alphabets for each of the 26 individual ciphers. Of course a weak random number generator would render the cipher susceptible to cracking, but otherwise it should be a pretty decent symmetric key cipher. For a computer to generate a unique / random tableau is trivial, and if we can reliably generate the same tableau for sender and receiver we can ensure the algorithm is deterministic. 

> Note: Were using the stock random number generator provided by python. This is considered a pseudo-random number generator, so you wouldn't necessarily be using this in a production system. But, maybe our version of Vigenère will be viable. That's a discussion for later.

#### Randomized

![](http://f.cl.ly/items/0o2D0x2m2x2O2A182I3V/vigenere_randomized.png)

#### Symetric Key

Speaking of keys, what do we use as a key for our randomized Vigenère? How do we guarantee that the encryption and decryption are both done using an identical tableau? 

1. We have to guarantee that the tableau generation is done using the same random number generator by both parties.
2. We also need to send the `seed` used to prime the random number generator along with the keyword. 
3. Alternatively, we can actually use the seed as the actual Vigenère keyword.

#### Converting Integer Seed To Vigenère Key

Here is a function that we can use to turn some integer value into a keyword for our Vigenère cipher. It uses the method to turn integers into letters via modulo arithmetic.

```python

import random

#############################################################################
# keywordFromSeed -
#    Works by peeling off two digits at a time, and using modulo to map it into
#    the proper range of A-Z for use as a keyword.
# Example:
#    This example spells math, and I chose values 0-25 on purpose, but
#    it really doesn't matter what values we choose because 99 % 26 = 21 or 'V' 
#    or any value % 26 for that matter.
#
#    seed = 12001907
#    l1   = 12001907 % 100 = 07 = H
#    seed = 12001907 // 100 = 120019
#    l2   = 120019 % 100 = 19 = T
#    seed = 120019 // 100 = 1200
#    l3   = 1200 % 100 = 0 = A
#    seed = 1200 // 100 = 12
#    l4   = 12 % 100 = 12 = M
#    seed = 12 // 100 = 0
#
# @param {int} seed - An integer value used to seed the random number generator
#                     that we will use as our keyword for vigenere
# @return {string} keyword - a string representation of the integer seed
#############################################################################
def keywordFromSeed(seed):
    Letters = []

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 100
    return ''.join(Letters)

#Usage:

seed = 12001907

random.seed(12001907)

keyWord = keywordFromSeed(seed)

print(keyWord)   # Prints "MATH"

```

### Requirements:

- Create a folder called `First.Last.Vigenere` where YourName is actually your name: (e.g. Reyansh.Jones.Vigenere). Notice the dots, those are critical (letter grade off if not named correctly).
- Remainder of files goes in your folder.
- Create a file called `vig-main.py`.
- `vig-main.py` will be similar to the driver snippet except you will adjust the arguments accordingly.
- Here are some examples for you to base your code on: 
     - `python3 vig-main.py -m encrypt -seed 7487383487438734 -i plainText.txt -o encryptedText.txt`
     - `python3 vig-main.py -m decrypt -seed 7487383487438734 -i encryptedText.txt -o decryptedText.txt`
- Create another file called `randomized_vigenere.py`. This is where your Vigenere implentation will go.

##### Driver Snippet:
```python
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode", dest="mode", default = "encode", help="Encode or Decode")
    parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-t", "--type", dest="type",help="Encoding / Decoding mode [add,concat]")
    parser.add_argument("-b", "--blocksize", dest="blocksize",help="Blocksize for encoding / decoding")

    args = parser.parse_args()

    f = open(args.inputFile,'r')
    message = f.read()
    if(args.type == 'add'):
        data = bt.blockByAdd(message,args.mode,args.blocksize)
    else:
        data = bt.blockByConcat(message,args.mode,args.blocksize)
    o = open(args.outputFile,'w')
    o.write(str(data))


if __name__ == '__main__':
    main()
```
- Create another file called `randomized_vigenere.py` where you will place your implementation of the randomized vigenere.
- Your implementation does not have to be organized in a class, but should (at a minimum) provided the following functions:
    - `def keywordFromSeed(seed)`
    - `def encrypt(keyword)`
    - `def decrypt(keyword)`

#### What to Turn In

All your 



