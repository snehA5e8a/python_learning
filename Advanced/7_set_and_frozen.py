set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f'elements in set1 that are not in set 2 is {set1-set2}')
print(f'common elements/intersection of set1 & set 2 are {set1 & set2}')
print(f'showing union of  set1 & set 2 : {set1 | set2}')

s = {'__class__', '__delattr__', '__dir__', '__doc__', '__eq__'}
print('S: ', s)
print(f'type of s: {type(s)} and length: {len(s)}')

fs = frozenset(s)
s.add(4)
print('Is 5 in frozen set of S: ', 5 in fs)
print(s-fs)
