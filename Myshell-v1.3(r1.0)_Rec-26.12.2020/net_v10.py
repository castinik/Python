'''
	tools network script
	
	~ SUPPORT> dbug20
	- net version 1.0
'''
import socket
import subprocess as sub
import suphelp_v10 as shelp
import netifaces as ni
import scapy.all as scapy



def net(inp = ''):
    commands = {'-url' : url,
    '-my' : myip,
    '-conf' : config,
    '-netscan' : netscan
    }
    count = 0
    result = 0
    choice = ''
    if inp == '-h':
        shelp.help('ip')
        return
    if inp == '':
        print('ip must have an argument')
        return   		
    for char in inp:
        if char != ' ':
            choice += char
            count += 1
        else: break
    arrg = inp[count + 1:]
    try:
        try:
            commands[choice](arrg)
        except:
            commands[choice]()
    except:
        return 

def url(argument): #  dbug11
    if argument == '':
        print('ip -url must have an argument')
        return
    try:
        ip = socket.gethostbyname('www.' + argument)
        print('url\'s ip: ' + ip)
    except:
        print('invalid argument')
        return


def myip():
    try:
        s = socket.socket(socket.AF_INET,            socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        print('local ip: ', ip)
        #print(socket.gethostbyaddr(ip)[0])
        s.close()
    except:
        print('can\'t get ip')
        
        
def config(argument = ''): 
    if argument == 'hwinfo':
        nif = ni.interfaces()
        for scheda in nif:
        	diz_ind = ni.ifaddresses(scheda)
        	passed = False
        	if ni.AF_PACKET in diz_ind.keys():
        		mac_addr = diz_ind[ni.AF_PACKET][0]['addr']
        		for elem in mac_addr.split(':'):
        			if elem != '00':
        				passed = True
	        			break
        	if passed:
        		print('Scheda', scheda,
	    	      '- MAC addr. :', diz_ind[ni.AF_PACKET][0]['addr'])
        		if ni.AF_INET in diz_ind.keys():
	        		for ind in diz_ind[ni.AF_INET]:
	        			print('Indirizzo IP :', ind['addr'])
        return
    if argument != '':
        argument = ' ' + argument
    try:
        print(sub.call('ifconfig' + argument, shell=True))
        return
    except Exception as e:
        print('\nERROR: ', e, '\n')
        

def netscan(ip):
    if ip == '':
    	print('ip -netscan must have an argument')
    	return
    print('#check')
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    clients_list = []
    print('#check')
    printresult(answered_list)
	   	
def printresult(answered_list):
	clients_list = []
	for element in answered_list:
		clients_dict = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
		clients_list.append(clients_dict)
	print('\n IP\t\t\tMAC Address\n-------------------------------------------')
	for client in clients_list:
	    print(client['ip'] + '\t|\t' + client['mac'] + ' |')
	print('-------------------------------------------\n')
     
