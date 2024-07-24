def running_avg(A):
    for i in range(1, len(A)):
        anchor = A[i]
        j = i - 1
        while j >= 0 and anchor < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = anchor

        if i == 1:
            median = (A[0]+A[1])/2
            print(median, '\n')
        elif i%2 == 0: #if odd number of elements
            print(A[(i//2)],'\n')
        else: #if even number of elements
            m = (i + 1)//2 #avg of middle 2, middle first index
            median = (A[m]+A[m-1])/2
            print(median, '\n')

            #even index 4 - odd number of elements 5 - middle element 3 ie 5//2
            #odd index 5 - even number of elements 6 - middle 2: 3&4 - half of i+1/2


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    print(elements)
    running_avg(elements)
    print(elements)


