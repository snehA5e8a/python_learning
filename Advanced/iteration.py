class RemoteControl():
    def __init__(self):
        self.channels = ["HBO","cnn","abc","espn"]
        self.index = -1 #initial position when TV is off

    def __iter__(self):
        return self #ret

    def __next__(self): #implementation of next
        self.index += 1
        if self.index >= len(self.channels):
            raise StopIteration

        return self.channels[self.index]

r = RemoteControl()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


class fib_itr:
    def __init__(self, limit):
        self.limit = limit
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.limit > 1:
            num = self.prev + self.curr
            print(num)
            self.prev = self.curr
            self.curr = num
            self.limit -= 1
        else:
            raise StopIteration

lim = input('Enter the count of Fib series you want to see: ')
fib_print = fib_itr(int(lim))
print(fib_itr)

while True:
    try:
        next(fib_print)
    except StopIteration:
        print(f'First {lim} elements of Fibonacci series')
        break