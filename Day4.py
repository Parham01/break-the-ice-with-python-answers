import re

'''
Question 14:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
'''


def count_uppercase_and_lowercase():
    sentence = input("write a sentence: ")
    uppercase = len(re.findall(r"([A-Z])", sentence))
    lowercase = len(re.findall(r"([a-z])", sentence))

    print(f"UPPER CASE {uppercase}\nLOWER CASE {lowercase}")


count_uppercase_and_lowercase()

'''
Question 15:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
'''


def calculate_number():
    a = input("enter a number: ")
    print(int(a) + int(a * 2) + int(a * 3) + int(a * 4))


calculate_number()
