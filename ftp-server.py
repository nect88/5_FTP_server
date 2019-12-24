import socket
import os
import shutil
import time

PORT = 9049

def process(req):

    if req == 'look': 
        return '; '.join(os.listdir())

    elif req == 'mkdir': #sozdanie papka
	
        name=conn.recv(1024).decode()
        try:
        	print(name)
        	os.mkdir(name)
        	return "OK"
        except:
            return "Fail"
 #delite papka   
    elif req == 'deldir':
	
        name1=conn.recv(1024).decode()
        try:
            print(name1)
            os.rmdir(name1)
            return "OK"
        except:
            return "Fail"
    elif req == 'delfile':
    		
        name2=conn.recv(1024).decode()
        try:
            print(name2)
            os.remove(name2)
            return "OK"
        except:
            return "Fail"
    elif req == 'renamefile':
	
        name3=conn.recv(1024).decode()
        name4=conn.recv(1024).decode()
        try:
            print(name3,name4)
            os.rename(name3,name4)
            return "OK"
        except:
            return "Fail"
    elif req == 'copycs':
        print(1)
        data=conn.recv(1024).decode()
        
        msg = data.split("\n")
        #while data:
        #    data=conn.recv(1024).decode()
        #    msg += data
        name=msg[0]
        print(name, msg)
        try:
            f= open(name,'w')
            print(name)
            for line in msg:
        	    if (line!=msg[0]):
        		    f.write(line+"\n")
            f.close()
            return 'ok'
        except:
            return 'fail'
    elif req == 'copysc':
        print(1)
        name=conn.recv(1024).decode()
        print(name)
        f=open(name,'r')
        for line in f:
            conn.send(line.encode())
        f.close()
        time.sleep(1)
        return ''
    elif req == 'exit':
        conn.close()
    else:
        return 'bad request'

sock = socket.socket()
sock.bind(('', PORT))
sock.listen()

while True:
    print("Port:",PORT)
    conn, addr = sock.accept()
    print(addr)

    request = conn.recv(1024).decode()
    print(request)
    response = process(request)
    conn.send(response.encode())

sock.close()
