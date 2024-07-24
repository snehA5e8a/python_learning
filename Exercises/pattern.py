def print_pattern(a):
    for i in range(a+1):
        str = ''
        for n in range(i):
            str = str + '*'
        print(str)


a = int(input('Line count: '))
print_pattern(a)