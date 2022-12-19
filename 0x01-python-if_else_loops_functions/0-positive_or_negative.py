#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
<<<<<<< HEAD
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")
=======
    print("{:d} is positive".format(number))
elif number == 0:
    print("{:d} is zero".format(number))
else:
    print("{:d} is negative".format(number))
>>>>>>> 5309eb00fc8adb0b5af40081a98636a272dde793
