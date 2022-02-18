'''
	main commands script
	
	- comms version 1.0
'''
import os, sys, shutil
import subprocess as sub
import suphelp_v10 as shelp

path_file = ''


def mvt(argument):
	if len(argument) != 0:
		if argument == '-h':
			shelp.help('mvt')
			return
		npath = argument
		try:
			os.chdir(npath)
		except:
			print('no path found')
	else:
		print('mvt must have an argument')
		
		
def mk(argument):
	if len(argument) != 0:
		try:
			os.makedirs(argument)
			print('created directory')
		except:
			print('directory not created')
	else:
		print('mkdir must have an argument')


def rmdirectory(argument): #  dbug22
		path = os.getcwd()
		if argument[:3] == '-h':
		    shelp.help('rmdirectory')
		    return
		if argument[:3] == '-a ':
		    iter_rmdir(argument[3:])
		    dir_path = path + '/' + argument[3:]
		    os.rmdir(dir_path)
		    print('removed directory not empty')
		    os.chdir(path)
		    return
		if len(argument) != 0:
			if argument not in os.listdir():
			    print('no directory to remove')
			    return
			dir_path = path + '/' + argument
			try:
				os.rmdir(dir_path)
				print('removed directory')
			except:
				print('directory is not empty')
		else:
			print('rmdir must have an argument')


def rmfile(argument):
		path = os.getcwd()
		file_path = path + '/' + argument
		if len(argument) != 0:
			try:
				os.remove(file_path)
				print('file removed')
			except:
				print('no file to remove')
		else:
			print('rmfile must have an argument')
			
			
def ls(argument):
	path = os.getcwd()
	listed = {}
	supportlist = []
	if argument == '-h':
		shelp.help('ls')
		return
	try:
		list = os.listdir()
	except Exception as e:
		print('\nERROR: comms ls: ', e, '\n')
		return
	if len(list) == 0:
	    print('nothing to list')
	    return
	try:
	    if argument == '-s':
	        ls_size(list)
	    else:
	        print('\n')
	        for x in list:
	            try:
	                new_path = path + '/' + x
	                os.chdir(new_path)
	                os.chdir(path)
	                string = '- [dir] - ' + x
	                listed[x] = string
	                supportlist.append(x)
	            except:
	                string = '-  ---  - ' + x
	                listed[x] = string
	                supportlist.append(x)
	        supportlist.sort()
	        for x in range(0, len(supportlist)):
		        keys = supportlist[x]
		        print(listed.get(keys))
	        print('\n')
	except Exception as e:
	    print('\nERROR: comms ls: ', e, '\n')


def ls_size(list):
	path = os.getcwd()
	byte_size = 0
	listed = {}
	supportlist = []
	print('\n')
	for x in list:
		try:
			new_path = path + '/' + x
			os.chdir(new_path)
			byte_size = makesize()  # dbug2
			os.chdir(path)
			value_size = transform_size(byte_size)
			string = value_size + '- [dir] - ' + x
			listed[x] = string
			supportlist.append(x)
		except:
			byte_size = os.path.getsize(path + '/' + x)
			value_size = transform_size(byte_size)
			string = value_size + '-  ---  - ' + x
			listed[x] = string
			supportlist.append(x)
	supportlist.sort()
	for x in range(0, len(supportlist)):
		keys = supportlist[x]
		print(listed.get(keys))
	print('\n')
	
	
