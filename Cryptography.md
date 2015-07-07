**Cryptography**

Cryptography is the study of secret writing. The subject basically has three names, cryptography, cryptology and cryptanalysis, which are often used interchangeably. Cryptology is the study of communication over a non-secure channel and problems relating to that task. The process of designing systems for communication over non-secure channels is called cryptography. Cryptanalysis deals with breaking such systems.

Since the days of antiquity people have needed to send messages or data in a format so that no unauthorized individuals could read the information. This was usually done by encoding the original message and only the party to whom the message was sent would know the method of decoding the message. The method of encoding and decoding a message is usually referred to as a Cryptographic System or Cryptosystem for short. One of the earliest recorded cryptosystem was used by Julius Caesar and bears his name the Caesar Cipher.

To describe the Caesar Cipher, write the letters of the alphabet on one line. Clearly we will use the English alphabet, which by the way, was not the alphabet the Caesar used. Below the line you just wrote write the alphabet again except this time start with the letter "D" when you get to the letter "Z" start over with the letter "A".

| PlainText | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CipherText | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |

The top line is known as the plaintext line and the bottom is known as the ciphertext line. Suppose we wanted to send the message:

"MEET ME AT NOON"

The process of encoding the message would be as follows. Locate the letter "M" in the plaintext line and record the corresponding letter in the ciphertext line; in this case it is the letter "P". We continue on with the same process. Thus the message that we would send:

"PHHW PH DW QRRQ"

To decode this message the recipient would just reverse the process. That is, locate the letter "P" in the ciphertext line and record the corresponding letter "M" in the plaintext line.

There is nothing special about starting the ciphertext line with the letter "D"; any letter you choose would create a Caesar Cipher (sometimes called a Shift Cipher). You would probably not want to start the ciphertext line with the letter "A".

_Shift Cipher_

In general a Shift Cipher is just that, we shift the cipher text _n_ units to the right. In the Caesar Cipher the letter "A" is shifted 3 units to the right and is associated with the letter "D" in the cipher text row. Thus the Caesar Cipher is a Shift Cipher with _n_=3. Suppose we wanted to create a shift cipher with _n_=7. Then the letter "A" would be shifted 7 units to the right in the cipher text row. Therefore the letter "A" would be associated with the letter "H". Thus a key for this cipher would be:

| PlainText | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CipherText | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E | F | G |

To encode a message using this cipher we would follow the same procedure as we did above, one letter at a time. Suppose we wanted to send the message:

"THE ANSWER TO THE FIRST QUESTION IS FALSE"

Using the key we would produce the following cipher text:

"AOL HUZDLY AV AOL MPYZA XBLZAPVU PZ MHSZL"

Suppose that you intercepted the following message that you know was encoded by a shift cipher. What strategy would you employ to try to decode the message? Here is the message.

"Z CFFBVU RK KYV WZIJK RJJZXEDVEK REU KYV REJNVI KF KYV WZIJK HLVJKZFE ZJ KILV"

_Class Activity:_

_Divide the class into groups. Decode the above message. Write down the strategies used to accomplish this task. What was the shift value for the code? Write down the key for this cipher._

| PlainText | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CipherText |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |

Depending on the length of the ciphertext that is available one might want to employ a frequency analysis attack. This attack takes advantage of the knowledge of the language being used. For example, count the occurrences of each of the letters in the ciphertext. The following table is a relative frequency of the occurrence of each letter in the alphabet for the English language.

| Letter | Frequency | Letter | Frequency |
| --- | --- | --- | --- |
| a | 0.08167 | n | 0.06749 |
| b | 0.01492 | o | 0.07507 |
| c | 0.02782 | p | 0.01929 |
| d | 0.04253 | q | 0.00095 |
| e | 0.12702 | r | 0.05987 |
| f | 0.02228 | s | 0.06327 |
| g | 0.02015 | t | 0.09056 |
| h | 0.06094 | u | 0.02758 |
| i | 0.06966 | v | 0.00978 |
| j | 0.00153 | w | 0.02360 |
| k | 0.00772 | x | 0.00150 |
| l | 0.04025 | y | 0.01974 |
| m | 0.02406 | z | 0.00074 |

\*Relative frequencies of Letter in general English Language, taken from _Cryptographical Mathematics_, by Robert Edward Lewand

