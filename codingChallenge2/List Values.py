# Coding Challenge 2
### Chelsea Lizardo
### NRS 528
#
#
# Using this list:
j = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]

# # 1.) Make a new list that has all the elements less than 5 from this list in it and print out this new list.

this_list = []

# use a for loop to iterate through numbers less than five from this list
for i in j:

    if i < 5:

        this_list.append(i)
# print(this_list)
print(this_list)

# 2.) Write this in one line of Python.
# append that_list and include the for loop in the same bracket
that_list = []
[that_list.append(i) for i in j if i < 5]
# print(that_list)
print(that_list)
