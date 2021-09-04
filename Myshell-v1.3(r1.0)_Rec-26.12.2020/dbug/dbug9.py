import os

def search(argument):
	list_to_scan = os.listdir()
	list_tourned = []
	
	for item in list_to_scan:
		if argument in item:
			list_tourned.append(item)
	for item in list_tourned:
		try:
			os.chdir(os.getcwd() + '/' + item)
			os.chdir(os.getcwd())
			print('- [dir] - ' + item)
		except:
			print('-  ---  - ' + item)
	