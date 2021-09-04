'''
	install script
	
	- completes the functionality of myShell
'''
	
import os
from subprocess import call

def install():
	counter_str_logpath = 1
	# installing requirements library
	try:
		print('installing requirements...')
		requirements()
	except Exception as e:
		print('\nERROR: install: ', e, '\n')
	# creation of start file 'myshell.txt'
	file = open('myshell.sh', 'w')
	file.write(shabang + '\npython \'' + install_path + '/myshell_v10.py\'')
	file.close()
	print('myshell.sh created...')
	try:
		call(['chmod', '+x' , 'myshell.sh'])
		print('guaranteed execution permits...')
	except Exception as e:
		print('\nERROR: install: ', e, '\n')
		print('no guaranteed execution permits...\nyou must set permission manually')
	# updating the current variable of myShell
	try:
		mod_var()
		print('variable on file\'s system updated...')
	except Exception as e:
		print('\nERROR: install mod_var: ', e, '\n')
		print('myShell has incomplete functionality')
	print('myshell is ready to start')
	
	
def mod_var():
	os.chdir(install_path)
	counter_service = 0
	for pyfile in list_file:
		counter_line = 0
		# save on list the file's contents
		file = open(pyfile, 'r')
		text = file.readlines()
		file.close()
		# find the right variable 
		for line in text:
			if 'path_file = ' in line[:12]:
				text[counter_line] = 'path_file = \'' + log_path + list_service [counter_service] + '\'\n'
			counter_line += 1
		# write on the file 
		file = open(pyfile, 'w')
		for line in text:
			file.write(line)
		file.close()
		counter_service += 1


def requirements():
	try:
		file = open(log_path + '/requirements.txt')
		text = file.readlines()
		file.close()
	except Exception as e:
		print('\nERROR: install requirements: ', e, '\n')
		return
	for line in text:
		try:
			call(['pip', 'install', line])
		except Exception as e:
			print('\nERROR: install requirements: ', e, '\n')
		

# all service file are put here
list_service = ['/svpath.txt', '/help.txt']
# all file that need support are put here
#  with the variable 'file_path' prewrited
list_file = ['comms_v10.py', 'suphelp_v10.py']

shabang = '#!/usr/bin/sh'
# path of myshell program
install_path = os.getcwd()	
# path of log folder
log_path = install_path + '/log'

install()