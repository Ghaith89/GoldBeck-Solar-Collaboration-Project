import clr

# Import RevitNodes
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
Fa_pos = []

ind = []
for i in IN[0]:
	count = 0
	for n in IN[1]:
		count = count+1
		if i == n :
		
			ind.append(count-1)

OUT = ind