def cd(argument):
	path = os.getcwd()
	svpatharg = '--' + argument[2:]
	try:
		file = open(path_file, 'r')
		lines = file.readlines()
		file.close()
	except Exception as e:
		print('\nERROR: comms cd: ', e, '\n')
		return
	try:
		list = os.listdir()
		if argument == '-h':
		    shelp.help('cd')
		    return
		if argument in list:
			os.chdir(path + '/' + argument)
		elif argument == svpatharg:
		    for line in range(0, len(lines)):
		        string = lines[line].strip()
		        if string[:len(argument) - 2]== argument[2:]:
		        	os.chdir(string[len(argument) + 3:])
		    return
		elif argument == "..":
			lpath = []
			x = 0
			for k in path:
				lpath.insert(x, k)
				x += 1
			path = ''
			lpath.reverse()
			for m in lpath:
				path += m
			z = 0
			for i in path:
				if '/' != i and i != '\\':
					lpath[z] = ''
				else:
					lpath[z] = ''
					break
				z += 1
			lpath.reverse()
			path = ''
			for y in lpath:
				path += y
			os.chdir(path)
		elif len(argument) == 0:
			print('cd must have an argument')
		else:
			try:
				new_path = elaborate(argument)
				os.chdir(new_path)
			except:
				print('no directory found')
	except Exception as e:
			print('\nERROR: comms cd: ', e, '\n')
			
			
def elaborate(argument): #  dbug1
	count = 0
	path = os.getcwd()
	list = os.listdir()
	list_low = []
	new_arg = argument.lower()
	for x in list:
		list_low.append(x.lower())
		if new_arg in list_low:
			new_path = path + '/' + list[count]
			return new_path
		else:
			count += 1


def makesize(): #  dbug3, dbug4, dbug5
	charging = []
	path = os.getcwd()
	contents = os.listdir()
	s_imbol = '#'
	MAX = 30
	bytesize = 0
	i = 0
	for i in range(1, MAX):
 	   charging.append(s_imbol * i + ' ' * (MAX - 1 - i))
	for file in contents:
		s = 'listing ' + charging[i] + '\r'
		print(s, end='')
		i += 1
		if i >= MAX - 1:
		    i = 0
		try:
		    os.chdir(path + '/' + file)
		    byte = makesize()
		    bytesize += byte
		except:
			try:
				bytesize = (os.path.getsize(os.getcwd() + '/' + file) + bytesize)
			except:
				pass
	return bytesize
	
	
def transform_size(size_value): #  dbug6
	kilobyte = 1000
	megabyte = 1000000
	gigabyte = 1000000000
	terabyte = 1000000000000
	max = 7
	count = 0
	tab = '' 
	string_size = ''
	if size_value >= kilobyte and size_value < megabyte:
		size_value /= kilobyte
		word = ' KB '
	elif size_value >= megabyte and size_value < gigabyte:
		size_value /= megabyte
		word = ' MB '
	elif size_value >= gigabyte and size_value < terabyte:
		size_value /= gigabyte
		word = ' GB '
	elif size_value >= terabyte:
		size_value /= terabyte
		word = ' TB '
	else:
		word = ' b  '
	list_value = list(str(size_value))
	list_size = []
	for x in list_value:
		string_size += x
		count += 1
		if count == max:
			break
	for x in range(0, max - len(string_size)):
		tab += ' '
	returned_string = string_size + tab + word
	return returned_string
	
	
def color(argument): #  dbug7
	colors = {'default' : "\x1B[0m", 'red' : "\x1B[31m", 'green' : "\x1B[32m", 'yellow' : "\x1B[33m", 'blue' : "\x1B[34m", 'pink' : "\x1B[35m", 'lightblue' : "\x1B[36m", 'white' : "\x1B[37m"}
	if argument == '-h':
	    shelp.help('color')
	    return
	elif argument == '' or argument == ' ':
	    print('color must have an argument')
	    return
	try:
		if argument in colors.keys():
			sys.stdout.write(colors[argument])
		else:
			print('No existing color')
			return
	except Exception as e:
		print('\nERROR: comms cd: ', e, '\n')
		return

				
def search(argument):
	list_to_scan = os.listdir()
	list_tourned = []
	path = os.getcwd()
	count = 0
	if argument == '-h':
	    shelp.help('search')
	    return
	if argument == '':
		print('src must have an argument')
		return
	for item in list_to_scan:
		if argument in item:
			list_tourned.append(item)
			count += 1
	if count == 0:
		print('no item found')
		return
	for item in list_tourned: # dir or not
		try:
			os.chdir(path + '/' + item)
			os.chdir(path)
			print('- [dir] - ' + item)
		except:
			print('-  ---  - ' + item)
		os.chdir(path)
			
			
