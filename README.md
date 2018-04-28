# GoldBeck-Solar-Collaboration-Project
The project aim is to automate repetitive tasks in roof plans for solar panels. I have collaborated with the CAD team in GoldBeck Solar in Manheim region. The project has been achieved using IronPython inside Dynamo Studio and the Revit API.
===================================================================================
ِ##Author Ghaith Tish
===================================================================================
These files have been assigned to Dynamo VisualProgramming Batteries to achieve functionality
that is not existed in the software or tfor better list management to optimize the Visual Programming script.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Note:
These scripts can only be used in Dynamo inside Autodesk Revit.
The scripts operates on Revit Families.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The Files are the following:
1_Project01.rvt
2_Cluster02.dyf
3_PanelGrouping 01.dyf

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.py Scripts Files:
1_Restructure list For 2D sorting.py: Orders the families from left to right and from top to bottom.
2_SortingGroupingKabelling.py : Sorting the families groups and creating cabels that links them to the power unite of the building.
3_ColouringPanelsByParameters.py: Coloring Panels famiies according to their group.
4_DefineStart_EndPts.py: This helps to optimize the sub cabeles length because every subcabel aims to connect either the start or the end of the group to the main cabels.
5_GroupLinesByDirection.py: This helps in defining overlaping cabels and delet them.
6_RemoveDuplicateCabels.py: Comparing cabels and delete them when they overlap based on theis start end points overlaping.
7_Assign Values to the text Parameters.py: assiging The numbering ID to every group of panels. The ID includes these three numbers a.b.c a is the main cabel, b is because each socket can take up to six groups and c is because each subsocket can take up to four groups.
8_ColouringPanelsByParameters.py: Colouring the panels according to their ID numbers.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

How to use the Program:
1_ Put the three files in the same folder so the script an locate the custer Dynamo file (Cluster02.dyf).
2_ Open the Project01.rvt.
3_ Lunch Dynamo plugin from inside Revit.
4_Open the PanelGrouping 01.dyf script and run it.
