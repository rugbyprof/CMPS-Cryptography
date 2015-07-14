vigenere = [[0 for i in range(26)] for i in range(26)]

#Build the vigenere matrix
row = 0
col = 0
for i in range(26*26):
    vigenere[row][col] = chr(((col+row)%26)+65)
    col = col + 1
    if col >= 26:
        col = 0
        row = row + 1

# encrypt
# param v : vigenere table
# param k : key
# param m : message
# param ki: key index
# param mi: message index
def encrypt(v,k,m,ki,mi):
    row = ord(m[mi]) - 65
    col = ord(k[ki]) - 65
    print(row,col)
    return v[row][col]

# decrypt
# param v : vigenere table
# param k : key
# param em : encrypted message
# param ki: key index
# param mi: message index
def decrypt(v,k,em,ki,emi):
    pass

# printMatrix
#
#
def printMatrix(v):
    i=0
    j=0
    k=0
    line = ""

    for i in range(26*26):
        line = line + v[j][k]
        j = j + 1
        if j >= 26:
            print(line)
            line = ""
            j = 0
            k = k + 1


key = "I love crypto"
key = key.upper()
key = key.replace(" ", "")

print(key)

message = "We are going to invade europe tomorrow"
message = message.upper()

print(encrypt(vigenere,key,message,0,0))

cipherText = ""

for i in range(len(message)):
    mi = i
    ki = i % len(key)
    print(message[i])
    if ord(message[i]) == 32:
        cipherText = cipherText + ' '
    else:
        cipherText = cipherText + encrypt(vigenere,key,message,ki,mi)


print(cipherText)
