import arcpy
import shutil
import os


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [YEDIRME]


class YEDIRME(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Yedirme"
        self.description = "Bu modül çeþitli iþlemler sonucu oluþan küçük alanlarý, en uzun sýnýra sahip olan komþu alanlara yedirir. NOT: Modül çalýþýrken hata alýndýðýnda lütfen C nin altýndaki silTrs klaörünü silip tekrar modülü çalýþtýrýnýz"
        self.canRunInBackground = False

    def getParameterInfo(self):
	in_feature_class=arcpy.Parameter (
            displayName="Bolmecik (!Klasörden seçiniz)",
            name="in_feature_class",
            datatype="Feature Layer",
            parameterType="Required",
            direction="Input")

	AlanMiktari=arcpy.Parameter (
            displayName="Yedirilecek Max. Alan Degeri(m2)",
            name="AlanMiktari",
            datatype="Double",
            parameterType="Required",
            direction="Input")

	sonfeature=arcpy.Parameter (
            displayName="Kaydet",
            name="sonfeature",
            datatype="Feature Layer",
            parameterType="Required",
            direction="Output")

        params = [in_feature_class,AlanMiktari,sonfeature]
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
	in_feature_class=parameters[0].valueAsText
	AlanMiktari=parameters[1].valueAsText
	sonfeature=parameters[2].valueAsText
        arcpy.CreateFolder_management("C:/", "silTrs")
	arcpy.CreatePersonalGDB_management("C:/silTrs", "silinecek.mdb")
       	arcpy.env.workspace=r'C:\silTrs\silinecek.mdb'
	field='BLM_NO'
	arcpy.SplitByAttributes_analysis(in_feature_class, "C:\silTrs\silinecek.mdb", field)
	featureclasses = arcpy.ListFeatureClasses()
	i=0
	j=0
	for fc in featureclasses:
    	    tempLayer="Lay"+str(i)
            arcpy.MakeFeatureLayer_management(fc, tempLayer)
	    arcpy.SelectLayerByAttribute_management(tempLayer, "NEW_SELECTION", "SHAPE_Area<={}".format(AlanMiktari)or "Shape_Area<={}".format(AlanMiktari))
	    outFeatureClass="Out"+str(j)
	    arcpy.Eliminate_management(tempLayer, outFeatureClass, "LENGTH")
            i=i+1
	    j=j+1
	outfeatureclasses = arcpy.ListFeatureClasses("Out*")
	arcpy.Merge_management(outfeatureclasses, sonfeature)
	arcpy.Delete_management(r'C:\silTrs')
	arcpy.DeleteField_management(sonfeature, "FID_BOLMECIK")
        return
