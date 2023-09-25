
###########################################################################
# HEADER COMMENTS
###########################################################################
### __filename__ = "cse4313_003_pset01.py"
### __Python version__ = "3.11.0"
### __copyright__ = "Copyright 2022, CSE4313 Problem Set 01"
### __credits__ = ["Jieung Kim", "XXX"]
### __license__ = "GPL"
### __version__ = "1.0.0"
###########################################################################

import numpy as np
import string

"""
Please keep in mind the following items for all questions:
1. To work with valid input/output pairs, refer to the 
   test cases provided in `cse4313_003_pset01_test.py`.
2. There are no hidden test cases. So, if you pass all test cases in 
   `cse4313_003_pset01_test.py`, you will get the full credit 
   (type `python3 cse4313_003_pset01_test.py`).
3. Please implement the function efficiently and consider additional helper 
   functions if needed.
4. While you are free to implement additional functions, DO NOT CHANGE THE 
   SIGNATURE OF THE TOP-LEVEL FUNCTION.
   - def CRT(n, r):
   - def playfair(key, message, encrypt=True):
   - def Hill(key, message, encrypt=True):
5. You are free to import any other packages (e.g., numpy) in this file,
   but DO NOT TOUCH ANYTHING IN THE TEST FILE.
6. If there are any unclear parts while implementing these functions,
   please feel free to ask any questions through any channels available.
"""

###########################################################################
# Chinese remainder theorem (20 pts)
###########################################################################
"""
This function implements the Chinese Remainder Theorem (CRT) to find a 
unique value of x mod N, given a list of mod values (n_1, n_2, ..., n_n)
and their corresponding residues (r_1, r_2, ..., r_n).

Parameters:
  n: list of mod values
  r: list of residues
Returns:
  A list [x, N], where x is the unique solution mod N
"""  
def CRT(n, r):
  prod = 1
  for i in range(len(n)):
    prod *= n[i]
    
  cnt = 0
  for i in range(len(n)):
    p = prod // n[i]
    gcd, x, y = EEA(p, n[i])
    cnt += r[i] * x * p

  result = [cnt % prod, prod]

  return result

