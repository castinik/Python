#pylint:disable=W0612

# dbug.prova.py

import os
import subprocess as sub

for x in os.listdir():
    print(x)
inp = input()

def cat(argument):
    typef = {'py' : 'python', 'txt' : 'txt'}
    string = ''
    count = 0
    path = os.getcwd()
    for char in argument:
        count += 1
        if char == '.':
            string = argument[count:]
    
    print(typef[string])
    print(argument)
    sub.run([typef[string], argument])
    

cat(inp)