import argparse
import sys

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--physics', help='Physics Mark')
    p.add_argument('--chemistry', help='Chemistry Mark')
    p.add_argument('--maths', help='Maths Mark')
    # parse_args() returns a "Namespace" object containing arg name & its associated value/ None if no value passed
    marks = p.parse_args()

    print(marks.physics)
    print(marks.chemistry)
    print(marks.maths)

    n = 0  # To get the count of provided args, as the args are optional, not a good code. Best option to make it pos
    if marks.physics:
        phy = int(marks.physics)
        n += 1
    else:
        phy = 0
    if marks.chemistry:
        chem = int(marks.chemistry)
        n += 1
    else:
        chem = 0
    if marks.maths:
        mat = int(marks.maths)
        n += 1
    else:
        mat = 0

    #n = len(vars(marks))  # Namespace obj non iterable, converting to dict using vars() to access values
    print(n)
    avg = (phy+chem+mat)/n
    print('Average of marks: ', avg)
