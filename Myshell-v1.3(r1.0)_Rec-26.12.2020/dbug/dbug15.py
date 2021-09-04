import os

def ls(argument):
	path = os.getcwd()
	byte_size = 0
	listed = {}
	supportlist = []
	if len(argument) != 0:
		print('ls needs no argument')
		return
	try:
		print('\n')
		list = os.listdir()
		for x in list:		
			try:
				new_path = path + '/' + x
				os.chdir(new_path)
				byte_size = makesize()  # dbug2
				os.chdir(path)
				value_size = transform_size(byte_size)
				string = value_size + '- [dir] - ' + x
			#	x = x[0:5]
				listed[x] = string
				supportlist.append(x)
			except:
				byte_size = os.path.getsize(path + '/' + x)
				value_size = transform_size(byte_size)
				string = value_size + '-  ---  - ' + x
			#	x = x[0:5]
				listed[x] = string
				supportlist.append(x)
		supportlist.sort()
		for x in range(0, len(supportlist)):
			keys = supportlist[x]
			print(listed.get(keys))
		print('\n')
	except:
		print('nothing to list')
		
		
def transform_size(size_value): #  dbug6
	kilobyte = 1000
	megabyte = 1000000
	gigabyte = 1000000000
	terabyte = 1000000000000
	max = 7
	count = 0
	tab = '' 
	string_size = ''
	if size_value >= kilobyte and size_value < megabyte:
		size_value /= kilobyte
		word = ' KB '
	elif size_value >= megabyte and size_value < gigabyte:
		size_value /= megabyte
		word = ' MB '
	elif size_value >= gigabyte and size_value < terabyte:
		size_value /= gigabyte
		word = ' GB '
	elif size_value >= terabyte:
		size_value /= terabyte
		word = ' TB '
	else:
		word = ' b  '
	list_value = list(str(size_value))
	list_size = []
	for x in list_value:
		string_size += x
		count += 1
		if count == max:
			break
	for x in range(0, max - len(string_size)):
		tab += ' '
	returned_string = string_size + tab + word
	return returned_string
	
def makesize(): #  dbug3, dbug4, dbug5
	bytesize = 0
	path = os.getcwd()
	contents = os.listdir()
	for file in contents:
		try:
			os.chdir(path + '/' + file)
			byte = makesize()
			bytesize += byte
		except:
			try:
				bytesize = (os.path.getsize(os.getcwd() + '/' + file) + bytesize)
			except:
				pass
	return bytesize
	
while True:
	ls('')
	imp = input()