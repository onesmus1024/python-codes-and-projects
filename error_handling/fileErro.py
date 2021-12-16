try:
    f1 =open("wordlist.txt","r")
       
except FileNotFoundError as fileError1:
    print(fileError1)
else:
    for line in f1:
        print(line)
finally:
    print("file closed")