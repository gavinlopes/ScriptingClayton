#Turns maya's MEL code into Python
import maya.cmds as cmds
#Define the function "Rename" takes an argument (variable) "name" which is a string but can be any data type.
def Rename(name):
    #Start the list at 1 when renaming
    counter = 1
    #Searching the string for pound sign and assigning the num it finds to num of char.    
    num_of_char = name.count('#')
    #create a tupel w/ 3 parts. and assign to string_parts ex_'L_Arm_', '##', '_Jnt'
    #String_parts[0] = 'L_Arm_'
    #String_parts[1] = '##' 
    #String_parts[2] = '_Jnt'     
    string_parts = name.partition('#' * num_of_char)
    
    #if there is something in string_parts[1] run the following code.    
    if string_parts[1]:
        #Grab the number of obj in maya scene and put them in num selected variable.
                
        numberSelected = cmds.ls(selection = True)
        #Taking the tuple string_parts and convert into list and store list in rename_list.   
        rename_list = list(string_parts)
        #For each item in the list num selected. Run the following code. 
        for item in numberSelected:
            #Taking our list from tuple and changing index one from # to counter num.
            #str(counter) Converting counter from int to string.
            rename_list[1] = str(counter)
            #Zfill takes an int (num_of_char) and puts that many zeros in front of what ever value
            #...is in rename_list[1] and then we assign it back to itself.
            rename_list[1] = rename_list[1].zfill(num_of_char)
            #From here we pull maya.cmds.rename. Rename take an obj and string
            #Because we are in a for in loop we use item as obj and then because name is
            #...contained in list we need to concatanant the list.(rename_list[0] + rename_list[1] + string_parts[2] )
            cmds.rename(item, (rename_list[0] + rename_list[1] + string_parts[2] ))
            #Updating the counter because if we have more than one item selected we need it to change into num 2 and so forth.
            counter += 1
            
   #If there is nothing in string_parts[1] then run the following code and 
   #And send user an Error. 
    else:   
        cmds.error('Characters are not sequential. input another string.')
  
    
#Run Function Rename and pass string argument.
Rename('L_Arm_##_Jnt')

import maya.cmds as cmds

window = cmds.window( title="Jnt Renamer", widthHeight=(200, 55) )
cmds.columnLayout( adjustableColumn=True )
cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'both', 0), columnWidth=[(1, 350), (2, 200)] )
cmds.text( label='Name' )
userInput = cmds.textField()

cmds.button( label='Rename' )
cmds.button( label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)') )
cmds.setParent( '..' )
cmds.showWindow( window )
