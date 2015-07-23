## Not Done

## Randomized Vigenère

#### Overview:

This slight alteration of the original Vigenère cipher that was originally described by Giovan Battista Bellaso in 1553 will allow us to create a more secure version of the cipher, leveraging the power of computers and random number generation. The original version of the Vigenère cipher used a tableau that contained 26 alphabets, each differing by a shift of one.

#### Original

![](http://f.cl.ly/items/3K011s3A2y3d1R2z2t1m/Screen%20Shot%202015-07-22%20at%205.39.26%20PM.png)

The randomized version contains randomly generated alphabets for each of the 26 individual ciphers. Of course a weak random number generator would render the cipher susceptible to cracking, but otherwise it should be a pretty decent symmetric key cipher. 

#### Randomized

![](http://f.cl.ly/items/0o2D0x2m2x2O2A182I3V/vigenere_randomized.png)

#### Symetric Key

Speaking of keys, what do we use as a key for our randomized Vigenère? How do we guarantee that the encryption and decryption are both done using an identical tableau? 

1. We have to guarantee that the tableau generation is done using the same random number generator by both parties.
2. We also need to send the `seed` used to prime the random number generator along with the keyword. 
3. OR we can use the seed AS the keyword!

#### Seed As Vigenère Key



