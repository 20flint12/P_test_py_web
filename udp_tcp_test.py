
import socket
import struct


# UDP_IP="127.0.0.1"
# UDP_IP="192.168.1.43"
UDP_IP="255.255.255.255"
UDP_PORT = 6100

sockUDP = socket.socket( socket.AF_INET, # Internet
                      socket.SOCK_DGRAM ) # UDP
sockUDP.bind( (UDP_IP,UDP_PORT) )

addr = ["",0]
data = []
while True:

    print "==="
    data,addr = sockUDP.recvfrom( 1024 ) # buffer size is 1024 bytes

    if len(data) == 6:
        # Parse data
        print "1. From UDP addr:", addr
        print "   Message Data:", struct.unpack("BBBBBB",data)
        break


# print "addr:", addr
print "   Response..."



# print data
print "2. sockUDP.sendto:", sockUDP.sendto(data,addr)




##########################################################################



TCP_IP = addr[0]
TCP_PORT = 5800
print "   (TCP_IP,TCP_PORT)", TCP_IP, TCP_PORT




sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print "3. sockTCP.bind"

# sockTCP.bind( ("192.168.1.12", 5800) )
sockTCP.bind( (TCP_IP, TCP_PORT) )

sockTCP.listen(1)

conn, addr = sockTCP.accept()
print 'Connection address:', addr


# sockTCP.connect( (TCP_IP, TCP_PORT) )
# sockTCP.connect( ('192.168.1.12', 5800) )

buff = ""
buff += struct.pack("B",0xF5)
buff += struct.pack("B",0x73)
buff += struct.pack("B",0x79)
buff += struct.pack("B",0x6E)
buff += struct.pack("B",0x63)
buff += struct.pack("B",0x0A)
buff += struct.pack("B",0xF7)
print "   buff:", struct.unpack("BBBBBBB",buff)

print "4. sockTCP.send(buff)"
sockTCP.send(buff)

data = sockTCP.recv(12)
print "5. sockTCP.recv(12)"

print "   received data:", struct.unpack("BBBBBBBBBBBB",data)
sockTCP.close()
