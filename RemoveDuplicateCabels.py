import clr
clr.AddReference('ProtoGeometry')
clr.AddReference("RevitNodes")
from Autodesk.DesignScript.Geometry import *
import Revit
clr.ImportExtensions(Revit.Elements)

def uniq(input):

  output = []
  for x in input:
    if x not in output:
      output.append(x)

  return output

def roundptscoordiates(Pts):

	Roundedpts = []
	for i in Pts:
		rounded = []
		x = i.X
		x = int(x)
		rounded.append(x)
		y = i.Y
		y = int(y)
		rounded.append(y)
		z = i.Z
		z = int(z)
		rounded.append(z)
		Roundedpts.append(rounded)

	return Roundedpts


def cleanLines(List_lines):

	EndPts = []
	for i in List_lines:
		End = i.EndPoint
		EndPts.append(End)
	EndPts = roundptscoordiates(EndPts)
	UniEndPts = uniq(EndPts)
	Lin_EndPt = zip(List_lines, EndPts)
	List_Gr = [[y[0] for y in Lin_EndPt if y[1]== x] for x in UniEndPts]
	line_len = [[i.Length for i in x] for x in List_Gr]
	LiLen = zip(List_Gr, line_len)
	
	LiLen = [zip(i[1],i[0]) for i in LiLen]
	LiLen = [sorted(i) for i in LiLen]
	#LiLen = [i.reverse() for i in LiLen]

	LiLen = [i[len(i)-1][1] for i in LiLen]

	return LiLen

OUT = cleanLines(IN[0])