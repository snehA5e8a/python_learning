#storing multiple values for single key
class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)] #list of list to store multiple values in single has value
    def get_hash(self, key):
        s = 0
        for char in key:
            s += ord(char)
        return s % self.max

    def __getitem__(self, index):
        h = self.get_hash(index)
        for item in self.arr[h]:
            if item[0] == index:
                return item[1]


    def __setitem__(self, key, value):
        h = self.get_hash(key)
        F = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key: #if replacing the value of key
                self.arr[h][idx] = (key, value)
                F = True
        if not F: #not replacing, the hash value of 2 keys are same, so appending
            self.arr[h].append((key, value))


    def __delitem__(self, key):
        h = self.get_hash(key)
        for ind, item in enumerate(self.arr[h]):
if item[0] == key: #item is a dict
                del self.arr[h][ind]


t = HashTable()
print(t.get_hash('march 23'))
print(t.get_hash('march 14'))
t['march 23'] = 23
t['march 14'] = 14
print(t.arr)
t['april 11'] = 'april 11'
t['march 14'] = 50
t['jan 15'] = 'j.pappa'
t['april 16'] = 'pappa'
t['aug 18'] = 'sneha'
print(t.arr)
t.__delitem__('aug 18')
print (t.arr)
