import array as arr1
nums=[]
for k in reversed(range(0,100)):
    nums.append(k)
print(nums)
arr1 = arr1.array('i',[2,3,7,8,10])
age1 =list(arr1)
age =[14,3,4]

def selectionsort(arr):

    for i in range(0,len(arr)-1):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]:
                min=j
        temp=arr[i]
        arr[i]=arr[min]
        arr[min]=temp

    return print(arr)

selectionsort(nums)
