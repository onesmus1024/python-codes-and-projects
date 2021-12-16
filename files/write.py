#file in python

file = open("wordlist.txt","w")
number_of_word=int(input("enter number of words to enter in wordlist\n"))
flag = 0
while flag<number_of_word:
    name =input("enter name number "+ str(flag)+"\n ")
    flag=flag+1
    file.write(name)
    
file.close()


