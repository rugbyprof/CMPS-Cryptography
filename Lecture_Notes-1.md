- String concatenation with `+`
- String replication with `*`
- `print` function
- String `indexing`:

```python
spam = "hello world"
print (spam[3])
```

- String `negative indexing`:

```python
spam = "hello world"
print (spam[-1])
# Outputs: d
```

- String `slicing`:

``` python
spam = "hello world"
print (spam[3:5])
# Outputs: lo
```

- `blank slice` indexing:

``` python
spam = "hello world"
print (spam[:5])
# Outputs: lo
```

- Prompt user for input:

``` python
x = input()
print(x)
# Outputs: whatever user typed in (spaces allowed)
```

- Length of a string: `len(varName)`

- Defining a code block:

``` python
i = 10
while i >= 0:
    print(i)
    i = i - 1
```

- Operators

| Sign | Description|
|------|------------|
| <    | Less than  |
| >    | Greater than |
| <=   | Less than or equal to |
| >=   | Greater than or equal to |
| ==   | Equal to |
| !=   | Not equal to | 

- Character functions:

    - .lower()
    - .upper()
    - len()
    - find()
    - range()
    
```python

plain_text = "Hello world. Please encrypt me."
cipher_text = ""

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encrypt(letter,key):
    letter = ord(letter)
    letter = letter - 65
    letter = (letter + key) % 26
    letter = letter + 65
    return chr(letter)
    
print(plain_text)

key = 0

for i in range(len(plain_text)):
    if plain_text[i].upper() in LETTERS:
        #cipher_text = cipher_text + chr((ord(plain_text[i].lower())+key) % 26)
        #print(ord(plain_text[i].upper())-65)
        print(encrypt(message[i],key))
    else:
        cipher_text = cipher_text + plain_text[i]
    
print(cipher_text)
```
