# Task 1 - Use what you have learned to process the Landsat files provided, this time, you know you are
# interested in the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the
# Landsat 8 imagery. Data provided are monthly (a couple are missing due to cloud coverage) during the
# year 2015 for the State of RI.

# Before you start, here is a suggested workflow:

# 1) Extract the Step_3_data.zip file into a known location.
# 2) For each month provided, you want to calculate the NVDI, using the equation: NDVI = (nir - vis) / (nir + vis)
# https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index. Consider using the Raster Calculator Tool
# in ArcMap and using "Copy as Python Snippet" for the first calculation.


import os, arcpy

arcpy.CheckOutExtension("Spatial")
listMonths = ["02", "04", "05", "07", "10", "11"]

# Change the directory you are using, and make an output directory to store all of the files named NDVI output

directory = r"C:\data\06_Cheating\Step_3_data_lfs"
outputDirectory = os.path.join(directory, "NDVI_output")
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

# Then use a for loop that will iterate though each folder containing the months and  will isolate the 4th and 5th band
# files into lists. Print the bands

for month in listMonths:
    print("Creating NDVI for " + month)
    arcpy.env.workspace = os.path.join(directory, "2015" + month)
    Band4 = arcpy.ListRasters("*", "TIF")
    Band4 = [x for x in Band4 if "B4" in x]
    Band5 = arcpy.ListRasters("*", "TIF")
    Band5 = [x for x in Band5 if "B5" in x]
    print(Band5)
    print(Band4)

    # Then we can use the raster calculator to do the NDVI calculation using the equation: nvdi = (nir - vis) / (nir + vis)
    # and use the Band4 and Band5 list to do so

    calculation = 'Float("' + Band5[0] + '" - "' + Band4[0] + '") / Float("' + Band5[0] + '" + "' + Band4[0] + '")'
    #Print the results and join output directory to NDVI 2015
    print(calculation)
    arcpy.gp.RasterCalculator_sa(calculation, os.path.join(outputDirectory, "NDVI2015" + month + ".tif"))
    print("NDVI has run successfully")