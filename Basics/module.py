import math
import calendar
print('Math directory:', dir(math))
a = int(input('Enter the number to find square root: '))
print(math.sqrt(a))
b = int(input('Enter the number to find factorial: '))
print(math.factorial(b))
c = int(input('Enter the number to find log: '))
print('Log to base 10', math.log10(c))
print('Log to base 2', math.log2(c))
m = int(input('Enter your birth month: '))
y = int(input('Enter your birth year: '))
print(calendar.month(y, m))
