if command == 'NAME':
   connection.send(f"Твоє ім'я: {client_name}".encode())
elif command == 'EXIT':
   connection.send(f"Бувай {client_name}".encode())
   connection.close()
else:
   connection.send('Такої команди не існує'.encode())
server_socket.close()
