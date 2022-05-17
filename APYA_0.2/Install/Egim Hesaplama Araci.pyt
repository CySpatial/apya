import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Egim]


class Egim(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Egim Hesabi"
        self.description = "Ýnputlar girildikten sonra otomatik olarak YUKSEKLIK alaný 0 ve 'null' olanlar silinerek plan sýnýrýna göre 500 m buffer olustulur ve buna göre clip edilir. Ayrýca TIN veriside otomatik olarak clip edilerek olusur.Tin verisi output ismine .tin eklenerek oluþturulur. ESYUKSELTI katmaný 'YUKSEKLIK' alanýný, Eðimi hesaplanacak olan katmanýnda 'EGIM' alaný içermesi gereklidir. Aksi taktirde sistem hata verir. Eðer araç hata vermiþse ve varsa C nin altýnda bulunan 'dd1' ve 'zel' dosyalarý silinir ve araç tekrar çalýþtýrýlýr. Designed by Mustafa Ceyhan."
        self.canRunInBackground = False

    def getParameterInfo(self):
        GEODATABASE=arcpy.Parameter (
            displayName="VERITABANI",
            name="GEODATABASE",
            datatype="workspace",
            parameterType="Required",
            direction="Input")
       
        
        ESYUKSELTI=arcpy.Parameter (
            displayName="ESYUKSELTI KATMANI",
            name="ESYUKSELTI",
            datatype="Feature Layer",
            parameterType="Required",
            direction="Input")
        
        Output_TIN=arcpy.Parameter (
            displayName="TIN KAYDET",
            name="Output_TIN",
            datatype="TIN",
            parameterType="Required",
            direction="Output")

	EGIM_KATMAN=arcpy.Parameter (
            displayName="EÐÝMÝ HESAPLANACAK KATMAN",
            name="EGIM_KATMAN",
            datatype="Feature Layer",
            parameterType="Required",
            direction="Input")

        params=[GEODATABASE,ESYUKSELTI,Output_TIN,EGIM_KATMAN]
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
        
	GEODATABASE=parameters[0].valueAsText
	arcpy.env.workspace =GEODATABASE
	ESYUKSELTI=parameters[1].valueAsText
	Output_TIN = parameters[2].valueAsText
	EGIM_KATMAN = parameters[3].valueAsText
	arcpy.Buffer_analysis(EGIM_KATMAN,"BUFFER","500 Meters","FULL","ROUND","ALL")
	arcpy.MakeFeatureLayer_management(ESYUKSELTI,"ESYUKSELTI_NEW")
	arcpy.SelectLayerByAttribute_management("ESYUKSELTI_NEW","NEW_SELECTION","[YUKSEKLIK]=0 or [YUKSEKLIK] is null")
	arcpy.DeleteFeatures_management("ESYUKSELTI_NEW")
	arcpy.CreateTin_3d(Output_TIN, "", "ESYUKSELTI_NEW YUKSEKLIK Hard_Line <None>", "DELAUNAY")
	arcpy.EditTin_3d(Output_TIN, "BUFFER <None> <None> Soft_Clip", "DELAUNAY")
	arcpy.TinRaster_3d(Output_TIN, "C:\dd1", "FLOAT", "LINEAR", "CELLSIZE 40", "1")
	arcpy.Slope_3d( "C:\dd1", "C:\zel", "PERCENT_RISE", "1")
	arcpy.gp.ZonalStatisticsAsTable_sa(EGIM_KATMAN, "OBJECTID", "C:\zel", "mus", "DATA", "ALL")
	arcpy.JoinField_management (EGIM_KATMAN, "OBJECTID", "mus", "OBJECTID_1", "MEAN")
	arcpy.CalculateField_management(EGIM_KATMAN, "EGIM","int(!MEAN!)","PYTHON_9.3")
	arcpy.DeleteField_management(EGIM_KATMAN, "MEAN")
	arcpy.DeleteField_management(EGIM_KATMAN, "MEAN_1")
	arcpy.Delete_management("C:\dd1")
	arcpy.Delete_management("C:\zel")
	arcpy.Delete_management("mus")
	arcpy.Delete_management("BUFFER")
        


	return



