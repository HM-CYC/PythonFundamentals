# Write a Python program to perform encryption and decryption using a predefined

#  مفتاح التشفير و فك التشفير
ENC_KEY = 15
DEC_KEY = -15


#Python ord(), chr() functions bulit in function

#Python ord() and chr() are built-in functions. They are used to convert a character to an int and vice versa.
# Python ord() and chr() functions are exactly opposite of each other.

#  خوارزميه التششفير

def encrypt(test):
    encrypted_test = ''.join(chr(ord(char) + ENC_KEY) for char in test)
    return encrypted_test
 #  خوارزميه فك التشفير
def decrypt(encrypted_test):
    decrypted_test = ''.join(chr(ord(char) + DEC_KEY) for char in encrypted_test)
    return decrypted_test

test = input("Enter a test: ")

encrypted_test = encrypt(test)
print("Encrypted test:", encrypted_test)
decrypted_test = decrypt(encrypted_test)
print("Decrypted test:", decrypted_test)



