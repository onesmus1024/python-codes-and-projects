import array
arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)

def is_sorted(a,n):
    if a[n-1]<a[n-2] and n>=0:
        return print("not sorted")
    else:
        is_sorted(a, n-1)
is_sorted(arr, n)