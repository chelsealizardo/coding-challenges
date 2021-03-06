
# For my midterm, I wanted to isolate South Kingston and set as extent,
# create buffer around water features, and label the buffer areas as a 0 and non-buffer areas as 1

# First I am importing the os and arcpy modules as well as setting the work environment. I am creating a temporary
# work space for the intermediate files. Later i will delete this folder.

import os, arcpy

from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput = True

# CHANGE WORKSAPCE HERE

directory = r"C:\data\Toolbox_Midterm"
arcpy.env.workspace = directory
tempDirectory = os.path.join(directory, "intermediate_files")
if not os.path.exists(tempDirectory):
    os.mkdir(tempDirectory)


# Instead of working with the entire state of RI, I want to isolate SOUTH KINGSTON and set that as my processing extent

in_features = "towns.shp"
out_feature_class = os.path.join(tempDirectory, "SouthKingstown.shp")
where_clause = '"NAME" = ' + "'SOUTH KINGSTOWN'"

arcpy.Select_analysis(in_features, out_feature_class, where_clause)


if arcpy.Exists(out_feature_class):
    print("Town selection successful")

desc = arcpy.Describe(out_feature_class)
YMin = desc.extent.YMin
YMax = desc.extent.YMax
XMin = desc.extent.XMin
XMax = desc.extent.XMax

arcpy.env.extent = arcpy.Extent(XMin, YMin, XMax, YMax)

print(r"Extent:\n YMin: {0},\n YMax: {1},\n XMin: {2},\n XMax: {3}".format(desc.extent.YMin, desc.extent.YMax,
                                                                              desc.extent.XMin, desc.extent.XMax))


# Create a list of just water feature from all shapefiles
# Run loop to create a buffer layer by also converting to raster for all water features within processing extent

waterFeatures = arcpy.ListFeatureClasses("*", "ALL")
waterFeatures = [x for x in waterFeatures if "towns" not in x]


for x in waterFeatures:
    in_source_data = x + ".shp"
    maximum_distance = 100
    cell_size = 4
    out_direction_raster = os.path.join(tempDirectory, x[0:5] + "_buffer.img")

    EucDistance(in_source_data, maximum_distance, cell_size, out_direction_raster)
print("Euclidean Distance calculated for " + x)


# With the newly created buffer rasters, am now going to run the IS NULL tool to label the buffer areas as a 0
# and non-buffer areas as 1

arcpy.env.workspace = tempDirectory

buffer_lyr = arcpy.ListRasters("*", "ALL")
print(buffer_lyr)

for y in buffer_lyr:
    in_raster = y
    outIsNull = arcpy.sa.IsNull(in_raster)
    outIsNull.save(os.path.join(tempDirectory, y[0:5] + "_restraint.img"))
print("Restraint raster created for " + y)



#Delete all the intermediate files that are stored in the interediate folder by deleting the entire folder.

arcpy.env.workspace = tempDirectory

arcpy.Delete_management(r"'SouthKingstown' ; 'Lakes_buffer' ; 'Lakes_restraint' ; 'wetla_buffer' ; 'wetla_restraint' ; 'River_buffer' ; 'River_restraint'")

arcpy.Delete_management(tempDirectory)

print("Intermediate files deleted")