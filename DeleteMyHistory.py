import maya.cmds as cmds

def DeleteMyHistory():
    selection = cmds.ls(selection = True)
    for items in selection
        cmds.delete(ch = True)