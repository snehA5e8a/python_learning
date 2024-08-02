import time


def time_it(func):  # Function taken as arg to the function
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)  # To be called inside wrapper function
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper


@time_it  # Equivalent to calc_square = time_it(cal_square)
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result


@time_it  # Equivalent to calc_cube = time_it(cal_cube)
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result


array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
print(out_cube[:5], out_cube[99995:])
