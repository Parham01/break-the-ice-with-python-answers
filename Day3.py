import re

'''
Question 10:
Write a program that accepts a sequence of whitespace separated words as input and prints
the words after removing all duplicate words and sorting them alphanumerically.
'''


def delete_duplicate():
    sequence = set(input("write a sequence: ").split(' '))
    print(*sequence)


delete_duplicate()

'''
Question 11:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as 
its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
'''


def divisible_binary():
    binary_digits = input("enter binary: ").split(',')
    divisible_by_5 = []
    for binary_digit in binary_digits:
        if (int(binary_digit, 2) % 5) == 0:
            divisible_by_5.append(binary_digit)
    print(','.join(divisible_by_5))


divisible_binary()

'''
Question 12:
Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''


def even_number():
    for even in range(1000, 3001):
        if even % 2 == 0:
            yield str(even)


even_numbers = list(even_number())
print(','.join(even_numbers))

'''
Question 13:
Write a program that accepts a sentence and calculate the number of letters and digits.
'''


def count_letters_and_digits():
    sentence = input("write a sentence: ")
    letters = len(re.findall(r"([a-zA-Z])", sentence))
    digits = len(re.findall("\d", sentence))

    print(f"LETTERS {letters}\nDIGITS {digits}")


count_letters_and_digits()
