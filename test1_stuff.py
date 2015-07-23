import sys
import pprint

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

def main():
    # message = []
    # message.append(list("THE WOR"))
    # message.append(list("LD IS N"))
    # message.append(list("OT ENOU"))
    # message.append(list("GH     "))
    # print_md_table(message)
    #
    # alphabet = []
    # nums = []
    # for i in range(26):
    #     nums.append(i)
    # alphabet.append(nums)
    # alphabet.append(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    # print_md_table(alphabet)
    #
    # answer1 = []
    # nums = []
    # for i in range(len("EUCLID IS THE FATHER OF GEOMETRY")):
    #     nums.append(i)
    # answer1.append(nums)
    # answer1.append(list("EUCLID IS THE FATHER OF GEOMETRY"))
    # answer1.append(list("                                "))
    # print_md_table(answer1)


    nums1 = []
    for i in range(20):
        nums1.append(i)
    nums2 = []
    for i in range(20,40):
        nums2.append(i)
    answer2 = []
    answer2.append(nums1)
    answer2.append(list("THE ARMY WILL INVADE"))
    answer2.append(nums2)
    answer2.append(list(" ON 07 25 AT 1300   "))
    pp = pprint.PrettyPrinter(depth=6)
    pp.pprint(answer2)
    print_md_table(answer2)

    answer3 = []
    length = len("ARMY INVADING ON 07 25 AT 1300")
    nums = []
    for i in range(length):
        nums.append(i)
    answer3.append(nums)
    answer3.append(list("ARMY INVADING ON 07 25 AT 1300"))
    answer3.append(list("                              "))
    print_md_table(answer3)

if __name__ == '__main__':
    main()
