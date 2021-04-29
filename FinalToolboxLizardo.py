# For the final challenge in NRS 528, we have been asked to create a python toolbox that contains a minimum of three
# simple tools for undertaking geoprocessing and file managment operations. The three tools I have chosen to create are
# a NDVI tool, a buffer by 100 m tool and a List Raster tools. All of the data is also provided.


import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "Lizardo Final Python Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [buffer_100m, Produce_NDVI, ListRasters]


class buffer_100m(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Buffer Tool" # Give your tool a label
        self.description = "This tool will buffer the .shp files provided by 100 meters"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        shapefile = arcpy.Parameter(name="shp1",
                               displayName="First shapefile:",
                               datatype="DEFeatureClass",
                               parameterType="Required",
                               direction="Input")
        params.append(shapefile)
        shapefile_output = arcpy.Parameter(name="shapefile_output",
                                      displayName="Output destination for first buffered shapefile:",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Output")
        params.append(shapefile_output)
        shapefile2 = arcpy.Parameter(name="shapefile2",
                               displayName="Second shapefile (optional):",
                               datatype="DEFeatureClass",
                               parameterType="Optional",
                               direction="Input")
        params.append(shapefile2)
        shapefile2_output = arcpy.Parameter(name="shapefile2_output",
                                      displayName="Output destination for second buffered shapefile:",
                                      datatype="DEFeatureClass",
                                      parameterType="Optional",
                                      direction="Output")
        params.append(shapefile2_output)
        shapefile3 = arcpy.Parameter(name="shapefile3",
                               displayName="Third shapefile (optional):",
                               datatype="DEFeatureClass",
                               parameterType="Optional",
                               direction="Input")
        params.append(shapefile3)
        shapefile3_output = arcpy.Parameter(name="shapefile3_output",
                                      displayName="Output destination for third buffered shapefile:",
                                      datatype="DEFeatureClass",
                                      parameterType="Optional",
                                      direction="Output")
        params.append(shapefile3_output)
        return params


    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        shapefile = parameters[0].valueAsText
        shapefile_output = parameters[1].valueAsText
        shapefile2 = parameters[2].valueAsText
        shapefile2_output = parameters[3].valueAsText
        shapefile3 = parameters[4].valueAsText
        shapefile3_output = parameters[5].valueAsText

        inputFeatures = shapefile
        outputFeatures = shapefile_output
        distance = "100 meters"
        sideType = "FULL"
        lineEndType = "ROUND"
        dissolveOption = "NONE"
        dissolveField = "#"
        method = "PLANAR"
        arcpy.Buffer_analysis(inputFeatures, outputFeatures, distance, sideType,
                              lineEndType, dissolveOption, dissolveField, method)

        if len(parameters) > 2:
            inputFeatures = shapefile2
            outputFeatures = shapefile2_output
            distance = "100 meters"
            sideType = "FULL"
            lineEndType = "ROUND"
            dissolveOption = "NONE"
            dissolveField = "#"
            method = "PLANAR"
            arcpy.Buffer_analysis(inputFeatures, outputFeatures, distance, sideType,
                                  lineEndType, dissolveOption, dissolveField, method)

        if len(parameters) > 4:
            inputFeatures = shapefile3
            outputFeatures = shapefile3_output
            distance = "100 meters"
            sideType = "FULL"
            lineEndType = "ROUND"
            dissolveOption = "NONE"
            dissolveField = "#"
            method = "PLANAR"
            arcpy.Buffer_analysis(inputFeatures, outputFeatures, distance, sideType,
                                  lineEndType, dissolveOption, dissolveField, method)
        arcpy.AddMessage("Buffering of files completed!")
        return


class Produce_NDVI(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "NDVI Calculation Tool" # # Give your tool a label
        self.description = "This tool will take in two .TIF bands (Band4 and Band5) and produce an NDVI output."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        parameters = []
        band4 = arcpy.Parameter(name="band4",
                                 displayName="Band 4 Location:",
                                 datatype="GPRasterLayer",
                                 parameterType="Required",
                                 direction="Input")
        parameters.append(band4)
        band5 = arcpy.Parameter(name="band5",
                                 displayName="Band 5 Location:",
                                 datatype="GPRasterLayer",
                                 parameterType="Required",
                                 direction="Input")
        parameters.append(band5)
        ndvi_output = arcpy.Parameter(name="NDVI_outputs",
                                      displayName="Enter Location for NDVI output:",
                                      datatype="GPRasterLayer",
                                      parameterType="Required",
                                      direction="Output")
        parameters.append(ndvi_output)
        return parameters

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        band4 = parameters[0].valueAsText
        band5 = parameters[1].valueAsText
        NDVI_output = parameters[2].valueAsText



        calculation =arcpy.gp.RasterCalculator_sa('Float("' + band5 + '"-"' + band4 + '") / Float("' + band5 + '"+"' + band4 + '")',
        NDVI_output)
        print(calculation)
        arcpy.AddMessage("NDVI calculations completed!")
        return

class ListRasters(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "ListRasters Tool" # Give your tool a label
        self.description = "This tool will search a desired folder and list all raster files of a specified type."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        parameters = []
        input_raster = arcpy.Parameter(name="input_raster", # Variable name
                                     displayName="Enter the desired folder:", # Text that will be displayed in GUI
                                     datatype="DEFolder", # Type of data that can be inputted/outputted
                                     parameterType="Required", # Required|Optional|Derived
                                     direction="Input") # Input|Output
        parameters.append(input_raster)
        file = arcpy.Parameter(name="file_type", # Variable name
                                    displayName="Enter the raster file extension:", # Text that will be displayed in GUI
                                    datatype="GPString",  # Type of data that can be inputted/outputted
                                    parameterType="Required",  # Required|Optional|Derived
                                    direction="Input") # Input|Output
        parameters.append(file)
        return parameters

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_raster = parameters[0].valueAsText
        file = parameters[1].valueAsText

        arcpy.env.workspace = input_raster
        raster_list = arcpy.ListRasters("*", file)
        raster_list = [x for x in raster_list if "_BQA.tif" not in x]
        arcpy.AddMessage("The files ending in " + file + " are " + str(raster_list) + ".")
        arcpy.AddMessage("The number of " + file + " files in that folder is " + str(len(raster_list)) + ".")
        return