############ Utilities #################
def textToBinary(text):
    """Returns the binary represenation of the input arg text

    Arguments:
        text(str): text to be converted to binary

    Return:
        str: binary representation of input arg text
    """
    if len(text) != 8:
        return -1
    return ''.join(bin(ord(c)) for c in text).replace('b','')

def binaryToDecimal(binString):
    return int(binString, 2)

def decimalToBinary(num):
    return bin(num)[2:]

def padd4(binString):
    padd = (4 - len(binString)) * "0"
    return padd + binString

############## Key #####################
def pc1(binString):
    """Permutes a 64 bit key (binString) into a 56 bit key

    Arguments:
        binString(str): 64 bit binary representation of original key

    Return:
        str: 56 bit permuted key from the input which is the original 64 bit key
    """
    pc1Vector = [57,  49,  41,  33,  25,  17,   9,
                  1,  58,  50,  42,  34,  26,  18,
                 10,   2,  59,  51,  43,  35,  27,
                 19,  11,   3,  60,  52,  44,  36,
                 63,  55,  47,  39,  31,  23,  15,
                  7,  62,  54,  46,  38,  30,  22,
                 14,   6,  61,  53,  45,  37,  29,
                 21,  13,   5,  28,  20,  12,   4]
    pc1BinString = ""
    for num in pc1Vector:
        pc1BinString += binString[num-1]
    return pc1BinString

def keySplitHalf(binString):
    """Splits the 56 bit key into two halves

    Arguments:
        binString(str): The 56 bit key after going through pc1

    Return:
        tuple(str, str): 
            first argument:  28-bit left half of original 56 bit input arg binString
            second argument: 28-bit right half of original 56 bit input arg binString
    """
    half = int(len(binString)/2)
    c = binString[0:half]
    d = binString[half:len(binString)]
    return (c,d)

def leftRotate(c, d, roundN):
    """Applies appropriate left rotate for the current round that the DES encryption is in

    Arguments:
        c (str): 28-bit left half of orinal key after going through pc1
        d (str): 28-bit right half of orinal key after going through pc1
        roundN (int): current round that the DES encryption is in

    Return:
        tuple(str, str): 
            first argument:  28-bit string of input arg c after left rotating for its current round 
            second argument: 28-bit string of input arg d after left rotating for its current round
    """
    roundLeftShift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    n_shift = roundLeftShift[roundN]
    tempBinString1 = c[n_shift:] + c[:n_shift]
    tempBinString2 = d[n_shift:] + d[:n_shift]
    return (tempBinString1, tempBinString2)

def pc2(c, d):
    """Permutes the 56 bit key into a 48 bit key

    Arguments:
        c (str): 28-bit left half of orinal key after going through pc1 and left rotation
        d (str): 28-bit right half of orinal key after going through pc1 and left rotation

    Return:
        str: 48 bit binary used for the current round of DES encryption
    """
    binString = c + d
    pc2Vector = [14,  17,  11,  24,   1,   5,
                  3,  28,  15,   6,  21,  10,
                 23,  19,  12,   4,  26,   8,
                 16,   7,  27,  20,  13,   2,
                 41,  52,  31,  37,  47,  55,
                 30,  40,  51,  45,  33,  48,
                 44,  49,  39,  56,  34,  53,
                 46,  42,  50,  36,  29,  32]
    pc2BinString = ""
    for num in pc2Vector:
        pc2BinString += binString[num-1]
    return pc2BinString

############# Message ##################

def initialPermutation(binString):
    """Returns a permuted binary string of 64 bit message (binString)

    Arguments:
        binString(str): 64 bit representation of message

    Return:
        str: 64 bit permuted message
    """
    permutationVector =  [58, 50, 42, 34, 26, 18, 10, 2,
                          60, 52, 44, 36, 28, 20, 12, 4,
                          62, 54, 46, 38, 30, 22, 14, 6,
                          64, 56, 48, 40, 32, 24, 16, 8,
                          57, 49, 41, 33, 25, 17, 9,  1,
                          59, 51, 43, 35, 27, 19, 11, 3,
                          61, 53, 45, 37, 29, 21, 13, 5,
                          63, 55, 47, 39, 31, 23, 15, 7]
    permutedBinString = ""
    for num in permutationVector:
        permutedBinString += binString[num-1]
    return permutedBinString

def messageSplitHalf(binString):
    """Splits the 64 bit message from current round into two halves

    Arguments:
        binString(str): The 64 bit message after initial permutation

    Return:
        tuple(str, str): 
            first argument:  32-bit left half of 64 bit input arg binString
            second argument: 32-bit right half of 64 bit input arg binString
    """
    half = int(len(binString)/2)
    l = binString[0:half]
    r = binString[half:len(binString)]
    return (l,r)

def expansionPermutation(r):
    """Expands the 32 bit message to 48 bits for the current round 

    Arguments:
        r(str): The right half 32 bit message from previous round

    Return:
        str: 48 bit expanded binary string
    """
    eVector = [32,   1,   2,   3,   4,   5,
                4,   5,   6,   7,   8,   9,
                8,   9,  10,  11,  12,  13,
               12,  13,  14,  15,  16,  17,
               16,  17,  18,  19,  20,  21,
               20,  21,  22,  23,  24,  25,
               24,  25,  26,  27,  28,  29,
               28,  29,  30,  31,  32,   1]
    expansionBinString = ""
    for num in eVector:
        expansionBinString += r[num-1]
    return expansionBinString

