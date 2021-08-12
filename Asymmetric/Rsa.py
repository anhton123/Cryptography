


import random
import ast

def is_prime(num):
    """Checks if arg num is a prime number
    Args:
        num (int): number that's passed in as argument
    Returns:
        bool: returns true if num is prime and false if num is not prime
    """
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def gcd(p,q):
    """Function to find the greatest common divisor of p and q
    Args:
        p (int): first num arg
        q (int): second num arg
    Returns:
        int: returns the greatest commond divisor of p and q
    """
    if p <= 0 or q<= 0:
        return 0
    while q != 0:
        p, q = q, p%q
    return p


def is_coprime(x, y):
    """Function to check if x is a coprime of y
    Args:
        x (int): number to compare with if its a coprime
        y (int): reference number to compare to if x is a coprime
    Returns:
        boolean: return true if x is coprime of y, return false if x isn't coprime of y
    """
    return gcd(x, y) == 1


def get_e(phi, n):
    """Function to give a value to e, which is the value used in the encryption key
    Args:
        phi (int): euler's totient
        n (int): the value of the multiplication between p and q
    Returns:
        boolean: return e
    """
    # 1. Makes a list of all of the coprimes between 1 < n < phi 
    #    where n is coprime to both n and phi
    coprime_lst = []
    for i in range (3,phi,2):
        if is_coprime(i, phi) and is_coprime(i, n):
            coprime_lst.append(i)
    # 2. Chooses a random value in the coprime_lst
    e = random.choice(coprime_lst)
    return e

def get_d(phi, e):
    """Function to give a value to d, which is the value used in the decryption key
    Args:
        phi (int): euler's totient
        e (int): the value of e in the encryption key
    Returns:
        boolean: returns d
    """
    # 1. Creates a secure number that will be used to make sure
    #    the value d won't be easy to crack
    secure_num = random.randint(3, 6)
    count = 0
    # 2. Finds a value for d
    for i in range(1, 10000000, 1):
        if e * i % phi == 1:
            if count == secure_num:
                return i
            else:
                count += 1

def generate_keyPairs(p, q):
    """Function that returns a pair of tuples for the private and public key
    Args:
        p (int): first prime number
        q (int): second prime number
    Returns:
        tuple of ints: returns private and public key in this format: ((e, n), (d, n))
    """
    n = p * q
    phi = (p-1) * (q-1)
    e = get_e(phi, n)
    d = get_d(phi, e)
    return ((e,n),(d,n))

def rsa_e(message, e, n):
    """Function that encrypts a single char with encryption key
    Args:
        message(char): char to be encrypted
        e (int):       value of e in encryption key
        n (int):       the value of the multiplication between p and q
    Returns:
        char: returns encrypted value of mesasge using encryption key
    """
    if n <= 0:
        return -1
    o = ord(message)
    cipher = ord(message) ** e % n
    return chr(cipher)

def rsa_d(cipher, d, n):
    """Function that decrypts a single char with decryption key
    Args:
        message(char): char to be encrypted
        d (int):       value of d in decryption key
        n (int):       the value of the multiplication between p and q
    Returns:
        char: returns decrypted value of cipher using decryption key
    """
    if n <= 0:
        return -1
    message = ord(cipher) ** d % n
    return chr(message)
    
def rsa_encrypt(txt, p, q):
    """Asymmetric RSA encryption algorithim

    Returns:
        tuple (string value of encrypted text, 
               list of char values of encrypted txt, 
               String representing key values): 
               returns the cipher text of input using RSA encryption algorithim
    """

    ((e,n),(d,n)) = generate_keyPairs(p, q)
    cipher = []
    for char in txt:
        cipher.append(rsa_e(char, e, n))
    return ("".join(cipher), cipher,"Private Key: (d,n) = ({}, {})".format(d,n))

def rsa_decrypt(cipher, d, n):
    """Asymmetric RSA decryption algorithim
    Args:
        cipher(string): cipher to be decrypted
        d (int):       value of d in decryption key
        n (int):       the value of the multiplication between p and q
    Returns:
        str: returns the original text of input using RSA decryption algorithim
    """
    cipher = ast.literal_eval(cipher)
    message = []
    for char in cipher:
        message.append(rsa_d(char, d, n))
    return "".join(message)


