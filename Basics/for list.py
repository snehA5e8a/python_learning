name = ['sneha', 'John', 'Divya', 'George', 'Aiden', 'Hazel']
age = [31, 32, 29, 27, 4, 3]
if len(age) < len(name):
    n = len(age)
else:
    n = len(name)
total = 0
for i in range(n):
    print('Name: ', name[i], ': Age: ', age[i])
    total = total + age[i]
avg = total/len(age)
print('Average age is: ', avg)


# continue, break - no colon
while (i < 8):
    print(i)
    i = i+1