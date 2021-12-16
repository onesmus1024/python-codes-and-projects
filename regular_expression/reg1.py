import re

p = re.compile('ones')
try:
    f1 =open("wordlist.txt","r")
       
except FileNotFoundError as fileError1:
    print(fileError1)
else:
    for line in f1:
        match = p.match(line)
        if(match==None):
            pass
        elif(match.group()=='ones'):
            print("file contain ones")
        else:
            pass
finally:
    if(f1.closed==False):
        f1.close()
    else:
        pass