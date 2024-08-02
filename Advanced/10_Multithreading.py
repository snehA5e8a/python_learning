import time
import threading


def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()
calc_cube(arr)
calc_square(arr)
print("No multithreading, done in : ", time.time()-t)

t = time.time()
t1 = threading.Thread(target=calc_square, args=(arr,))  # Argument is a tuple, so ',' is mandatory if only one arg
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()
# Join the main function at this line, main calls join here to get o/p at this point and proceed rest of code after
# completing t1 and t2
t1.join()
t2.join()

print("With multithreading done in : ", time.time()-t)
