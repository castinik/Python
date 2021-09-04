import socket

def ipurl(arrg):
	ip = socket.gethostbyname('www.' + arrg)
	print(ip)



while True:
	hostname = input()
	ipurl(hostname)