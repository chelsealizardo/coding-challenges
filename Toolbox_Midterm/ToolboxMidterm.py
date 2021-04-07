# For my Midterm Toolbox, I wanted to create a fucntioning code that checks what trails cross resevoir bodies in Rhode
# Island. The tools that I decided to include: Buffer, Clip, and intersect. The data I will be using is the
# Bikeways_and_Trails.shp and Public_Water_Reservoirs.shp that I have retreived from RIGIS and am currently using in my
# NRS 522 "GIS Analysis of Environmental Data" class taught by Dr. Jason Parent. In each code block I identify what tool
# I am using, give a quick description of what the tool does, and then include the code that can be run and produce
# a file that can be used in ArcPro.
#
#
# The first thing we always want to do is to import all of the libraries that we will be using in our code

import arcpy
import os

from arcpy import env
from notebook.notebookapp import raw_input

arcpy.CheckOutExtension("Spatial")
# Arcpy overwrite tool allows files to overwrite when saving to avoid the script from crashing during trials
arcpy.env.overwriteOutput = True


directory = r"C:\Data\Students_2021\Lizardo\coding-challenges\Toolbox_Midterm"
arcpy.env.workspace = directory
tempDirectory = os.path.join(directory, "intermediate_files")
if not os.path.exists(tempDirectory):
    os.mkdir(tempDirectory)

# Tool 1: Extent Tool
# Name: MidtermToolbox.py
# Description: The extent tool allows us to isolate an area specified by providing the coordinate of the lower left
# corner and the coordinate of the upper right corner in map units.
# Instead of working with the entire state of RI, I want to specifically work with Narragansett and use that
# as my extent

in_features = os.path.join(directory, r"Municipalities__1997_-shp", "towns.shp")
out_feature_class = os.path.join(tempDirectory, "Narragansett.shp")
where_clause = '"NAME" = ' + "'NARRAGANSETT'"

arcpy.Select_analysis(in_features, out_feature_class, where_clause)


if arcpy.Exists(out_feature_class):
    print("The tool has run successfully!")

desc = arcpy.Describe(out_feature_class)
YMin = desc.extent.YMin
YMax = desc.extent.YMax
XMin = desc.extent.XMin
XMax = desc.extent.XMax

arcpy.env.extent = arcpy.Extent(XMin, YMin, XMax, YMax)
print("Extent:\n YMin: {0},\n YMax: {1},\n XMin: {2},\n XMax: {3}".format(desc.extent.YMin, desc.extent.YMax,
                                                                              desc.extent.XMin, desc.extent.XMax))



# Tool 2: Buffer Tool
# Name: MidtermToolbox.py
# Description: The buffer tool allows the user to.
# For shapefile Bikeways_and_Trails use a buffer of 100 meters
## We can use the buffer toolon Bikes_and_trailways.shp,to buffer the area by 100 meters
in_features = r"C:\Users\chels\Schoolwork\Spring2021\GEO_522\Module3\Module_3c\data\Bikeways_and_Trails\Bikeways_and_Trails.shp"
# We can use the out_feature_class to create an output file for our buffer
out_feature_class = r"C:\Users\chels\Schoolwork\Spring2021\GEO_522\Module3\Module_3c\data\Bikeways_and_Trails\Bikeways_and_Trails_Output.shp"
buffer_distance_or_field = "100 meter"
line_side = "#"
line_end_type = "#"
dissolve_option = "#"
dissolve_field = "#"
method = "GEODESIC"
arcpy.Buffer_analysis(in_features, out_feature_class, buffer_distance_or_field, line_side, line_end_type, dissolve_option, dissolve_field, method)


# Tool 3: Clip tool
# Name: MidtermToolbox.py
# Tool Description: This tool is used to cut out a piece of one feature class using one or more of the features in
# another feature class. This is particularly useful for creating a new feature class—also referred to as study area
# or area of interest (AOI)—that contains a geographic subset of the features in another, larger feature class.
# Objective: Clip major roads that fall within the study area. For this case, I will be using the clip tool to

# Set workspace that we will be working from
env.workspace = "C:\data\Toolbox_Midterm"

# Set local variables and makesure that an ouput feature class is also created
in_features = "C:\data\Toolbox_Midterm\Public_Water_Reservoirs\Public_Water_Reservoirs.shp"
clip_features = "C:\data\Toolbox_Midterm\Bikeways_and_Trails\Bikeways_and_Trails.shp"
out_feature_class = "C:\data\Toolbox_Midterm\Bikeways_and_Trails\Trails_near_resevoirs_output.shp"
xy_tolerance = ""

# Execute Clip
arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)

# Now you can delete these files off your machine usig arcpy delete tool anda simple elseif statement asking for user input

userInput = raw_input("Would you like to delete the files now: yes or no? ")
userInput = userInput.lower()

if userInput == "yes":
    arcpy.Delete_management(tempDirectory)
    print("Files have successfully deleted")
elif userInput == "no":
    print("Files have been kept successfully")
else:
    print("Please pick yes or no")




