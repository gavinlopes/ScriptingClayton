import maya.cmds as cmds

def RunAutoRig(radioBtn):
    print (radioBtn)
    if radioBtn == 1:
        selected = cmds.ls(selection = True)
        parents = []
        children = []
        for i in range(0, len(selected):
            if i % 2:
                parents.append(selected[i])
            else :
                children.append(selected[i])
        for j in range(0,len(selected) / 2):
            cmds.parentConstraint(parents[j],children[j])
    if radioBtn == 2:
       selected = cmds.ls(selection = True)
       parents = []
       children = []
       for i in range(0, len(selected)):
           if i <= len()selected) / 2 -1:
           else:
               children.append(select[i])
       for j in range(0,len(selected) / 2):
           cmds.parentConstraint(parents[j],children[j])