#SEVER CODE
print('Starting Server')
#Perudo Game

n_players=int(raw_input('How many players? '))
#set up socket
print('Setting up connection')
import socket
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50002              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
conn=[]
print('Waiting for playes')
for i in range(n_players):
    s.listen(1)
    conn.append(s.accept())
    print 'Connected by', conn[i,1]

print conn
print 'all players joined'

def gendice(p_health):
    
