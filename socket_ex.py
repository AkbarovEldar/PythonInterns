import socket

sock = socket.socket()
sock.bind(('localhost', 8888))
sock.listen()
conn, addr = sock.accept()
while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    if not data:
        continue
        data.find()
    conn.send("hello".encode())
conn.close()


addr = ('localhost', 8888)
if socket.has_dualstack_ipv6():
    s = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
else:
    s = socket.create_server(addr)