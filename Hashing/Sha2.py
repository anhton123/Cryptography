def encrypt(input, privkey=None, pubKey=None):
    """SHA2 Hashing algorithim

    Args:
        input (str): string data that is to be encrypted
        privKey (str): no private key. defaulted to None
        pubKey (str): no public key. defaulted to None


    Returns:
        str: returns the hash value of input using SHA2 hashing algorithim
    """

    bin_string = ''.join(format(ord(i), '08b') for i in input)
    original_length = len(bin_string)

    bin_string_with_1 = ''.join(format(ord(i), '08b') for i in input) + "10000000"
    byte_list = [bin_string_with_1[i:i + 8] for i in range(0, len(bin_string_with_1), 8)]

    while len(byte_list) % 512 != 440:
        byte_list.append('00000000')
    byte_list.append(bin(original_length)[2:].zfill(8))

    pass
