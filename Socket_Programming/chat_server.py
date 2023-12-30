
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
from RSA import decrypt

PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( 'DE1_SoC' )
#hostName = gethostbyname('localhost')
#hostName = gethostbyname( 'DESKTOP-A30LB1P' )

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))

print("Test server listening on port {0}\n".format(PORT_NUMBER))
#client_public_key=''
public = None

while True:
    (data, addr) = mySocket.recvfrom(SIZE)
    data = data.decode()
    
    if data.find('public_key') != -1:
        # Extract the public key from the received message
        public_key_data = re.findall(r'\d+', data)
        if len(public_key_data) == 2:
            public = (int(public_key_data[0]), int(public_key_data[1]))
            print('public key is : %d, %d' % (public[0], public[1]))
    else:
        if public is not None:
            cipher = int(data)
            print(str(cipher) + ':',end='')
            # Decrypt the received data using the public key
            data_decoded = decrypt(public, cipher)
            print(data_decoded)
        else:
            print("No public key received. Cannot decrypt the message.")

sys.exit()


