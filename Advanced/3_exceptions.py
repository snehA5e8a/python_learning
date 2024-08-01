#try - except - finally
try:
    f = open('C://Users/91974/PycharmProjects/pythonProject/Test Python/Basics/poem for hash.txt')
    # Some expressions which may produce unknown exceptions.
    s = 5/0
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    f.close()
    print('file closed')

# User defined exception
class accident(Exception):
    def __init__(self, msg):
        self.msg = msg
    def print_exception(self):
        print('There is an exception: ', self.msg)

try:
    raise accident('car crash')
except accident as a:
    print('user defined exception:', a)


a = int(input('Enter numerator: '))
b = int(input('Enter denominator: '))
try:
    z = a/b
except Exception as e:
    z = 'none'
    print("Whew, we can't do that here because ", e)
    print('Exception type: ', type(e).__name__)
print(a, '/', b, '=', z)

#try - except - else

a = 3
b = 3
try:
    c = ((a+b) / (a-b))
except ZeroDivisionError:
    print ("a/b result in 0")
else:
    print(c)

