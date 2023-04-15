#chocolate distribution problem



def merge(A,B):
    (m,n)=(len(A),len(B))
    (C,i,j,k)=([],0,0,0)
    while k<m+n:
        if (i==m):
            C.extend(B[j:])
            k=k+(n-j)
        elif(j==n):
            C.extend(A[i:])
            k=k+(m-i)
        elif(A[i]<B[j]):
            C.append(A[i])
            (i,k)=(i+1,k+1)
        else:
            C.append(B[j])
            (j,k)=(j+1,k+1)
    return C
def mergesort(A):
    n=len(A)
    if n<=1:
        return A
    L=mergesort(A[:n//2])
    R=mergesort(A[n//2:])
    B=merge(L,R)
    return B

def findMindiff(arr,n,m):
    if (m==0 or n==0):
        return 0
    arr.sort()
    if n<m:
        return-1
    min_diff=arr[n-1]-arr[0]
    for i in range(len(arr)-m+1):
        min_diff=min(min_diff,arr[i+m-1]-arr[i])

    return min_diff

print (findMindiff([12, 4, 7, 9, 2, 23, 25, 41,
           30, 40, 28, 42, 30, 44, 48,
           43, 50],17,7))