#lumoto - pivot on end

def partition(arr, start, end):
    pivot = arr[end]
    p_index = start
    for i in range(start, end):
        if arr[i]<=pivot:
            arr[i], arr[p_index] = arr[p_index], arr[i]
            p_index += 1

    arr[p_index],arr[end] = arr[end], arr[p_index]
    return p_index


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
