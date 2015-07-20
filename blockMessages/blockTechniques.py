import collections
import math
import pprint


def blockByStrings(message,block_size=128,encode=True):

    if encode == True:
        mb = list(map(ord,message))
        mb2 = ''
        for i in range(len(mb)):
            if(mb[i]<99):
                mb2 += '0'
            mb2 += str(mb[i])
        mb2 = int(mb2)
        return mb2
    else:
        return len(str(message))


def blockByConcat(message,block_size=128,encode=True):

    count = 0
    block = 0
    blocks = []

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

    # messageBytes = message.encode('ascii') # convert the string to bytes
    #
    # blockInts = []
    # for blockStart in range(0, len(messageBytes), blockSize):
    #     # Calculate the block integer for this block of text
    #     blockInt = 0
    #     for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
    #         blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
    #     blockInts.append(blockInt)
    # return blockInts


def blockByAddition(message,mode,block_size=128):

    byteSize = 256          # One byte has 256 different values.
    blockSize = int(block_size)
    blockInts = []
    count = 0
    pp = pprint.PrettyPrinter(depth=6)

    mode = mode.lower()

    #pp.pprint(message)
    if mode == 'encrypt':
        messageLength = len(message)
        mb = list(map(ord,message))
        tempSum = 0
        count = 0
        for i in range(len(mb)):
            tempSum += mb[i] * (byteSize ** (i % blockSize))
            count += 1
            if count % blockSize == 0:
                blockInts.append(tempSum)
                tempSum = 0
        return(blockInts)
    else:
        blockInts = message

        for i in range(len(blockInts)):
            pp.pprint(blockInts[i])

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
