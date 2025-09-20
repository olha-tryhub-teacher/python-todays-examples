# client

from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('localhost', 12345))

name = input("Для підключення на сервер введіть своє ім'я: ")
client_socket.send(name.encode())
print(client_socket.recv(1024).decode())
command = input('Введіть команду (NAME, EXIT): ')
client_socket.send(command.encode())
print(client_socket.recv(1024).decode())

client_socket.close()


# server
from socket import *
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
connection, address = server_socket.accept()
client_name = connection.recv(1024).decode()
print(f"Користувач {client_name} під'єднався!")
connection.send(f"Вітаю {client_name} на сервері".encode())
command = connection.recv(1024).decode()
if command == 'NAME':
   connection.send(f"Твоє ім'я: {client_name}".encode())
elif command == 'EXIT':
   connection.send(f"Бувай {client_name}".encode())
   connection.close()
else:
   connection.send('Такої команди не існує'.encode())
server_socket.close()
