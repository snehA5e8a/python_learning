country = {
    'china': 143,
    'india': 136,
    'usa': 32,
    'pakistan': 21}

def print_all():
    for c in country:
        print(c, '===>', country[c])
    return

def add():
    new_c = input('Enter country name: ')
    if new_c.lower() in country:
            print('It already exists!!')
            return
    else:
        new_p = int(input('Enter population: '))
        country[new_c] = new_p
    print_all()

def query():
    c_name = input('Enter country name to know: ')
    if c_name.lower() in country:
        print(country[c_name.lower()])
    else:
        print("Country doesn't exists")
def remove():
    c_name = input('Enter country name to be removed: ')
    if c_name.lower() in country:
        del country[c_name.lower()]
        print_all()
    else:
        print("Country doesn't exists")
def main():
    command = input("Enter operation (add, remove, query or print'):\n")
    if command.lower() == 'add':
        add()
    elif command.lower() == 'query':
        query()
    elif command.lower() == 'remove':
        remove()
    elif command.lower() == 'print':
        print_all()
if __name__ == '__main__':
    main()
    s = input('Do you want to run again?')