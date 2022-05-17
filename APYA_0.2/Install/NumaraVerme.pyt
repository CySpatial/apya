import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Siralama]


class Siralama(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Nokta Duzenle"
        self.description = "Ornek Alan katmaný olusturulduktan sonra bu araç X_KOORD ve Y_KOORD alanlarýna göre sýralama yapýlarak NOKTA_NO numaralandýrýlýr. Designed by Mustafa Ceyhan"
        self.canRunInBackground = False

    def getParameterInfo(self):
        
	in_dataset=arcpy.Parameter (
            displayName="Ornek Alan",
            name="in_dataset",
            datatype="Feature Layer",
            parameterType="Required",
	    direction="Input"
		)

	out_dataset=arcpy.Parameter (
            displayName="Kaydet",
            name="out_dataset",
            datatype="Feature Layer",
            parameterType="Required",
	    direction="Output"
		)
        params = [in_dataset,out_dataset]
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
        
	in_dataset = parameters[0].valueAsText
	out_dataset=parameters[1].valueAsText
	sort_fields = [["Y_KOORD", "DESCENDING"],["X_KOORD", "ASCENDING"]]
	arcpy.Sort_management(in_dataset, out_dataset, sort_fields,"UR")
	expression ="autoIncrement()"
	codeblock ="""rec=0 
def autoIncrement(): 
 global rec 
 pStart = 1  
 pInterval = 1 
 if (rec == 0):  
  rec = pStart  
 else:  
  rec += pInterval  
 return rec"""
 	arcpy.CalculateField_management(out_dataset, "NOKTA_NO", expression, "PYTHON_9.3", codeblock)


        return
