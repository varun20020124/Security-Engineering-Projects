from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import re
import struct
from RSA import decrypt
import des
PORT_NUMBER = 5000
SIZE = 8192

#hostName = gethostbyname( '192.168.1.3' )
hostName = gethostbyname( 'DE1_SoC' )
#hostName = gethostbyname( 'localhost' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind(  (hostName, PORT_NUMBER)  )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))

#client_public_key=''
#des_key=''

while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        (data, addr) =  mySocket.recvfrom(1024)
        data = data.decode()


        if data.find('public_key') != -1:  # client has sent their public key
        # Retrieve public key and private key from the received message (message is a string!)
           #print('Public key is: %s' % (data))
           public_key_data = re.findall(r'\d+', data)
           if len(public_key_data) == 2:
                public_key_e, public_key_n= (int(public_key_data[0]), int(public_key_data[1]))
                print('Public key is: %d, %d' % (public_key_e, public_key_n))

                
        elif data.find('des_key') != -1:  # client has sent their DES key
            # Read the next 8 bytes for the DES key by running (data, addr) = mySocket.recvfrom(SIZE) 8 times
            des_key_parts = []
            for _ in range(8):
                (part, _) = mySocket.recvfrom(SIZE)
                des_key_parts.append(part)
            # Combine the parts into the full encrypted DES key
            encrypted_des_key = b''.join(des_key_parts)
           # print("%s" %(encrypted_des_key))
            # Decrypt the DES key using RSA
            des_key_decoded=[]
            if public_key_e != 0 and public_key_n != 0:
                public=(public_key_e ,public_key_n)
                des_key_decoded = []
                for data in des_key_parts:
                    cipher=int(data)
                    #print(cipher)
                    des_key_decoded+= decrypt(public,cipher)
                des_key=''
                for i in des_key_decoded:
                            des_key=des_key+str(i)
                print("DES key decoded = "+str(des_key))
                # Now we will receive the image from the client
                (data, addr) = mySocket.recvfrom(SIZE)
                # Decrypt the image using the DES key
                if des_key != 'dummyval':
                    decoder=des.des()
                    rr=decoder.decrypt(des_key,data,cbc=False) # this is in string  format, must convert to byte format
                    rr_byte=bytearray()
                    for x in rr:
                        rr_byte+=bytes([ord(x)])
                    file2=open(r'penguin_decrypted.jpg',"wb") 
                    file2.write(bytes(rr_byte))
                    file2.close()
                    print ('decrypting image completed')
        else:
            continue

mySocket.close()  # close the connection




