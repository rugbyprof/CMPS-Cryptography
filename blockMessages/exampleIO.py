import argparse
import sys
import math
import blockTechniques as bt

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--mode", dest="mode", default = "encode", help="Encode or Decode")
    parser.add_argument("-i", "--inputfile", dest="inputFile", help="Input Name")
    parser.add_argument("-o", "--outputfile", dest="outputFile", help="Output Name")
    parser.add_argument("-t", "--type", dest="type",help="Encoding / Decoding mode [add,concat]")
    parser.add_argument("-b", "--blocksize", dest="blocksize",help="Blocksize for encoding / decoding")

    args = parser.parse_args()

    f = open(args.inputFile,'r')
    message = f.read()
    if(args.type == 'add'):
        data = bt.blockByAdd(message,args.mode,args.blocksize)
    else:
        data = bt.blockByConcat(message,args.mode,args.blocksize)
    o = open(args.outputFile,'w')
    o.write(str(data))


if __name__ == '__main__':
    main()
