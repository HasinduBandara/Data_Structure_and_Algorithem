'''A = []

for x in range(10):
    A.append(int(input("Enter a Number: ")))
print(A)

def insertionsort(A):
    for j in range(1,len(A)):
        key = A[j]
        i=j-1
        while (i>0 and A[i]>key):
            A[i+1] = A[i]
            i=i-1
        A[i+1] = key

insertionsort(A)
print('Sorted Array ')

for d in range(len(A)):
    print(A[d])
'''
#*******************QuickSort*********************

    
def partition(arr, low, high):

    i = (low - 1)
    pivot=arr[high]
    for j in range(low,high):
        if arr[j]<= pivot:
            i = i + 1
            arr[i],arr[j] = arr[j], arr[i]
    arr[i+1],arr[high] = arr[high], arr[i+1]
    return(i+1)

def quicksort(arr,low,high):
    if low<high:
        q=partition(arr,low,high)
        quicksort=(arr,low,q-1)
        quicksort=(arr,q+1,high)
quicksort(arr,0,len(arr)-1)
print('Sorted Array...')
for i in range(len(arr)):
    print(arr[i])
        
    
              
                   
                    
     
