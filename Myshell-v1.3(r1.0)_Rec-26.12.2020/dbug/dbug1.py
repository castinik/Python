import os

path = os.getcwd()

argument = input(path + '$')

def support(argument):
	count = 0
	path = os.getcwd()
	list = os.listdir()
	list_low = []
	new_arg = argument.lower()
	for x in list:
		list_low.append(x.lower())
		if new_arg in list_low:
			new_path = path + '/' + list[count]
			return new_path
		else:
			count += 1

new_path = support(argument)
print(new_path)
os.chdir(new_path)
print(os.getcwd())