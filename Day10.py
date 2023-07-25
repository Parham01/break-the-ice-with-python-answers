"""
Question 31:
Define a function which can print a dictionary where the keys are numbers
between 1 and 20 (both included) and the values are square of keys.
"""
"""
Question 32:
Define a function which can generate a dictionary where the keys are 
numbers between 1 and 20 (both included) and the values are square of keys. 
The function should just print the keys only.
"""


def squares_dict():
    di = {}
    for i in range(1, 21):
        di[i] = i ** 2
    print(di)
    print(*di.keys())


squares_dict()

"""
Question 33:
Define a function which can generate and print a list where the values 
are square of numbers between 1 and 20 (both included).
"""
"""
Question 34:
Define a function which can generate a list where the values are square 
of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list.
"""
"""
Question 35:
Define a function which can generate a list where the values are 
square of numbers between 1 and 20 (both included). 
Then the function needs to print the last 5 elements in the list.
"""
"""
Question 36:
Define a function which can generate a list where the values are 
square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list.
"""


def squares_list():
    li = [i ** 2 for i in range(1, 21)]
    print(li)
    print(li[:5])
    print(li[-5:])
    print(li[5:])


squares_list()

"""
Question 37:
Define a function which can generate and print a tuple where 
the value are square of numbers between 1 and 20 (both included).
"""


def squares_tuple():
    tup = tuple([i ** 2 for i in range(1, 21)])
    print(tup)


squares_tuple()
