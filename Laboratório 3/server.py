from sys import stdin
from DataLayer.FileSystemAccessor import FileSystemAccessor;
import json;
import socket
import select
import sys
import multiprocessing


accessor = FileSystemAccessor("../files")

HOST = ''    
PORTA = 5000 

def HandleConnection(sock,address):
	while True:
		request = sock.recv(1024)
		if not request: break 
		else:
			requestObject = json.loads(request)
			print(requestObject)
			try:
				fileContent = accessor.GetFile(requestObject["FileName"])
				counter = fileContent.count(requestObject["Word"])
				sock.send(bytes(json.dumps({"Status":"Ok","Result":counter}), "utf-8")) 
			except:
				print("File Not Found")
				sock.send(bytes(json.dumps({"Status" :"Error"}), "utf-8")) 
	print("Conexão encerrada com: ",address)
	sock.close() 


def main():
	clientes = []

	sock = socket.socket() 

	sock.bind((HOST, PORTA))
	sock.listen(5) 
	sock.setblocking(False)

	entradas = [sock, sys.stdin.fileno()]

	while True:
		leitura, escrita, excecao = select.select(entradas, [], [])
		
		for pronto in leitura:
			if pronto == sock:
				newSock, address = sock.accept() 
				print ('Conectado com: ', address)
				cliente = multiprocessing.Process(target=HandleConnection, args=(newSock,address) )
				cliente.start()
				clientes.append(cliente)
			else:
				command = input()
				if command == 'fim': #solicitacao de finalizacao do servidor
					for c in clientes: #aguarda todos os processos terminarem
						c.join()
					sock.close()
					sys.exit()


main()