import maya.cmds as cmds


class renamer_UI():

    def __init__(self):
    
        self.my_window = 'superAwesomeCoolWindow'
    
    
    def CreateWindow(self):
    
        self.delete()
        
        self.my_window = cmds.window( self.my_window, title="Incremental Renamer", widthHeight=(300, 150))
        
        self.grid_Layout = cmds.gridLayout(parent = self.my_window, numberOfColumns=2,
        
        cellWidthHeight=(150, 25), autoGrow = True, allowEmptyCells = True)
        
        cmds.text(parent = self.grid_Layout, label = "Enter new name", height = 75)
        
        cmds.text(parent = self.grid_Layout, label="e.g. Arm_##_Jnt", height = 75)
        
        self.userInput = cmds.textField(parent = self.grid_Layout, placeholderText = 'Name of new object...')
        
        cmds.button(parent = self.grid_Layout, label = 'Rename', c = lambda * x: self.getUserInput())
        
        cmds.button(parent = self.grid_Layout, label='Close',
        
        command=('cmds.deleteUI(\"' + self.my_window + '\", window=True)') )
        
        cmds.showWindow(self.my_window)
    
    def getUserInput(self):
    
        field_value = cmds.textField(self.userInput, q = True, text = True)
        
        Rename(self, field_value)
    
    def delete(self):
    
        if cmds.window(self.my_window, exists = True):
        
            cmds.deleteUI(self.my_window)
    
    def Rename(self,name):
    
        counter = 1
        
        num_of_char = name.count('#')
        
        string_parts = name.partition('#' * num_of_char)
        
        if string_parts[1]:
    
            numberSelected = cmds.ls(selection = True)
            
            rename_list = list(string_parts)
            
            for item in numberSelected:
        
                rename_list[1] = str(counter)
                
                rename_list[1] = rename_list[1].zfill(num_of_char)
                
                cmds.rename(item, (rename_list[0] + rename_list[1] + string_parts[2] ))
                
                counter += 1
        
            else:
    
                cmds.error("Characters are not sequential. input another string.")

ui = renamer_UI()

ui.CreateWindow()