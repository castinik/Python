import os


pathpc = 'C:\\Users\\Utente\\Documents\\Programmazione\\Python\\Programmi\\MyShell\\help'
pathmb = '/storage/emulated/0/fileterm/MyShell/help'


commands = {'stdhelp' : '#eoa001#', 'mkfil' : '#eoa001#eoa002#','mvitem' : '#eoa002#eoa003#', 'echo' : '#eoa003#oea004#', 'ls' : '#eoa004#eoa005'}

def help(argument): #  dbug12
	path = os.getcwd()
	eoarg = commands[argument]
	flag = False
	try:
		os.chdir(pathpc)
		file = open(pathpc + '\\help.txt')
	except:
		pass
	try:
		os.chdir(pathmb)
		file = open(pathmb + '/help.txt')
	except:
		pass
	os.chdir(path)
	lines = file.readlines()
	for nline in range(0, len(lines)):
		string = lines[nline].strip()
		if string == eoarg[0:8]: # start help
			flag = True
		if flag == True:
			try:
				string = lines[nline + 1].strip() #to avoid '#eoa#'
				if string == eoarg[7:]: # stop help
				    break
				print('stop help')
				print(string)
			except:
				pass
	file.close()