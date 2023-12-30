
import random


#fnction for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(e, z):
    ###################################your code goes here#####################################
    x1, x2, y1, y2, z1, z2 = 0, 0, 1, 0, 0, 1
    add = z
    while e % z != 0:
        m = e % z 
        r = e // z 
        x1, x2, y1, y2, z1, z2 = y1 - r * x1, y2 - r * x2, x1, x2, y1, y2
        e, z = z, m
        if x1 < 0:
            while x1 < 0:
                x1 += add
    return x1
    
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
           else: 
               return True 
  
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################
    z=(p-1)*(q-1)
    n=p*q
    while True:
        e= random.randint(2,n-1)
        if gcd(e,z)==1:
            break
    
    public_key=(e,n)
    private_key=(get_d(e,z),n)

    return public_key, private_key

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    #cipher=0
    cipher = (pow(ord(plaintext),pk[0],pk[1]))
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    #plain='a'
    plain = chr((pow(ciphertext,pk[0],pk[1])))
    return ''.join(plain)

