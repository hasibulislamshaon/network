import socket
mysocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysocket.connect(('freecodecamp.org',80))
cmd='GET https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/networking-write-a-web-browser\n\n'.encode()
mysocket.send(cmd)
while True:
    data=mysocket.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysocket.close()#this is an example practice of the tutorial that i am learning