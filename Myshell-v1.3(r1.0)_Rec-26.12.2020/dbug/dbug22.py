import os
import comms_v11 as cm

def rmdir_not_empty(argument):
    path = os.getcwd()
    pathdir = path + '/' + argument
    if len(argument) != 0:
        os.chdir(pathdir)
        contents = os.listdir()
        for item in contents:
            try:
                os.chdir(pathdir + '/' + item)
                os.chdir(pathdir)
                rmdir_not_empty(item)
                os.rmdir(pathdir + '/' + item)
            except:
                os.chdir(pathdir)
                os.remove(pathdir + '/' + item)
                
        
cm.ls('')
inp = input()
rmdir_not_empty(inp)
cm.rmdirectory(inp)
cm.ls('')


                