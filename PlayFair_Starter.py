import pprint
import re

def generateAlphabet():
    #Create empty alphabet string
    alphabet = ""
    
    #Generate the alphabet
    for i in range(0,26):
        alphabet = alphabet + chr(i+65)
        
    return alphabet


def cleanString(s,options = {'up':1,'reNonAlphaNum':1,'reSpaces':'_','spLetters':'X'}):
    """
    Cleans message by doing the following:
    - up            - uppercase letters
    - spLetters     - split double letters with some char
    - reSpaces      - replace spaces with some char or '' for removing spaces
    - reNonAlphaNum - remove non alpha numeric
    - reDupes       - remove duplicate letters

    @param   string -- the message
    @returns string -- cleaned message
    """
    if 'up' in options:
        s = s.upper()
        
    if 'spLetters' in options:
        #replace 2 occurences of same letter with letter and 'X'
        s = re.sub(r'([ABCDEFGHIJKLMNOPQRSTUVWXYZ])\1', r'\1X\1', s)
        
    if 'reSpaces' in options:
        space = options['reSpaces']
        s = re.sub(r'[\s]', space, s)
    
    if 'reNonAlphaNum' in options:
        s = re.sub(r'[^\w]', '', s)
        
    if 'reDupes' in options:
        s= ''.join(sorted(set(s), key=s.index))
        
    return s

def generateSquare(key):
    """
    Generates a play fair square with a given keyword.

    @param   string   -- the keyword
    @returns nxn list -- 5x5 matrix
    """
    row = 0     #row index for sqaure
    col = 0     #col index for square
    
    #Create empty 5x5 matrix 
    playFair = [[0 for i in range(5)] for i in range(5)]
    
    alphabet = generateAlphabet()
    
    #uppercase key (it meay be read from stdin, so we need to be sure)
    key = cleanString(key,{'up':1,'reSpaces':'','reNonAlphaNum':1,'reDupes':1})
    
    print(key)
    
    #Load keyword into square
    for i in range(len(key)):
        playFair[row][col] = key[i]
        alphabet = alphabet.replace(key[i], "")
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    #Remove "J" from alphabet
    alphabet = alphabet.replace("J", "")
    
    #Load up remainder of playFair matrix with 
    #remaining letters
    for i in range(len(alphabet)):
        playFair[row][col] = alphabet[i]
        col = col + 1
        if col >= 5:
            col = 0
            row = row + 1
            
    return playFair

def sameRow(digraph,playFair):
    """
    Returns true if digraph is on same row

    @param   list -- the digraph e.g. [X,C]
    @returns digraph -- new digraph shifted to the right
    """
    
    for row in playFair:
        newDigraph = ['','']
        if digraph[0] in row and digraph[1] in row:
            newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
            newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
            return newDigraph
    
    return []

def transpose(playFair):
    """
    Turns columns into rows of a cipher square

    @param   list2D -- playFair square
    @returns list2D -- square thats transposed
    """
    #Create empty 5x5 matrix 
    trans = [[0 for i in range(5)] for i in range(5)]
    
    for col in range(5):
        for row in range(5):
           trans[col][row] = playFair[row][col] 
           
    return trans
    
def getCodedDigraph(digraph,square):
    """
    Turns a given digraph into its encoded digraph 

    @param   list -- digraph
    @returns list -- encoded digraph
    """
    newDigraph = ['','']

    #Check to see if digraph is in same row
    for row in square:
        if digraph[0] in row and digraph[1] in row:
            newDigraph[0] = row[((row.index(digraph[0])+1)%5)]
            newDigraph[1] = row[((row.index(digraph[1])+1)%5)]
            return newDigraph

    return []


###########################################################################

message = "The fox has foot problems and has been hoodwinked. Can you beleive it?"
key = 'Mathematics is Awesome foxy lady!!'

message = cleanString(message)
playFair = generateSquare(key)

print(key)
print(message)
print()
for list in playFair:
    print(list)
print()
transPlayFair = transpose(playFair)
print()
for list in transposed:
    print(list)

print(getCodedDigraph(['E','Z'],transPlayFair))
print(getCodedDigraph(['E','Z'],playFair))
