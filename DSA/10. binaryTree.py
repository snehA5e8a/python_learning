class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if self.data == data:
            return
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTree(data)

        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTree(data)

    def inOrder(self): #smallest to root to largest, root value in between left and right tree - ascending order
        elements = []
        if self.left:
            elements += self.left.inOrder()

        elements.append(self.data) #once left done of lowest level

        if self.right:
            elements += self.right.inOrder()

        return elements

    def search(self, val):
        if self.data == val: #handling the end case
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self): #leftmost is minimum
        if self.left:
            return self.left.find_min()
        else:
            return self.data #end case



    def find_max(self): #rightmost is max
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        elements = self.inOrder()
        s = 0
        for i in elements:

            s += i
        return s
        #left_sum = self.left.calculate_sum() if self.left else 0
        #right_sum = self.right.calculate_sum() if self.right else 0
        #return self.data + left_sum + right_sum

    def preOrder(self): #root to left to left then right
        elements = [self.data]
        if self.left:
            elements += self.left.preOrder()
        if self.right:
            elements += self.right.preOrder()
        return elements
    def postOrder(self): #smallest level left and right then upper, last root
        elements = []
        if self.left:
            elements += self.left.postOrder()
        if self.right:
            elements += self.right.postOrder()
        elements.append(self.data) #lowest level to upper to root
        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.left.find_max()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self



def buildTree(elements):
    root = BinarySearchTree(elements[0])
    for i in range(1, len(elements)):
        root.addChild(elements[i])
    return root


if __name__ == '__main__':
    #countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    #country_tree = buildTree(countries)
    #print("UK is in the list? ", country_tree.search("UK"))
    #print("Sweden is in the list? ", country_tree.search("Sweden"))


    num = [4, 58, 9, 7, 6, 8, 69, 75]
    num_tree = buildTree(num)
    print(num_tree.preOrder())
    num_tree.delete(4)
    print(num_tree.preOrder())


