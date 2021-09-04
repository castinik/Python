import os
import comms_v11 as cm
import mkfile_v11 as mf
import suphelp_v10 as shelp


print('< < < < myShell > > > >\n\nversion 1.2\ndbug14\n\nType h or help for know about the commands\n')
count = 0
flag = True
inp = ''
commands = {'mv': cm.mv, 'ipurl': cm.ipurl, 'echo': 'echo', 'mkfil': mf.file, 'mkdir': cm.mk, 'rmdir': cm.rmdirectory, 'rmfil': cm.rmfile, 'pwd': cm.pwd, 'src': cm.search, 'ls': cm.ls, 'cd': cm.cd, 'color': cm.color, 'cl': cm.clear, 'h': shelp.standard_help, 'help': shelp.standard_help, 'ex': 'ex', 'p': cm.prova}

def catch(inp, flag):
	x = 0
	choice = ''
	argument = ''
	tab = ''
	while choice not in commands and len(inp) != 0:
		choice = inp[0:x]
		tab = inp[x:x + 1]
		argument = inp[x + 1:]
		if x > len(inp):
			break
		x += 1
	if choice in commands and tab not in (' ', ''):
		print('invalid sintax')
		return flag
	if len(inp) != 0 and choice not in commands:
		print('command \'' + inp + '\' not found')
		return flag
	if inp == '': 
		return flag
	if choice == 'echo' and argument == 'on':
		return True
	elif choice == 'echo' and argument == 'off':
		return False
	if choice == 'ex': 
		return
	try:
		try:
			commands[choice](argument)
			return flag
		except:	
			commands[choice]()
			return flag
	except:
		print('\nERROR: Unhandled Exception\n')
		return flag

while True:
	flag = catch(inp, flag)
	if flag == True:
		inp = input(os.getcwd() + '>')		
	elif flag == False:
		inp = input('>')
	elif flag == None:
		break
	