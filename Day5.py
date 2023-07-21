'''
Question 16:
Use a list comprehension to square each odd number in a list.
The list is input by a sequence of comma-separated numbers.
'''


def square_of_odd_number():
    numbers = input("write numbers: ").split(',')
    odd_numbers = [str(int(i) ** 2) for i in numbers if int(i) % 2 != 0]
    print(','.join(odd_numbers))


square_of_odd_number()

'''
Question 17:
Write a program that computes the net amount of a bank account based a transaction log from console input.
D 100
W 200
D means deposit while W means withdrawal.
'''


def bank():
    deposit = 0
    withdrawal = 0
    while True:
        bank_account = input().split(' ')
        if bank_account[-1] == '':
            break
        if bank_account[0] == 'D':
            deposit += int(bank_account[1])
        elif bank_account[0] == 'W':
            withdrawal += int(bank_account[1])
    print(deposit - withdrawal)


bank()
