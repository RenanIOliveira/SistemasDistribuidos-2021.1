# Exemplo basico socket (lado passivo)

import socket

HOST = ''    
PORTA = 5000 

sock = socket.socket() 

sock.bind((HOST, PORTA))

sock.listen(1) 

novoSock, endereco = sock.accept() 
print ('Conectado com: ', endereco)

while True:
	msg = novoSock.recv(1024)
	if not msg: break 
	else: novoSock.send(msg) 

novoSock.close() 
sock.close() 
