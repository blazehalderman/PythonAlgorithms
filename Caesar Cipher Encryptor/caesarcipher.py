"""
  Given a non-empty string of lowercase letters and a non-negative integer
  representing a key, write a function that returns a new string obtained by
  shifting every letter in the input string by k positions in the alphabet,
  where k is the key.
"""

def caesarCipherEncryptor(string, key):
    # Write your code here.
	s_string = ""
	
	for i in range(len(string)):
		rot = ord(string[i]) + (key % 26)
		if(rot > 122):
			rot -= 26
		s_string += chr(rot)
    return s_string