def EEA(a, b):
  if b == 0:
    return a, 1, 0
  
  gcd, x1, y1 = EEA(b, a % b)
  x = y1
  y = x1 - (a // b) * y1
  
  return gcd, x, y

 
###########################################################################
# Playfair cipher (40 pts)
###########################################################################
"""
This function implements the Playfair cipher with the given key string
and message. In this case, we assume the key table with I and J together
in the same cell.

Parameters:
  key: key string
  message: message string
  encrypt: True if we hope to encrypt the message with the given key.
           False if we hope to decrypt the message with the given key.

Returns:
  return_message: an encrypted or decrypted message written in upper case.

Notes:
1. The return value (return_message) always consists of upper case 
   characters. This implies that you have to transform lower case
   characters in the key and/or message parameters into upper case
   characters. It is recommended that you convert the input text to
   upper case characters as soon as the top-level function is called 
   if it contains lower case characters.
2. Similarly, the return value (return_message) does not contain
   any whitespace. This implies that you have to remove whitespace
   in the message parameter. It is recommended that you remove whitespaces
   as soon as the top-level function is called if it contains whitespaces.
3. For the odd number of messages and the messages that contain two
   identical characters in adjacent locations, please follow the rule in 
   the slide, book, and the explanation during the lecture (add X).
4. The key string can have the same letter multiple times.
   In this case, key generation will ignore those letters from
   the second occurrence.
"""
def playfair(key, message, encrypt=True):
  matrix = playfair_matrix(key)

  if(encrypt == True):
    result = playfair_encrypt(message, matrix)
  else:
    result = playfair_decrypt(message, matrix)

  return result

def playfair_matrix(keyword):
  key = ""
  for i in keyword.upper():
    if i not in key and i in string.ascii_uppercase:
      key += i
  for i in string.ascii_uppercase:
    if i not in key and i != 'J':
      key += i

  matrix = [key[i:i+5] for i in range(0, 25, 5)]
  
  return matrix

def get_position(matrix, ch):
  for i, row in enumerate(matrix):
    if ch in row:
      return i, row.index(ch)
  return None, None

def playfair_encrypt(plaintext, matrix):
  pairs = []
  plaintext = plaintext.replace(" ", "")
  plaintext = plaintext.upper().replace("J", "I")
  
  for i in range(0, len(plaintext), 2):
    if i == len(plaintext)-1:
      pairs.append((plaintext[i], "X"))
    elif plaintext[i] == plaintext[i+1]:
      pairs.append((plaintext[i], "X"))
      pairs.append((plaintext[i+1], "X"))
    else:
      pairs.append((plaintext[i], plaintext[i+1]))

  ciphertext = ""
  for pair in pairs:
    row1, col1 = get_position(matrix, pair[0])
    row2, col2 = get_position(matrix, pair[1])
    if row1 == row2:
      ciphertext += matrix[row1][(col1+1)%5]
      ciphertext += matrix[row2][(col2+1)%5]
    elif col1 == col2:
      ciphertext += matrix[(row1+1)%5][col1]
      ciphertext += matrix[(row2+1)%5][col2]
    else:
      ciphertext += matrix[row1][col2]
      ciphertext += matrix[row2][col1]

  return ciphertext

def playfair_decrypt(ciphertext, matrix):
  pairs = []
  for i in range(0, len(ciphertext), 2):
    pairs.append((ciphertext[i], ciphertext[i+1]))

  plaintext = ""
  for pair in pairs:
    row1, col1 = get_position(matrix, pair[0])
    row2, col2 = get_position(matrix, pair[1])
    if row1 == row2:
      plaintext += matrix[row1][(col1-1)%5]
      plaintext += matrix[row2][(col2-1)%5]
    elif col1 == col2:
      plaintext += matrix[(row1-1)%5][col1]
      plaintext += matrix[(row2-1)%5][col2]
    else:
      plaintext += matrix[row1][col2]
      plaintext += matrix[row2][col1]

  return plaintext

###########################################################################
# Hill cipher (40 pts)
###########################################################################
"""
This function implements the Hill cipher with the given key string
and message. We assume that the matrix size is always 3 x 3, which 
implies that the key will always consists of 9 characters.

Parameters:
  key: key string
  message: message string
  encrypt: True if we hope to encrypt the message with the given key.
           False if we hope to decrypt the message with the given key.

Returns:
  return_message: an encrypted or decrypted message written in upper case.

Notes:
1. The return value (return_message) always consists of upper case 
   characters. This implies that you have to transform lower case
   characters in the key and/or message parameters into upper case
   characters. It is recommended that you convert the input text to
   upper case characters as soon as the top-level function is called 
   if it contains lower case characters.
2. Similarly, the return value (return_message) does not contain
   any whitespace. This implies that you have to remove whitespace
   in the message parameter. It is recommended that you remove whitespaces
   as soon as the top-level function is called if it contains whitespaces.
3. When the input message cannot be divided by 3 (after removing whitespaces),
   Add minimum numbers of "X" at the end to make it to be divided by 3.
4. We represent each letter from A to Z with a number from 0 to 25.
5. The key is separated into three-letter blocks (strings), and each block
   becomes a row in the matrix K. Each letter is substituted by a number in
   the same way as the plaintext. For example, "RRFVSVCCT" becomes:
     [[17, 17, 5],
      [21, 18, 21],
      [2, 2, 19]]
6. We always assume that users provide a key that has an inverse key.
   This implies that you do not need to perform a sanity check on the key
   to see if it can generate a decrypt key. We do not handle this scenario
   in our test cases either.
"""
def hill(key, message, encrypt=True):
  if(encrypt == True):
    result = hill_encrypt(message, key)
  else:
    result = hill_decrypt(message, key)

  return result

def text_to_matrix(text):
  message = [ord(char) - 65 for char in text]
  matrix = np.array(message).reshape(-1, 3).T
  
  return matrix

def key_to_matrix(key):
  key = [ord(char) - 65 for char in key]
  matrix = np.array(key).reshape(3, 3)
  
  return matrix

def matrix_to_text(matrix):
  text = ''
  for row in matrix:
    for elem in row:
      text += chr(elem + 65)
  return text

def hill_encrypt(plaintext, key):
  plaintext = plaintext.replace(" ","")
  plaintext = plaintext.upper()
  
  while len(plaintext) % 3 != 0:
    plaintext += 'X'
  
  key = key.upper()
  
  plain_matrix = text_to_matrix(plaintext)
  key_matrix = key_to_matrix(key)
  cipher_matrix = np.matmul(key_matrix, plain_matrix).T % 26
  cipher_text = matrix_to_text(cipher_matrix)
  return cipher_text

def hill_decrypt(cipher_text, key):
  key = key.upper()
  cipher_matrix = text_to_matrix(cipher_text)
  key_matrix = key_to_matrix(key)
  inverse_key = np.linalg.inv(key_matrix)
  plain_matrix = np.matmul(inverse_key, cipher_matrix).T % 26
  plain_text = matrix_to_text(plain_matrix)
  return plain_text
