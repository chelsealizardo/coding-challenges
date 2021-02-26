"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" part_2.py 
def main(arg):
    print("My argument: " + str(arg))

arguement_1 = main(sys.argv[1])
arguement_2 = main(sys.argv[2])
arguement_3 = main(sys.argv[3])

arguements = [arguement_1, arguement_2, arguement_3]
print(arguements)
pause
