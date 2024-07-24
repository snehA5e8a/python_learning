a = int(input('Enter numerator: '))
b = int(input('Enter denominator: '))
try:
    z = a/b
except Exception as e:
    z= 'none'
    print("Whew, we can't do that here because ", e)
    print('Exception type: ', type(e).__name__)
print(a, '/', b, '=', z)
