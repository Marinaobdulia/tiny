import random
import sys

first = int(sys.argv[1])
last = int(sys.argv[2])
random_number = int(random.randint(first, last))
user_number = int(input('guess the number: '))

while random_number != user_number:
    user_number = int(input('Try again! Guess the number: '))

print('Good job! You guessed my number! Bye :)')