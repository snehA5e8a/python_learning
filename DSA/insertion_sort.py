def insertion_sort(A):
    for i in range (1,len(A)):
        anchor = A[i]
        j = i-1
        while j>=0 and anchor<A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = anchor

if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    print(elements)
    insertion_sort(elements)
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
        insertion_sort(elements)
        print(f'sorted array: {elements}')
