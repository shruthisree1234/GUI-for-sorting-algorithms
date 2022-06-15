def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def heapify(arr, n, i):
    largest = i  
    l = 2 * i + 1     
    r = 2 * i + 2     
 
    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)

def partition(arr, start, end):
    pivot_index = start 
    pivot = arr[pivot_index]

    while start < end:

        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if(start < end):
            arr[start], arr[end] = arr[end], arr[start]

    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end

def quickSort(arr, start, end):
    if (start < end):

        p = partition(arr, start, end)
        quickSort(arr, start, p - 1)
        quickSort(arr, p + 1, end)

def partitionThreeWay(arr, first, last, start, mid):
    pivot = arr[last]
    end = last
    
    while (mid[0] <= end):
         
        if (arr[mid[0]] < pivot): 
            arr[mid[0]], arr[start[0]] = arr[start[0]], arr[mid[0]] 
            mid[0] = mid[0] + 1
            start[0] = start[0] + 1
  
        elif (arr[mid[0]] > pivot):
            arr[mid[0]], arr[end] = arr[end], arr[mid[0]]
            end = end - 1
             
        else:
            mid[0] = mid[0] + 1
 
def quickSortThreeWay(arr, first, last):
    if (first >= last):
        return

    if (last == first + 1):
         
        if (arr[first] > arr[last]): 
            arr[first], arr[last] = arr[last], arr[first]
            return

    start = [first]
    mid = [first]
    partitionThreeWay(arr, first, last, start, mid)
    quickSortThreeWay(arr, first, start[0] - 1)
    quickSortThreeWay(arr, mid[0], last)

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1

        arr[j + 1] = key

def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i

        for j in range(i+1, len(arr)):

            if arr[min_idx] > arr[j]:
                min_idx = j
      
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 