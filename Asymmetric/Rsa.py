def encrypt(isFile, input, privKey, pubKey):
    """Asymmetric RSA encryption algorithim

    Args:
        isfile (boolean): boolean that represents if the user data is a file or text data.
             isFile = true if user data is a .txt file, isFile = false otherwise
        input (str): string data that is to be encrypted. if isFile == true, 
            input will be the directory of the .txt file. if isFile == false, input would be a string
        privKey (str): private key used for encryption
        pubKey (str): public key used for encryption

    Returns:
        str: returns the cipher text of input using RSA encryption algorithim
    """
    pass

def decrypt(isFile, input, privKey, pubKey):
    """Asymmetric RSA decryption algorithim

    Args:
        isfile (boolean): boolean that represents if the user data is a file or text data.
             isFile = true if user data is a .txt file, isFile = false otherwise
        input (str): string data that is to be encrypted. if isFile == true, 
            input will be the directory of the .txt file. if isFile == false, input would be a string
        privKey (str): private key used for decryption
        pubKey (str): public key used for decryption

    Returns:
        str: returns the original text of input using RSA decryption algorithim
    """
    pass