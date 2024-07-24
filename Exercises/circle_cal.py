import math
def circle_calc(r):
    area = math.pi* pow(r,2)
    circ = 2 * math.pi * r
    dia = 2*r
    return area, circ, dia

if __name__=='__main__':
    r = int(input('Enter the radius of the circle: '))
    area, circ, dia = circle_calc(r)
    print(f'Area= {area}\nCircumference = {circ} \nDiameter = {dia} ')