def pwd(argument):
	if argument != '':
		print('pwd needs no argument')
		return	
	print(os.getcwd())


def clear(argument):
	if argument != '':
		print('cl needs no argument')
		return
	if sys.platform == 'linux':
	    try:
	        clear = os.system('clear')
	    except:
	        print('something went wrong')
	else:
		try:
		    cls = os.system('cls')
		except:
		    print('something went wrong')


def echo(argument):
	if argument == 'on':
		return True
	elif argument == 'off':
		return False	
	elif argument == '-h':
	    shelp.help('echo')
	    return
	else:
	    print(argument)
	    return 


def move(argument):
	if argument == '-h':
	    shelp.help('mvitem')
	    return
	path = os.getcwd()
	if argument == '': # exc
		print('mvitem must have an argument')
		return
	if argument not in os.listdir(): # exc 
		print('no item to move')
		return
	try:
		inp_path = input('Insert the destination path:\n')
		if inp_path[0:3] == 'cwd': # rapid option
			if inp_path[3:4] != ' ' or len(inp_path[4:]) == 0: #exc
				print('invalid sintax')
				return
			else:
			    dest_path = path + '/' + inp_path[4:]
		if inp_path[0:3] == 'bck': # rapid option
			cd('..')
			if len(inp_path[4:]) != 0:
				if inp_path[3:4] != ('', ' '): # exc
					print('invalid sintax')
					return
				else:
				    dest_path = os.getcwd() + '/' + inp_path[4:]
			else:
				dest_path = os.getcwd()
		try:
		   shutil.move(path + '/' + argument, dest_path)
		   print('item moved')
		except:
		    shutil.move(path + '/' + argument, inp_path)
		    print('item moved')
		os.chdir(path)
		return
	except:
		print('no destination path found')
		os.chdir(path)


def copy(argument):
	if argument == '-h':
	    shelp.help('cp')
	    return
	path = os.getcwd()
	if argument == '': # exc
		print('cp must have an argument')
		return
	if argument not in os.listdir(): # exc 
		print('no item to copy')
		return
	try:
		inp_path = input('Insert the destination path:\n')
		if inp_path[0:3] == 'cwd': # rapid option
			if inp_path[3:4] != ' ' or len(inp_path[4:]) == 0: #exc
				print('invalid sintax')
				os.chdir(path)
				return
			else:
			    dest_path = path + '/' + inp_path[4:]
		if inp_path[0:3] == 'bck': # rapid option
			cd('..')
			if len(inp_path[4:]) != 0:
				if inp_path[3:4] != ('', ' '): # exc
					print('invalid sintax')
					os.chdir(path)
					return
				else:
				    dest_path = os.getcwd() + '/' + inp_path[4:]
			else:
				dest_path = os.getcwd()
		try:
		   os.chdir(path)
		   iter_copy(dest_path, argument)
		   print('file copied')
		except:
		    os.chdir(path)
		    iter_copy(inp_path, argument)
		    print('file copied')
		os.chdir(path)
		return
	except:
		print('no destination path found')
		os.chdir(path)
		return
		
		
def iter_copy(dest_path, argument):
	path = os.getcwd()
	pathdir = path + '/' + argument
	destpathdir = dest_path + '/' + argument
	os.chdir(dest_path)
	if argument not in os.listdir():
	    os.makedirs(argument)
	os.chdir(pathdir)
	contents = os.listdir()
	for item in contents:
	    try:
	        os.chdir(pathdir + '/' + item)
	        os.chdir(pathdir)
	        iter_copy(destpathdir, item)
	    except:
	        os.chdir(pathdir)
	        shutil.copy(pathdir + '/' + item, destpathdir)


