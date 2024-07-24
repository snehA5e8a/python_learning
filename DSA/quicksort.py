
def partition (arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]
    while start < end:
        while arr[start] <= pivot and start<len(arr)-1:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start<end:
            arr[start], arr[end] = arr[end], arr[start] #swaping start and right

    arr[pivot_index], arr[end] = arr[end], arr[pivot_index] #swaping pivot
    return end
def quick_sort(arr, start, end):
    if start<end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi+1, end)

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    print(elements)
    quick_sort(elements, 0, len(elements)-1)
    print(elements)
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    print(elements)
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)

    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements) - 1)
        print(f'sorted array: {elements}')
