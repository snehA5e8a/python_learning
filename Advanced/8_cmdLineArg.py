import argparse

if __name__ == '__main__':
    # The argparse module’s support for command-line interfaces is built around an instance of argparse.ArgumentParser.
    # It is a container for argument specifications and has options that apply to the parser as whole
    # Creating parser object
    parser = argparse.ArgumentParser('calc mini', '3 basic calculations on 2 variables')
    #  Defining arguments
    parser.add_argument('number1', help='first number')
    parser.add_argument('--number2', help='second number')
    parser.add_argument('--operation', help='operation', choices=['add', 'subtract', 'multiply', '+', '-', '*'])

    args = parser.parse_args()  # Parse arguments
    # Access arguments
    print(args.number1)
    print(args.number2)
    print(args.operation)

    n1 = int(args.number1)
    if args.number2:
        n2 = int(args.number2)
    else:
        n2 = 0
    result = None

    if args.operation == 'add' or args.operation == '+':
        result = n1+n2
    elif args.operation == 'subtract' or args.operation == '-':  # Not working for -
        result = n1-n2
    elif args.operation == 'multiply' or args.operation == '*':  # Not working for *
        result = n1*n2

    print('Result = ', result)
