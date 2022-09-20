import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org',80))
cmd='GET http://data.pri4e.org/romeo.txt HTTP/1.0\n\n'.encode()
