# Exemplo basico socket (lado ativo)

import socket
import json

HOST = 'localhost' 
PORTA = 5000       

sock = socket.socket()  

sock.connect((HOST, PORTA)) 


def showResultMessage(resultObject, file, word):
    if(resultObject["Status"] != "Ok"):
        print("Erro no servidor. Arquivo não encontrado");
    else:
        print("Foram encontrados "+ str(resultObject["Result"]) +" ocorrência(s) de '"+ word + "' no arquivo '" + file +"'")

def AskForInput():
    print("Digite o Nome do arquivo: (ou 'exit' para finalizar)")
    fileName = input()
    if(fileName=="exit"): 
        return "exit",""
    print("Digite a palavra:")    
    word = input()
    return fileName,word

while(1):
    fileName,word = AskForInput()
    if(fileName == "Exit"): break
    requestObject = {"Word":word, "FileName":fileName}
    sock.send(bytes(json.dumps(requestObject),"utf-8"))
    resposta = sock.recv(1024) 
    resultObj = json.loads(str(resposta,  encoding='utf-8'))
    showResultMessage(resultObj,fileName,word);


sock.close()