

def padd(msg):
    msg_length = len(string_to_binary(msg))
    pad = "1" + ("0"*(448 - msg_length - 1))
    length2 = bin(len(string_to_binary(msg)))[2:]
    length1 = "0"*(64 - len(length2))
    ret = string_to_binary(msg) + pad + length1 + length2
    print(ret)
    print(len(ret))




def string_to_binary(msg):
    return ''.join(bin(ord(c)) for c in msg).replace('b','')


padd("abc")

# print(bin(24)[2:])