### Number Theory

- GCD
- Finding Multiplicative Inverse mod M ( _ax_ ![](http://f.cl.ly/items/1c0A2q3H3j071r3j0503/CodeCogsEqn.png) _1 ( mod m )_)
- Division Algorithm
- Euclidian Algorithm
- Congruences
- Modular Exponentiation
- Fermat's Little Thm
- Euler's Thm
- Primitive Roots Modulo P

### Python

- What is printed by the Python code?
```python
x = 5
y = x + 3
x = x - 1
z = 10
x = x + z
print('x: {}, y: {}, z: {}'.format(x, y, z))
```
- What is printed by the Python code?
```python
 print(14//4, 14%4, 14.0/4)
```
- What is printed by the Python code?
```python
print(2*'No' + 3*'!')
print(2 * ('No' + 3*'!'))
```
- What is printed by the Python code?
Be careful: Note the backslashes:
```python
print('how\nis it\nnow')
```
- What is printed by the Python code?
```python
for z in [2, 4, 7, 9]:
 print(z - 1)
```
- What is printed by the Python code?
```python
print('2' + '3')
```
- What is printed by the Python code?
```python
def f1():
 print('Hi')
def f2():
 print('Lo')
f2()
f1()
f1()
```
- What is printed by the Python code?
```python
def func():
 print('Yes')
print('No')
func()
```
- What is printed by the Python code?
```python
def func(x):
 print(2*x)
func(5)
func(4)
```
- What is printed by the Python code?
```python
def func(x):
 return x - 1
print(func(3) * func(5))
```
- What is printed by the Python code?
```python
n = 3 #1
for x in [2, 5, 8]: #2
 n = n + x #3
print(n) #4
```
- What is printed by the Python code?
```python
print(list(range(3)))
```
- What is printed by the Python code?
```python
for i in range(3):
 print('Hello again!')
 ```
- What is printed by the Python code?
```python
for i in range(4):
 print(i)
 ```
- What is printed by the Python code?
```python
def s(x): #1
 return x*x #2
for n in [1, 2, 10]: #3
 print(s(n)) #4
 ```
- What is printed by the Python code?
```python
def s(x): #1
 return x*x #2
tot = 0 #3
for n in [1, 3, 5]: #4
 tot = tot + s(n) #5
print(tot) #6
```
- What is printed by the Python code?
```python
x = 2.5679
y = 9.0
print('Answers {:.3f} and {:.3f}'.format(x, y))
```
- What is printed by the Python code?
```python
d = dict()
d['left'] = '<<'
d['right'] = '>>'
print('{left} and {right} or {right} and {left}'.format(**d))
```
- Write a Python program that prompts the user for two numbers, reads them in, and prints out the
product, labeled.
- Given a string s, write a short expression for a string that includes s repeated five times.
- Suppose you know x is an integer and ys is a string representing an integer. For instance, x is 3 and
ys is '24'. Write code to print out the arithmetic sum of the two. In the example case, 27 would be
printed.
- Suppose you are given a list of words, wordList. Write Python code that will write one line for each
word, repeating that word twice. For example if wordList is ['Jose', 'Sue', 'Ivan'], then
your code would print
Jose Jose
Sue Sue
Ivan Ivan
- Write code to create a Python dictionary (the dict type). Add two entries to the dictionary: Associate
the key ‘name’ with the value ‘Juan’, and associate the key ‘phone’ with ‘508-1234’
- Complete the code for the following function so it matches its documentation:
```python
def doubleList(numberList):
 ''' For each of the numbers in the list numberList, print a line
 containing twice the original number. For example,
 doubleList([3, 1, 5]) would print
 6
 2
 10
 '''
```
- Assuming a function process is already defined, write two lines of code, using a for-loop, that is
equivalent to the following:
```python
process('Joe')
process('Sue')
process('Ann')
process('Yan')
```
