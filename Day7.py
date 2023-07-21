'''
Question 20:
Define a class with a generator which can iterate the numbers,
which are divisible by 7, between a given range 0 and n
'''


class DivisibleGenerator:
    def by_7(self, n):
        for i in range(0, n + 1):
            if i % 7 == 0:
                yield i


number = int(input("Write a number: "))
divisible = DivisibleGenerator()
for d in divisible.by_7(number):
    print(d)

'''
Question 21:
A robot moves in a plane starting from the original point (0,0). 
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.The trace of robot movement is shown as the following:

UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps. 
Please write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.
'''


def robot_moves():
    movement = 0
    while True:
        steps = input().split(' ')
        if len(steps) <= 1:
            break
        if steps[0] == ("UP" or "RIGHT"):
            movement += int(steps[1])

        if steps[0] == ("DOWN" or "LEFT"):
            movement -= int(steps[1])

    print(round(int(movement)))


robot_moves()
