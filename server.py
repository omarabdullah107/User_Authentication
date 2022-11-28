import socket
import hashlib


username  = ["papayaga","omar","ahmed","amr"]
password = ["monomonothealone2022","helloiamomar","helloiamahmed","helloiamamr"]

hashed_passwords = []
hashed = ""


for i in range(0,len(password)):
    hashed = hashlib.sha256(password[i].encode('utf-8')).hexdigest()
    hashed_passwords.append(hashed)
#print(hashed_passwords)


dataa = [[username[0]+hashed_passwords[0]],[username[1]+hashed_passwords[1]],[username[2]+hashed_passwords[2]],[username[3]+hashed_passwords[3]]]
#print(data)



SERVER_IP = '192.168.1.4'
SERVER_PORT = 5699


with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print('Server is listening')
    s.listen(1)
    conn,addr = s.accept()
    print(f'Connection accepted from :{addr}')
    with conn:
        while(True):
            conn.send(b'Hello World')
            data =  conn.recv(1024)
            print(data)
            strdata = data.decode()
            print(strdata)
            for i in range(0,len(dataa)):
                if(strdata == dataa[i]):
                    conn.send(b'Authenticated')
                    auth =  conn.recv(1024)
                if(strdata != dataa[i]):
                    conn.send(b'Incorrect username or password')
                    no =  conn.recv(1024)
            
            break

   



