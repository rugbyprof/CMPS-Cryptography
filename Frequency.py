from pprint import pprint
import operator

message = "Line 8 is a for loop that will set the key variable with the values 0 up to (but not including) 26. Instead of hard-coding the value 26 directly into our program, we use the return value from len(LETTERS) so that if we modify LETTERS the program will still work. See the Encrypt Non-Letter Characters section in the last chapter to read why."

message = message.upper()

frequency = {}

for i in range(26):
    frequency[chr(i+65)] = 0
    
pprint(frequency)

print(message)

count = 0

for i in range(len(message)):
    if (ord(message[i]) >= 65 and ord(message[i]) <= 92):
        count = count + 1
        frequency[message[i]] = frequency[message[i]] + 1

for i in range(26):
    frequency[chr(i+65)] = round(frequency[chr(i+65)] / count,5)
    

sorted_freq = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)

pprint(frequency)
pprint(sorted_freq)
