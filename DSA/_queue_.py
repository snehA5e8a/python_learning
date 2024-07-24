from collections import deque
import threading
import time

q = deque()
q.appendleft(5)
q.appendleft(8)
q.appendleft(10)
print(q)
print(q.pop())
print(q.pop())
print(q.pop())




class Queue:

    def __init__(self):
        self.buffer = deque()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
    def pop(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def front(self):
        if len(self.buffer)>0:
            return self.buffer[-1]

    def view_que(self):
        i = 1
        l = len(self.buffer) + 1
        for i in range(l):
            print(' ', self.buffer[-i], ' ')

    def appendleft(self, val):
        return self.buffer.appendleft(val)

order_que = Queue()

def takeOrder(order):
    for o in order:
        print('Taking order: ', o)
        order_que.appendleft(o)
        time.sleep(0.5)

def deliver():
    time.sleep(1)
    while order_que.size()>0:
        o = order_que.pop()
        print('Delivering order: ', o)
        time.sleep(2)

def binary_num(f,l):
    num = deque()
    num.appendleft('1') #start with 1
    j = 0
    for i in range(l):
        front = num[-1]
        if j>f: #printing from f only, though creating binary remains same
            print("", front)
        num.appendleft(front+'0') #add 0 and 1 to the prev numbers to get next 2 binary nums
        num.appendleft(front + '1')
        num.pop()
        j += 1



if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    t1 = threading.Thread(target=takeOrder, args=(orders,))
    t2 = threading.Thread(target=deliver)

    #t1.start()
    #print(order_que.front())
    #t2.start()

binary_num(10,20)



