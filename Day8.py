"""
Question 22:
Write a program to compute the frequency of the words from the input.
The output should output after sorting the key alphanumerically.
"""


def alphabetical_sorting():
    words_list = input(">> ").split(' ')
    words_list.sort()
    words_count_dict = {word: words_list.count(word) for word in words_list}
    for word, num in words_count_dict.items():
        print(f"{word}:{num}")


alphabetical_sorting()


'''
Question 23:
Write a method which can calculate square value of number
'''


def square():
    num = int(input("write a number: "))
    return num ** 2


square()

'''
Question 24:
Python has many built-in functions, and if you do not know how to use it, 
you can read document online or find some books. 
But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function
'''


print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


def roast():
    """
this function is useless like you
    """
    return None


print(roast.__doc__)

'''
Question 25:
Define a class, which have a class parameter and have a same instance parameter.
'''


class Boring:
    bored_value = 0

    def __init__(self, bored_value=0):
        self.bored_value = bored_value


boring1 = Boring(100)
print(Boring.bored_value, boring1.bored_value)
