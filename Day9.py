"""
Question 26:
Define a function which can compute the sum of two numbers.
"""


def sum_numbers():
    num1 = int(input("first number>> "))
    num2 = int(input("second number>> "))
    print(num1 + num2)


sum_numbers()

"""
Question 27:
Define a function that can convert a integer into a string and print it in console.
"""


def int_to_str():
    n = int(input(">> "))
    print(str(n))


int_to_str()

"""
Question 28:
Define a function that can receive two integer numbers in string form 
and compute their sum and then print it in console.
"""


def sum_numbers2():
    num1 = input("first number>> ")
    num2 = input("second number>> ")
    print(int(num1) + int(num2))


sum_numbers2()

"""
Question 29:
Define a function that can accept two strings as input and concatenate them and then print it in console.
"""


def sum_str():
    str1 = input(">> ")
    str2 = input(">> ")
    print(str1 + str2)


sum_str()

"""
Question 30:
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print all strings line by line.
"""


def str_len():
    str1 = input(">> ")
    str2 = input(">> ")
    if len(str1) > len(str2):
        print(str1)
    elif len(str1) < len(str2):
        print(str2)
    else:
        print(str1)
        print(str2)


str_len()
