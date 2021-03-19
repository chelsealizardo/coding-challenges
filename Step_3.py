
#####
# Step 3 - Python Script from Tools
#####

# NOTE THAT THIS TASK IS ALSO YOUR CODING CHALLENGE THIS WEEK, I DO NOT EXPECT US TO COMPLETE THIS IN CLASS.

# Task 1 - Use what you have learned to process the Landsat files provided, this time, you know you are
# interested in the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the
# Landsat 8 imagery. Data provided are monthly (a couple are missing due to cloud coverage) during the
# year 2015 for the State of RI.

# Before you start, here is a suggested workflow:

# 1) Extract the Step_3_data.zip file into a known location.
# 2) For each month provided, you want to calculate the NVDI, using the equation: nvdi = (nir - vis) / (nir + vis)
# https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index. Consider using the Raster Calculator Tool
# in ArcMap and using "Copy as Python Snippet" for the first calculation.

# The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided. As part of your
# code submission, you should also provide a visualization document (e.g. an ArcMap layout), showing the patterns for
# an area of RI that you find interesting.


import arcpy
import os

arcpy.env.overwriteOutput = True

# Set your workspace and remove any files that are not TIF files
arcpy.env.workspace = r"C:\data\06_Cheating\Step_3_data_lfs\Monthly_Composites\Monthly_201502"
listRasters = arcpy.ListRasters("*", "TIF")

# print listRasters to verify that the code actually worked
print(listRasters)

# Remove the BQA.tif file from the list, replace 201502 with the correct string.
listRasters = [x for x in listRasters if "_BQA.tif" not in x]
# listRasters = [x for x in listRasters if "201502" not in x]
print(listRasters)

# arcpy.CompositeBands_management(listRasters,
#                                 r"C:\data\06_Cheating\Step_3_data_lfs\Monthly_Composites\201502_Composite.tif")



# Now edit the arcpy.CompositeBands_Management tool to run the 201502 data,

# print("Compositing Bands... ")
# arcpy.CompositeBands_management(in_rasters=listRasters, out_raster= r"C:\data\06_Cheating\Step_3_data_lfs\201502.tif")
# print("Compositing Bands... Finished")

listMonths = ["201502", "201504", "201505", "201507", "201510", "201511"]
outputDirectory = r"C:\data\06_Cheating\Step_3_data_lfs\Monthly_Composites"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)


for month in listMonths:
    arcpy.env.workspace = r"C:\data\06_Cheating\Step_3_data_lfs\Monthly_Composites\Monthly_" + str(month)
    listRasters = arcpy.ListRasters("*", "TIF")
    print("For month: " + month + ", there are: " + str(listRasters) + " bands to process.")
# Remove any _BQA.tif files that may be in your directory
    listRasters = [x for x in str(listRasters) if "_BQA.tif" not in x]
    print(listRasters)
    arcpy.CompositeBands_management(listRasters,
                                    os.path.join(outputDirectory, r"Monthly_" + str(month) + "Composites.tif"))


