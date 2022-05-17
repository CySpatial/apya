import arcpy
import pythonaddins
import os

class ButtonClass1(object):
    """Implementation for APYA_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r'C:\APYA_0.2\Install\OrnekNokta.pyt', 'OrnekNokta4')
        pass

class ButtonClass2(object):
    """Implementation for APYA_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r'C:\APYA_0.2\Install\NumaraVerme.pyt', 'Siralama')
        pass

class ButtonClass4(object):
    """Implementation for APYA_addin.button_3 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r'C:\APYA_0.2\Install\Egim Hesaplama Araci.pyt', 'Egim')
        pass

class ButtonClass5(object):
    """Implementation for APYA_addin.button_4 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r'C:\APYA_0.2\Install\BAKI.tbx', 'BAKI')
        pass

class ButtonClass51(object):
    """Implementation for APYA_addin.button_2 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        os.startfile(r'C:\APYA_0.2\Install\Teblig_299.pdf')
        pass

class ButtonClass52(object):
    """Implementation for APYA_addin.button_9 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        os.startfile(r'C:\APYA_0.2\Install\cizimIzahname.pdf')
        pass

class ButtonClass53(object):
    """Implementation for APYA_addin.button_10 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        os.startfile(r'C:\APYA_0.2\Install\APYA_HELP.chm')
        pass

class ButtonClass6(object):
    """Implementation for APYA_addin.button_5 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r'C:\APYA_0.2\Install\Plan Topology Kontrol.pyt', 'KONTROL')
        pass

class ButtonClass7(object):
    """Implementation for APYA_addin.button_6 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r'C:\APYA_0.2\Install\Plan Topology Kontrol.pyt', 'KONTROL1')
        pass

class ButtonClass8(object):
    """Implementation for APYA_addin.button_7 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog(r'C:\APYA_0.2\Install\Yedirme.pyt','YEDIRME')
        pass

class ButtonClass9(object):
    """Implementation for APYA_addin.button_8 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        os.startfile(r'C:\APYA_0.2\Install\AmenajmanYonetmelik.pdf')
        pass
