import socket

HOST = '127.0.0.1'
PORT = 12345
msg = input('[write] >_: ').encode().strip()

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
s.send(msg)

print (f'''{HOST}:{PORT} send >> ${msg}''')

s.close()
