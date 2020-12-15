import maya.cmds as cmds

class MyToolBoxUI():

    def __init__(self):
        self.my_window = "ToolBox"
        
    def DeleteSelf(self):
        if cmds.window(self.my_window, exists = True):
           cmds.deleteUI(self.my_window)
    def CreateWindow(self):
        self.DeleteSelf()

        self.my_window = cmds.window(self.my_window, w = 350, h = 350, mnb = True, mxb = False, title= "Tool_Box")
        self.grid = cmds.gridLayout(parent = self.my_window, 
        numberOfColumns= 1,numberOfRows = 5, cellWidthHeight = (75,50))
        cmds.button(parent = self.grid, label = "Renamer",c = lambda * x: self.LoadRenamer())
        cmds.button(parent = self.grid, label = "RPG",c = lambda * x: self.LoadAuto_Pop())
        cmds.showWindow(self.my_window)
        
    def LoadAuto_Pop(self):
        import AutoPop_UI
        reload(AutoPop_UI)
        AutoPop_UI.UI.CreateWindow()
        
    def LoadRenamer(self):
        import Renamer_UI
        reload(Renamer_UI)
        Renamer_UI.ui.CreateWindow()
        
UI = MyToolBoxUI()
UI.CreateWindow()
        
    
        