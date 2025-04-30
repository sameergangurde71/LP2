print("hello world")
print("te")

def selectionSort():
    for i in range (len(arr)):
        min = float('inf')
        for j in range(i+1,len(arr)):
          if(arr[i]>arr[j]):
            arr[i],arr[j] = arr[j],arr[i]

print(selctionSort([89,75,41,23,65,12,36,10])
