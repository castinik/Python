import os
import mkfile_v11 as mf

favdict = {}
pathfile = '/storage/emulated/0/fileterm/MyShell/log'

def favpath(argument):
    fpath = os.getcwd()
    if argument[:3] == '-s ':
        os.chdir(pathfile)
        if 'svpath.txt' not in os.listdir():
            file = open('svpath.txt', 'w')
            file.close()
        file = open('svpath.txt', 'a')
        file.write('\n' + argument[3:] + ' as: ' + fpath)
        file.close()
        print('saved ', argument[3:], ' as: ', fpath)
        os.chdir(fpath)
    elif argument[:4] == '-ls':
        print(favdict.items())
        for item in favdict.keys():
            print(item, ' as: ', favdict[item])
        return
    elif argument[:3] == '-d ':
        favdict.pop(argument[3:])
        return
    else:
        if argument in favdict.keys():
            print(argument, ' already saved as: ', favdict[argument])
            return
        favdict[argument] = fpath
        print('saved ', argument, ' as: ', fpath)
        for item in favdict.items():
            print(item)
        return
        
while True:
    favpath(input())