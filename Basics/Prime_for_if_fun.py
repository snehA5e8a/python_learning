def prime():
    print('__name__:', __name__)
    n = int(input('Enter the number: '))
    listp = []
    for i in range(2, n + 1):
        p = True
        for j in range(2, i):
            if i % j == 0:
                p = False
                j = i
        if p:
            listp.append(i)
    print(listp)
    print('There are', len(listp), ' prime numbers under', n)
    cont = input('Do you want to continue?')
    return cont

v = prime()

if 'y' in v:
    prime()
else:
    print('Thank you, hope you enjoyed it')
