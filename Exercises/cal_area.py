def calculate_area(b,h,s = 'triangle'):
    if s == 'rectangle':
        area = b*h
        print('area of ', s , 'is ', area)
    elif s == 'triangle':
        area = 0.5*b*h
        print('area of triangle is ', area)
    else:
       print("Sorry, we don't know")
b = int(input('Enter base: '))
h = int(input('Enter height: '))
s = str(input('Enter shape: '))
a = calculate_area(b,h,s)