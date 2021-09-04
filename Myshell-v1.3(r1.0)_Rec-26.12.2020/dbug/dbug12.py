import os

pathpc = 'C:\\Users\\Utente\\Documents\\Programmazione\\Python\\Programmi\\MyShell\\help'
pathmb = '/storage/emulated/0/fileterm/MyShell/help'

def standard_help(arrg):
	flag = False
	path = os.getcwd()
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
		if string == '#eoa#':
			flag = True
		if flag == True:
			try:
				string = lines[nline + 1].strip() #to avoid '#eoa#'
				print(string)
			except:
				pass
	file.close()

while True:
	standard_help(input())