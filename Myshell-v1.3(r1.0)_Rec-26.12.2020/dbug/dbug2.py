import os


path = os.getcwd()
file = input()
size = os.path.getsize(path + "\\" + file)
print(size)