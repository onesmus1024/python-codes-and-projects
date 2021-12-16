def fibo(n):
    if n ==1 or n<=0:
        return 1
    else:
        result =n*fibo(n-1)

    return result


print(fibo(0))