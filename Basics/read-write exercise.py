t = open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\exercise.txt', 'r')
print(t.read())
t = open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\exercise.txt', 'r')
def countNum(a):
    c = 0
    for line in t:
        c = c + line.count(a)
    print(c)
b = input('Number to be counted: ')
countNum(b)
t_out = open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\exercise1.txt', 'w')
t = open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\exercise.txt', 'r')
for line in t:
    n = line.split(',')
    sum = 0
    for num in n:
        sum = sum + int(num)
    t_out.write('Sum: '+ str(sum) + ' |' + line)
t_out = open('C:\\Users\\91974\\Dropbox\\My PC (LAPTOP-8H6ILBDB)\\Documents\\python files\\exercise1.txt', 'r')
print(t_out.read())
t_out.close()
t.close()
