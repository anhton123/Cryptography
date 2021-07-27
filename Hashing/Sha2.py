def encrypt(isFile, input, privKey, pubKey):
    """SHA2 Hashing algorithim

    Args:
        isfile (boolean): boolean that represents if the user data is a file or text data.
             isFile = true if user data is a .txt file, isFile = false otherwise
        input (str): string data that is to be encrypted. if isFile == true, 
            input will be the directory of the .txt file. if isFile == false, input would be a string
        privKey (str): no private key. defaulted to None
        pubKey (str): no public key. defaulted to None

    Returns:
        str: returns the hash value of input using SHA2 hashing algorithim
    """
    pass