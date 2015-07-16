import collections
import math


def blockByStrings(message,block_size=128,encode=True):

    mb = list(map(ord,message))
    mb2 = ""
    for i in range(len(mb)):
        mb2 += str(mb[i])
    mb2 = int(mb2)
    print(mb2)
    print()

def blockByConcat(message,block_size=128,encode=True):

    if encode == True:
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


def blockByAddition(message,block_size=128,encode=True):

    byte_size = 256 # One byte has 256 different values.

    if encode == True:
        messageLength = len(message)
        mb = list(map(ord,message))
        encoded = 0
        for i in range(messageLength):
            encoded += mb[i] * (byte_size ** (i % block_size))
        return encoded
    else:
        decoded = []
        i = 0
        while message > 0:
            asciiNumber = (message // (byte_size**(block_size-i)))
            message = message % (byte_size**(block_size-i))
            decoded.insert(0, chr(asciiNumber))
            i += 1
        print(decoded)
        decoded = ''.join(decoded)
        return decoded

def main():
    message = "kindness to he horrible reserved ye Effect twenty "

    # print(message)
    # print(len(message))
    #
    # encoded = blockByConcat(message,128,True)
    # decoded = blockByConcat(encoded,128,False)
    #
    # print(encoded)
    # print(decoded)

    encoded = blockByAddition(message,128,True)
    decoded = blockByAddition(encoded,128,False)

    print(encoded)
    print('"{}"'.format(decoded))

    s = " "*128
    print('"{}"'.format(s))

if __name__ == '__main__':
    main()
