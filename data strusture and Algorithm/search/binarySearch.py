age = list(range(0,100,10))
print(age)
search_key=int(input("enter number to search:\n"))
def binarySearch(arr=[],search_key=None,arr1=[]):
    list1 = list()
    if  len(arr)==0 or search_key not in arr:
        print("search key not found")
        return 
    else:
        pivot = int(len(arr)/2)
        if search_key != arr[pivot]:
            if search_key<arr[pivot]:
                arr = arr[0:pivot]
                binarySearch(arr,search_key,arr1)
            elif search_key>arr[pivot]:
                arr = arr[pivot:]
                binarySearch(arr,search_key,arr1)
            else:
                pass
        else:
            print("search key found  at index ",end='')
            print(arr1.index(search_key))
        
binarySearch(age,search_key,age)