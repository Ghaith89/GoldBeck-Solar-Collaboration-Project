# GoldBeck-Solar-Collaboration-Project

The project aim is to automate repetitive tasks in roof plans for solar panels. I have collaborated with the CAD team in GoldBeck Solar in Manheim region. The project has been achieved using IronPython inside Dynamo Studio and the Revit API.
___________________________________________________________________________________
ِ**Author** Ghaith Tish

These files have been assigned to Dynamo VisualProgramming Batteries to achieve functionality
that is not existed in the software or tfor better list management to optimize the Visual Programming script.

___________________________________________________________________________________
**Note:**
These scripts can only be used in Dynamo inside Autodesk Revit.
The scripts operates on Revit Families.
___________________________________________________________________________________

**The Files are the following:**
1. Project01.rvt
2. Cluster02.dyf
3. PanelGrouping 01.dyf

___________________________________________________________________________________

**.py Scripts Files:**
1. Restructure list For 2D sorting.py: Orders the families from left to right and from top to bottom.
2. SortingGroupingKabelling.py : Sorting the families groups and creating cabels that links them to the power unite of the building.
3. ColouringPanelsByParameters.py: Coloring Panels famiies according to their group.
4. DefineStart_EndPts.py: This helps to optimize the sub cabeles length because every subcabel aims to connect either the start or the end of the group to the main cabels.
5. GroupLinesByDirection.py: This helps in defining overlaping cabels and delet them.
6. RemoveDuplicateCabels.py: Comparing cabels and delete them when they overlap based on theis start end points overlaping.
7. Assign Values to the text Parameters.py: assiging The numbering ID to every group of panels. The ID includes these three numbers a.b.c a is the main cabel, b is because each socket can take up to six groups and c is because each subsocket can take up to four groups.
8. ColouringPanelsByParameters.py: Colouring the panels according to their ID numbers.

__________________________________________________________________________________

**How to use the Program:**
1. Put the three files in the same folder so the script an locate the custer Dynamo file (Cluster02.dyf).
2. Open the Project01.rvt.
3. Lunch Dynamo plugin from inside Revit.
4. Open the PanelGrouping 01.dyf script and run it.
