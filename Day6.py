import re

'''
Question 18:
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.

Following are the criteria for checking the password:

At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
'''


def password_checker():
    passwords = input("write passwords: ").split(',')
    verified_passwords = []
    pattern = re.compile(r"(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}")
    for password in passwords:
        if re.match(pattern, password):
            verified_passwords.append(password)
    print(','.join(verified_passwords))


password_checker()

'''
Question 19:
You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.
'''


def sort_name_age_score():
    data_list = []
    while True:
        info = tuple(input().split(','))
        if len(info) <= 1:
            break
        data_list.append(info)
    print(sorted(data_list))


sort_name_age_score()
