import fractions

class cryptoMath:
    # Extended Euclidean algorithm
    #   returns a triple (g, x, y), such that ax + by = g = gcd(a, b)
    def egcd(self,a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    # GCD
    #   returns the greatest common denominator. Thats it.
    def gcd(self,a, b):
        while a != 0:
            a, b = b % a, a
        return b

    # Mod Inverse V1
    #   returns the modular multiplicative inverse (x) of a and m.
    #   where ax = 1 (mod m) (= means congruent here)
    def modinv(self,a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            #raise Exception('modular inverse does not exist')
            return None
        else:
            return x % m

    # Euler's totient function
    #   returns some integer that represents the positive integers
    #   less than or equal to n that are relatively prime to n.
    def phi(self,n):
        amount = 0

        for k in range(1, n + 1):
            if self.gcd(n, k) == 1:
                amount += 1

        return amount

class MultiplicativeCipher:

    SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    Ciphertext = ""
    Plaintext = ""

    def __init__(self,multiplier=1025,shifter=7):
        self.crypto = cryptoMath()

        # If key sent in is not relatively prime with the length of
        # symbols then keep adding 1 until it is.
        while self.crypto.modinv(multiplier,len(self.SYMBOLS)) == None:
            multiplier += 1

        # Set Multiplier to the possibly adjusted Multiplier
        self.Multiplier = multiplier
        self.Shifter = shifter

        # Get the inverse key using our mod inverse function
        self.InverseMultiplier = self.crypto.modinv(self.Multiplier,len(self.SYMBOLS))

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

    def setKey(n):
        pass

def main():
    multi = MultiplicativeCipher()
    cipherText = multi.encrypt("this is a super awesome year 2000+ message!!!")
    print(cipherText)
    decoded = multi.decrypt(cipherText)
    print(decoded)

if __name__ == '__main__':
    main()
