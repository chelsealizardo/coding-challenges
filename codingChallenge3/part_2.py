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
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"
def main(arg):
    print("My argument: " + str(arg))

arguement_1 = main("hello! Here are three random interesting facts I bet you didnt know about!")
arguement_2 = main("McDonald’s once made bubblegum-flavored broccoli in attempt to get kids to eat healthier!")
arguement_3 = main("A cow-bison hybrid is called a “beefalo” and you can buy its meat in at least 21 states!")
arguement_4 = main("Octopuses lay 56,000 eggs at a time.The mother spends six months so devoted to protecting the eggs that she doesn’t eat. The babies are the size of a grain of rice when they’re born.")

arguements = [arguement_1, arguement_2, arguement_3]
print(arguements)




