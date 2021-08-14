def xor(binString1, binString2):
    binaryReturn = ""
    for i in range(len(binString1)):
        if (binString1[i] == 1 and binString2[i] == 0) or (binString1[i] == 0 and binString2[i] == 1):
            binaryReturn += "1"
        else:
            binaryReturn += "0"
    return binaryReturn

def add(binString1, binString2):
    binaryReturn = ""
    carry = False
    for i in range(len(binString1) - 1, -1, -1):
        if binString1[i] == "1" and binString2[i] == "1":
            carry = True
        if carry == True:
            
