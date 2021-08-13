def encrypt(msg, privkey=None, pubkey=None):
    """SHA2 Hashing algorithim

    Args:
        msg (str): string data that is to be encrypted
        privkey (str): no private key. defaulted to None
        pubkey (str): no public key. defaulted to None


    Returns:
        str: returns the hash value of input using SHA2 hashing algorithim
    """
    # Some initialized constants
    a = h0 = 0x6a09e667
    b = h1 = 0xbb67ae85
    c = h2 = 0x3c6ef372
    d = h3 = 0xa54ff53a
    e = h4 = 0x510e527f
    f = h5 = 0x9b05688c
    g = h6 = 0x1f83d9ab
    h = h7 = 0x5be0cd19

    consts = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
              0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
              0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
              0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
              0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
              0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
              0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
              0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

    binary_list = pre_processing(msg)
    binary_list = create_message_schedule(binary_list)
    binary_list = process_messages(binary_list)

    # Beginning the encryption
    for i in range(0, 64):
        s1 = rotate_right(e, 6) ^ rotate_right(e, 11) ^ rotate_right(e, 25)
        ch = (e & f) ^ (~e & g)
        temp1 = h + s1 + ch + consts[i] + int(binary_list[i], 2)

        s0 = rotate_right(a, 2) ^ rotate_right(a, 13) ^ rotate_right(a, 22)
        maj = (a & b) ^ (a & c) ^ (b & c)
        temp2 = s0 + maj

        h = g
        g = f
        f = e
        e = d + temp1
        d = c
        c = b
        b = a
        a = temp1 + temp2

    h0 += a
    h1 += b
    h2 += c
    h3 += d
    h4 += e
    h5 += f
    h6 += g
    h7 += h

    return f'{a:x}{b:x}{c:x}{d:x}{e:x}{f:x}{g:x}{h:x}'


# Formatting the input message as well as padding
def pre_processing(msg):
    bin_string = ''.join(format(ord(i), '08b') for i in msg)
    original_length = len(bin_string)

    bin_string_with_1 = ''.join(format(ord(i), '08b') for i in msg) + "10000000"
    binary_list = [bin_string_with_1[i:i + 8] for i in range(0, len(bin_string_with_1), 8)]

    while len(binary_list) % 56 != 0:
        binary_list.append('00000000')
    binary_list.extend(['00000000' for i in range(7)])
    binary_list.append(bin(original_length)[2:].zfill(8))

    return binary_list


# The messaging scheduler. Condenses the messages into 32 bit words.
def create_message_schedule(lst):
    new_list = []
    string = ""
    for val in lst:
        string += val
        if len(string) == 32:
            new_list.append(string)
            string = ""
    new_list.extend(["00000000000000000000000000000000" for i in range(48)])
    return new_list


# Processes the messages
def process_messages(input_list):
    for i in range(16, 64):
        #rotated_s0one = format(rotate_right(int(input_list[i - 15], 2), 7), '#032b')[2:]

        rotated_s0one = bin(rotate_right(int(input_list[i - 15], 2), 7))[2:].zfill(32)
        rotated_s0two = bin(rotate_right(int(input_list[i - 15], 2), 18))[2:].zfill(32)
        right_shifts0 = bin(int(input_list[i - 15], 2) >> 3)[2:].zfill(32)

        rotated_s1one = bin(rotate_right(int(input_list[i - 2], 2), 17))[2:].zfill(32)
        rotated_s1two = bin(rotate_right(int(input_list[i - 2], 2), 19))[2:].zfill(32)
        right_shifts1 = bin(int(input_list[i - 2], 2) >> 10)[2:].zfill(32)

        s0 = int(rotated_s0one, 2) ^ int(rotated_s0two, 2) ^ int(right_shifts0, 2)
        s1 = int(rotated_s1one, 2) ^ int(rotated_s1two, 2) ^ int(right_shifts1, 2)

        if len(format(int(input_list[i - 16], 2) + s0 + int(input_list[i - 7], 2) + s1, '#034b')) == 34:
            input_list[i] = format(int(input_list[i - 16], 2) + s0 + int(input_list[i - 7], 2) + s1, '#034b')[2:]
        else:
            input_list[i] = format(int(input_list[i - 16], 2) + s0 + int(input_list[i - 7], 2) + s1, '#034b')[3:]

    return input_list


# Helper function that right rotates values
def rotate_right(x, n):
    return int(f"{x:032b}"[-n:] + f"{x:032b}"[:-n], 2)

value = input("Please input your text: ")
print(encrypt(value))
