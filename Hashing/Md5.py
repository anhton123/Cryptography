"""

    MIT License
    Copyright (c) 2016-2021 The Algorithms
    Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

import math

def rearrange(bitString32):
    """ Regroups the given binary string for md5 hashing
    Arguments:
        bitString32 (str): string to be rearranged

    Raises:
        ValueError: if the given string is not a 32 bit binary string

    Returns:
        str: rearranged string for md5 hashing
    """
    if len(bitString32) != 32:
        raise ValueError("Need length 32")
    newString = ""
    for i in [3, 2, 1, 0]:
        newString += bitString32[8 * i : 8 * i + 8]
    return newString


def reformatHex(i):
    """Converts the given integer into 8-digit hex number.
    Arguments:
            i (int):  input arg i to be converted into 8-digit hex number
    >>> reformatHex(666)
    '9a020000'
    Returns:
        int: 8-digit hex number of input arg i
    """

    hexrep = format(i, "08x")
    thing = ""
    for i in [3, 2, 1, 0]:
        thing += hexrep[2 * i : 2 * i + 2]
    return thing

def pad(bitString):
    """Fills up the binary string to a 512 bit binary string

    Arguments:
            bitString (str): string representation of the binary value of input text
    Returns:
            str: padded value of bitString input
    """
    startLength = len(bitString)
    bitString += "1"
    while len(bitString) % 512 != 448:
        bitString += "0"
    lastPart = format(startLength, "064b")
    bitString += rearrange(lastPart[32:]) + rearrange(lastPart[:32])
    return bitString


def getBlock(bitString):
    """Splits the binary represenation thats passed in as arg as into blocks of 32 bits

    Arguments:
        bitString(str): binary representation of string

    Return:
        list: list of binary values
    """
    currPos = 0
    while currPos < len(bitString):
        currPart = bitString[currPos : currPos + 512]
        mySplits = []
        for i in range(16):
            mySplits.append(int(rearrange(currPart[32 * i : 32 * i + 32]), 2))
        yield mySplits
        currPos += 512

def not32(i):
    """ Converts input i into the "opposite" 32 bit value

    Args:
        i (int): number to be converted into opposite 32 bit balue

    Returns:
        int: int value that is the opposite 32 bit value of i
    """
    i_str = format(i, "032b")
    new_str = ""
    for c in i_str:
        new_str += "1" if c == "0" else "0"
    return int(new_str, 2)


def sum32(a, b):
    """ Returns a value from args a and b that is used for md5 hashing

    Args:
        a (int): input arg a
        b (int): input arg b

    Returns:
        int: value used for md5 hashing
    """
    return (a + b) % 2 ** 32


def leftrot32(i, s):
    """ Returns a value input i left shifted by s

    Args:
        i (int): input arg i
        s (int): input arg s

    Returns:
        int: value of input arg i left shifted s
    """
    return (i << s) ^ (i >> (32 - s))


def md5_hash(txt):
    """Returns a 128 bit hash code of the string 'testString'

    Arguments:
        txt (str): text to be hashed

    Returns:
        str: 128 bit representation of hashed input text
    """

    bs = ""
    for i in txt:
        bs += format(ord(i), "08b")
    bs = pad(bs)

    tvals = [int(2 ** 32 * abs(math.sin(i + 1))) for i in range(64)]

    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    s = [
        7,12,17,22,
        7,12,17,22,
        7,12,17,22,
        7,12,17,22,
        5,9,14,20,
        5,9,14,20,
        5,9,14,20,
        5,9,14,20,
        4,11,16,23,
        4,11,16,23,
        4,11,16,23,
        4,11,16,23,
        6,10,15,21,
        6,10,15,21,
        6,10,15,21,
        6,10,15,21,
    ]

    for m in getBlock(bs):
        A = a0
        B = b0
        C = c0
        D = d0
        for i in range(64):
            if i <= 15:
                # f = (B & C) | (not32(B) & D)
                f = D ^ (B & (C ^ D))
                g = i
            elif i <= 31:
                # f = (D & B) | (not32(D) & C)
                f = C ^ (D & (B ^ C))
                g = (5 * i + 1) % 16
            elif i <= 47:
                f = B ^ C ^ D
                g = (3 * i + 5) % 16
            else:
                f = C ^ (B | not32(D))
                g = (7 * i) % 16
            dtemp = D
            D = C
            C = B
            B = sum32(B, leftrot32((A + f + tvals[i] + m[g]) % 2 ** 32, s[i]))
            A = dtemp
        a0 = sum32(a0, A)
        b0 = sum32(b0, B)
        c0 = sum32(c0, C)
        d0 = sum32(d0, D)

    digest = reformatHex(a0) + reformatHex(b0) + reformatHex(c0) + reformatHex(d0)
    return digest
