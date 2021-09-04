import os
import comms_v11 as cm
import getch


def texting(ftop = 'newfile.txt'):
    text = ''
    count = 0
    while True:
        inp = getch.getch()
        if inp == '\x7f':
            count -= 1
            text = text[0:count]

        else:
            text += inp
            count += 1
        os.system('clear')
        print(text[0:count], '#')
        

texting()
        