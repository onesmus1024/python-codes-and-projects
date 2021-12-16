from cryptography.fernet import Fernet

try:
    f1 = open("wordlist.txt","wb")
except FileNotFoundError as fileErro:
    print(fileErro)
else:
    f1.write(Fernet.generate_key())
finally:
    f1.close()
try:
    f2 = open("wordlist.txt","rb")
except FileNotFoundError as fileErro:
    print(fileErro)
else:
    print(f2.read().decode())
finally:
    f2.close()