# Coding Challenge 4
### Chelsea Lizardo
### NRS 528
#
#
# Main focus: find a particular tool that I like in arcpy. Set up the tool to run in Python,
# add some useful comments, and importantly, provide some example data in your repository
# (try to make it open source, such as Open Streetmap, or RI GIS. You can add it as a zip file to your repository.

# The tool I will be using today is known as the erase tool and can be found in the Overlay toolset.
# I will be using this tool to create a feature class that overlays the Input Features with the polygons of the Erase Features.
# Only those portions of the input features falling outside the erase features outside boundaries are copied to the output feature class.

# Start by importing system modules that will be needed for this code block
import arcpy
from arcpy import env

#set the environment settign
env.workspace = 'C:\data\codingChallenge4\codingChallenge4\codingChallenge4.gdb'

# Select suitable vegetation patches from all vegetation
veg = "Landcover 2011"
suitableVeg = "C:\data\codingChallenge4\codingChallenge4\codingChallenge4.gdb/landcover 2011"
whereClause = "HABITAT = 1"
arcpy.Select_analysis(veg, suitableVeg, whereClause)

# Buffer areas of impact around major roads
roads = "majorrds"
roadsBuffer = "C:\data\codingChallenge4\codingChallenge4\codingChallenge4.gdb/buffer_output"
distanceField = "Distance"
dissolveField = "Distance"
arcpy.Buffer_analysis(roads, roadsBuffer, distanceField, "FULL", "ROUND", "LIST", dissolveField)

# Erase areas of impact around major roads from the suitable vegetation patches
eraseOutput = "C:\data\codingChallenge4\codingChallenge4\codingChallenge4.gdb"
xyTol = "1 Meters"
arcpy.Erase_analysis(suitableVeg, roadsBuffer, eraseOutput, xyTol)