import fractions
import cryptoMath

class MultiplicativeCipher:

    SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    Ciphertext = ""
    Plaintext = ""

    def __init__(self,multiplier=1025,shifter=7):

        # If key sent in is not relatively prime with the length of
        # symbols then keep adding 1 until it is.
        while cryptoMath.modinv(multiplier,len(self.SYMBOLS)) == None:
            multiplier += 1

        # Set Multiplier to the possibly adjusted Multiplier
        self.Multiplier = multiplier
        self.Shifter = shifter

        print(self.Multiplier,self.Shifter)

        # Get the inverse key using our mod inverse function
        self.InverseMultiplier = cryptoMath.modinv(self.Multiplier,len(self.SYMBOLS))

    def encrypt(self,plaintext):
        self.Ciphertext = ''
        for symbol in plaintext:
            if symbol in self.SYMBOLS:
                # encrypt this symbol
                symIndex = self.SYMBOLS.find(symbol)
                self.Ciphertext += self.SYMBOLS[(symIndex * self.Multiplier + self.Shifter) % len(self.SYMBOLS)]
            else:
                self.Ciphertext += symbol # just append this symbol unencrypted
        return self.Ciphertext

    def decrypt(self,ciphertext):
        self.Plaintext = ''
        for symbol in ciphertext:
            if symbol in self.SYMBOLS:
                # encrypt this symbol
                symIndex = self.SYMBOLS.find(symbol)
                self.Plaintext += self.SYMBOLS[((symIndex - self.Shifter) * self.InverseMultiplier) % len(self.SYMBOLS)]
            else:
                self.Plaintext += symbol # just append this symbol unencrypted
        return self.Plaintext

    def setKeys(self,m,s):
        self.Multiplier = m
        self.Shifter = s

    def getKeys(self):
        return  [self.Multiplier,self.Shifter]

def main():
    multi = MultiplicativeCipher(104729,13)
    cipherText = multi.encrypt("this is a super awesome year '2000' message!!!")
    print(cipherText)
    for i in range(95):
        for j in range(95):
            if cryptoMath.gcd(i,95) == 1:
                multi.setKeys(i,j)
                decoded = multi.decrypt(cipherText)
                print(decoded)

if __name__ == '__main__':
    main()
