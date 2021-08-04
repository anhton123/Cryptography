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

def get_p():
    """Returns a valid number for prime number p

    Returns:
        int: returns a number that is prime
    """
    n = int(input("Please enter a prime number, p, where p is in the range of 23 <= p <= 97: "))
    while is_prime(n) == False or n <= 22 or n >= 98:
        n = int(input("{} is not a valid number, please enter another prime number between 23 and 97: ".format(n)))
    return n

def get_q():
    """Returns a valid number for prime number q

    Returns:
        int: returns a number that is prime
    """
    n = int(input("Please enter a another prime number, q, where q is in the range 23 <= p <= 97: "))
    while is_prime(n) == False:
        n = int(input("{} is not a valid number, please enter another prime number between 23 and 97: ".format(n)))
    return n

def gcd(p,q):
    """Function to find the greatest common divisor of p and q
    Args:
        p (int): first num arg
        q (int): second num arg
    Returns:
        int: returns the greatest commond divisor of p and q
    """
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
    # print("n = p*q = {}*{} = {}".format(p,q,n))
    # print("phi = (p-1)*(q-1) = ({}-1)*({}-1) = {}".format(p,q,phi))
    print("public key: (e, n) = ({}, {})".format(e,n))
    print("private key: (d, n) = ({}, {})".format(d, n))
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
    o = ord(cipher)
    message = ord(cipher) ** d % n
    return chr(message)


def encrypt():
    """Asymmetric RSA encryption algorithim

    Returns:
        str: returns the cipher text of input using RSA encryption algorithim
    """
    inp = input("Please enter some text value to be encrypted (less than 50 characters): ")
    while len(inp) > 50:
       inp = input("You entered more than 50 characters!\nPlease enter some text value to be encrypted (less than 50 characters): ") 
    # 1. Gets two prime numbers p and q 
    p = get_p()
    q = get_q()
    # 2. Generates private and public keys
    ((e,n),(d,n)) = generate_keyPairs(p, q)
    # 3. Encryption
    cipher = []
    for char in inp:
        cipher.append(rsa_e(char, e, n))
    print("Your encrypted message: " + "".join(cipher) + " -")
    print("Copy this list if you want to decrypt it: " + str(cipher))
    return cipher

def decrypt():
    """Asymmetric RSA decryption algorithim

    Returns:
        str: returns the original text of input using RSA decryption algorithim
    """

    # 1. Decryption
    temp = input("Please enter the list of the encrypted values to be decrypted: ")
    cipher = ast.literal_eval(temp)
    d = int(input("Enter the value of \"d\" in private key (d, n): "))
    n = int(input("Enter the value of \"n\" in private key (d, n): "))
    message = []
    for char in cipher:
        message.append(rsa_d(char, d, n))
    print("Your deciphered message: " + "".join(message))
    return message


if __name__ == "__main__":
    inp = input("Enter 'e' for encrypt, 'd' for decrypt, or 'q' for quit: ")
    while inp != 'q':
        if inp == 'e':
            encrypt()
            inp = input("Enter 'e' for encrypt, 'd' for decrypt, or 'q' for quit: ")
        elif inp == 'd':
            decrypt()
            inp = input("Enter 'e' for encrypt, 'd' for decrypt, or 'q' for quit: ")
        else:
            print("Wtf u just pressed")
            break

