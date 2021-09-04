#pylint:disable=C0301
import os
import sys
import comms_v11 as cm
import mkfile_v11 as mf
import suphelp_v10 as shelp


print('Welcome in myshell!\nversion 1.2\n\nType h or help for know about the commands\n')

def catch():
	commands = {'mv' : cm.mv, 'ex' : ex, 'mkfil' : mf.file, 'mkdir' : cm.mk, 'rmdir' : cm.rmdirectory, 'rmfil' : cm.rmfile, 'ls' : cm.ls, 'cd' : cm.cd, 'color' : cm.color , 'h' : shelp.case, 'help' : shelp.case}
	choice = ''
	x = 0
	path = os.getcwd()
	inp = input(path + '>')
	print('len input ', len(inp))
	while choice not in commands and len(inp) != 0:
		choice = inp[0:x]
		tab = inp[x:x+1]
		argument = inp[x+1:]
		print('inp [', x, ']' + choice + '-tab>' + tab + '|' + '-argument>' + argument + '|') #Check
		if x > len(inp):
			break
		x += 1
	print('choice ', choice)
	if choice in commands and tab not in (' ', ''):
		print('invalid sintax')
		return
	if len(inp) != 0 and choice not in commands:
		print('command \'' + inp + '\' not found')
		return
	print('input ' + inp)
	if inp == '':
			return
	try:
		try:
			commands[choice](argument)
		except:
			commands[choice]()
	except:
		pass
	return choice

def ex():
	print('bye bye!')
	
while True:
	exit = catch()
	if exit == 'ex':
		break
	catch()
