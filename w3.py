"""
    =========== Exercise 1 =============
    I have provided some starter code below
    that creates a result variable, and a number_1
    variable. Your goal is to make number_1 equal 11
    after the operations that have been done to it.
"""
result = 0
number_1 = 5
number_1 += 52
# Do more operations on number 1 until it equals eleven

number_1 -= 2
number_1 /= 5

result = number_1
print(result == 11)
"""
    =========== Exercise 2 =============
    Take input from the command line, and convert it to
    an int. Now pick a range (i.e. 0-10), and create a set
    of conditional statements that prints the string
    representation of the number input by the user.
    For example if someone put in 8, then it would print 'eight'.
    Hint: Use if, elif and else statements.
"""
num = int(input("Type in a number 0-10: "))

if num == 0:
    print("Zero")
elif num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Threw")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
elif num == 6:
    print("Six")
elif num == 7:
    print("Seven")
elif num == 8:
    print("Eight")
elif num == 9:
    print("Nine")
elif num == 10:
    print("Ten")


"""
    =========== Exercise 3 =============
    Before running the code below try to
    figure out which print statement will
    execute and why. Then uncomment the code
    and check if you were right.
"""
number = 0
number += 15
number //= 2
number *= 6
number -= 4
if number < 10:
    print("Less than 10")
elif 10 <= number <= 20:
    print("Between 10 and 20")
elif 20 <= number <= 30:
    print("Between 20 and 30")
elif 30 <= number <= 40:
    print("Between 30 and 40")
else:
    print("Â¯\_(ãƒ„)_/Â¯")