# Coding Challenge 2
## Chelsea Lizardo
## NRS 528
#
#
# Construct a rudimentary Python script that takes a series of inputs as a command from a bat file, and does something to them. The rules:
#
# Minimum of three arguments to be used.
# You must do something interesting in 15 lines or less within the Python file.
# Print or file generated output should be produced.

import sys

def print_arg(arg):
    for i in arg:
        print("My argument: " + str(i))


arguements = [sys.argv[1], sys.argv[2], sys.argv[3]]
print(print_arg(arguements))



# This did not work for me, you seem to have flipped the function of the bat and the python file.
# I have fixed what you have produced. your input from the bat is Argument1 Argument2 Argument3, all the python
# script does is read those variables in and prints them. We should chat about this.

