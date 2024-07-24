def bubble_sort(arr):
    l = len(arr)
    i = 0
    while l>0:
        for i in range(l-1):
            if arr[i]> arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                i += 1
        l -= 1
        i =0

def bubble_sort1(arr,key):
    l = len(arr)
    i = 0
    while l>0:
        for i in range(l-1):
            if arr[i][key]> arr[i+1][key]:
                temp = arr[i][key]
                arr[i][key] = arr[i+1][key]
                arr[i+1][key] = temp
                i += 1
        l -= 1
        i =0


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    print(elements)
    bubble_sort(elements)
    print(elements)

    elements = [1,2,3,4,2,0]
    print(elements)
    bubble_sort(elements)
    print(elements)

    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    print(elements)
    bubble_sort(elements)
    print(elements)

    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]
    print(elements)
    bubble_sort1(elements, 'transaction_amount')
    print(elements)



