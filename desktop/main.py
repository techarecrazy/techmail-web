import socket

sock = socket.socket()
sock.connect(("serveo.net", 4096))
user = input('User: ')

sock.send(f"{input('Method SEND/LIST: ')}\n{user}\n{input('Password: ')}\n{input('Another user: ')}\n{input('Title: ')} - {user}\n::{input('Text: ')}".encode())
print(sock.recv(8192).decode())
