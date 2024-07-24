#first element with min, second with min of rest of unsorted
def selection_sort(a):
    for i in range(len(a)-1): #first number to right
        min_index = i
        for j in range(min_index+1, len(a)): #optimised from min index
            if a[j] <= a[min_index]: #finding the index of minimum value
                min_index = j
        if i != min_index:
            a[i], a[min_index] = a[min_index], a[i]

def selection_sort_key(a, key):
    for order in key[-1::-1]: #first sort by last key, then that sorted one by first key
        for i in range(len(a)-1): #first number to right
            min_index = i
            for j in range(min_index+1, len(a)):
                if a[j][order] <= a[min_index][order]:
                    min_index = j
            if i != min_index:
                a[i], a[min_index] = a[min_index], a[i]

if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for elements in tests:
        selection_sort(elements)
        print(elements)
    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    selection_sort_key(
        elements, ['First Name', 'Last Name'])
    print(f'Array after Multi-Level Sorting:', *elements, sep='\n')