_Exercise 1:_ The following is a message encoded with a Caesar cipher, at the end is a frequency analysis of the contents. Use this information to decode the message.

OXDA BLXAN JWM BNENW HNJAB JPX XDA OJCQNAB KAXDPQC

OXACQ XW CQRB LXWCRWNWC, J WNF WJCRXW, LXWLNRENM

RW URKNACH, JWM MNMRLJCNM CX CQN YAXYXBRCRXW

CQJC JUU VNW JAN LANJCNM NZDJU.

A: 11 B: 6 C: 15 D: 4 E: 2 F: 1 G: 0 H: 2 I: 0 J: 13 K: 2 L: 6

M: 7 N: 18 O: 3 P: 2 Q: 6 R: 9 S: 0 T: 0 U: 4 V: 1 W: 14 X: 14

Y: 2 Z: 1

In practice, cryptographers usually group messages into blocks of letters. There are two obvious advantages for this practice. Single and double letter words are easily guessed. The second reason is for programming. Processing data of a constant given size is more efficient.

Let's add this wrinkle to our Shift cipher using a block size of 5 letters. Suppose we want to encode the following message using a shift cipher with shift value 6:

"THE FIRST ASSIGNMENT IS EASY I DID IT IN TWO MINUTES"

First we remove the spaces and rearrange the letters into groups of five.

"THEFI RSTAS SIGNM ENTIS EASYI DIDIT INTWO MINUT ES"

Now apply the shift cipher to each letter and send the message in groups of five letters.

"ZNKLO XYZGY YOMTS KTZOY KGYEO JOJOZ OTZCU SOTAZ KY"

The idea of placing the ciphertext into blocks of letters of consistent length and then coding each of those blocks does take care of the small word recognition break.

_Exercise 2:_ Decode the following message, the block length is five, and a shift cipher was employed. Fill out the frequency table to help you find the shift value.

NVKYV GVFGC VFWKY VLEZK VUJKR KVJZE FIUVI KFWFI

DRDFI VGVIW VTKLE ZFEVJ KRSCZ JYALJ KZTVZ EJLIV UFDVJ

KZTKI REHLZ CZKPG IFMZU VWFIK YVTFD DFEUV WVEJV GIFDF

KVKYV XVEVI RCNVC WRIVR EUJVT LIVKY VSCVJ JZEXJ FWCZS

VIKPK FFLIJ VCMVJ REUFL IGFJK VIZKP UFFIU RZERE UVJKR

SCZJY KYZJT FEJKZ KLKZF EWFIK YVLEZ KVUJK RKVJF WRDVI

ZTR

A: B: C: D: E: F: G: H: I: J: K: L:

M: N: O: P: Q: R: S: T: U: V: W: X:

Y: Z:

In order to model this mathematically, we need to introduce some mathematical concepts. The first is Modular Arithmetic.

**Modular Arithmetic**

Suppose that it is 10pm., what time will it be 3 in hours? Most people will answer this question correctly, 1am. Basically we start counting over whenever we hit 12:00. Modular arithmetic works the same way, matter of fact, it is often introduced under the name "clock arithmetic". There is nothing special about the number 12, we could use any whole number. Let us introduce this concept with a little more rigor.

_ **The Division algorithm:** _

Let **a** , **b** be integers, then there exists integers **q** , **r** such that **b=qa+r** , where **0**  **<**  **r < | a |.** The integer **q** is called the quotient and the integer **r** is called the remainder. In this case **a** is refered to as the divisor and **b** is called the dividend.

Example:

Let a=15, and b=24, then we have 24=1\*15 + 9. Note that because we insist that r is between 0 and a, this representation is unique.

Let a=5 and b=47, then we have 47=(9)(5)+2.

Let a=12 and b=3, then we have 3=(0)(12)+3.

Let a=-7, and b=36, then we have 36 = (-5)(-7) + 1.

You have used the division algorithm since elementary school, you just may have not known it. When you learned long division you were using the division algorithm, and of course the remainder is the value of r.

![](data:image/png;base64,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AACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUAgAAABCIQAAAAiFAAAAIBQCAACAUP8Hbn72zJztsCMAAAAASUVORK5CYII=) R1

40

45

45

06

5

1

So, 4456=5\*891+1.

