import random   
import copy     # to support deep copy of lists
import pprint
import math
import re       # supports regular expressions
import os
###################################################################

# Hard coded dictionary
frequency = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}

# Dynamically generated dictionary

frequency2 = {}

for i in range(26):
    frequency2[chr(i+65)] = 0

# loop over list of key value pairs and
# insert random values in for frequency's
for k,v in frequency.items():
    print(k,v)
    r = int.from_bytes(os.urandom(1), byteorder="little")/255
    frequency[k] = r

print(frequency)

###################################################################

# seeding random number generator so we can
# generate pseudo random numbers again and again
random.seed(66)
for i in range(5):
    print(random.randint(1, 100))

# Muiltipy the string with a random value between 4 and 40 inclusive
# to create a string of some random length.
message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)
print(message)

message = list(message)

random.shuffle(message)

print(message)

message = ''.join(message)

print(message)

###################################################################

#Copy vs Deep Copy
spam1 = [0, 1, 2, 3, 4, 5]
cheese1 = spam1

spam1[1] = 'hello'

print("spam1 = ",spam1)
print("cheese1 = ",cheese1)

print()

#Deep copy
spam2 = [0, 1, 2, 3, 4, 5]
cheese2 = spam2

cheese2 = copy.deepcopy(spam2)

spam2[1] = 'hello'

print("spam2 = ",spam2)
print("cheese2 = ",cheese2)

###################################################################

pp = pprint.PrettyPrinter(depth=6)

keyLength = 8

message = "For a long time, cryptography has been deemed the exclusive realm of experts." 
message = message.upper()

# Remove all characters that are NOT alphanumeric or an underscore
message = re.sub(r'[\s]', '_', message)
message = re.sub(r'[^\w]', '', message)

pp.pprint(message)

##################################################################

# Create empty transposition block
transPosBlock = []

rows = math.floor(len(message) / keyLength)
if((len(message) / keyLength)-rows > 0):
    rows += 1

for i in range(rows):
    transPosBlock.append([' '] * keyLength)
    
pp.pprint(transPosBlock)

print()

##################################################################
# Load message into block

for i in range(len(message)):
    row = math.floor(i / keyLength)
    col = i % keyLength
    transPosBlock[row][col] = message[i]

pp.pprint(transPosBlock)

print()

##################################################################
# Loop through block in a column wise fashion thereby 
# encrypting message

encrypted = ''
for i in range(keyLength):
    for j in range(rows):
        encrypted += transPosBlock[j][i]
    
print(encrypted)

print()

##################################################################
# Copy encrypted message back into block (wrong way)

for i in range(len(encrypted)):
    row = math.floor(i / keyLength)
    col = i % keyLength
    transPosBlock[row][col] = encrypted[i]
    
pp.pprint(transPosBlock)

decrypted = ''
for i in range(keyLength):
    for j in range(rows):
        decrypted += transPosBlock[j][i]
    
print(decrypted)


##################################################################
# Resize block reversing rows and colums so we can decrypt
# the encrypted message

transPosBlock = []

for i in range(keyLength):
    transPosBlock.append([''] * rows)

for i in range(len(encrypted)):
    row = math.floor(i / rows)
    col = i % rows
    transPosBlock[row][col] = encrypted[i]
        
pp.pprint(transPosBlock)
        
decrypted = ''
for i in range(rows):
    for j in range(keyLength):
        decrypted += transPosBlock[j][i]
    
print(decrypted)

##################################################################

print("Enter 1 for encrypt 2 for decrypt:")
x = input()

flag = 1

while(flag == 1):
    if(x == '1'):
        print("you want to encrypt")
        flag = 0
    elif(x=='2'):
        print("you want to decrypt")
        flag = 0
    else:
        print("improper entry ass wipe")
        print("Enter 1 for encrypt 2 for decrypt:")
        x = input()





        
