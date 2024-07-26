def fib_with_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


try:
    n = int(input('Enter the number under which you want to see fib series: '))
    for f in fib_with_gen(): #yield values of fib_with_gen generator function
        if f < n:
            print(f)
except TypeError as e:
    print(f'{e}: Type error occured')
except ValueError as v:
    print(f'{v}: Value error occured')
