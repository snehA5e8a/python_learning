words = ['cat', 'window', 'ball']
print([i for i in words])

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
print({i:b for i, b in zip(integer, binary) })

integer = [1, -1, 2, 3, 5, 0, -7]
print('additive inverse: ', [-i for i in integer])

integer = [1, -1, 2, -2, 3, -3]
print({i*i for i in integer})
