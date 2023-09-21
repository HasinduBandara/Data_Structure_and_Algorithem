import math
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
        for t in range(0,(q+1)-i):
            A[r-t]=A[q-t]
    #k-1 changed to k       
    for t in range(0,k):
        #also t+1 is chaged to t
        A[l+t]=TEMP[t]
        
def MERGESORT(A,l,r):
    if l<r:
        q=math.floor((l+r)/2)
        MERGESORT(A,l,q)
        MERGESORT(A,q+1,r)
        MERGE(A,l,q,r)
        
B=[345,56,34,56,33,32,188,90,101,190]   
MERGESORT(B,0,len(B)-1)
print(B)
        
    
