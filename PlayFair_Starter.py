import pprint
import re

#Create empty 5x5 matrix 
playFair = [[0 for i in range(5)] for i in range(5)]

message = "The fox and the hound have been hoodwinked"

#Create alphabet string
alphabet = ""

for i in range(0,26):
    alphabet = alphabet + chr(i+65)
    
print(alphabet)

#remove duplicates from key preserving order
key = 'mathematics'
key = "".join(sorted(set(key), key=foo.index))

#uppercase key (it meay be read from stdin, so we need to be sure)
key = key.upper()

print(key)

row = 0
col = 0
for i in range(len(key)):
    playFair[row][col] = key[i]
    alphabet = alphabet.replace(key[i], "")
    col = col + 1
    if col >= 5:
        col = 0
        row = row + 1
        
#Remove "J" from alphabet
alphabet = alphabet.replace("J", "")

#Load up remainder of playFair matrix with 
#remaining letters
for i in range(len(alphabet)):
    print(row,col,alphabet[i])
    playFair[row][col] = alphabet[i]
    col = col + 1
    if col >= 5:
        col = 0
        row = row + 1   
    
print(alphabet)

message = message.upper()

#replace 2 occurences of same letter with letter and 'X'
message = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', message)

print(message)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(playFair)