To understand the process of modular arithmetic we are going to use the division algorithm, but we are going to focus on the value of r. Choose a value for **a** in the division algorithm and keep it fixed. For example suppose we choose **a=5** , what are all the possible values for b, if we insist r=0. Clearly that means b must be a multiple of 5. Form a set with all the possible multiples of 5, and call that set

0={…, -15, -10, -5, 0, 5, 10, 15, …}.

What are the possible values of b if we insist that r=1, call this set of integers

1={…, -14, -9, -4, 1, 6, 11, 16, …}.

Repeat this process with the remaining allowable values for r. Recall that r must be between 0 and a, not including the value of a. This process in completed in the following table.

| **r** | **Set of integers** |
| --- | --- |
| 0 | {…, -15, -10, -5, 0, 5, 10, 15, …} |
| 1 | {…, -14, -9, -4, 1, 6, 11, 16, …} |
| 2 | {…, -13, -8, -3, 2, 7, 12, 17, …} |
| 3 | {…, -12, -7, -2, 3, 8, 13, 18, …} |
| 4 | {…, -11, -6, -1, 4, 9, 14, 19, …} |

Note that every integer falls into one of these 5 sets. This allows one to answer questions about the integers by just considering these 5 sets. The values of r are called the set representatives modulo 5. Typically we talk about the representatives of each of these sets in terms of their smallest non-negative member. Therefore we will denote the integers modulo 5 by the symbol **Z**** 5 **. Since we are going to focus our attention on the remainders, we will follow the convention of using the smallest non-negative member as a representative. Thus we can think of** Z ****5** as the set {0,1,2,3,4}.

There is nothing special about the number 5, in fact we could choose any integer to perform the above process. This leads us to the following definition.

**Definition** : Let n be a positive integer. The integers modulo n is the set

Z n= {0,1,2, …, n-1}.

The next logical question to ask would be how does arithmetic in **Z**** n **work. Basically it works the same way as it does in the integers, with a little twist. Lets refer back the** Z ****5** , suppose we wanted to calculate 1+3 in **Z**** 5**. Take any element in the set 1 and add it to any element in the set 3, where does your result reside. The answer should be in the set 4. We will write this operation in the following form

1+3≡4 (mod 5).

The symbol (mod 5) alerts the reader that we are doing the arithmetic in **Z**** 5**. Also note that we have written a different symbol for equality. This new symbol ≡ stands for the word congruent. We say that two integers are congruent modulo 5 if they are in the same set listed above. For example 4≡19 (mod 5), since both 4 and 19 are in the set labeled 4.

Suppose we wanted to calculate 3+4 (mod 5). One could just add 3+4 to get 7, then locate 7 in the above sets and observe that 7 is a member of 2. Therefore,

3+4≡2 (mod 5).

This method may seem a little cumbersome. An alternative way of thinking about this process is as follows. Suppose we wanted to do the following calculation.

4+7≡? (mod 8)

Add the right side of the equation just as you would in the integers, 4+7=11. Take the result and divide it by 8, record the remainder. Thus,

4+7≡3 (mod 8).

This method will work for addition, subtract and multiplication.

Example: Calculate 5\*31 (mod 12)

Solution: First calculate 5\*31 = 155. Next apply the division algorithm to get

155=12(12)+11.

Therefore 5\*31≡155≡11 (mod 12).

_Exercise 3:_Construct an addition table and multiplication table for **Z**** 12**.

| **+** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 1 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 2 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 3 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 4 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 5 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 6 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 7 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 8 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 9 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 10 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 11 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |

| **\*** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 1 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 2 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 3 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 4 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 5 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 6 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 7 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 8 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 9 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 10 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
| 11 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |

Let us return to the Caesar Cipher for a moment. We want to model the Caesar Cipher using modular arithmetic. To do this we need to create two functions, one the encoding function and the other the decoding function. We will label the encoding function (n) and the decoding function (n), where n is a numeric value that represents a letter of the alphabet.

Is there any sort of setup we should agree upon before starting the modeling process? What assumptions should we make, concerning these two functions? Should these functions have any specific properties?

The first thing we might want to agree on is how we are going to convert the alphabet into numbers. For example we might want to assign the letter "A" to the number "0", "B" to the number "1", and so on. The chart below maybe useful.

| PlainText | A | B | C | D | E
 | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NumEqu. | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

