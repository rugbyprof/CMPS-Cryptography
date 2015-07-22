import collections
import math
import pprint

# This file shows two methods of turning a string into an integer in a recoverable
# way. In other words, we can return the integer back to the original string without
# any string corruption.

# This function turns a string into a function by simple concatination. Any ordinal
# value < 100 is prepended with a '0' and then concatenated. This allows us to reverse
# the process and decode the string by stripping off three digits at a time and
# converting.
#
# Good:
#     Easy to implement and understand.
#
# Bad:
#     Large integer for any given string.
def blockByConcat(message,mode,block_size=128):

    blockSize = int(block_size)     # Block size needed to divide large messages
                                    # into multiple 'chunks'
    mode = mode.lower()

    if mode == 'encode':
        mb = list(map(ord,message))
        encoded = 999
        for i in range(len(mb)):
            encoded *= 1000
            encoded += mb[i]
        return encoded
    else:
        decoded = []
        while message > 999:
            decoded.insert(0,chr(message % 1000))
            message = message // 1000
        decoded = ''.join(decoded)
        return decoded



# This function turns a string into an integer by continuously "adding" each characters
# ordinal value to a previous sum by raising it to some exponent based on byte size and
# position. Almost like converting between bases, but in this case were creating a number
# of base "256".
#
# Implentation:
#
#     "HELLO" would be = H * 256^0 + E * 256^1 + L * 256^2 + L * 256^3 + O * 256^4 = TOTAL
#
# To reverse it:
#
#     O = TOTAL // 256^4
#         TOTAL = TOTAL % 256^4
#     L = TOTAL // 256^3
#         TOTAL = TOTAL % 256^3
#     L = TOTAL // 256^2
#         TOTAL = TOTAL % 256^2
#     E = TOTAL // 256^1
#         TOTAL = TOTAL % 256^1
#     H = TOTAL // 256^0 or H = TOTAL
#
# @param string - message: The incoming message either in plaintext or encoded as integer
# @param string - mode: Encode into an integer or decode into a string.
# @param int - block_size: This is needed to divide large strings into equal length chunks.
def blockByAdd(message,mode,block_size=128):
    byteSize = 256                  # One byte has 256 different values.
    blockSize = int(block_size)     # Block size needed to divide large messages
                                    # into multiple 'chunks'
    mode = mode.lower()

    if mode == 'encode':
        messageLength = len(message)
        ordinalMessage = list(map(ord,message))
        encoded = 0
        for i in range(len(ordinalMessage)):
            encoded += ordinalMessage[i] * (byteSize ** (i))
        return encoded
    else:
        message = int(message)
        i = blockSize
        decoded = []
        while message > 0:
            letter = message // (byteSize ** (i))
            message = message % (byteSize ** (i))
            i -= 1
            decoded.insert(0,chr(letter))
        return ''.join(decoded)

def main():
    message = "The army will invade in exactly three weeks at 2100 hours."

    print("Plain text message: {}\n".format(message))

    print("Running blockByAddition-")
    print("Encoded:")
    encoded = blockByAddition(message,'encode',128)
    print(encoded)
    print("Decoded:")
    decoded = blockByAddition(encoded,'decode',128)
    print(decoded)
    print("")
    print("Running blockByConcat-")
    print("Encoded:")
    encoded = blockByConcat(message,'encode',128)
    print(encoded)
    print("Decoded:")
    decoded = blockByConcat(encoded,'decode',128)
    print(decoded)

if __name__ == '__main__':
    main()
