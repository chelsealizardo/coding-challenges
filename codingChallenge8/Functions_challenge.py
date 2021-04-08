# For this coding challenge, I made a function that will sort through a directory and pull out
# the necessary files for an NDVI(B4 & B5), which we learned about in Lesson 6. I will use for loops to identify
# these files and also to exclude all unnecessary bands as well.

import arcpy

arcpy.env.overwriteOutput = True

# The data I used is our Arcpy lecture,specifically the Step 3 data which gives us monthly band composites and I copied
# the data into my coding challenge 8 folder. So the first step I did was assign a variable to my data location which
# will be used in the for loop.
monthly_raster = r"C:\data\codingChallenge8\Monthly_201502"


# using a similar format from previous classes, we can define a function by using the "def"
# followed by the function name and arguments in parentheses, and use for loops

def NDVI(a, b):
    # We also want to set a current workspace for which we will be using while running this code
    arcpy.env.workspace = a
    monthly_raster = arcpy.ListRasters("*", b)
    monthly_raster = [x for x in monthly_raster
                      if "_B1.tif" not in x]
    monthly_raster = [x for x in monthly_raster
                      if "_B2.tif" not in x]
    monthly_raster = [x for x in monthly_raster
                      if "_B3.tif" not in x]
    monthly_raster = [x for x in monthly_raster
                      if "_B6.tif" not in x]
    monthly_raster = [x for x in monthly_raster
                      if "_B7.tif" not in x]
    monthly_raster = [x for x in monthly_raster
                      if "_B8.tif" not in x]
    monthly_raster = [x for x in monthly_raster
                      if "_B9.tif" not in x]
    monthly_raster = [x for x in monthly_raster
                      if "_B10.tif" not in x]
    monthly_raster = [x for x in monthly_raster
                      if "_B11.tif" not in x]
    monthly_raster = [x for x in monthly_raster
                      if "_BQA.tif" not in x]

    print("There are " + str(len(monthly_raster)) + " files ready for NDVI")
    print("Files available for NDVI: " + str(monthly_raster))


# #If you would like, you can return the output of the code, but this step is not necessary
#   return NDVI

# The result will be how many files are we have available for NDVI and which of those files end in .tif
NDVI(r"C:\data\codingChallenge8\Monthly_201502", "TIF")
print("The Function has run successfully!")
print("Yay!")
