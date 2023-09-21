numberArray=list(map(int,input('Enter number inputs : ').split()))

def selection_sort(A):
    n=len(A)
    for j in range(0,n-1):
        smallest=j
        for i in range(j+1,n):
            if A[i]<A[smallest]:
                smallest=i
          
        A[j],A[smallest]=A[smallest],A[j]

#B=[12,3,1,4,34,67]
selection_sort(numberArray)
print(numberArray)
