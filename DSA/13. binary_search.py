def linear_search(arr, val):
    for index, element in enumerate(arr):
        if element==val:
            return index
    return -1

def binary_search(arr,val,start, end):
    mid = (start+end)//2
    if (arr[0] == val): #finding val
        return 0
    while start<=end:
        if arr[mid] ==val:
            return mid
        if arr[mid] < val: #searching right side
            start = mid+1
            return binary_search(arr, val, start, end)
        if arr[mid]>val: #searching left side
            end = mid -1
            return binary_search(arr, val,start, end)
    return -1 #if not found

def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find,0, len(numbers)-1)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)




if __name__ == '__main__':
    numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 22

    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search")
    index = binary_search(numbers_list, number_to_find, 0, len(numbers_list)-1)
    print(f"Number found at index {index} using binary search")

    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 17
    indices = find_all_occurances(numbers, number_to_find)
    print(f"Indices of occurances of {number_to_find} are {indices}")
