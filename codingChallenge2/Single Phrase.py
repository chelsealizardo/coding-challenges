# Coding Challenge 2
### Chelsea Lizardo
### NRS 528
#
#
string = 'hi dee hi how are you mr dee'
#Count the occurrence of each word, and print the word plus the count.

def word_count(str):
    counts = dict()
    words = str.split()

    for w in words:
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1

    return counts

print( word_count('hi dee hi how are you mr dee'))