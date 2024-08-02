def check_neg(fun):
    def parameter(x):
        if type(x) is int and x > 0:
            return fun(x)
        else:
            raise Exception('Argument is not a non negative integer:', x)
    return parameter


@check_neg
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)


if __name__ == '__main__':
    for i in [1.345, -1, 10]:
        try:
            print(factorial(i))
        except Exception as e:
            print(e)

