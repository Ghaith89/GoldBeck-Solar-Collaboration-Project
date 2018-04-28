import clr

# Import RevitNodes
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

ele = []
count = -1
for i in IN[0]:

	count = count+1
	val = IN[1][count]
	m = i.SetParameterByName("Bezeichnung Kabelbrücke", str(val))
	ele.append(m)


OUT = ele