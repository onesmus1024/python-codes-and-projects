from cryptography.fernet import Fernet

key = Fernet.generate_key()#key generation

#print(key)
cipher = Fernet(key)
message = b'it is getting better each day'
cipherText=cipher.encrypt(message)
print("*"*100)
print("this is the cipher text")
print(cipherText)
print("*"*100)
plainText = cipher.decrypt(cipherText)
print("*"*100)
print("this is the plaintext decrypted")
print(plainText.decode())
print("*"*100)