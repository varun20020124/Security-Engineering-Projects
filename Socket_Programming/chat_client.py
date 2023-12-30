import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair,encrypt,decrypt

SERVER_IP    = gethostbyname( 'DE1_SoC' )
#SERVER_IP    = gethostbyname( 'localhost' )
PORT_NUMBER = 5000
SIZE = 1024
print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )
message='hello'

#first generate the keypair
#get these two numbers from the excel file
p=1297193
q=1297561
###################################your code goes here#####################################
#generate public and private key from the p and q values
#hint: use generate_keypair() function from RSA.py
#public=[0,0]
#private=[0,0]
public, private = generate_keypair(p,q)
message=('public_key: %d %d' % (public[0], public[1]))
mySocket.sendto(message.encode(),(SERVER_IP,PORT_NUMBER))
while True:
        message=input()
        message.join('\n')
        ###################################your code goes here#####################################
        #message is a string input received from the user, encrypt it with RSA character by character and save in message_encoded
        #message encoded is a list of integer ciphertext values in string format e.g. ['23131','352135','54213513']
        #hint: encrypt each character in message using RSA and store in message_encoded
        #message_encoded=['1','135','53']
        #[mySocket.sendto(code.encode(),(SERVER_IP,PORT_NUMBER)) for code in message_encoded] # do not change [sends message through socket]
        message_encoded = [str(encrypt(private, i)) for i in message]
        [mySocket.sendto(code.encode(), (SERVER_IP, PORT_NUMBER)) for code in message_encoded]
       
sys.exit()