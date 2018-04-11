from socket import *

host = "127.0.0.1" # set to IP address of target device
port = 13002 # choose a different port for each device
address = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("Enter message to send or type 'exit': ")
    UDPSock.sendto(bytes(data, 'utf8'), address) # Data through UDP must be sent as raw data (bytes). Encoding is
                                                 # mandatory, it can be changed but there is no reason for using
                                                 # something different from utf8.
    if data == "exit":
        break
UDPSock.close()