Note that there are twenty-six letters in our alphabet, and we have the numbers 0 through 25 listed below the letters. To describe the Caesar cipher using modular arithmetic we will be working modulo 26, or in other words we will be working in **Z**** 26**. When we encoded a letter in the Caesar cipher we merely translated the letter of the alphabet by three (3) places. So our encoding function would look like:

(n) ≡ n + 3 (mod 26)

Suppose we wanted to encode the message "WE LEAVE AT NOON". First convert the letters into the corresponding integers in our agreed upon chart. Thus we have the string of integers "22 04 11 04 00 21 04 00 19 13 14 14 13". For technical reasons we often write all single digit integers as two digit integers, 04 instead of 4. The next step is to evaluate the encoding function at each of the integers in our sequence.

To encode "W" evaluate (22)=22+3=25 (mod 26) corresponding letter Z

To encode "E" evaluate (04)=04+3=7 (mod 26) corresponding letter H

To encode "L" evaluate (11)=11+3=14 (mod 26) corresponding letter O

To encode "A" evaluate (00)=00+3=3 (mod 26) corresponding letter D

To encode "V" evaluate (21)=21+3=24 (mod 26) corresponding letter Y

To encode "T" evaluate (19)=19+3=22 (mod 26) corresponding letter W

To encode "N" evaluate (13)=13+3=16 (mod 26) corresponding letter Q

To encode "O" evaluate (14)=14+3=17 (mod 26) corresponding letter R

Message: W E L E A V E A T N O O N

Numeric conversion: 22 04 11 04 00 21 04 00 19 13 14 14 13

Evaluation of (n): 25 07 14 07 03 24 07 03 22 16 17 17 16

Cipher Text: Z H O H D Y H D W Q R R Q

Therefore the message that would be sent would be "ZH OHDYH DW QRRQ". To decode the message we would use the same process except this time place the cipher text in the message slot, convert to an integer, evaluate the decoding function and finally convert the integers back into text. The decoding function in this case would be:

(n) ≡ n - 3 (mod 26)

_Exercises 4:_ Write out the encoding function for a shift cipher with a shift value of 12. Convert the message "MATHEMATICS IS FUN" to its numerical values. Evaluate the encoding function (n) for each value. Write the corresponding cipher text. Write the decoding function (n).

In the Caesar Cipher you discovered how to mathematically model it using modular arithmetic. You created two functions  (n) and  (n). In this section we are going to work with a similar type of cipher called an affine cipher. They can be modeled using modular arithmetic just like the Caesar cipher, matter of fact, the Caesar cipher is an affine cipher.

An affine cipher has an encoding function that looks like  (n) ≡ an +b (mod 26), where a and b are integers between 0 and 26.

Suppose we let a=5 and b=2. Therefore the encoding function would look like  (n) ≡ 5n +2 (mod 26). To encode the letter "A", we would evaluate  (0) ≡ 5\*0+2 ≡ 2 (mod 26), So the letter "C" would be put in place of the letter "A". Suppose we wanted to encode the letter "L". Evaluate the encoding function  (11) ≡ 5\*11+2 ≡ 57 ≡ 5 (mod 26). So the letter "L" would be replaced by the letter "F". Fill in the remaining letters in the chart below, when a=5 and b=2.

| Plaintext | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ciphertext | C |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 | F |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |

Repeat the same process, except this time let a=2 and b=5. Fill in the cipher text row of the following chart.

| Plaintext | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Ciphertext |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |
 |

3. Is the encoding scheme in problem 2 a good one? Explain why or why not?

4. Are there any bad choices for the value of a? If there are bad choices for the value of a, what are they?

The second part of a good cryptosystem is having a decoding function the work the same way that the encoding functions does. In the case of an affine cipher, our decoding function has the same form as our encoding function. Namely,  (n) ≡An+B (mod 26), where A and B are integers between 0 and 26. We used capital letter for A and B this time to alert you to the fact that "A" and "a" may not be the same values and the same goes for "B" and "b".

We use the symbol ≡ for congruence because it behaves similar an equation. To get use to working and ultimately solving congruences we need the following theorem.

Theorem: Let _m_>1 be an integer.

1. If a1 ≡ a2 (mod _m_) and b1 ≡ b2 (mod _m_), then

a1 ± b1 ≡ a2 ± b2 (mod _m_) and a1 **·** b1 ≡ a2 **·** b2 (mod _m_)

