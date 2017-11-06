# Echo client program
import socket

HOST = '10.16.227.222'    # The remote host
PORT = 50001              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
sendText=raw_input()
s.sendall(sendText)
data = s.recv(1024)
print 'Received echo of ', repr(data)
s.close()
