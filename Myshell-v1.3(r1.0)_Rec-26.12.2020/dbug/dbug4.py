def func_size(argument):
	max = 7
	tab = ''
	word = ''
	if argument >= 1024:
		new_arg = argument / 1024
		worked = '{:.6}'.format(new_arg)
		word = 'kB '
	else:
		new_arg = argument
		worked = argument
		word = 'b  '
	arg = str(worked)
	val = max - len(arg)
	size = '> ' + str(worked) + (' ' * val) + word
	return size
	
while True:
	att = int(input())
	print(func_size(att))