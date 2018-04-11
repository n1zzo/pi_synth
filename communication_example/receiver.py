import select
from socket import *

host = ""
port_list = [13000, 13001] # list of ports chosen for the other devices
buf = 1024 # input buffer
address_list = [(host, port_list[0]), (host, port_list[1])] # address_list must have the same number of elements of
                                                            # port_list. Pay attention to the sequential number.

UDPSock_list = [socket(AF_INET, SOCK_DGRAM), socket(AF_INET, SOCK_DGRAM)] # UDPSock_list must have the same number of
                                                                          # elements of port_list. Items are all equal.

count = 0

# Binding
for sock in UDPSock_list:
    UDPSock_list[count].bind(address_list[count])
    count += 1

print("Waiting to receive messages...")

data = ""

# Listen for messages
while data != "exit":
    for sock in UDPSock_list:
        ready = select.select([sock], [], [], 0.1)
        if ready[0]:
            (data, addr) =sock.recvfrom(buf)
            data = str(data)[2:-1] # data is received as a string of bytes. When bytes are casted to string two
                                   # two characters are added at the beginning (b') and one is added at the end (')
                                   # this line deletes from the received string the first two and the last characters.
            print("Received message: " + data)

# Close connections
for sock in UDPSock_list:
    sock.close()