import os, shutil
import comms_v11 as cm

def iter_copy(dest_path, argument):
	print('chiamata copy con dest path: ', dest_path)
	print('ed argument: ', argument)
	path = os.getcwd()
	pathdir = path + '/' + argument
	destpathdir = dest_path + '/' + argument
	print('destpathdir: ', destpathdir)
	
	os.chdir(dest_path)
	if argument not in os.listdir():
	    os.makedirs(argument)
	os.chdir(pathdir)
	contents = os.listdir()
	for item in contents:
	    try:
	        os.chdir(pathdir + '/' + item)
	        os.chdir(pathdir)
	        print('#\nentry in try#', item)
	        iter_copy(destpathdir, item)
	        print('#out of try#', item)
	    except:
	        print('#\ncopy file#', item)
	        print('#dest path#', destpathdir)
	        os.chdir(pathdir)
	        print(os.getcwd())
	        shutil.copy(pathdir + '/' + item, destpathdir)
	return
    	  
    	    
print(os.getcwd())
cm.ls('')
opath = os.getcwd()
cm.cd('prova')
print(os.getcwd())
cm.ls('')
inp = input()
iter_copy(opath, inp)
print('#path di partenza#')
cm.ls('')
cm.cd(opath)
cm.ls('')
    	
    	
    	
    	
    	    
    	    
	    
	    
	    
	