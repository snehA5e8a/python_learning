#not complete, 5 is totally removed

def shel_dupl(a): #created
    div = 2
    gap = len(a)//div
    l = len(a)
    while gap > 0:
        to_del = []
        for i in range(gap, len(a)):
            anchor = a[i]
            j = i
            while j >= gap and a[j-gap] >= anchor:
                if a[j-gap] == anchor:
                    to_del.append(a[j-gap])
                a[j] = a[j-gap]
                j -= gap
            a[j] = anchor
        to_del.sort()
        for i in to_del:
            a.remove(i)
        div *= 2
        gap = len(a)//div
        to_del.sort()
        for i in to_del:
            a.remove(i)

def shell_sort(arr): #copied
    n = len(arr)
    div = 2
    gap = n//div
    while gap > 0:
        index_to_delete = []
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >= temp:
                if arr[j-gap] == temp:
                    index_to_delete.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        index_to_delete=list(set(index_to_delete))
        index_to_delete.sort()
        if index_to_delete:
            for i in index_to_delete[-1::-1]: #last to first in 1 step by step
                del arr[i]
        div *= 2
        n = len(arr)
        gap = n//div


if __name__ == '__main__':
    a = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    print(a)
    shel_dupl(a)
    print(a)