1. Let _a_ be an integer. Then

_a_ **·** _b_ ≡ 1 (mod m) for some integer _b_ if and only if gcd(_a,m_)=1

5. Find the decoding function for the cipher created in problem 1. ( Here is a hint: Locate the letter "A" in the ciphertext line of the chart in problem 1. What is the corresponding letter in the plaintext line? The numerical representation of that letter is the value for B in the decoding formula.)

_Exercise 5:_ The following message was encoded using an affine cipher. Determine the encoding function  (n) and the decoding function  (n) and decode the message.

"JO RZP CFWH ICH IJLH LFSR TJGCHUB FUH MUHFXFMEH"

### Greatest Common Divisors

Recall the Division algorithm, suppose that we have two integers **a** , **b** such that when the algorithm is performed we have **r=0**. In this case we say that **a**"is a divisor of" **b** , or merely **a**"divides" **b**. We denote this by the symbol **a|b**. An alternative way of thinking about it is if **a|b** , then there exists an integer _k_ such that **b** =_k_ **a**.

Example: Let a=6 and b=24, apply the division algorithm and we get that 24=4\*6+0. Thus 6 divides 24, or 6|24.

**Theorem:** Let _a_, _b_ and _c_ be integers.

1. If _a|b_ and _b|c_, then _a|c_
2. If _a|b_ and _b|a_, then _a=±b_
3. If _a|b_ and _a|c_, then _a|(b+c)_ and _a|(b-c)_

_Prove given in class_

Let m, n be two integers, we say that d is a common divisor of m, n if d|m and d|n. If d is the largest such common divisor then we call d the greatest common divisor and denote it by d=gcd(m,n). There are several ways of calculating the greatest common divisor. One method that you may have seen in elementary school is just to list the divisors of each number, circle the divisors that are in both lists and then pick the largest.

Example: Find the gcd(48,30).

The divisors of 48 are {1,2,3,4,6,8,12,16,24,48}.

The divisors of 30 are {1,2,3,5,6,10,15,30}.

Examination of the lists reveals that {1,2,3,6} are all common divisors of 48 and 30. The largest element of that list is 6. Therefore gcd(48,30)=6.

This method is not very practical if the integers get large. Even with the integer 48 some of the divisors could have been missed. A better method that is extremely fast is to use the division algorithm repeatedly. Perform the division algorithm with the two given integers. If the remainder is zero, stop the smaller number is the greatest common divisor. If the remainder is not zero, perform the division algorithm with the divisor and remainder, repeat this process until the remainder is zero. The last non-zero remainder is the greatest common divisor. This method is known as the Euclidean Algorithm.

The key to this algorithm comes from the following:

**Lemma:** If _a=qb+r_, then gcd(_a,b_)=gcd(_b,r_).

_Proof:_ If _d_=gcd(_a,b_), then _d|a_ and _d|b_, so _d|(a-qb)_ or _d|r_. Thus, _d_ is a common divisor of _b_ and _r_. If c is an arbitrary divisor of _b_ and _r_, then _c|(qb+r)_, hence _c|a_. This makes _c_ a common divisor of _a_ and _b_, so _c ≤ d_. By definition _d_=gcd(_b,r_).

Example: Find the gcd(48,30).

48=1\*30+18

30=1\*18+12

18=1\*12+6

12=2\*6+0. Thus gcd(48,30)=6.

_Exercise 6:_

1. Show that 5|20 and 23|1081.

1. List all the divisors of the following integers
  1. 72
  2. 616

1. Use the Euclidean Algorithm to find the following.
  1. gcd(318,3243)
  2. gcd(21,364)
  3. gcd(34709,100313)

**Definition:** Let m, n be integers. If gcd(m,n)=1, then m and n are said to be relatively prime.

From time to time, it will be necessary to calculate the number of integers less than or equal to a given integer **n** that are relatively prime to **n**. The function that does this is called the Euler Phi function. We denote this by _φ_( **n** ).

Example: Calculate _φ_ (6).

Note that the gcd(1,6)=1, gcd(2,6)=2, gcd(3,6)=3, gcd(4,6)=2, gcd(5,6)=1 and gcd(6,6)=6. Therefore only the numbers 1 and 5 are relatively prime to 6. Thus _φ_ (6)=2.

