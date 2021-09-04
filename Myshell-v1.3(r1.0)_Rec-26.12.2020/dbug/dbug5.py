import os

def makesize():
	bytesize = 0
	path = os.getcwd()
	contents = os.listdir()
	for file in contents:
		print(path)
		try:
			print('p1')
			os.chdir(path + '/' + file)
			print('p2')
			print('entry in directory')
			byte = makesize()
			print('byte in underfolder ', byte)
			bytesize += byte
		except:
			try:
				bytesize = (os.path.getsize(os.getcwd() + '/' + file) + bytesize)
				print('file singolo ' + file, os.path.getsize(os.getcwd() + '/' + file))
				print('totale',bytesize)
			except:
				print('pass of file ' + file)
	print('byte returned ', bytesize)
	return bytesize
			
while True:
	print(makesize())
	a = input()