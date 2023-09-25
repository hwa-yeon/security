###########################################################################
# HEADER COMMENTS
###########################################################################
### __filename__ = "cse4313_003_pset01_test.py"
### __Python version__ = "3.11.0"
### __copyright__ = "Copyright 2022, CSE4313 Problem Set 01"
### __credits__ = ["Jieung Kim"]
### __license__ = "GPL"
### __version__ = "1.0.0"
###########################################################################

import numpy
import unittest
import cse4313_003_pset01

class CSE4313_003_PSET01_TEST(unittest.TestCase):

  # Test cases for CRT (5 pts per each)
  def test_CRT_1(self): # 5 pts
    n_values = [3, 5]
    r_values = [2, 4]
    answer = cse4313_003_pset01.CRT(n_values, r_values)
    self.assertEqual([14, 15], answer)

  def test_CRT_2(self): # 5 pts
    n_values = [3, 5, 7]
    r_values = [2, 3, 2]
    answer = cse4313_003_pset01.CRT(n_values, r_values)
    self.assertEqual([23,105], answer)

  def test_CRT_3(self): # 5 pts
    n_values = [11, 19, 21]
    r_values = [5, 7, 17]
    answer = cse4313_003_pset01.CRT(n_values, r_values)
    self.assertEqual([3503,4389], answer)
    
  def test_CRT_4(self): # 5 pts
    n_values = [11, 19, 21, 53]
    r_values = [5, 7, 17, 52]
    answer = cse4313_003_pset01.CRT(n_values, r_values)
    self.assertEqual([192230,232617], answer)

  # Test cases for Playfair (5 pts per each)
  def test_Playfair_1_encrypt(self): # 5 pts
    key = "MYKEY"
    message = "THISSANEXAMPLE"
    answer = "PONQTESFZEBUNK"
    result = cse4313_003_pset01.playfair(key, message)
    self.assertEqual(result, answer)    

  def test_Playfair_1_decrypt(self): # 5 pts
    key = "MYKEY"
    message = "PONQTESFZEBUNK"
    answer = "THISSANEXAMPLE"
    result = cse4313_003_pset01.playfair(key, message, False)
    self.assertEqual(result, answer)

  def test_Playfair_2_encrypt(self): # 5 pts
    key = "secret"
    message = "my secret message"
    answer = "LZECRTCSITCVAHBT"
    result = cse4313_003_pset01.playfair(key, message)
    self.assertEqual(result, answer)    

  def test_Playfair_2_decrypt(self): # 5 pts
    key = "secret"
    message = "LZECRTCSITCVAHBT"
    answer = "MYSECRETMESXSAGE"
    result = cse4313_003_pset01.playfair(key, message, False)
    self.assertEqual(result, answer)

  def test_Playfair_3_encrypt(self): # 5 pts
    key = "inha"
    message = "a"
    answer = "HY"
    result = cse4313_003_pset01.playfair(key, message)
    self.assertEqual(result, answer)    

  def test_Playfair_3_decrypt(self): # 5 pts
    key = "inha"
    message = "HY"
    answer = "AX"
    result = cse4313_003_pset01.playfair(key, message, False)
    self.assertEqual(result, answer)

  def test_Playfair_4_encrypt(self): # 5 pts
    key = "computer"
    message = "I am a Student"
    answer = "HBPRKBCIRLRV"
    result = cse4313_003_pset01.playfair(key, message)
    self.assertEqual(result, answer)    

  def test_Playfair_4_decrypt(self): # 5 pts
    key = "computer"
    message = "HBPRKBCIRLRV"
    answer = "IAMASTUDENTX"
    result = cse4313_003_pset01.playfair(key, message, False)
    self.assertEqual(result, answer)

  # Test cases for Hill (5 pts per each)
  def test_Hill_1_encrypt(self): # 5 pts
    key = "abxbtsbqs"
    message = "THISSANEXAMPLEX"
    answer = "JKPSWUNJXTEUNHV"
    result = cse4313_003_pset01.hill(key, message)
    self.assertEqual(result, answer)    

  def test_Hill_1_decrypt(self): # 5 pts
    key = "abxbtsbqs"
    message = "JKPSWUNJXTEUNHV"
    answer = "THISSANEXAMPLEX"
    result = cse4313_003_pset01.hill(key, message, False)
    self.assertEqual(result, answer)

  # Test cases for Hill (5 pts per each)
  def test_Hill_2_encrypt(self): # 5 pts
    key = "aaxbwdrrv"
    message = "my secret message"
    answer = "YWCBVRQQTYMYOOE"
    result = cse4313_003_pset01.hill(key, message)
    self.assertEqual(result, answer)    

  def test_Hill_2_decrypt(self): # 5 pts
    key = "aaxbwdrrv"
    message = "YWCBVRQQTYMYOOE"
    answer = "MYSECRETMESSAGE"
    result = cse4313_003_pset01.hill(key, message, False)
    self.assertEqual(result, answer)

  # Test cases for Hill (5 pts per each)
  def test_Hill_3_encrypt(self): # 5 pts
    key = "ABXBTSBQS"
    message = "A"
    answer = "GTC"
    result = cse4313_003_pset01.hill(key, message)
    self.assertEqual(result, answer)    

  def test_Hill_3_decrypt(self): # 5 pts
    key = "ABXBTSBQS"
    message = "GTC"
    answer = "AXX"
    result = cse4313_003_pset01.hill(key, message, False)
    self.assertEqual(result, answer)

  # Test cases for Hill (5 pts per each)
  def test_Hill_4_encrypt(self): # 5 pts
    key = "AAXBWDRRV"
    message = "I am a Student"
    answer = "QSYVLDOUHJGN"
    result = cse4313_003_pset01.hill(key, message)
    self.assertEqual(result, answer)    

  def test_Hill_4_decrypt(self): # 5 pts
    key = "AAXBWDRRV"
    message = "QSYVLDOUHJGN"
    answer = "IAMASTUDENTX"
    result = cse4313_003_pset01.hill(key, message, False)
    self.assertEqual(result, answer)

if __name__ == '__main__':
  unittest.main()