In the above example note that we had to calculate several gcd's, if our integer is large this would be somewhat time consuming. Is there an easier way to calculate _φ_ (n). Of course the answer is yes. The following theorems will allows us to calculate _φ_ (n) more efficiently.

If _n_ is a prime number, then every integer less than _n_ is relatively prime to it; hence, _φ_(_n_)=_n_-1. On the other hand, if _n_>1 is composite, then _n_ has a divisor _d_ such that 1<_d_<_n_. It follows that there are at least two integers that are not relatively prime to _n_, namely _d_ and _n_. Therefore, _φ_(_n_) ≤ _n_-2. This proves the following theorem

**Theorem:** _φ_(n)=n-1 if and only if n is prime.

**Theorem:** If p is prime and k>0, then _φ_(pk)=pk - pk-1 = pk(1 – 1/p).

_Proof given in class_

**Theorem:** Suppose that a, b are integers such that gcd(a,b)=1, then _φ_ (ab)= _φ_ (a) _φ_ (b).

_Proof given in class_

Example: Calculate _φ_ (35), since 35=7(5) and gcd(7,5)=1, we have _φ_ (35)= _φ_ (7) _φ_ (5). Now 7 and 5 are both prime, therefore _φ_ (35) = _φ_ (7) _φ_ (5) = (7-1)(5-1) = 24.

In our last example we actually factored the number into a product of primes. We did not use the full power of our theorem. Suppose we wanted to calculate _φ_ (42), we could use the fact that 42 = 6(7). Note that gcd(6,7)=1, so _φ_ (42)= _φ_ (6) _φ_ (7) = 2 (7-1) = 12.

_Exercise 7:_

1. Evaluate the following:
  1. _φ_ (81)
  2. _φ_ (481)
  3. _φ_ (200)

1. For what integers is _φ_ (x) = 12.

1. List all the divisors of 30. Calculate _φ_ (d) for each divisor of 30. Add the values of the Euler Phi functions. What do you see?

Generalized Substitution Ciphers

Both Shift ciphers and Affine Ciphers fall into a larger group of monoalphabetic ciphers, the group is called Substitution ciphers. In this group the letters of the alphabet are rearranged in some fashion to form the ciphertext. In the case of the shift cipher the letters in the cipher text line are shifted to the right. In the affine cipher each letters placement is dictated by an equation. In general a substitution cipher could place the ciphertext in any order. The difficulty in decoding a message using a substitution cipher does increase, especially if a block size is incorporated. In this case the two main tools in decoding the message are the frequency analysis and the double letter analysis. Realize that when a block design is incorporated the double letter analysis is less effective, a word could end with the same letter the next word starts with.

_Discussion questions:_

1. How many shift ciphers are there?
2. How many affine ciphers are there?
3. How many substitution ciphers are there?
4. How long will an exhaustive search take?

_Exercise 8:_ The following message was encoded using a substitution cipher and a block size of 6. Decode the message:

"EHDAHC XHEEHD AERJEZ TERAUW ATEZHX FRAERA CEZTXH

DQACZX ERABZX NEHTWM MACERA TQZXPT JXNJCC HFTHMH

WECJPA HWTMHC EWXAHC EHEJYA JCBTJP JZXTEJ TAFHME

CHWDQA TJXNDO HLLHTZ XPAXNE RAB"

Frequency table:

A: B: C: D: E: F: G: H: I: J: K: L:

M: N: O: P: Q: R: S: T: U: V: W: X:

Y: Z:

RSA Public Key Encryption

In the previous sections we have been studying the Caesar cipher and affine ciphers. In both of those schemes, knowledge about the encoding function can be used to completely determine the decoding function. There are also several tactical problems if one is going to implement either one of these type codes on a large scale. For example if one wanted to communicate with several different people and wanted each communication to be private even within the group, several different codes would need to be used. From an administrative view this would be a nightmare. These are some of the issues that lead to the concept of a public key encryption system.

Looking back on the affine ciphers, we noted that calculating the inverse function was relatively easy given the function. The idea behind a public key cryptosystem is to find a function that is easy to calculate, but without a "crucial" fact the inverse of the function is extremely hard or better yet impossible to derive. These types of functions are called "trapped door" functions. In this section we will introduce the RSA Public Key encryption system. The security of this system lies in our inability to efficiently find the prime factorization of a large integer.

Here is the set-up:

