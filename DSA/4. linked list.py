class Node:
    def __init__(self, data=None, Next=None):
        self.data = data
        self.next = Next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None: #if its first node itself
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next: #iterating from head to end, via next value in self.head, until finding end value ie next = none
            itr = itr.next

        itr.next = Node(data, None)


    def print(self):
        if self.head is None:
            print('Linked list is empty')
            return

        itr = self.head
        listt = ''

        i = 1
        while itr:
            listt += str(i) + ') ' + str(itr.data) + '\n'
            itr = itr.next
            i = i+1
        print('Data in the linked list \n')
        print(listt)


    def insert_set(self,data_set):
        self.head = None
        for data in data_set:
            self.insert_at_end(data)

    def link_length(self):
        l = 0
        itr = self.head
        while itr:
            l = l+1
            itr = itr.next
        return l


    def remove_at_index(self, index):
        if index<0 or index >= self.link_length():
            raise Exception('Invalid index')
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count = count +1

    def find_index_value(self, n):
        if n< self.link_length() and n>0:
            itr = self.head
            while n>0:
                itr = itr.next
                n -= 1
            print(itr.data)
        else:
            print('no index ', n)


    def insert_at(self, index, data): #inserting just before the index, so the current value at index will be on index+1
        if index < 0 or index >= self.link_length():
            raise Exception('Invalid index')
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                break
            itr = itr.next


    def remove_by_value(self, key):
        itr = self.head
        if itr.data == key:
            self.head = itr.next
            return

        while itr:
            if itr.next is None:
                break
            if itr.next.data == key:
                itr.next = itr.next.next
                return
            itr = itr.next
        print(key,' not found')



if __name__ == '__main__':
    ll = LinkedList()

    ll.insert_set(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.find_index_value(-5)
    ll.insert_after("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()