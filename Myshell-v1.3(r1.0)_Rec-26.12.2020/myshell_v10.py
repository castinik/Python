#pylint:disable=C0410
#pylint:disable=C0103
#pylint:disable=C0301
#pylint:disable=W0150
#pylint:disable=C0303
'''
	main shell script
	
	~ SUPPORT> dbug8 - dbug10 - dbug14
	- myshell version 1.0
'''
import os, time, sys
import comms_v10 as cm
import mkfile_v10 as mf
import suphelp_v10 as shelp
import net_v10 as net


version = '1.0'
time = time.ctime()
system = sys.platform

count = 0
flag = True
inp = ''

commands = {'mvt': cm.mvt,
'net': net.net,
'echo': cm.echo,
'file': mf.file,
'mkdir': cm.mk,
'rmdir': cm.rmdirectory,
'mvitem': cm.move,
'cp' : cm.copy,
'rmfile': cm.rmfile,
'pwd': cm.pwd,
'src': cm.search,
'ls': cm.ls,
'cd': cm.cd,
'color': cm.color,
'cl': cm.clear,
'cat': cm.cat,
'svpath' : cm.favpath,
'h': shelp.help,
'help': shelp.help,
'ex': 'ex'}

cm.clear('')
print('< < < < myShell > > > >\n\n-', time,'\n- version -', version,'\n- system -', system, '\n\nType h or help for know about the commands\n')


def catch(inp, flag = True):
	x = 0
	choice = ''
	argument = ''
	tab = ''
	if inp in commands:
		choice = inp
	else:
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
	if choice == 'ex':
		print('---- bye bye ----')
		return		
	try:
		try:
			returned = commands[choice](argument)
		except:
			returned = commands[choice]()
		finally:
			try:
				if returned == True or returned == False:
					return returned
				else:
					return flag
			except Exception as e:
				pass	
	except Exception as e:
	    print('\nERROR: Unhandled Exception: ', e, '\n')
	    return flag


while True:
	flag = catch(inp, flag)
	if flag == True:
		inp = input(os.getcwd() + '>')
	elif flag == False:
		inp = input('>')
	elif flag == None:
		break
