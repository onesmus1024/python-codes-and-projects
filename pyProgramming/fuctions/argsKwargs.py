ls = [0,9]
num = list(range(*ls))
city_code = dict(kisumu=120,nairobi=122)

def city(list1,city_codes):
    for i in list1:
        print(i,end='')
    print()
    print("#"*100)
    for k,v in city_codes.items():
        print(k + " = ", v)


city(num, city_code)
print("-"*100)
def unpacking(kisumu="130",nairobi="30"):
    print(kisumu)

unpacking(**city_code)