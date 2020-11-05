import maya.cmds as cmds
import random

def RandomDuplication (selectedObj, numDuplications, minX, maxX, minY, maxY, minZ, maxZ ):
    
    for X in selectedObj:
        for N in range(numDuplications):
            cmds.duplicate(X)
                        
            cmds.move (random.randrange(minX,maxX),random.randrange(minY,maxY),random.randrange(minZ,maxZ),X)
            
        
RandomDuplication (cmds.ls(selection=True), 5, 0, 10, 0, 10, 0, 10)

RandomDuplication (cmds.ls(selection=True), 20, -10, 0, -10, 0, -10, 0)

RandomDuplication (cmds.ls(selection=True), 40, -75, 20, -20, 30, 5, 40)
