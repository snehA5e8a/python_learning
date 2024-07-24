n = int(input('Enter the number: '))
print('The odd numbers under ', n, 'are:\n')
for i in range(1, n):
    if i % 2 != 0:
        print(i)

