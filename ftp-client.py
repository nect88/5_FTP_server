import socket

HOST = 'localhost'
PORT = 9049

while True:
    sock = socket.socket()
    sock.connect((HOST, PORT))
    print('Menu vosmojnostey:\n SMORET - look\n CREATE DIR - mkdir\n YDALIT DIR - deldir\n YDALIT FILE - delfile\n RENAME FILE - renamefile\n UPLOAD - copycs\n            DOWNLOAD - copysc\n EXIT - exit')
    request = input('myftp@shell$ ')
    sock.send(request.encode())   
    if (request == "mkdir") or (request == "deldir") or (request == "delfile"):
        name=str(input("Enter the name:"))
        sock.send(name.encode())
        response = sock.recv(1024).decode()
        print(response)
    elif (request == 'renamefile'):
        name=str(input("Enter old name:"))
        sock.send(name.encode())
        name2=str(input("Enter new name:"))
        sock.send(name2.encode())
        response = sock.recv(1024).decode()
        print(response)
    elif (request == 'copycs'):
        name=str(input('Enter name:'))
        
        f=open(name,'r')
        name += '\n'
        print(name)
        sock.send(name.encode())
        for line in f:
            sock.send(line.encode())
        f.close()
        response = sock.recv(1024).decode()
        print(response)
    elif (request == 'copysc'):
        name=str(input('Enter name:'))
        sock.send(name.encode())
        f=open(name,'w')
        data=sock.recv(1024).decode()
        msg = data.split("\n")
        print(name)
        for line in msg:
            f.write(line+"\n")
        f.close()
        
    elif (request == "exit"):
        try:
            sock.close()
        except:
            print('fals')
    else:
        print('')
