### Implement the Play Fair cipher

### Notes

- All code needs to be uploaded to your github repository
- I can't access your github repository if you don't first complete the github assignment.
- All code needs to be written by you unless:
    - It's code I've given you from class
    - You cite the location you obtained the code from.
    - Small snippets (1-2 lines need not be cited), but a block of code ( 5 or more lines) needs to be.
- Your code needs to be thoroughly commented
- Your code needs to be organized (use of functions and / or classes). Not just a hodgepodge of top down coding.

#### What I should see:

Whether or not you use the given starter code, your program should perform the following:

- Prompt the user with a menu (should look very similar):

```
Playfair Encryption Tool (P.E.T)
Written By: (Your Name Here)
********************************************************
1. Encipher
2. Decipher
3. Quit
=>
********************************************************
```

-----

- If the user chooses ___1___:

```
Playfair Encryption Tool (P.E.T)
Written By: (Your Name Here)
********************************************************
Please enter a keyword: 
=> (type keyword here)
********************************************************
```

Then

```
Playfair Encryption Tool (P.E.T)
Written By: (Your Name Here)
********************************************************
Please enter a message: 
=> (type message here)
********************************************************
```

Then

```
Playfair Encryption Tool (P.E.T)
Written By: (Your Name Here)
********************************************************
Your encrypted message is:  
=> (encrpyted message prints here)
********************************************************
```

-----

- If the user chooses ___2___:

```
Playfair Encryption Tool (P.E.T)
Written By: (Your Name Here)
********************************************************
Please enter a keyword: 
=> (type keyword here)
********************************************************
```

Then

```
Playfair Encryption Tool (P.E.T)
Written By: (Your Name Here)
********************************************************
Enter the encrypted message: 
=> (type message here)
********************************************************
```

Then

```
Playfair Encryption Tool (P.E.T)
Written By: (Your Name Here)
********************************************************
Your decrypted message is:  
=> (decrpyted message prints here)
********************************************************
```

### Additional Requrements:

- Keyword needs to have all special characters, spaces, and numbers removed (as well as uppercased).
    - For example: Hello 007, the world is not enough!!! => HELOTHWRDISNUGH
- Message needs to be treated in a similar fashion. Extra credit for devising a method to put spaces back in.
- File name: `playfair.py` (This is not a request, it is a requirement).
- The top of your program should have this comment block:

```
###############################################
# Name: (Your Name)
# Class: CMPS XXXX Cryptography
# Date: 13 July 2015
# Program 1 - Playfair Cipher
###############################################
```


