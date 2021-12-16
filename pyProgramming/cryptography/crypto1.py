import rsa

(public_key,private_key) = rsa.newkeys(1024)
message = b'programming is awesome'

cipherText = rsa.encrypt(message, public_key)
plainText = rsa.decrypt(cipherText, private_key)
message1 = plainText.decode()
print(message1)