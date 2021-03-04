# Coding Challenge 2

# 1. List values
# Using this list:
#
# [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
# Make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
#
lst1 = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
lst2 = ['dog', 'hamster', 'snake']

# 1.) Determine which items are present in both lists.
#Define intersection of the two list using def and intersection functions

def intersection(lst1, lst2):
# create list 3 using a for loop that iterates through to find common items in both lists
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
#print intersection
print(intersection(lst1, lst2))

# 2.) Determine which items do not overlap in the lists.
def intersection2(lst1, lst2):
# create list 3 using a for loop that iterates through to find common items in both lists
# use logic gate "not" to perform opposite operation on list
    lst3 = [value for value in lst1 if value not in lst2]
    lst4 = [value for value in lst2 if value not in lst1]
    lst5 = lst3 + list(set(lst4) - set(lst3))
    return lst5
#print intersection
print(intersection2(lst1, lst2))


#Feedback, suggest numerically naming your files so they appear in the same order as the Challenge readmes to make
# my life easier, i.e. Task_1.py, Task_2.py. Minor point. I also like to have hte chapllenge text at the top of the page
# again just makes life easier.

# Snake did not show in the not-overlap. This is because you were leading from lst1 and not considering values in lst2
# that were unique. The set comparison with a reverse of lst3 (in lst4) gives us the correct answer.