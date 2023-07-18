'''
Question 1:
Write a program which will find all such numbers which are divisible by 7 but are 
not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained
should be printed in a comma-separated sequence on a single line.
'''


def divisible_by_7():
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=',')


divisible_by_7()

'''
Question 2:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
'''


def factorial():
    num = int(input("\nwrite a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(fact)


factorial()

'''
Question 3:
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary
'''


def numbers_dictionary():
    num = int(input("write a number: "))
    dictionary = {}
    for i in range(1, num + 1):
        dictionary[i] = i * i
    print(dictionary)


numbers_dictionary()
