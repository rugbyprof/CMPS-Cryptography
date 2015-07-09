Playfair Cipher

The Playfair cipher is a crypto system that encodes two letters at a time (called digraphs). This system was invented around 1854 by Sir Charles Wheatstone. He named the system after a friend, the Baron Playfair of St. Andrews, who lobbies the government for its use. This system was used during World War II and it was used by the British forces in the Boer War.

The letters of the alphabet are arranged in a 5 x 5 square. Since the English language has 26 letters, the letters I and J are equated. Typically a keyword or key phase would be used to construct the playfair square. We will use the key phrase "Mathematics rules the world".

| M | A | T | H | E |
| --- | --- | --- | --- | --- |
| I/J | C | S | R | U |
| L | W | O | D | B |
| F | G | K | N | P |
| Q | X | V | Y | Z |

To encode the message:

MY FOOT IS BROKE SEND HELP

1. Separate any double letters with an X.

MY FOXOT IS BROKE SEND HELP

1. Take your message an put it in groups of two letters, if you message has an odd number of letters add an "X" at the end.

MY FO XO TI SB RO KE SE ND HE LP

1. a) If the letters of a diagraph lie on the same row of the Playfair square, we replace each letter by the letter to its immediate right, wrapping around to the first column is necessary.

b) If the letters of a diagraph lie on the same column of the Playfair square, we replace each letter by the letter directly below, wrapping up the first row if necessary.

c) If the letters are in different rows and columns of the square, this forms the corners of a square inside the Playfair square. We encode each letter with the other corner on the same row.

Example: The first diagraph "MY" is encoded by 3c), the other corners of the interior square are "HQ".

| **M** | A | T | **H**| E |
| --- | --- | --- | --- | --- |
| I/J | C | S | R | U |
| L | W | O | D | B |
| F | G | K | N | P |
| **Q** | X | V | **Y** | Z |

The first eight diagraphs are encoded by the same method. Looking at the diagraph "ND", they are in the same column, hence they will be replaced with the letter directly below. Thus "N" is replaced by "Y" and "D" is replaced by "N". The diagraph "ND" becomes "YN" .

The next diagraph "HE", the letters are in the same row. Each letter is replaced with the letter to the right. Thus "H" is replaced by "E" and "E" is replaced by "M" (note we needed to wrap around on this one). Therefore the diagraph "HE" is replaced by "EM".

Putting all this together we have:

Plain text: MY DO XO TI SB RO KE SE ND HE LP

Cipher text: HQ KL VW MS UO SD PT UT YN EM BF

Set up a Playfair Square using the key phrase: "Love is a many splendored thing".

|
 |
 |
 |
 |
 |
| --- | --- | --- | --- | --- |
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

Use this to encode the message:

THE AMBASSADOR IS MISSING