def cat(argument): #  dbug19, exec
    typef = {'py' : 'python',
    'txt' : 'txt',}
    string = ''
    count = 0
    if argument == '-h':
        shelp.help('cat')
        return
    if argument == '':
        print('cat must have an argument')
        return
    try:
        for char in argument:
            count += 1
            if char == '.':
                string = argument[count:]
            if '.' not in argument:
                for key in typef:
                    if argument in typef[key]:
                        sub.run([typef[key]])
                        return
        sub.run([typef[string], argument])
    except:
        try:
            print('run ', argument, '...')
            typef[string](argument[:count])
        except:
            print('impossible to run: ', argument)
        
        
def iter_rmdir(argument): #  dbug21
    path = os.getcwd()
    pathdir = path + '/' + argument
    if len(argument) != 0:
        os.chdir(pathdir)
        contents = os.listdir()
        for item in contents:
            try:
                os.chdir(pathdir + '/' + item)
                os.chdir(pathdir)
                iter_rmdir(item)
                os.rmdir(pathdir + '/' + item)
            except:
                os.chdir(pathdir)
                os.remove(pathdir + '/' + item)
     
     
def favpath(argument):
    fpath = os.getcwd()
    favdict = {}
    if argument == '-h':
        shelp.help('svpath')
        return
    if argument == '' or argument == ' ':
        print('svpath must have an argument')
        return
# > save path in file 'svpath.txt'
    if argument[:3] == '-s ':
        try:
            control_file = open(path_file, 'r')
            lines = control_file.readlines()
            control_file.close()
        except Exception as e:
            print('\nERROR: comms svpath: ', e, '\n')
            return
# control existence of argument
        for line in range(0, len(lines)):
            string = lines[line].strip()
            if argument[3:] == string[:len(argument[3:])]:
                print(argument[3:] + ' already exist as: ' + string[len(argument[3:]):])
                return 
# else save new argument as path . . .
        file = open(path_file, 'a')
        file.write('\n' + argument[3:] + ' as: ' + fpath)
        file.close()
        print('saved ', argument[3:], ' as: ', fpath)
        return
# > list path in file 'svpath.txt'
    elif argument[:5] == '-lss':
        try:
         	file = open(path_file, 'r')
         	lines = file.readlines()
         	file.close()
        except Exception as e:
         	print('\nERROR: comms svpath: ', e, '\n')
         	return
        for line in range(0, len(lines)):
            print(lines[line].strip())
        return
# > list path in dict 'favdict{}'
    elif argument[:3] == '-ls':
        for item in favdict.keys():
            print(item, ' as: ', favdict[item])
        return
# > remove path in file 'svpath.txt'
    elif argument[:4] == '-rm ':
# copy of 'svpath.txt' in list 'newlistfile' for modify the elements
        newlistfile = []
        try:
	           file = open(path_file, 'r')
	           lines = file.readlines()
	           file.close()
        except Exception as e:
            print('\nERROR: comms svpath: ', e, '\n')
            return
        for line in range(0, len(lines)):
            string = lines[line].strip()
            if string[:len(argument[3:]) - 1] != argument[4:]:
                newlistfile.append(string)
# check the existence of argument
        if len(lines) == len(newlistfile):
            print(argument[4:] + ' doesn\'t exist!')
            return
# else remove the argument and path
        file = open(path_file, 'w')
        for line in newlistfile:
            file.write(line + '\n')
        file.close()
        return
# > remove path in dict 'favdict{}'
    elif argument[:3] == '-d ':
# check the existence of argument
        if argument[3:] not in favdict:
            print(argument[3:] + ' doesn\'t exist!')
            return
# else remove the argument and path
        favdict.pop(argument[3:])
        return
# > save path in dict 'favdict{}'
    else:
# check the existence of argument
        if argument in favdict.keys():
            print(argument, ' already saved as: ', favdict[argument])
            return
# save the argument 
        favdict[argument] = os.getcwd()
        print('saved ', argument, ' as: ', os.getcwd())
 
