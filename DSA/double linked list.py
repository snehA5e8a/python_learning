class Node:
    def __init__(self,data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Dlinked:
    def __init__(self):
        self.head = None
    def print_forward(self):
        if self.head is None:
            print('This list is empty')
            return
        itr = self.head
        dlist = ''
        while itr:
            dlist += str(itr.data) + '->'
            itr = itr.next
        print(dlist)


    def link_length(self):
        l = 0
        itr = self.head
        while itr:
            l = l + 1
            itr = itr.next
        return l


    def print_backward(self):
        if self.head is None:
            print('This list is empty')
            return
        itr = self.head
        dlist = ''
        while itr.next:
            itr = itr.next
        tail = itr
        while tail:
            dlist+= str(tail.data) + '<-'
            tail = tail.prev
        print(dlist)


    def insert_at_begining(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
        else:
            node = Node(data, None, self.head)
            self.head.prev = node
            self.head = node


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, itr, None)

    def insert_set(self, data_set):
        self.head = None
        for data in data_set:
            self.insert_at_end(data)



    def insert_at(self, index, data):
        if index < 0 or index > self.link_length():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1



if __name__ == '__main__':
    ll = Dlinked()
    ll.insert_set(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    ll.insert_at(6, "dates")
    ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print_forward()


