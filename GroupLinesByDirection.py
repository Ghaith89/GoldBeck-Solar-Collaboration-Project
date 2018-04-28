
import clr
# Import RevitNodes
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GroupByDirection(List_lines):

	list_St = [i.StartPoint for i in List_lines]
	list_StX = [i.X for i in list_St]
	list_StY = [i.Y for i in list_St]

	list_Ed = [i.EndPoint for i in List_lines]
	list_EdX = [i.X for i in list_Ed]
	list_EdY = [i.Y for i in list_Ed]

	dirX = [list_EdX[i]-list_StX[i] for i in range(len(List_lines))]
	dirY = [list_EdY[i]-list_StY[i] for i in range(len(List_lines))]

	DirNum = [dirX[i]+dirY[i] for i in range(len(List_lines))]
	List_Vec = zip(List_lines, DirNum)
	Gr_linesA = [i[0] for i in List_Vec if i[1]>0]
	Gr_linesB = [i[0] for i in List_Vec if i[1]<0]
	Gr_lines = []
	Gr_lines.append(Gr_linesA)
	Gr_lines.append(Gr_linesB)

	return Gr_lines

N = GroupByDirection(IN[0])

OUT = N