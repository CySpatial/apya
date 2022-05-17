import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""
        
        # List of tool classes associated with this toolbox
        self.tools = [KONTROL,KONTROL1]



class KONTROL(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Topology Kontrol Aracý"
        self.description = "DATASET katmaný ve TUM_SINIR input olarak alýnýr. TUM_SINIR burada tüm türkiye ya da topolojisi yapýlacak olan plan ünitesinin komsu seflikleri içeren katmaný ifade eder. DATASET katmaný içerisinde BOLME, BOLMECIK katmaný bulunmalýdýr. Araç çalýþtýrýldýktan sonra Topology olusur ve otomatik olarak amenajman için gerekli olan tüm topoloji kurallarý (üst üste binme, arada boþluk katmanlar arasýnda gibi) tanýmlanýr. Hatalarý görmek için arcmap topology toolu çaðrýnýz ve show errors penceresinden bu hatalarý kontrol ediniz. Designed by Mustafa CEYHAN"
        self.canRunInBackground = False
        

    def getParameterInfo(self):
        DATASET=arcpy.Parameter (
            displayName="DATASET SEÇ",
            name="Dataset",
            datatype="DATASET",
            parameterType="Required",
            direction="Input")
        """in_features.filter.list=["Point", "Polyline", "Polygon"]"""
        
        TUM_SINIR=arcpy.Parameter (
            displayName="TUM_SINIR SEÇ",
            name="TUM_SINIR",
            datatype="Feature Layer",
            parameterType="Required",
            direction="Input")
        """field.parameterDependencies=[in_features.name]
        field.filter.list=["Short","Long","Double","Float","Text"]"""




        params=[DATASET,TUM_SINIR]
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
    
        input_feature_class=parameters[1].valueAsText
        env_dataset=parameters[0].valueAsText
        arcpy.env.workspace =env_dataset
        arcpy.MakeFeatureLayer_management(input_feature_class, "sil1")
        arcpy.SelectLayerByLocation_management("sil1","WITHIN_A_DISTANCE","PLAN_SINIRI","1 meters")
        arcpy.CopyFeatures_management("sil1","KOMSU_SEFLIKLER")
        arcpy.Dissolve_management("BOLME", "BOLME_DISSINIR", "PLAN_ID", "", "MULTI_PART", "DISSOLVE_LINES")
        arcpy.Dissolve_management("BOLMECIK", "BOLMECIK_DISSINIR", "PLAN_ID", "", "MULTI_PART", "DISSOLVE_LINES")
        Topology1 = "Topology"
        Topology2 = Topology1
        Topology3 = Topology2
        Topology__2_ = Topology1
        Topology3_1 = Topology__2_
        Topology4 = Topology1
        Topology__4_ = Topology1
        Topology5 = Topology1
        arcpy.CreateTopology_management(env_dataset, "Topology", "")
        arcpy.AddFeatureClassToTopology_management("Topology", "BOLME", "1", "1")
        arcpy.AddFeatureClassToTopology_management("Topology", "BOLMECIK", "1", "1")
        arcpy.AddFeatureClassToTopology_management("Topology", "PLAN_SINIRI", "1", "1")
        arcpy.AddFeatureClassToTopology_management("Topology", "KOMSU_SEFLIKLER", "1", "1")
        arcpy.AddFeatureClassToTopology_management("Topology", "BOLME_DISSINIR", "1", "1")
        arcpy.AddFeatureClassToTopology_management("Topology", "BOLMECIK_DISSINIR", "1", "1")
        arcpy.AddRuleToTopology_management(Topology1, "Must Not Overlap (Area)", "BOLME", "", "", "")
        arcpy.AddRuleToTopology_management(Topology1, "Must Not Overlap (Area)", "BOLMECIK", "", "", "")
        arcpy.AddRuleToTopology_management(Topology1, "Boundary Must Be Covered By Boundary Of (Area-Area)", "PLAN_SINIRI", "", "KOMSU_SEFLIKLER", "")
        arcpy.AddRuleToTopology_management(Topology1, "Boundary Must Be Covered By Boundary Of (Area-Area)", "PLAN_SINIRI", "", "BOLME_DISSINIR", "")
        arcpy.AddRuleToTopology_management(Topology1, "Boundary Must Be Covered By Boundary Of (Area-Area)", "PLAN_SINIRI", "", "BOLMECIK_DISSINIR", "")
        arcpy.ValidateTopology_management(Topology2, "Full_Extent")
        arcpy.ValidateTopology_management(Topology4, "Full_Extent")
        arcpy.ValidateTopology_management(Topology5, "Full_Extent")
        arcpy.AddRuleToTopology_management(Topology1, "Must Not Have Gaps (Area)", "BOLME", "", "", "")
        arcpy.AddRuleToTopology_management(Topology1, "Must Not Have Gaps (Area)", "BOLMECIK", "", "", "")
        arcpy.ValidateTopology_management(Topology__2_, "Full_Extent")
        arcpy.ValidateTopology_management(Topology__4_, "Full_Extent")



        return

class KONTROL1(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Topology Silme Aracý"
        self.description = "Bu araç daha önceden oluþmuþ olan topology'i ve olustur aracý ile oluþan KOMSU_SEFLIKLER, BOLME_DISSINIR, BOLMECIK_DISSINIR katmanlarý siler. Çünkü olustur aracý ile yeniden topology oluþturmak için bu gereklidir. Aksi taktirde hata verir. Designed by Mustafa CEYHAN "
        self.canRunInBackground = False

    def getParameterInfo(self):
        DATASET=arcpy.Parameter (
            displayName="DATASET SEÇ",
            name="Dataset",
            datatype="DATASET",
            parameterType="Required",
            direction="Input")
        """in_features.filter.list=["Point", "Polyline", "Polygon"]"""
        params=[DATASET]
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

        env_dataset=parameters[0].valueAsText
        arcpy.env.workspace =env_dataset
        arcpy.Delete_management("Topology") 
        arcpy.Delete_management("BOLME_DISSINIR")
        arcpy.Delete_management("BOLMECIK_DISSINIR")
	arcpy.Delete_management("KOMSU_SEFLIKLER") 

        return