def xor(binString1, binString2):
    """Does xor operation on the input args 

    Arguments:
        binString1(str): first binary string to have xor operation
        binString2(str): second binary string to have xor operation

    Return:
        str: binary string of binString1 xor binString2
    """ 
    binaryReturn = ""
    for i in range(len(binString1)):
        if (binString1[i] == "1" and binString2[i] == "0") or (binString1[i] == "0" and binString2[i] == "1"):
            binaryReturn += "1"
        else:
            binaryReturn += "0"
    return binaryReturn

def sBoxParser(binString):
    """Helper function for "sBox()" function. Parses appropriate values for row and columns. 

    Arguments:
        binString(str): 6 bit binary string

    Return:
        tuple(int, int): 
            first argument: row value to be used for sbox vector
            second argument: column value to be used for sbox vector
    """
    row = binString[0] + binString[5]
    col = binString[1:5]
    return (binaryToDecimal(row), binaryToDecimal(col))

def sBox(binString):
    """Applies sbox algorithim to input arg binString 

    Arguments:
        binString(str): 48 bit binary string

    Return:
        str: 48 bit binary string after sbox algorithim
    """
    sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0,  7],
            [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
        
           [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

           [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    
           [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    
           [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    
           [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
        
           [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    
           [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]] ]
    binString = [binString[i:i+6] for i in range(0, len(binString), 6)]
    returnBinString = ""
    for i in range(len(binString)):
        row, col = sBoxParser(binString[i])
        num = sbox[i][row][col]
        returnBinString += padd4(decimalToBinary(num))
    return returnBinString

def permuteAfterSBox(binString):
    """Returns a 32 bit binary permuted binary string of 32 bit message (meant to be used after sbox)

    Arguments:
        binString(str): 32 bit binary value

    Return:
        str: 32 bit binary value
    """
    permuteVector = [16,   7,  20,  21,
                     29,  12,  28,  17,
                      1,  15,  23,  26,
                      5,  18,  31,  10,
                      2,   8,  24,  14,
                     32,  27,   3,   9,
                     19,  13,  30,   6,
                     22,  11,   4,  25]
    purmuteBinString = ""
    for num in permuteVector:
        purmuteBinString += binString[num-1]
    return purmuteBinString

def eff(R, K):
    """Returns 32 bit binary value after applying the function f in DES encryption

    Arguments:
        R(str): 32 bit binary which is the right half of message for the previous round
        K(str): 48 bit binary which is the key for the current round

    Return:
        str: 32 bit binary after performation "eff" function
    """
    E = expansionPermutation(R)
    KE = xor(E, K)
    S = sBox(KE)
    f = permuteAfterSBox(S)
    return f

def getR(L, R, K):
    """Returns 32 bit binary value after computing f xor L

    Arguments:
        L(str): 32 bit binary which is the left half of message for the previous round
        R(str): 32 bit binary which is the right half of message for the previous round
        K(str): 48 bit binary which is the key for the current round

    Return:
        str: 32 bit binary after performation "eff" function
    """
    f = ""
    f = eff(R, K)
    R = xor(L, f)
    return R

def finalPermutation(binString):
    """Returns a permuted binary string of 64 bit message after applying rounds

    Arguments:
        binString(str): 64 bit binary value after applying the "rounds" section of DES

    Return:
        str: 64 bit permuted message
    """    
    finalPermutationVectorTable = [40,     8,   48,    16,    56,   24,    64,   32,
                                   39,     7,   47,    15,    55,   23,    63,   31,
                                   38,     6,   46,    14,    54,   22,    62,   30,
                                   37,     5,   45,    13,    53,   21,    61,   29,
                                   36,     4,   44,    12,    52,   20,    60,   28,
                                   35,     3,   43,    11,    51,   19,    59,   27,
                                   34,     2,   42,    10,    50,   18,    58,   26,
                                   33,     1,   41,     9,    49,   17,    57,   25]
    purmuteBinString = ""
    for num in finalPermutationVectorTable:
        purmuteBinString += binString[num-1]
    return purmuteBinString

def des_encrypt(key, message):
    """Applies DES algorithim with given 8 character key and 8 character message

    Arguments:
        key(str): 8 character key used for encryption/decryption
        message(str): 8 character message to be encrypted

    Return:
        str: 16 digit hex value for the encrypted message
    """
    message = textToBinary(message)
    key = textToBinary(key)
    # 1. Initial Permutation for message and key
    permutedMsg = initialPermutation(message)
    permutedKey = pc1(key)
    # 2. Splitting permutted message and key
    (C, D) = keySplitHalf(permutedKey)
    (L, R) = messageSplitHalf(permutedMsg)
    # 2. Rounds
    for round in range(16):
        # This code deals with key for current round
        (C, D) = leftRotate(C, D, round)
        key = pc2(C, D)
        # This code deals with message for current round
        tempR = getR(L, R, key)
        L = R
        R = tempR
    # 3. Bit Swapping
    binString = R + L
    # 4. Inverse Initial Permutation
    cipher = finalPermutation(binString)
    return hex(int(cipher,2))[2:]

def des_decrypt(key, cipher):
    pass

#print(des_encrypt("0001001100110100010101110111100110011011101111001101111111110001","0000000100100011010001010110011110001001101010111100110111101111"))
print(des_encrypt("ABCDEFGH", "HelloWor"))
