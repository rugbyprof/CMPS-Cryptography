import pprint

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

# encrypt
# param v : vigenere table
# param k : key
# param m : message
# param ki: key index
# param mi: message index
def encrypt(v,k,m,ki,mi):
    row = ord(m[mi]) - 65
    col = ord(k[ki]) - 65
    return v[row][col]


key = "I love crypto"
key = key.upper()

message = "We are going to invade europe tomorrow"
message = message.upper()

#Create empty 5x5 matrix
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


encrypted = encrypt(vigenere,key,message,0,0)

print(encrypted)

#pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(vigenere)
printMatrix(vigenere)
