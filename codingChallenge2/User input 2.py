# Coding Challenge 2
### Chelsea Lizardo
### NRS 528
#
#
# Using the following dictionary, ask the user for a word, and compute the Scrabble word score for
#that word (Scrabble is a word game, where players make words from letters, each letter is worth a point value):
# letter_scores = {
#     "aeioulnrst": 1,
#     "dg": 2,
#     "bcmp": 3,
#     "fhvwy": 4,
#     "k": 5,
#     "jx": 8,
#     "qz": 10
# }
print("Welcome everybody to Scrabble! ")
# Ask user input to pick a word
word = input("Pick a word: ")
# create a dictionary to keep track of the score-worth of each letter.
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
# use the scrable_score function to take a string word as input and return the equivalent score for that word
# change the string word output into an int to return equivalent score
def scrabble_score(word) -> int:
# set total = 0 because we want to make sure that the score begins at zero
    total = 0
#set a for loop to
    for letter in word:
#set a try/except statement to prevent user from inputting invalid inputs
        try:
            total += score[letter]
        except:
            print("Error: Invalid input.")
            return 0
    return total
#print(scrabble_score(word))
print(scrabble_score(word))

print('Thanks for playing! :)')
