arr = list(range(0,100,10))
print(arr)
print(len(arr))
search_key =int(input("enter your search key:\n"))


def BinarySearch(arr,low,high,search_key):
    if high>=low:
        mid = int((high+low)/2)
        print(mid)
        if arr[mid]==search_key:
            print("search key found at index ",end='')
            print(arr.index(search_key))
        elif search_key>arr[mid]:
            return BinarySearch(arr,mid+1,high,search_key)
        elif search_key<arr[mid]:
            return BinarySearch(arr,low,mid-1,search_key)
    else:
        print("element is not in the array")
            



BinarySearch(arr,0,len(arr),search_key)