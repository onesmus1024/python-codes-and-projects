import array as arr
def bubblesort(arr):
    for i in range(0,len(arr)):
        swapped=False
        for j in range(0,len(arr)-1-i):
            
            if arr[j]>arr[j+1]:
                temp =arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                swapped=True
        if not swapped:
            break

    return print(arr)
arr1 = arr.array('i',[1,2,3,4])
arrsorted=[1,2,3,4,5]
arr=[20,6,4,1,]
bubblesort(arr)
bubblesort(arr1)
bubblesort(arrsorted)

