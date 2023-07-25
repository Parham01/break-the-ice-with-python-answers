"""
Question 44:
Write a program which can map() to make a list whose elements
are square of numbers between 1 and 20 (both included).
"""


def square_of_numbers():
    li = list(map(lambda x: x ** 2, range(1, 21)))
    print(li)


square_of_numbers()

"""
Question 45:
Define a class named American which has 
a static method called printNationality.
"""
"""
Question 46:
Define a class named American and its subclass NewYorker.
"""


class American:
    @staticmethod
    def nationality():
        print("American")


class NewYorker(American):
    pass


person1 = American
person1.nationality()
