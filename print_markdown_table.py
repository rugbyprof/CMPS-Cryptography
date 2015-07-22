def print_md_table(data):
    table = []
    temp = []

    for v in data[0]:
        temp.append('|{}'.format(v))
    temp.append("|")
    table.append(''.join(temp))

    temp = []
    for v in data[0]:
        temp.append("|:---:")
    temp.append("|")
    table.append(''.join(temp))

    temp = []

    rows = len(data)
    cols = len(data[0])

    for row in range(1,rows):
        temp = []
        for col in range(cols):
            temp.append('|{}'.format(data[row][col]))
        temp.append("|")
        table.append(''.join(temp))


    for row in table:
        print(row)

if __name__ == '__main__':

    data = []
    temp = []
    temp.append(' ')
    for i in range (26):
        temp.append(i)
    data.append(temp)
    for i in range(26):
        temp = []
        for j in range(26):
            temp.append( chr(((j+i)%26)+65) )
        shuffle(temp)
        temp.insert(0,i)
        data.append(temp)

    print_md_table(data)
