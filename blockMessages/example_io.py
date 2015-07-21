import argparse
import sys
import math

def main():
    parser = argparse.ArgumentParser()

    message = list("He went such dare good mr fact.")
    print(len(message))

    parser.add_argument("-m", "--mode", dest="mode", default = "encode", help="Encode or Decode")
    parser.add_argument("-i", "--inputfile", dest="inputFile", default = "input.txt", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", default = "output.txt", help="Output Name")

    args = parser.parse_args()

    if args.mode == 'encode':
        f = open(args.inputFile,'r')
        message = f.read()
        data = encodeByAddition(message)
        o = open(args.outputFile,'w')
        o.write(str(data))
    else:
        f = open(args.inputFile,'r')
        message = f.read()
        message = int(message)
        data = decodeByAddition(message)
        o = open(args.outputFile,'w')
        o.write(data)

def encodeByAddition(message,block_size=128):

    byteSize = 256          # One byte has 256 different values.
    blockSize = int(block_size)
    blockInts = []
    count = 0

    messageLength = len(message)
    mb = list(map(ord,message))
    print(mb)
    Sum = 0
    for i in range(len(mb)):
        Sum += mb[i] * (byteSize ** (i % blockSize))
        print(Sum)
    return Sum

def decodeByAddition(message,block_size=128):

    byteSize = 256          # One byte has 256 different values.
    blockSize = int(block_size)
    blockInts = []
    i = 5
    letter = 0
    newMessage = []

    print("Message: ",message,"\n")
    while message > 0:
        chunk = (byteSize ** (i))

        letter = message // chunk
        message = message % chunk
        i -= 1
        newMessage.insert(0,chr(letter))

    return ''.join(newMessage)

def encodeByConcatination(message):
    total = 0

    #print(list(map(ord,message)))

    count = 0
    for i in message:
        i = ord(i)
        print(i)
        total = total * 1000 + i

        count = count + 1

    return total


def decodeByConcatination(value):
    decoded = []
    while value > 0:
       decoded.insert(0,chr(value % 1000))
       value = (value // 1000)
    return ''.join(decoded)

if __name__ == '__main__':
    main()
