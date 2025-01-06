def bubble_sort(arr, *args):
    n = len(arr)
    swaped = False
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaped = True
        if not swaped:
            break
    return arr