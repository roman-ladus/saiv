# saiv/sorting.py

def merge_sort(arr, capture_frame=None):
    if capture_frame:
        capture_frame(arr)
    
    def _merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            _merge_sort(L)
            _merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i]['value'] <= R[j]['value']:
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

            if capture_frame:
                capture_frame(arr)

    _merge_sort(arr)


def quick_sort(arr, capture_frame=None):
    if capture_frame:
        capture_frame(arr)
    
    def _quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            if capture_frame:
                capture_frame(arr)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]['value']
        i = low - 1
        for j in range(low, high):
            if arr[j]['value'] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)


def heap_sort(arr, capture_frame=None):
    if capture_frame:
        capture_frame(arr)
    
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left]['value'] > arr[largest]['value']:
            largest = left
        
        if right < n and arr[right]['value'] > arr[largest]['value']:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            if capture_frame:
                capture_frame(arr)
            heapify(arr, n, largest)
    
    n = len(arr)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        if capture_frame:
            capture_frame(arr)
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        if capture_frame:
            capture_frame(arr)
        heapify(arr, i, 0)
