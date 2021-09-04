import socket

def ip(inp = ''):
    print('def ip\ninput |' + inp + '|')
    commands = {'-url' : url,
    '-my' : myip,
    }
    count = 0
    choice = ''
    print('ip#1')
    if inp == '':
        print('ip must have an argument')
        return
    for char in inp:
        if char != ' ':
            print('for#')
            choice += char
            count += 1
        else: break
    arrg = inp[count + 1:]
    if arrg != '':
        print('arrg not None')
    print('|' + choice + '|') 
    print('|' + arrg + '|')
    try:
        try:
            commands[choice](arrg)
        except:
            commands[choice]()
    except:
        return 

def url(argument): #  dbug11
    print('def url\n')
    if argument == '':
        print('ipurl must have an argument')
        return
    try:
        ip = socket.gethostbyname('www.' + argument)
        print('url\'s ip: ' + ip)
    except:
        print('invalid argument')
        return

def myip():
    print('def myip\n')
    try:
        s = socket.socket(socket.AF_INET,            socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        print(s.getsockname()[0])
        s.close()
    except:
        print('can\'t get ip')