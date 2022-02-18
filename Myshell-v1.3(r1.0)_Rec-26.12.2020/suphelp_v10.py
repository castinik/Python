'''
	help management script
	~ SUPPORT> dbug12 - dbug13 - dbug16
	- suphelp version 1.0
	- help file support: .../Myshell-v.1.0/log/help.txt
    
'''

import os


commands = {'stdhelp' : '#eoa001#',
'file' : '#eoa001#eoa002#',
'mvitem' : '#eoa002#eoa003#',
'echo' : '#eoa003#oea004#',
'ls' : '#eoa004#eoa005#',
'color' : '#eoa005#eoa006#',
'search' : '#eoa006#eoa007#',
'cp' : '#eoa007#eoa008#',
'cat' : '#eoa008#eoa009#',
'rmdir' : '#eoa009#eoa010#',
'svpath' : '#eoa010#eoa011#',
'cd' : '#eoa011#eoa012#',
'ip' : '#eoa012#eoa013#',
'mvt' : '#eoa013#eoa014#'}

path_file = ''


def help(argument = 'stdhelp'): 
	path = os.getcwd()
	eoarg = commands[argument]
	flag = False
	try:
		file = open(path_file)
	except Exception as e:
		print('\nERROR: suphelp help: ', e, '\n')
		return
	lines = file.readlines()
	for nline in range(0, len(lines)):
		string = lines[nline].strip()
		if string == eoarg[0:8] or eoarg == '#eoa001#': # start help
		    flag = True
		if flag == True:
			try:
				string = lines[nline + 1].strip() #to avoid '#eoa#'
				if string != eoarg[7:] and string != '#eoa001#': # stop help
				    print(string)
				else:
				    break
			except:
				pass
	file.close()
