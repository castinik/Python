import time

n = 0
charging = []
MAX = 30
string = '#'
for i in range(1, MAX):
    print(string * i, ' ' * (MAX - 1 - i))
    charging.append(string * i + ' ' * (MAX - 1 - i))
    
print(charging)

for x in range(0,100):
    s = 'listing ' + charging[n] + '\r'
    print(s, end='')
    time.sleep(0.1)
    n += 1
    if n == MAX - 1:
    	n = 0