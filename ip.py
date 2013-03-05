import socket
myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
hostname = socket.gethostname()
##socketname = socket.getsockname()


print dir(socket)

print myname
print myaddr
print hostname
print socketname
