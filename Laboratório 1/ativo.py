# Exemplo basico socket (lado ativo)

import socket

HOST = 'localhost' 
PORTA = 5000       

sock = socket.socket()  

sock.connect((HOST, PORTA)) 

msg = ""
while(1):
    print("Digite a mensagem a ser enviada: (ou 'exit' para finalizar)")
    msg = input()
    if(msg=="exit"): break

    sock.send(bytes(msg,"utf-8"))
    resposta = sock.recv(1024) 
    print("resposta: ",str(resposta,  encoding='utf-8'))


sock.close()