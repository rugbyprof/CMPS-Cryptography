import collections
import math

DEFAULT_BLOCK_SIZE = 128 # 128 bytes
BYTE_SIZE = 256 # One byte has 256 different values.

message = "Kindness to he horrible reserved ye Effect twenty "
print(message)
print(len(message))
messageBytes = list(map(ord,message))
print(messageBytes)
print()

blockInt = 0

messageLength = len(message)

for i in range(messageLength):
    blockInt += messageBytes[i] * (BYTE_SIZE ** (i % DEFAULT_BLOCK_SIZE))

print(blockInt)
print()
message = []

for i in range(1,messageLength+1):
    asciiNumber = (blockInt // (BYTE_SIZE**(messageLength-i)))
    blockInt = blockInt % (BYTE_SIZE**(messageLength-i))
    message.insert(0, chr(asciiNumber))
message = ''.join(message)
print()
print(message)
