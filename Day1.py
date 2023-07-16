# Question 1
def divisible_by_7():
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=',')


divisible_by_7()


# Question 2
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(fact)


given_number1 = int(input("\nenter a number: "))
factorial(given_number1)


# Question 3
def numbers_dictionary(num):
    dictionary = {}
    for i in range(1, num + 1):
        dictionary[i] = i * i
    print(dictionary)


given_number2 = int(input("enter a number: "))
numbers_dictionary(given_number2)
