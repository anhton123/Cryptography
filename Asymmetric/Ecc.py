"""

The following code does work for the ECC algorithim, however there are a lot of bugs. 
This project also doesn't have a "server" component to it, so I can't really carry out
this ECC algorithim as I need a server/client relationship.

"""

import random
import sys

points_lst = []
for x in range(17):
	for y in range(17):
		if (x**3 + 7 - y**2) % 17 == 0:
			points_lst.append((x,y))

def modInverse(yp, p):
    for x in range(1, p):
        if (((yp%p) * (x%p)) % p == 1):
            return x
    return -1

def double(xp, yp, p):
    temp1 = ((3 * xp ** 2) % p)
    temp2 = modInverse(2 * yp, p)
    s = (temp1 * temp2) % p
    x_ret = (s**2 - 2*xp) % p
    y_ret = (s*(xp - x_ret) - yp) % p
    return x_ret, y_ret


def add(xp, yp, xq, yq, p):
    s = (yp - yq) / (xp - xq)
    xr = (s**2 - (xp + xq)) % p
    yr = (s*(xp - xr) - yp) % p
    return xr, yr 
    
def pop(a, b):
    return a + b
def add_point(xp, yp, p, n):
	# if xp == xq:
	# 	return -1
    xq, yq = double(xp, yp, p)
    for i in range(1, n):
        if xq == xp:
            return -1
        xq, yq = add(xp, yp, xq, yq, p)
    return xq, yq

if __name__ == "__main__":
    print("The curve used in this application is: y^2 = x^3 + 7 mod 17")
    print("The following points are points that exist in this curve:")
    for points in points_lst:
        print(str(points) + " ", end = "")
    print("\nWith the points that was listed above, choose one point.")
    x = int(input("Enter the the value of the x-coordintate for the point you chose: "))
    y = int(input("Enter the value of the y-coordintate for the point you chose: "))
    n = int(input("Please enter in a random number, n, where 1 <= n <= 16. This will be your private key: "))
    print("With your selected point: G = ({}, {}), we are going to find {}G by adding the point {} times".format(x, y,n, n))
    while add_point(x, y, 17, n -1) == -1:
        print("For mathematical reasons, your input, n, can't work, please reenter another value for n")
        n = int(input("Please enter in a random number, n, where 1 <= n <= 16. This will be your private key: "))
    print("Your point P1 = your public key * G = {}G = ".format(n) + str(add_point(x, y, 17, n -1)))
    server_n = random.randint(1, 16)
    print("Server chooses a number 1 <= n <= 16:")
    while add_point(x, y, 17, server_n -1) == -1:
        server_n = random.randint(1, 16)
    print("Server chose {} as its private key.".format(server_n))
    print("Server's point P2 = Server's public key = {}G = ".format(server_n) + str(add_point(x, y, 17, server_n -1)))
    print("Your point, P1, gets exchanged with server's point P2")
    if add_point(x, y, 17, ((server_n-1) * (n-1)) % 17) == -1:
        print("Oops, due to some math errors, we can't execute the encryption...")
        sys.exit()
    print("You get a new point = your private key * your received server point = " + str(add_point(x, y, 17, ((server_n - 1) * (n -1)) % 17)))
    print("The serves's new point =  the servers private key * the server's received point by you =  " + str(add_point(x, y, 17, ((n-1) * (server_n-1)) % 17)))
    print("(server_n * n % 17)G = {}G = ".format(server_n * n % 17) + str(add_point(x, y, 17, ((server_n-1) * (n-1)) % 17))) 

