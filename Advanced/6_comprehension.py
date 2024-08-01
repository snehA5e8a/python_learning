# List comprehension
words = ['cat', 'window', 'ball']
print('list print: ', [i for i in words if len(i)>3])

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x == y])

integer = [1, -1, 2, 3, 5, 0, -7]
print('additive inverse: ', [-i for i in integer])

# Dictionary comprehension
integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
print({i:b for i, b in zip(integer, binary)})  # Zip: i/p: lists, o/p: iterable tuples with respective elements


# Set comprehension
integer = [1, -1, 2, -2, 3, -3]
print({i*i for i in integer})  # Initialized as set - so no duplicate
