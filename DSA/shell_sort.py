def shell_sort(a):
    gap = len(a)//2
    while gap > 0:
        for i in range(gap, len(a)): #counter for anchors - left of which will be sorted (sub shell of gaps)
            anchor = a[i]
            j = i #counter for left of i
            while j>=gap and a[j-gap] >= anchor: #j>gap to avoid negative indices, once found a left element greater than anchor
                a[j] = a[j-gap] #shift copy that to anchor index
                j -= gap #shifting from left to right - loop to ensure
            a[j] = anchor #once left side of anchor comparisons and copying finished, copy the min number to left of the last
                          #found higher value than anchor, i to next value to and sub array, every element will be compared
        gap = gap//2


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]
    elements = [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1]
    for elements in tests:
        shell_sort(elements)
        print(elements)
