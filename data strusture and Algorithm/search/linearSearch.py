age =[10,20,30,40,50,60,70,80,90]
search_key = int(input("enter search key:\n"))

if search_key in age:
    for k in age:
      if k == search_key:
        print("search key found at index ",end='')
        print(age.index(search_key))
else:
    print("search key not found")