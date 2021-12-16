range1 = [0,10]
num = list(range(*range1))

try:
    index=num.index(4)
    print(index)
except ValueError:
    print(" 4 is not in that range or 4 is not in the list")
else:
    print("the number you are suching is in the list")
    num.append(-1)
    num.insert(0, 20)
    num.sort()
    num.remove(-1)
finally:
    print(num)