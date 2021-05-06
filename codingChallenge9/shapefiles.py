import arcpy

# set workspace and allow for overwrite

arcpy.env.workspace = r"C:\data\codingChallenge9"
arcpy.env.overwriteOutput = True

# Set variable to our input file and the fields that will be used

shp_in = r"C:\data\codingChallenge9\RI_Forest_Health_Works_Project_Points_All_Invasives\RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"
fields = ['Point_num', 'Site', 'Species', 'photo']

# Create a new file to determine how many photos are present, which can be found in the the
# attribute table in the shp layer

presence = arcpy.AddFieldDelimiters(shp_in, "photo") + " = 'y'"
arcpy.Select_analysis(shp_in, "photo_presence.shp", presence)
print("New File has been Created Successfully!")

# Now count how many sites have photos
count = 0
sites = list()
presence = arcpy.AddFieldDelimiters(shp_in, "photo") + " = 'y'"
with arcpy.SearchCursor("photo_presence.shp", presence, fields) as cursor:
    for row in cursor:
        if row[1] not in sites:
            count += 1
            sites.append(row[1])
print("Sites with photos =", count)
#
# # Now we should make list with all the sites then exclude any with even one photo
#
# all_sites = list()
# with arcpy.SearchCursor("photo_presence.shp", fields) as cursor:
#     for row in cursor:
#         if row[1] not in all_sites:
#             sites.append(row[1])
# count_two = 0
#
# for point in all_sites:
#     if point not in all_sites:
#         count_two += 1
#         print(point)
#
# print("Sites with no photos =", count_two)
#
# # Also want to print all of the sites to double check
#
# print("All sites", all_sites)
# presence.close()

# Now we can count the species
#
# species = list()
# with arcpy.da.SearchCursor() as cursor:
#     for row in cursor:
#         if row[2] not in species:
#             species.append(row[2])
#
# print("Invasive species:", species)
# print("Species List", len(species))
