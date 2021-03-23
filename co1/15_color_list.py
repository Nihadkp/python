# printout all colors from color list 1 not contained in color list 2
color_list_1=["gold","silver","yellow","orange","red","white"]
color_list_2=["green","black","grey","maroon","violet","red"]
print([i for i in color_list_1 if i not in color_list_2])