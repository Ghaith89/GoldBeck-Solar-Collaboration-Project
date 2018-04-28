	
import clr
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def dist_sort(Pt, List_cabel):
	dis_list = []
	for k in List_cabel:
		dis = Pt.DistanceTo(k)
		dis_list.append(dis)
	So = zip(dis_list, List_cabel)
	So.sort()
	#So.reverse()
	poso = [List_cabel for dis_list, List_cabel in So]
	clos_cabel = poso[0]
	return clos_cabel, Pt


def CabelGroupPts(List_vec, List_li):
	CabelGroup = []
	for i in List_li :
		S = [F for F in List_vec if F[0]==i]
		GrPts = [i[1] for i in S]
		#CabelGroup.append(i[0])
		CabelGroup.append(GrPts)
	return CabelGroup

def connectingCabels(List_pt, Line):
	List_lines = []
	for i in List_pt:
		poli = Line.ClosestPointTo(i)
		Li = Line.ByStartPointEndPoint(i, poli)
		List_lines.append(Li)
	return List_lines

def cleanLines(List_lines):
	EndPts = []
	for i in List_lines:
		End = i.EndPoint
		EndPts.append(End)
	Lin_EndPt = zip(List_lines, EndPts)
	List_Gr = [[y[0] for y in Lin_EndPt if y[1]== x] for x in EndPts]
	return [x[0] for x in List_Gr]

#Generate list of pts close to each cabel
List_vecCabelPt = []
for i in IN[2]:
	m = dist_sort(i, IN[1])
	List_vecCabelPt.append(m)
Ca = CabelGroupPts(List_vecCabelPt, IN[1])

#Generate list of Subcabels close to each cabel
listsub = []
co = 0
for f in Ca:
	co = co+1
	o = co-1
	subCabels = connectingCabels(f, IN[1][o])
	listsub.append(subCabels)



#OUT = CabelGroupPts(List_vecCabelPt, IN[1])

OUT = listsub




	
