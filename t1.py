print("hello world")
print("This is an example of selection sort")

def selectionSort(arr):
    for i in range (len(arr)):
        min = float('inf')
        for j in range(i+1,len(arr)):
          if(arr[i]>arr[j]):
            arr[i],arr[j] = arr[j],arr[i]

arr = [89,75,41,23,65,12,36,10]

print("Before Sorting", arr)
print(selectionSort(arr))
print("After sorting", arr)
