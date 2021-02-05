"""
   =========== Challenge 1 =============
    The code below generates a random number
    make a game that loops and takes user input 
    at the command line. The input is the user's
    guess at what the number is. Taking their input
    you should print either: 'too high', 'too low' or
    'Correct guess'.
    For example let's assume the number is 4 a sample
    output of the game would look like this:
        >> Enter Guess: 2
        Too Low
        >> Enter Guess: 5
        Too High
        >> Enter Guess: 4
        Correct Guess

import random
number = random.randint(1,10) # Generates a random number
guess = 0

while guess != number:
    guess= int(input("Enter guess between 1-10: "))
    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print("Correct Guess")

"""

"""
    =========== Challenge 2 =============
    Take two inputs from the command line, then
    convert both to an int the first number will
    be the starting number, and the second will be
    the ending number. Create a loop that goes from
    the starting number to the ending number, and only
    prints the even numbers.

first = int(input("First number: "))
second = int(input("Second number(Greater than the first): "))

while first <= second:
    if (first % 2) == 0:
        print(first)
    
    first += 1
"""
"""
    =========== Challenge 3 =============
    THIS CHALLENGE IS HARD, DON'T GET DISCOURADGED
                IF YOU CAN'T DO IT!
    Using the list below print the numbers
    in ascending order. It should look like this: 
    1
    2
    3
    4
    5
    6
    7
    8
    9
    HINTS:
    1. The pattern is that the list is in order where the
        same index on each list is in ascending order.
        i.e. 
        numbers[0][0] is 1
        numbers[1][0] is 2
        numbers[2][0] is 3
        etc.
    2. The simplest (and shortest) way to do this
        is with a loop counter variable, and a while loop.
"""
numbers = [
    [1, 4, 7],
    [2 ,5, 8],
    [3, 6, 9]
]

rows = len(numbers)
cols = len(numbers[0])
r = c = 0

while c < cols:

    while r < rows:
        print(numbers[r][c])
        r += 1

    c += 1 
    r = 0
