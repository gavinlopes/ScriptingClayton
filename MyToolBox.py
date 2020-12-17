import maya.cmds as cmds

class MyToolBoxUI():
    
    def __init__(self):
        self.my_window = "MyToolBox"
    def DeleteSelf(self):
        if cmds.window(self.my_window, exists = True):
           cmds.deleteUI(self.my_window)
    def CreateWindow(self):
        self.DeleteSelf()
        
        self.my_window = cmds.window(self.my_window, w = 400, h = 350, mnb = True, mxb = False, title= "Tool_Box")
        self.masterLayout = cmds.rowColumnLayout(parent=self.my_window, numberOfColumns = 1, cw = (1,400))  
        self.grid = cmds.gridLayout(parent = self.masterLayout, numberOfColumns= 1,numberOfRows = 5, cellWidthHeight = (400,50))
        cmds.button(parent = self.grid, label = "Renamer",c = lambda *x: self.LoadRenamer())
        cmds.button(parent = self.grid, label = "RPG",c = lambda *x: self.LoadAuto_Pop())
        cmds.button(parent = self.grid, label = "FreezeTransforms",c = lambda *x: self.LoadFreezeTransforms())
        cmds.button(parent = self.grid, label = "DeleteHistory",c = lambda *x: self.LoadDeleteHistory())
        cmds.button(parent = self.grid, label = "ParentGroup",c = lambda *x: self.LoadParentGroup())
        cmds.separator(parent = self.grid, height=50, style='shelf' )
        cmds.button(parent = self.grid, label = "AutoRig",c = lambda *x: self.LoadAutoRig())
        self.childParentRG = cmds.radioButtonGrp(parent= self.grid,  label='Selection Method: ', width = 400,labelArray2=['Parent then Child', 'Parents then Children'], numberOfRadioButtons=2)
        cmds.separator(parent = self.grid, height=50, style='shelf' )
        cmds.button(parent = self.grid, label = "DisplayJointRotations",c = lambda *x: self.LoadDisplayJointRotations())
        cmds.showWindow(self.my_window)
    def LoadAuto_Pop(self):
        import AutoPop_UI
        reload(AutoPop_UI)
        AutoPop_UI
    def LoadRenamer(self):
        import Renamer_UI
        reload(Renamer_UI)
        Renamer_UI
    def LoadFreezeTransforms(self):
        import FreezeTransforms
        reload(FreezeTransforms)
        FreezeTransforms.FreezeTransforms()
    def LoadDeleteHistory(self):
        import DeleteMyHistory
        reload(DeleteMyHistory)
        DeleteMyHistory.DeleteMyHistory()
    def LoadParentGroup(self):
        import ParentGroup
        reload(ParentGroup)
        ParentGroup.ParentGroup()    
    
    def LoadAutoRig(self):
        import AutoRig
        reload(AutoRig)
        selected = cmds.radioButtonGrp(self.childParentRG, q = True, select = True)
        AutoRig.RunAutoRig(selected)
        
    def LoadDisplayJointRotations(self):
        import ShowLocalAxis
        reload(ShowLocalAxis)
        ShowLocalAxis.ShowLocalAxis()
UI = MyToolBoxUI()
UI.CreateWindow()