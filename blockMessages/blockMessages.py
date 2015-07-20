import os
import sys
import argparse
import blockTechniques as bt

parser = argparse.ArgumentParser()

parser.add_argument("-f", "--filename", dest="fileName", default = "input.txt", help="File Name")
parser.add_argument("-m", "--mode", dest="mode", default = "encrypt", help="Encrypt or Decrypt")
parser.add_argument("-b", "--blocksize", dest="blockSize", default = "128", help="Block size")

args = parser.parse_args()

print(args.fileName,args.mode,args.blockSize)


f = open(args.fileName, 'r')
message = f.read()

encoded = bt.blockByAddition(message,args.mode,args.blockSize)

print(encoded)
