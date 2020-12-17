import maya.cmds as cmds

def ShowLocalAxis():
    selection = cmds.ls(selection = True)
    for item in selection:
        if cmds.getAttr(item + ".displayLocalAxis")== 0:
            cmds.setAttr(item + ".displayLocalAxis",1)
            cmds.setAttr(item + ".jointOrientX", channelBox = True)
            cmds.setAttr(item + ".jointOrientY", channelBox = True)
            cmds.setAttr(item + ".jointOrientZ", channelBox = True)
            cmds.setAttr(item + ".displayLocalAxis", channelBox = True)
        else:
            cmds.setAttr(item + ".displayLocalAxis",0)
            cmds.setAttr(item + ".jointOrientX", channelBox = False)
            cmds.setAttr(item + ".jointOrientY", channelBox = False)
            cmds.setAttr(item + ".jointOrientZ", channelBox = False)
            cmds.setAttr(item + ".displayLocalAxis", channelBox = False)
            
            
            
            
       