import math
#merge two sorted arrays
def MERGE(A,l,q,r):
    #in tute it is i=1 but it should be i=l
    i=l
    j=q+1
    k=0
    #temp array created with r elements
    TEMP=[0]*(r) 
    while i <= q and j<=r:
        #k from here to
        if A[i] <= A[j]:
            TEMP[k]=A[i]
            i=i+1 
        else:
            TEMP[k]=A[j]
            j=j+1 
        #k is moved to this position    
        k=k+1     

    if j>r:
        #q  chaged to q+1
        #to fill the values that is not taken from left array
        for t in range(0,(q+1)-i):
            A[r-t]=A[q-t]
    #copy from temp array to original array        
    #k-1 changed to k       
    for t in range(0,k):
        #also t+1 is chaged to t
        A[l+t]=TEMP[t]
#merge sort functions        
def MERGESORT(A,l,r):
    if l<r:
        q=math.floor((l+r)/2)
        MERGESORT(A,l,q)
        MERGESORT(A,q+1,r)
        MERGE(A,l,q,r)
#binary search method
def binarySearch(A,minn,maxx,key):
    if maxx < minn:
        return False
    
    else:
        mid =math.floor((minn+maxx)/2)
        
        if A[mid]<key:
            return binarySearch(A,mid+1,maxx,key)
        elif A[mid]>key:
            return binarySearch(A,minn,mid-1,key)
        else:
            return mid
            
numbers=list(map(int,input("Enter your numbers: ").split()))


flag=True
while flag:
    try:
        number=int(input("Enter the number that wated to be searched : "))
        flag=False
    except:
        print("Please enter a number")
        flag=True

output=binarySearch(numbers,0,len(numbers),number)    
if(output):
    print("Number is found with index ",output)
else:
    print("Number is not found.")
