import collections
age = [10,20,20,20,30,30,30,30,40,50,60,70,80,90]

frequency = collections.Counter(age)
print(frequency)
high=0
number=0
flag=0
for key,value in frequency.items():

    if value>high:
        high=value

        number=key
        
    elif value==high:
        flag=1
        number2=value
if flag == 1:
    print("high frequecy number are ",end=':')
    print(number2,end=',')
    print(number)
else:
    print(number)