# Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
# If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum.
# For example two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j


def inversion(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i] > arr[j]):
                count+=1
    return count

arr = list(map(int,input().split())) 
print("Inversion Count of an array are ",inversion(arr))