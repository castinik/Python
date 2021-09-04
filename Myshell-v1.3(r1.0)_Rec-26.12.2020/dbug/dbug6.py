

def transform_size(size_value):
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
	
while True:
	byte = int(input())
	print(transform_size(byte))