import maya.cmds as cmds
import random
class RandomPlacement():
    
            
    def __init__(self):
        self.PlacementArea = "Random_Placement_Gen"
             
    def CreateWindow(self):
        
        self.DeleteWindow()
            
        self.window = cmds.window(self.PlacementArea, w = 350, h = 350, mnb = True, mxb = False, title = "Random Placement")
        self.gridLayout = cmds.gridLayout(parent = self.window, numberOfColumns = 4,numberOfRows = 5, cellWidthHeight = (75,50), cr = True)
        
        cmds.text(parent = self.gridLayout, label = "" )
        cmds.text(parent = self.gridLayout, label = "Amount" )
        self.numOfDup = cmds.intField(parent = self.gridLayout)
        cmds.text(parent = self.gridLayout, label = "" )
        
        cmds.text(parent = self.gridLayout, label = "xMin")
        self.xMin = cmds.floatField(parent = self.gridLayout)
        cmds.text(parent = self.gridLayout, label = "xMax")
        self.xMax = cmds.floatField(parent = self.gridLayout)
        
        cmds.text(parent = self.gridLayout, label = "yMin")
        self.yMin = cmds.floatField(parent = self.gridLayout)
        cmds.text(parent = self.gridLayout, label = "yMax")
        self.yMax = cmds.floatField(parent = self.gridLayout)
        
        cmds.text(parent = self.gridLayout, label = "zMin")
        self.zMin = cmds.floatField(parent = self.gridLayout)
        cmds.text(parent = self.gridLayout, label = "zMax")
        self.zMax = cmds.floatField(parent = self.gridLayout)
        
        cmds.text(parent = self.gridLayout, label = "" )
        cmds.button(parent = self.gridLayout, label = "Execute", command = lambda * x: self.GetUserInfo())
        cmds.button(parent = self.gridLayout, label = "Cancel", command =('cmds.deleteUI(\"' + self.window +'\", window=True)'))
        
        cmds.showWindow(self.window)
    
    def GetUserInfo(self):
        
        minXValue = cmds.floatField(self.xMin, query = True, value = True)
        maxXValue = cmds.floatField(self.xMax, query = True, value = True)
        minYValue = cmds.floatField(self.yMin, query = True, value = True)
        maxYValue = cmds.floatField(self.yMax, query = True, value = True)
        minZValue = cmds.floatField(self.zMin, query = True, value = True)
        maxZValue = cmds.floatField(self.zMax, query = True, value = True)
        
        NumofDuplications = cmds.intField(self.numOfDup, query = True, value = True)
        RandomDuplication(minXValue, maxXValue, minYValue, maxYValue, minZValue, maxZValue, NumofDuplications)  
        
    def DeleteWindow(self):
        if cmds.window(self.PlacementArea, exists = True):
            cmds.deleteUI(self.PlacementArea)
            
    def RandomDuplication(self, minX, maxX, minY, maxY, minZ, maxZ, numDuplications):
        selecetedObj = cmds.ls(selection = True)
        for X in selectedObj:
            for N in range(numDumplications):
                cmds.duplicate(X)
                
                cmds.move (random.randrange(minX,maxX),random.randrange(minY,maxY), random.randrange(minZ,maxZ),X)
        
            
UI = RandomPlacement()
UI.CreateWindow()