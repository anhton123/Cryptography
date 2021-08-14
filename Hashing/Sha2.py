"""
    Implementation for SHA256 hashing algorithm
"""

def sha2_hash(msg):
    """
    SHA2 Hashing algorithm

    Args:
        msg (str): string data that is to be encrypted

    Returns:
        str: returns the hash value of input using SHA256 hashing algorithim
    """

    # Some constants
    h0 = hextobin('0x6a09e667')
    h1 = hextobin('0xbb67ae85')
    h2 = hextobin('0x3c6ef372')
    h3 = hextobin('0xa54ff53a')
    h4 = hextobin('0x510e527f')
    h5 = hextobin('0x9b05688c')
    h6 = hextobin('0x1f83d9ab')
    h7 = hextobin('0x5be0cd19')

    consts = ('0x428a2f98', '0x71374491', '0xb5c0fbcf', '0xe9b5dba5', '0x3956c25b', '0x59f111f1', '0x923f82a4', '0xab1c5ed5',
              '0xd807aa98', '0x12835b01', '0x243185be', '0x550c7dc3', '0x72be5d74', '0x80deb1fe', '0x9bdc06a7', '0xc19bf174',
              '0xe49b69c1', '0xefbe4786', '0x0fc19dc6', '0x240ca1cc', '0x2de92c6f', '0x4a7484aa', '0x5cb0a9dc', '0x76f988da',
              '0x983e5152', '0xa831c66d', '0xb00327c8', '0xbf597fc7', '0xc6e00bf3', '0xd5a79147', '0x06ca6351', '0x14292967',
              '0x27b70a85', '0x2e1b2138', '0x4d2c6dfc', '0x53380d13', '0x650a7354', '0x766a0abb', '0x81c2c92e', '0x92722c85',
              '0xa2bfe8a1', '0xa81a664b', '0xc24b8b70', '0xc76c51a3', '0xd192e819', '0xd6990624', '0xf40e3585', '0x106aa070',
              '0x19a4c116', '0x1e376c08', '0x2748774c', '0x34b0bcb5', '0x391c0cb3', '0x4ed8aa4a', '0x5b9cca4f', '0x682e6ff3',
              '0x748f82ee', '0x78a5636f', '0x84c87814', '0x8cc70208', '0x90befffa', '0xa4506ceb', '0xbef9a3f7', '0xc67178f2')

    # Processes the msg into 32 bit words
    binary_list = pre_processing(msg)
    binary_list = create_message_schedule(binary_list)
    binary_list = process_messages(binary_list)

    # Beginning the encryption
    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    f = h5
    g = h6
    h = h7

    for i in range(64):
        s1 = xor(right_rotate(e, 6), right_rotate(e, 11))
        s1 = xor(s1, right_rotate(e, 25))
        ch = xor(bin_and(e, f), bin_and(complement(e), g))
        temp1 = bin_add(h, s1, ch, hextobin(consts[i]), binary_list[i])[-32:]

        s0 = xor(right_rotate(a, 2), right_rotate(a, 13))
        s0 = xor(s0, right_rotate(a, 22))[-32:]
        maj = xor(bin_and(a, b), bin_and(a, c))
        maj = xor(maj, bin_and(b, c))[-32:]
        temp2 = bin_add(s0, maj)[-32:]

        h = g
        g = f
        f = e
        e = bin_add(d, temp1)[-32:]
        d = c
        c = b
        b = a
        a = bin_add(temp1, temp2)[-32:]

    h0 = bin_add(h0, a)[-32:]
    h1 = bin_add(h1, b)[-32:]
    h2 = bin_add(h2, c)[-32:]
    h3 = bin_add(h3, d)[-32:]
    h4 = bin_add(h4, e)[-32:]
    h5 = bin_add(h5, f)[-32:]
    h6 = bin_add(h6, g)[-32:]
    h7 = bin_add(h7, h)[-32:]

    return hex(int((h0 + h1 + h2 + h3 + h4 + h5 + h6 + h7), 2))[2:].upper()

