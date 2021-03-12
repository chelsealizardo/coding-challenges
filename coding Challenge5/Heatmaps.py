# Coding Challenge 2
### Chelsea Lizardo
### NRS 528
#
#
#
# For this coding challenge, I want you to practice the heatmap generation that we went through in class, but this time obtain your own input data, and I want you to generate heatmaps for TWO species.
#
# You can obtain species data from a vast array of different sources, for example:
#
# obis - Note: You should delete many columns (keep species name, lat/lon) as OBIS adds some really long strings that don't fit the Shapefile specification.
# GBIF
# Maybe something on RI GIS
# Or just Google species distribution data
# My requirements are:
#
# The two input species data must be in a SINGLE CSV file, you must process the input data to separate out the species (Hint: You can a slightly edited version of our CSV code from a previous session to do this), I recommend downloading the species data from the same source so the columns match.
# Only a single line of code needs to be altered (workspace environment) to ensure code runs on my computer, and you provide the species data along with your Python code.
# The heatmaps are set to the right size and extent for your species input data, i.e. appropriate fishnet cellSize.
# You leave no trace of execution, except the resulting heatmap files.
# You provide print statements that explain what the code is doing, e.g. Fishnet file generated.


import arcpy
import csv
import os
arcpy.env.overwriteOutput = True

with open("sharkdata.csv") as species_csv:
    csv_reader = csv.reader(species_csv, delimiter=',')

    line_count = 0

    for row in csv_reader:
        if line_count == 0:
            print("Column names are: " + str(row))
            line_count += 1
        line_count += 1
        print("Processed " + str(line_count) + " lines.")

    # We can do some basic tasks, for example, let's sum the "Population" column
    total = 0 #start counter at zero
    for row in csv.reader(species_csv):
        if total == 0:
            total += 1
            pass
        else:
            total += float(row[3])
# #3 = 4th column, in this case, population, remember Python uses zero indexing.
    print(format(total, 'f'))
# # format prints as float
    print(total)

#Make a list of the years and the countries in the dataset, how many years and countries are there?

list_scientificName = []
list_eventDate = []
with open("sharkdata.csv") as species_csv:
    total = 0  # start counter at zero
    for row in csv.reader(species_csv):
        if row[0] not in list_scientificName:
            list_scientificName.append(row[0])
        if row[2] not in list_eventDate:
            list_eventDate.append(row[2])

print(len(list_eventDate))
print(len(list_scientificName))

# # # 2) Calculate the species for every event date in the dataset.
list_eventDate = []
for date in list_eventDate:

    with open("sharkdata.csv") as species_csv:
        next(species_csv)

        total = 0

        for row in csv.reader(species_csv):
            if row[2] == date:
                total += float(row[3])

    print(str(date) + ": " + str(total))

    # # 3) Split the dataset into a file for each species, with the filename the name of the species, in a new
    # # directory using only Python
    os.mkdir("Species_Directory")

    species_list = []
    with open("sharkdata.csv") as species_csv:
        next(species_csv)
        for row in csv.reader(species_csv):
            if row[0] not in species_list:
                species_list.append(row[0])
    print(species_list)
    print(len(species_list))

    for scientificName in species_list:
        with open("sharkdata.csv") as species_csv:
            next(species_csv)
            for row in csv.reader(species_csv):
                if row[0] == scientificName:
                    file = open("Species_directory/" + scientificName +".csv", "a")
                    file.write(",".join(row))
                    file.write('\n')
        file.close()

path = "C:\Species_directory"
# create_dir = os.mkdir(r"C:\global_datasets")
check = os.path.exists(r"C:\Species_directory")



# Set your workspace to the directory where you are storing your files
arcpy.env.workspace = r"C:\data\coding Challenge5"

in_Table = r"sharkdata.csv"
x_coords = "decimalLongitude"
y_coords = "decimalLatitude"
z_coords = ""
out_Layer = "Mako and White shark"
saved_Layer = r"shark_data_output.shp"
#
# # Set the spatial reference
spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
# # convert csv file into shapefile, mind you it doesnt mak the shapefile output- so need a place to store output
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
print(arcpy.GetCount_management(out_Layer))

# Save to a layer file
arcpy.CopyFeatures_management(lyr, saved_Layer)

if arcpy.Exists(saved_Layer):
    print("Created file successfully!")
##### 3. Check the correct coordinate system has been applied (Hint: see last week!)

desc = arcpy.Describe(out_Layer)
X_Min = desc.extent.XMin
X_Max = desc.extent.XMax
Y_Min = desc.extent.YMin
Y_Max = desc.extent.YMax
print(desc, X_Min, X_Max, Y_Min, Y_Max)
##### 4. Visualize the file in ArcPro by dragging it into the program.

# 3. Generate a fishnet, but this time define the originCoordinate, yAxisCoordinate and oppositeCorner
# using the extracted extent from above. Hint: Formatting of the coordinate is important when generating
# the Fishnet, you must present it as: "-176.87 -41", note the space inbetween, and the fact that the
# entire thing is a string. Hint use: cellSizes of 0.25 degrees.

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

outFeatureClass = "species_data_Fishnet.shp"  # Name of output fishnet
print(str(X_Min) + " " + str(Y_Min))

# Set the origin of the fishnet
originCoordinate = str(X_Min) + " " + str(Y_Min)  # Left bottom of our point data
yAxisCoordinate = str(X_Min) + " " + str(Y_Min + 10)  # This sets the orientation on the y-axis, so we head north
cellSizeWidth = "0.25"
cellSizeHeight = "0.25"
numRows = ""  # Leave blank, as we have set cellSize
numColumns = ""  # Leave blank, as we have set cellSize
oppositeCorner = str(X_Max) + " " + str(Y_Max)   # i.e. max x and max y coordinate
labels = "NO_LABELS"
templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
geometryType = "POLYGON"  # Create a polygon, could be POLYLINE

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

# 4. Undertake a Spatial Join to join the fishnet to the observed points.
target_features = "species_data_Fishnet.shp"
join_features = "shark_data_output.shp"
out_feature_class = "species_data_HeatMap.shp"
join_operation = "JOIN_ONE_TO_ONE"
join_type = "KEEP_ALL"
field_mapping = ""
match_option = "INTERSECT"
search_radius = ""
distance_field_name = ""

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)
if arcpy.Exists(out_feature_class):
    print("Created Heatmap file successfully!")
    print("Deleting intermediate files")
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)