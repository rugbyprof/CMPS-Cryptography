import rabinMiller
import cryptoMath
import random
import os

def main():
    myRsa = Rsa()
    myRsa.makeKeyFiles()

class Rsa:
    def __init__(self):
        self.publicKey = ()
        self.privateKey = ()
        self.privateFileName = ""
        self.publicFileName = ""
        self.keySize = 128

    def generateKey(self,key_size=128):
        # Creates a public/private key pair with keys that are keySize bits in
        # size. This function may take a while to run.

        self.keySize = key_size

        # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
        print('Generating p prime...')
        p = rabinMiller.generateLargePrime(self.keySize)
        print('Generating q prime...')
        q = rabinMiller.generateLargePrime(self.keySize)
        n = p * q

        # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
        print('Generating e that is relatively prime to (p-1)*(q-1)...')
        while True:
            # Keep trying random numbers for e until one is valid.
            e = random.randrange(2 ** (self.keySize - 1), 2 ** (self.keySize))
            if cryptoMath.gcd(e, (p - 1) * (q - 1)) == 1:
                break

        # Step 3: Calculate d, the mod inverse of e.
        print('Calculating d that is mod inverse of e...')
        d = cryptoMath.modinv(e, (p - 1) * (q - 1))

        self.publicKey = (n, e)
        self.privateKey = (n, d)

        print('Public key:', self.publicKey)
        print('Private key:', self.privateKey)
        print()


    def makeKeyFiles(self,key_size=128):
        # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' (where x is the
        # value in name) with the the n,e and d,e integers written in them,
        # delimited by a comma.

        currentPath = os.getcwd()

        fileName = input('Enter file in which to save the key ({}/my_rsa/):'.format(currentPath))

        if fileName == '':
            print("Empty string entered. Defaulting to rsa.pub and rsa.priv")
            fileName = 'rsa'

        self.privateFileName = '{}/{}.priv'.format(currentPath,fileName)
        self.publicFileName = '{}/{}.pub'.format(currentPath,fileName)

        self.keySize = key_size
        # Our safety check will prevent us from overwriting our old key files:
        if os.path.exists(self.privateFileName) or os.path.exists(self.publicFileName):
            print('{}/{} already exists.'.format(currentPath,fileName))
            overWrite = input('Overwrite (y/n)? ')

        self.generateKey()

        print()
        print('The public key is a %s and a %s digit number.' % (len(str(self.publicKey[0])), len(str(self.publicKey[1]))))
        print('Writing public key to {}'.format(self.publicFileName))
        fo = open(self.publicFileName, 'w')
        fo.write('%s,%s,%s' % (self.keySize, self.publicKey[0], self.publicKey[1]))
        fo.close()

        print()
        print('The private key is a %s and a %s digit number.' % (len(str(self.privateKey[0])), len(str(self.privateKey[1]))))
        print('Writing private key to {}'.format(self.privateFileName))
        fo = open(self.privateFileName, 'w')
        fo.write('%s,%s,%s' % (self.keySize, self.privateKey[0], self.privateKey[1]))
        fo.close()

if __name__ == '__main__':
    main()
