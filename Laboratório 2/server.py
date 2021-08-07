from DataLayer.FileSystemAccessor import FileSystemAccessor;
import json;
import socket

# Exemplo basico socket (lado passivo)

HOST = ''    
PORTA = 5000 

def HandleConnection(sock):
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
	novoSock.close() 


sock = socket.socket() 
accessor = FileSystemAccessor("./files")

sock.bind((HOST, PORTA))
sock.listen(5) 

while True:
	novoSock, endereco = sock.accept() 
	print ('Conectado com: ', endereco)
	HandleConnection(novoSock)


