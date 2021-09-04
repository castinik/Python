
def func_tab2(argument):
	
	max = 6 
	tab = ''
	val = max - len(argument)
	size = str(argument) + (' ' * val)
	return size
	
def func_size(argument):
	max = 6
	tab = ''
	word = ''
	if argument >= 1024:
		new_arg = round(argument / 1024)
		word = 'Kbyte '
	else:
		new_arg = argument
		word = 'byte  '
	arg = str(new_arg)
	val = max - len(arg)
	size = '> ' + str(new_arg) + (' ' * val) + word
	return size
	
while True:
	word = int(input())
	tab = func_size(word)
	print(tab + '- [  -  ] - ' + ' name file/dir')
