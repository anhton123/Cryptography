"""
    This is my unit testing file for my assigned algorithims.
    As you can see, I have imported ONLY Rsa.py because the
    ECC algorithim is hard to implement without the help of a 
    server (which we don't really have one for this project).

    Use this link to see a video of a guy showing how to use the
    unit testing library in python:

    https://www.youtube.com/watch?v=6tNS--WetLI&t=1459s


    Please make your testing file similar format to what is shown
    below.

    In my Rsa.py file, I have the following functions (in order):
        - is_prime()
        - gcd()
        - is_coprime()
        - rsa_e()
        - rsa_d()
    Notice how in my tester, to test my actual code, I named the 
    testing functions "test_{insert functions above}". For 
    example, when I want to test my "is_prime()" function,
    I make a function in this tester file called "test_is_prime()".
    For simplicity sakes, you guys should do that too.

    Another thing to point out is the section divide where
    I divide one section to test the edge cases, and another 
    section to test normal cases. Edge cases are extremely 
    important to consider in coding, so try to find edge
    cases that will need to be tested.
"""


import unittest
import Rsa
import Ecc

class TestRSA(unittest.TestCase):

    # testing is_prime() function
    def test_is_prime(self):
        # edge cases
        self.assertEqual(Rsa.is_prime(1), False)
        self.assertEqual(Rsa.is_prime(2), True)
        self.assertEqual(Rsa.is_prime(-1), False)
        # normal cases
        self.assertEqual(Rsa.is_prime(4), False)
        self.assertEqual(Rsa.is_prime(5), True)
        self.assertEqual(Rsa.is_prime(13), True)
        self.assertEqual(Rsa.is_prime(31), True)
        self.assertEqual(Rsa.is_prime(25), False)
        self.assertEqual(Rsa.is_prime(290005), False)
        self.assertEqual(Rsa.is_prime(971), True)

    # testing gcd() function
    def test_gcd(self):
        # edge cases
        self.assertEqual(Rsa.gcd(1, 2),1)
        self.assertEqual(Rsa.gcd(0, 4),0)
        self.assertEqual(Rsa.gcd(-1, 2),0)
        # normal cases
        self.assertEqual(Rsa.gcd(2, 4),2)
        self.assertEqual(Rsa.gcd(3, 9),3)
        self.assertEqual(Rsa.gcd(9, 25),1)
        self.assertEqual(Rsa.gcd(6, 15),3)
        self.assertEqual(Rsa.gcd(15, 290),5)

    # testing is_coprime() function
    def test_is_coprime(self):
        # edge cases
        self.assertEqual(Rsa.is_coprime(1, 12),True)
        self.assertEqual(Rsa.is_coprime(0, 1),False)
        # normal cases
        self.assertEqual(Rsa.is_coprime(3, 4), True)
        self.assertEqual(Rsa.is_coprime(4, 12),False)
        self.assertEqual(Rsa.is_coprime(4, 13),True)
        self.assertEqual(Rsa.is_coprime(6, 7), True)
        self.assertEqual(Rsa.is_coprime(9, 12),False)
        self.assertEqual(Rsa.is_coprime(5, 14), True)
        self.assertEqual(Rsa.is_coprime(7, 15), True)
        self.assertEqual(Rsa.is_coprime(19, 31), True)

    # testing rsa_e() function
    def test_rsa_e(self):
        self.assertEqual(Rsa.rsa_e("a", 1, 1) ,   '\x00')
        self.assertEqual(Rsa.rsa_e("b", 0, -1),   -1)
        self.assertEqual(Rsa.rsa_e("c", 2, 0) ,   -1)
        # normal cases
        self.assertEqual(Rsa.rsa_e("d", 3, 65),    '(')
        self.assertEqual(Rsa.rsa_e("e", 4, 4),     '\x01')
        self.assertEqual(Rsa.rsa_e("f", 55, 260),  '\x1c')
        self.assertEqual(Rsa.rsa_e("!", 612, 390), 'ą')
        self.assertEqual(Rsa.rsa_e("x", 24, 809),  's')
        self.assertEqual(Rsa.rsa_e("y", 234, 142), 'O')

    # testing rsa_d() function
    def test_rsa_d(self):
        # edge cases
        self.assertEqual(Rsa.rsa_d("a", 1, 1) ,   '\x00')
        self.assertEqual(Rsa.rsa_d("b", 0, -1),   -1)
        self.assertEqual(Rsa.rsa_d("c", 2, 0) ,   -1)
        # normal cases
        self.assertEqual(Rsa.rsa_d("d", 3, 65),    '(')
        self.assertEqual(Rsa.rsa_d("e", 4, 4),     '\x01')
        self.assertEqual(Rsa.rsa_d("f", 55, 260),  '\x1c')
        self.assertEqual(Rsa.rsa_d("!", 612, 390), 'ą')
        self.assertEqual(Rsa.rsa_d("x", 24, 809),  's')
        self.assertEqual(Rsa.rsa_d("y", 234, 142), 'O')

    
if __name__ == "__main__":
    unittest.main()