def pre_processing(msg):
    """
    Formatting the input message as well as padding

    Args:
        msg (str): The input

    Returns:
        The msg padded in the right format as a list

    """
    bin_string = ''.join(format(ord(i), '08b') for i in msg)
    original_length = len(bin_string)

    bin_string_with_1 = ''.join(format(ord(i), '08b') for i in msg) + "10000000"
    binary_list = [bin_string_with_1[i:i + 8] for i in range(0, len(bin_string_with_1), 8)]

    while len(binary_list) % 56 != 0:
        binary_list.append('00000000')
    binary_list.extend(['00000000' for i in range(7)])
    binary_list.append(bin(original_length)[2:].zfill(8))

    return binary_list


def create_message_schedule(lst):
    """
    The messaging scheduler. Condenses the messages into 32 bit words.

    Args:
        lst (list): A list of the message in binary

    Returns:
        The input but condensed into 32 bit words

    """
    new_list = []
    string = ""
    for val in lst:
        string += val
        if len(string) == 32:
            new_list.append(string)
            string = ""
    new_list.extend(["00000000000000000000000000000000" for i in range(48)])
    return new_list

def process_messages(input_list):
    """
    Processes the messages

    Args:
        input_list (list): The 32 bit word list

    Returns:
        list: The input_list with its elements encrypted

    """
    for i in range(16, 64):
        rotated_s0one = right_rotate(input_list[i - 15], 7)
        rotated_s0two = right_rotate(input_list[i - 15], 18)
        right_shifts0 = right_shift(input_list[i - 15], 3)

        rotated_s1one = right_rotate(input_list[i - 2], 17)
        rotated_s1two = right_rotate(input_list[i - 2], 19)
        right_shifts1 = right_shift(input_list[i - 2], 10)

        s0 = xor(rotated_s0one, rotated_s0two)
        s0 = xor(s0, right_shifts0)
        s1 = xor(rotated_s1one, rotated_s1two)
        s1 = xor(s1, right_shifts1)

        input_list[i] = bin_add(input_list[i - 16], s0, input_list[i - 7], s1)[-32:]
    return input_list

def hextobin(h):
    """
    Hex to binary function

    Args:
        h (): A hexadecimal number

    Returns:
        The input but in binary

    """
    return bin(int(h, 16))[2:].zfill(32)

def xor(binstring1, binstring2):
    """
    XOR function for binary strings
    Args:
        binstring1 (string): A binary number represented in string format
        binstring2 (string): A binary number represented in string format

    Returns:
        The two inputs XOR together

    """
    binary_return = ''
    for i in range(32):
        if (binstring1[i] == '1' and binstring2[i] == '0') or (binstring1[i] == '0' and binstring2[i] == '1'):
            binary_return += '1'
        else:
            binary_return += '0'
    return binary_return

def bin_and(binstring1, binstring2):
    """
    AND function for binary strings

    Args:
        binstring1 (string): A binary number represented in string format
        binstring2 (string): A binary number represented in string format

    Returns:
        The two inputs added together

    """
    binary_return = ''
    for i in range(32):
        if binstring1[i] == '1' and binstring2[i] == '1':
            binary_return += '1'
        else:
            binary_return += '0'
    return binary_return

def complement(binstring):
    """
    Complement for binary strings

    Args:
        binstring (string): A binary number represented in string format

    Returns:
        The input's complement

    """
    binary_return = ''
    for i in range(32):
        if binstring[i] == '1':
            binary_return += '0'
        else:
            binary_return += '1'
    return binary_return

def bin_add(*bin_nums: str) -> str:
    """
    Addition for binary numbers

    Args:
        *bin_nums (): Values to be added

    Returns:
        The sum of all the values

    """
    return bin(sum(int(x, 2) for x in bin_nums))[2:].zfill(32)

def right_shift(binstring, num):
    """
    shifts to the right by num

    Args:
        binstring (): A binary number represented in string format
        num (): The shifting value

    Returns:
        The binary number shifted the correct amount

    """
    return binstring[:-num].zfill(32)

def right_rotate(binstring, num):
    """
    Function to rotate string to the right by num

    Args:
        binstring (): A binary number represented in string format
        num (): The number to rotate by

    Returns:
        The binary number rotated the correct amount

    """
    rotation = binstring[-num:]
    original = binstring[:-num]
    return (rotation + original).zfill(32)


