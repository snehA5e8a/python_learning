#print name and/or designation for the organisational chart
class TreeNode:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
        self.children = []
        self.parent = None


    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, type):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if type == 'name':
            print(prefix + self.data1)
        if type == 'designation':
            print(prefix + self.data2)
        if type == 'both':
            print(prefix + self.data1 + '(',  self.data2,')')
        if self.children:
            for child in self.children:
                child.print_tree(type)  #calling print tree function again on the child,
                                        # so it will run till there is children in self, if self.children:

    def print_level(self,n):
        s = self.get_level()
        for s in range(n):
            self.print_tree('both')
def build_product_tree():
    root = TreeNode("Nipul", 'CEO')

    Chinmay = TreeNode("Chinmay", 'CTO')
    Chinmay.add_child(TreeNode("Amir", ' Application Head'))
    Vishwa = TreeNode("Vishwa" , 'Infra Lead')
    Vishwa.add_child(TreeNode("Dhaval", 'Cloud Manager'))
    Vishwa.add_child(TreeNode("Abhijith", 'App manager'))
    Chinmay.add_child(Vishwa)


    Gels = TreeNode("Gels", 'HR Lead')
    Gels.add_child(TreeNode("Peter", ' Recruitment Manager'))
    Gels.add_child(TreeNode("Waqas", ' Policy Manager'))


    root.add_child(Gels)
    root.add_child(Chinmay)

    root.print_tree('designation')
    root.print_level(1)

if __name__ == '__main__':
    build_product_tree()

