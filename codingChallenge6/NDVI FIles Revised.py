

import os, arcpy
from arcpy.sa import *

workspace = input()
print("Workspace is: 'Provide workspace ")
# example :workspace = r"C:\data\codingChallenge6\Step_3_data_lfs"


# Create list containing all of the workspace files available
listMonths = os.listdir(workspace)
print(listMonths)

#Create a for loop to process the files in the workspace
for month in listMonths:
    arcpy.env.workspace = workspace + "\\" + str(month)  #This will change what folder is being processed in the loop
    listRasters = arcpy.ListRasters("*", "TIF")  # Create a variable to find the files with a .TIF extension
    # Remove all files except for B4.tif and B5.tif files from the list.
    B4Raster = [x for x in listRasters if "B4" in x]  # find the files and add them to the list
    print(B4Raster) #Print the result
    Red = workspace + "\\" + str(month) + "\\" + str(B4Raster[0])  # turns the element into a string
    print(Red) #Print the result
    B5Raster = [x for x in listRasters if "B5" in x]  # find the correct file
    print(B5Raster) #Print the result
    NIR = workspace + "\\" + str(month) + "\\" + str(B5Raster[0])  # turns the element into a string
    print(NIR) #Print the result
    print()  # space between loop iteration print outs

    output_raster = (Raster(NIR) - Raster(Red)) / (Raster(NIR) + Raster(Red))  # equation to calculate the NDVI
    output_raster.save(workspace + "\\" + str(month) + "_NDVI.tif")  # Saves the NDVI output

