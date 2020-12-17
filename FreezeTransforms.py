import maya.cmds as cmds

def FreezeTransforms():
    selection = cmds.ls(selection = True)
    for items in selection
        cmds.FreezeTransformations(0)
    