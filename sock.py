
import socket
import sys
 
HOST = ''   # Symbolic name, meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print('Socket bind complete')
 
#Start listening on socket
s.listen(1)
print('Socket now listening')
 
#now keep talking with the client
#wait to accept a connection - blocking call

try:
  conn, addr = s.accept()
  print('Connected with ' + addr[0] + ':' + str(addr[1]))
  
  while 1:
    data = conn.recv(1024)
    if not data:break
    print(type(data))
    print(data)
    d = data.decode('utf8')
    print(d)
    map(int, d.split(' '))
    print(type(d))
    print(d)
    map(lambda a: 2*a, d)

    
    conn.sendall(data)
  conn.close()
  s.close()
except KeyboardInterrupt:
  conn.close()
  s.close()
  

     

