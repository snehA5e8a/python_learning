phn = {'sneha': 9645900341, 'john': 9745825902, 'divya': 9633738894}
print(phn)
phn['george'] = 8592086118
print(phn)
phn['temp']= 1234
print(phn)
del phn['temp']
print(phn)
print(phn['george'])
for name in phn:
    print('name: ', name, ':: number:', phn[name])
for n,num in phn.items():
    print('name: ', n, 'number: ', num)
