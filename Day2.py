from math import sqrt

'''
Question 4:
Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every number
'''


def generate_list_tuple(csn):
    numbers_list = csn.split(',')
    numbers_tuple = tuple(numbers_list)
    print(numbers_list)
    print(numbers_tuple)


comma_separated_input = input()
generate_list_tuple(comma_separated_input)

'''
Question 5:
Define a class which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.

Also please include simple test function to test the class methods.
'''


class UpperString:
    def __init__(self):
        self.str = ""

    def getstring(self):
        self.str = input()

    def printstring(self):
        print(self.str.upper())


string1 = UpperString()
string1.getstring()
string1.printstring()

'''
Question 6:
Write a program that calculates and prints the value according to the given formula:

Q = Square root of [(2 * C * D)/H]

Following are the fixed values of C and H:
C is 50. H is 30.

D is the variable whose values should be input to your program in a comma-separated sequence.
'''


def calculate_sqrt(csn):
    c = 50
    h = 30
    for d in csn.split(','):
        answer = sqrt((2 * c * int(d)) / h)
        print(round(answer), end=',')


cs_input = input()

calculate_sqrt(cs_input)

'''
Question 7:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i _ j.

Note: i=0,1.., X-1; j=0,1,¡Y-1. Suppose the following inputs are given to the program: 3,5
'''


def two_dimensional_array(li):
    array = []
    for i in range(int(li[0])):
        array.append([])
        for j in range(int(li[1])):
            array[i].append(i * j)
    print(array)


dimensions = input().split(',')
two_dimensional_array(dimensions)

'''
Question 8:
Write a program that accepts a comma separated sequence of words as input and
prints the words in a comma-separated sequence after sorting them alphabetically.
'''


def string_sorting(str_list):
    sorted_list = sorted(str_list.split(','))
    print(','.join(sorted_list))


strings = input()
string_sorting(strings)

'''
Question 9:
Write a program that accepts sequence of lines as input and prints 
the lines after making all characters in the sentence capitalized.
'''


def capitalizing_lines():
    list_of_strings = []
    while True:
        input_lines = input().upper()
        if input_lines == '':
            break
        list_of_strings.append(input_lines)
    return list_of_strings


for cap_lines in capitalizing_lines():
    print(cap_lines)
