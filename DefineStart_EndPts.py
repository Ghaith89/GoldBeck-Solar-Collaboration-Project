import clr

# Import RevitNodes
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
pans = IN[0]


st_end = []
for gr_c in pans:
	k = []
	pa_st = gr_c[0]
	co = len(gr_c) - 1
	pa_ed = gr_c[co]

	po01 = pa_st.Location
	po02 = pa_ed.Location
	k.append(po01)
	k.append(po02)
	st_end.append(k)

	
OUT = st_end