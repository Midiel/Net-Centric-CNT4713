#TCP_Chat_Client

# Importing modules
from socket import socket, AF_INET, SOCK_STREAM

serverName = 'localhost'
serverPort = 12001

#creating a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

name = input('Enter alias: ')
print("\nCconnecting...\n")

clientSocket.connect((serverName, serverPort))
print("Connected to ", serverName, "(", serverPort, ")\n")

# sends an encoded message
clientSocket.send(name.encode())

# gets a message back from the server through TCP
s_name = clientSocket.recv(1024)

#decodes teh message from the server
s_name = s_name.decode()
print (s_name, "has joined the chat room\n")
print ("Enter [quit] to exit chat room\n")

# loop to keep connection active
while True:
    #gets a message from teh server through TCP
    message = clientSocket.recv(1024)

    # decodes the message
    message = message.decode()
    print(s_name, '>', message)
    message = input('Me > ')

    # check if client wants to end chat
    if message == "[quit]":
        message = "Left the chat..."
        clientSocket.send(message.encode())
        print("\n")
        break
    clientSocket.send(message.encode())
clientSocket.close()