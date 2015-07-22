import operator
import sys

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
characters = list(characters)

print(characters)

message = "Line 8 is a for loop that will set the key variable with the values 0 up to (but not including) 26. Instead of hard-coding the value 26 directly into our program, we use the return value from len(LETTERS) so that if we modify LETTERS the program will still work. See the Encrypt Non-Letter Characters section in the last chapter to read why."

message = message.upper()

frequency = {}

for i in characters:
    frequency[i] = 0.0

print(message)

count = 0

for i in range(len(message)):
    if (message[i] in characters):
        count = count + 1.0
        frequency[message[i]] += 1.0

for i in characters:
    frequency[i] = frequency[i] / count


print(frequency)
