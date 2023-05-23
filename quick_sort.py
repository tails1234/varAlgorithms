import time
import timeit
import random
def quicksort(a, low, high):
    if high <= low:
        return
    
    pivot = partition(a, low, high)
    quicksort(a, low, pivot-1)
    quicksort(a, pivot+1, high)
    
def partition(a, low, high):
    if high <= low:
        return
    p = (high+low)//2
    v = a[p]
    l = low
    a[p], a[high] = a[high], a[p]
    h = high-1
    # print(f"pivot: {a[high]} | low: {a[l]} | high: {a[h]}")
    # print(a)
    while l<h:
        while a[l]<=v and l<h:
            l+=1
        while a[h]>v and h>l:
            h-=1
        a[l], a[h] = a[h], a[l]
    if a[high] <= a[h]:
        a[h], a[high] = a[high], a[h]
        p = h
    elif a[high] <=a[h+1]:
        a[h+1], a[high] = a[high], a[h+1]
        p = h+1
    return p

def quicksort2(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index + 1, high)

def partition2(arr, low, high):
    pivot = arr[(low + high) // 2]
    i = low 
    j = high 

    while True:
        # i += 1
        while arr[i] < pivot:
            i += 1

        # j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j
        
        
        if arr[i] == arr[j]:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
    
        
        

a = [0,1,2,3,4,5,6,7,7,8,9,10,7]
s = time.time()
for i in range(10):
    random.shuffle(a)
    quicksort2(a, 0, len(a)-1)
    print(a)
t = time.time()

print(f"time: {t-s}")