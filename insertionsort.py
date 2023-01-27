#reference - https://www.youtube.com/watch?v=R_wDA-PmGE4

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i 
        while arr[j-1] > arr[j] and j > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        print(arr)

arr = [39, 77, 46, 23, 94, 3, 98, 19, 62, 2]
insertion_sort(arr)
print(arr)