1. Choose two prime numbers _p_ and _q_.
2. Set n=pq.
3. Find two integers e and d such thated=1 (mod _φ_ (n))

Publish the numbers n and e. Keep the number p, q, d, and _φ_ (n) secret. If someone wants to send you a message, they convert the message to a numerical value in some way and then they take that number raise it to the eth power and reduce it modulo n. When this number is received, one just raises it to the dth power and reduces modulo n. This will retrieve the original message. Lets go through an example.

In advance of sending any messages, agree on a standard to convert the text message into numerical form. We shall use the following chart.

| space | A | B | C | D | E | F | G | H | I | J |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 |

| K | L | M | N | O | P | Q | R | S | T | U |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |

| V | W | X | Y | Z | ? | & | ! | $ | # | \* |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 |

Suppose we pick p=3 and q=11, then n=33. If we wanted to set up a secure way to encode messages we would pick primes that were a lot bigger, but for the purpose of illustration we will use 3 and 11. The next job is to find the integers e and d. One way to accomplish this is to pick a number say e=3, then find the multiplicative inverse modulo 20, since _φ_ (33) = 20. Recall we did this sort of calculation earlier. Now the multiplicative inverse of 3 is 7 modulo 20. Therefore d=7. Next I would publish the numbers 33, 3.

Suppose someone wanted to send me the message "JUMP!''. They would first convert it from text to a sequence of numerical values. In this case

JUMP! becomes the sequence 10 21 13 16 29. For each number in the sequence they raise it to the 3rd power and reduce it modulo 33.

(10)=103=10 (mod 33)

(21)=213=21(mod 33)

(13)=133=19 (mod 33)

(16)=163=04 (mod 33)

(29)=293=02 (mod 33)

The sequence of numbers 10 21 19 04 02 would then be sent to me. Note if someone intercepted the sequence and converted back to text, they would get the message "JUSDA"

To decode the sequence of numbers 10 21 19 04 02, raise each one to the 7th power and reduce modulo 33.

(10)=107=10 (mod 33)

(21)=217=21 (mod 33)

(19)=197=13 (mod 33)

(04)=047=16 (mod 33)

(02)=027=29 (mod 33)

After converting this sequence of numbers to text, the original message is restored.

As previously mentioned the choice of p=3 and q=11 are not good choices if we want to build a secure code. Typically one would choose primes having several digits (more than a hundred). In the illustration just given, what other attacks are possible? Clearly we still could use word recognition, double letter assault, single letter words and character frequencies to attempt to break the code. All of these methods would yield good results. You might be asking the question, why did we design this code if the same attacks still yield good results. Well as is always true in endeavors like this one, we adapt the existing method to combat such attacks. Here is a better example of the way RSA is implemented currently; we will still be using primes that are relatively small by industrial standards.

Let p=71 and q=151, then n=pq=10117. Now calculate _φ_ (10117) = 9900. To find our encoding and decoding exponents all we really need to do is to pick e so that it is relatively prime to 9900, then calculate the multiplicative inverse modulo 9900. Suppose we choose e = 59. Then it turns out the d=839. To encode a message follow the same procedure that we did before, except this time we will calculate 4 digits at a time. We arrive at the decision because our modulus has 5 digits. Generally if our modulus has N digits we will select N-1 digits at a time.

Suppose we were going to encode the message:

MATH MODELING

Convert this text into numbers:

13 01 20 08 00 13 15 04 05 12 09 07

Note that we did include the space as the number 00. Next taking these digits and put them into groups of 4:

1301 2008 0013 1504 0512 0907

Use these numbers in our encoding scheme:

(1301) =130159 =7042 (mod 10117)

(2008) =200859 =1195(mod 10117)

(0013) =1359 =6935 (mod 10117)

(1504) =150459 =3522 (mod 10117)

(0512) =51259 =6708 (mod 10117)

(0907 )=90759 =8306 (mod 10117)

Thus we would send this string of numbers:

7042 1195 6935 3522 6708 8306

To decode this message all we would need to do is take each 4-digit number and raise it to the 839th power and reduce it modulo 10117. Before you get too worried, our calculators are not powerful enough to perform this task.So we will not be asking you to do these calculations by hand. After all this is just to illustrate the method.

Looking at this simple adaptation can you see that most of the attacks that we have discussed have become useless?
