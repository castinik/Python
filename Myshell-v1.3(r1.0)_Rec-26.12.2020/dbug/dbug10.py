import os
import comms_v11 as cm
import mkfile_v11 as mf
import suphelp_v10 as shelp


print('Welcome in myshell!\nversion 1.2\n\nType h or help for know about the commands\n')

#choice = ''
#argument = ''
#tab = ''
#inp = ''
#entry = True
count = 0


commands = {'mv' : cm.mv, 'echo' : 'echo', 'mkfil' : mf.file, 'mkdir' : cm.mk, 'rmdir' : cm.rmdirectory, 'rmfil' : cm.rmfile, 'pwd' : cm.pwd, 'src' : cm.search , 'ls' : cm.ls, 'cd' : cm.cd, 'color' : cm.color , 'h' : shelp.case, 'help' : shelp.case}

def catch(inp, flag):	
	x = 0
	choice = ''
	argument = ''
	tab = ''
	while choice not in commands and len(inp) != 0:
		choice = inp[0:x]
		tab = inp[x:x+1]
		argument = inp[x+1:]
		if x > len(inp):
			break
		x += 1
	print('inp ' + inp + 'choice ' + choice + 'argument ' + argument)
	if choice in commands and tab not in (' ', ''):
		print('invalid sintax')
		return
	elif choice == 'echo' and argument == 'on':
		start(True)
	elif choice == 'echo' and argument == 'off':
		flag = False
		start(False)
	if len(inp) != 0 and choice not in commands:
		print('command \'' + inp + '\' not found')
		return
	if inp == '':
		start(flag)
		print('inp == \'\' flag ', flag)
		return
	try:
		try:
			commands[choice](argument)
			start(flag)
		except:
			commands[choice]()
			start(flag)
	except:
		pass
	return
	
def start(arrg):
	flag = arrg
	if flag == True:
		inp = input(os.getcwd() + '>')
		catch(inp, flag)
	elif flag == False:
		inp = input('>')
		catch(inp, flag)
	return flag
	
while True:
	if count == 0:
		count += 1
		state = start(True)
		print('if', state)
	else:
		state = start(state)
		print('else', state)
		