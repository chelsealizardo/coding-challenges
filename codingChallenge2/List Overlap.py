# Coding Challenge 2
### Chelsea Lizardo
### NRS 528
#
#
#Using these lists:

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
    return lst3
#print intersection
print(intersection2(lst1, lst2))