#TCP_Chat_Server

#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one 
#datagram and get one reply and then the connection terminates.
from socket import socket, SOCK_STREAM, AF_INET

#Create a TCP socket 
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12001

# Assign IP address and port number to socket
serverSocket.bind(('', serverPort))

name = input('Enter alias: ')
serverSocket.listen(1)

print ("Waiting for clients...")
connection, addr = serverSocket.accept()

# Connection from client
client_name = connection.recv(1024).decode()
print (client_name, " connected from ", addr[0], "(", addr[1], ")\n")

print ('Enter [quit] to exit the chat room.')

connection.send(name.encode())

while True:
   message = input('Me > ')
   if message == '[quit]':
      message = "Left the chat..."
      clientSocket.send(message.encode())
      break
   connection.send(message.encode())
   message = connection.recv(1024).decode()
   if not message:
       continue

   print(client_name, '>', message)