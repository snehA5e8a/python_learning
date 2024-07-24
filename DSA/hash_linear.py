class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]
    def get_hash(self, key):
        s = 0
        for char in key:
            s += ord(char)
        return s % self.max

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]


    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            for h in range(self.max): #searching for next empty slot
                if self.arr[h] is None:
                    self.arr[h] = (key, value)
                    print('Key was already taken, it is filled in ', h)
                    break


    def __delitem__(self, key):
        h = self.get_hash(key)
        del self.arr[h]


t = HashTable()
t['march 23'] = 23
t['march 14'] = 14
t['march 32'] = 28
print(t.arr)
t['april 11'] = 'april 11'
t['march 14'] = 50
t['jan 15'] = 'j.pappa'
t['april 16'] = 'pappa'
t['aug 18'] = 'sneha'
print(t.arr)
t.__delitem__('aug 18')
print (t.arr)
