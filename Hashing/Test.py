"""
    Unit Testing for sha2 and Md5. Sha2 is specifically Sha256.
"""

import unittest
import Sha2
import Md5

class Test(unittest.TestCase):
    # Normal Cases
    case1 = 'hello world'
    case2 = 'raymond phan'
    case3 = 'league of legends'
    case4 = 'computer science'

    # Edge cases
    case5 = 'wiOARNiwonwaoinr'
    case6 = 'l'
    case7 = 'AWFWNAWrwqrw'
    case8 = 'wiwa;nfawionfwainfoiwanfwainfw'

    testing_list = [case1, case2, case3, case4, case5, case6, case7, case8]
    sha2_solutions_list = ['B94D27B9934D3E08A52E52D7DA7DABFAC484EFE37A5380EE9088F7ACE2EFCDE9',
                           'F59EC62D0271270B71E8A9E3B53B398D658F12DB514840B656EE2D6E6592FBD0',
                           '9EA5367E53CE031525D70849BDE3753832A59CF034B955584A79DA0F5C198E01',
                           '13A5670CC77404AA14B878E0B1A82651E705D21F7BA2956918A1406B26871A1F',
                           'CA3836CD209FAF401E3DA01C9C9FB0DA9AFF7CC6E433DBC779EF38ECF19F4968',
                           'ACAC86C0E609CA906F632B0E2DACCCB2B77D22B0621F20EBECE1A4835B93F6F0',
                           '6552802D69BD7D6189A700670A27406F8455D24CF6145C11E8E33D8548591AFF',
                           'F2267ED1E2A49DF12AF94BCE8FB0EFBCAEFEBFF4D2643E67E7712ADDF66FBB47'
                           ]
    md5_solutions_list = ['5eb63bbbe01eeed093cb22bb8f5acdc3',
                          'e64964db86b8d882bcfbc7ec449faa5f',
                          'cb950a37aa83a2a35e06a0eb2d25024d',
                          '80c18801f6ce7e664f788b70032cdcd1',
                          '9c17e2594743110248aeaf4883fd6fd3',
                          '2db95e8e1a9267b7a1188556b2013b33',
                          'ec97c0aad4ac92fd682cf1732736467d',
                          '23b6aa6c52733c274dc171c4eb0edadc']

    def test_sha2_hash(self):
        for i in range(len(Test.testing_list)):
            self.assertEqual(Sha2.sha2_hash(Test.testing_list[i]), Test.sha2_solutions_list[i])

    def test_md5_hash(self):
        for i in range(len(Test.testing_list)):
            self.assertEqual(Md5.md5_hash(Test.testing_list[i]), Test.md5_solutions_list[i])