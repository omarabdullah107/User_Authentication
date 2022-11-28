import socket
import hashlib



ausername = input("Enter your user name please")
apassword = input("Enter your password please")

ahashed = hashlib.sha256(apassword.encode('utf-8')).hexdigest()
#print(ahashed)

concate = ""
concate+= ausername + ahashed
#print(concate)


bytess = concate.encode('utf-8')
#print(bytess)


# '172.20.10.2'
SERVER_IP = '192.168.1.4'
SERVER_PORT = 5699

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    data = s.recv(1024)
    print(data)
    s.send(bytess)
    data =  s.recv(1024)
    print(data)
    

    #s.send(b'Done')
    
input()

