#pylint:disable=C0411
#pylint:disable=C0410
'''
	tools file script
	
	~ SUPPORT> dbug18
	- mkfile version 1.1
'''
import suphelp_v10 as shelp
import comms_v10 as cm
import getch, os

def mkwrite(title):
	texttp = ''
	if title in os.listdir():
	    file1 = open(title, 'r')
	    lines = file1.readlines()
	    for l in range (0, len(lines)):
	        string = lines[l].strip('\n')
	        texttp += string + '\n'
	    file1.close()
	else:
	    print('file created')
	try:
	    file = open(title, 'w')
	    text = texting(title, texttp)
	    file.write(text)
	    file.close()
	    print('file saved')
	except:
		print('file not saved, something is wrong')
	
def mkread(title):
	try:
		file = open(title, 'r')
	except:
		print('no file to open')
		return
	lines = file.readlines()
	print('\n<start file>')
	for l in range (0, len(lines)):
		string = lines[l].strip('\n')
		print(string)
	print('<end file>\n')
	file.close()
	
def mkappend(title):
	try:
		file1 = open(title, 'r')
		lines = file1.readlines()
		print('\n')
		for l in range (0, len(lines)):
			string = lines[l].strip('\n')
			print(string)
		file1.close()
	except:
		print('no file to open')
		return
	file = open(title, 'a')
	text = ''
	while True:
		line = input() + '\n'
		if 'EOF' in line or 'eof' in line:
			break
		text += line
	try:
		file.write(text)
		file.close()
		print('file modified and saved')
	except:
		print('no changes made, something is wrong')
		
def texting(name = 'new_text', ex_text = ''):
    text = ''
    intro = 'digit your text:\n'
    count = 0
    if ex_text != '':
        for char in ex_text:
            text += char
        count = len(ex_text)
    cm.clear('')
    print(name + '\n' + intro,text[0:count], '#')
    while True:
        inp = getch.getch()
        if inp == '\x7f': # mean canc
            count -= 1
            text = text[0:count]
        else:
            text += inp
            count += 1
        cm.clear('')
        print('file -> ' + name + '\n' + intro, text[0:count], '#')
        ex = count - 3
        if count < 0:
            count = 0
        if 'eof' in text[ex:]:
            text = text[0:ex]
            break
    return text
		
def file(inp):
	choice = inp[0:2]
	arrg = inp[3:]
	if choice == '-w' or choice == '-W':
		mkwrite(arrg) 
	elif choice == '-r' or choice == '-R':
		mkread(arrg)
	elif choice == '-a' or choice == '-A':
		mkappend(arrg)
	elif choice == '-h':
		shelp.help('file')
	elif len(choice) == 0: #imp_0.1
		print('file must have an argument\n')
		print('type file -h for know about the comands')
	else:
		print('invalid argument\n')
		print('type file -h for know about the comands')
		