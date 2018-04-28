import clr

# Import RevitNodes
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
pans = IN[0]
param = IN[1]
vals = True
count = 0
for gr_c in pans:
	count = count+1
	for pa  in gr_c:
		pa.SetParameterByName(param[count-1], vals)

	
OUT = pans