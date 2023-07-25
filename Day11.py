"""
Question 38:
With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print
the first half values in one line and the last half values in one line.
"""
"""
Question 39:
Write a program to generate and print another tuple whose 
values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
"""


def print_tuple():
    tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(f"{tup[:5]}\n{tup[5:]}")
    print(tup[1::2])


print_tuple()

"""
Question 40:
Write a program which accepts a string as input to 
print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
"""


def check_input():
    user_input = input(">>").lower()
    if user_input == "yes":
        print("Yes")
    else:
        print("No")


check_input()

"""
Question 41:
Write a program which can map() to make a list whose elements 
are square of elements in [1,2,3,4,5,6,7,8,9,10].
"""


def squares_list():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_li = list(map(lambda i: i ** 2, li))
    print(new_li)


squares_list()

"""
Question 42:
Write a program which can map() and filter() to make a 
list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
"""


def even_squares_list():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    new_li = list(map(lambda x: x ** 2, filter(lambda i: i % 2 == 0, li)))
    print(new_li)


even_squares_list()

"""
Question 43:
Write a program which can filter() to make a list whose 
elements are even number between 1 and 20 (both included).
"""


def even_numbers():
    li = list(filter(lambda x: x % 2 == 0, range(1, 21)))
    print(li)


even_numbers()
