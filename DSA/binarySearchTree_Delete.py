class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, root, value):
        if root is None:
            return root

        # If the value to be deleted is smaller than the root's value,
        # then it lies in left subtree
        if value < root.value:
            root.left = self._delete_recursive(root.left, value)

        # If the value to be deleted is greater than the root's value,
        # then it lies in right subtree
        elif value > root.value:
            root.right = self._delete_recursive(root.right, value)

        # If value is same as root's value, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest
            # in the right subtree)
            root.value = self._min_value(root.right)

            # Delete the inorder successor
            root.right = self._delete_recursive(root.right, root.value)

        return root

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value


# Helper function to insert a new node with the given value
def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if root.value == value:
            return root
        elif root.value < value:
            root.right = insert(root.right, value)
        else:
            root.left = insert(root.left, value)
    return root


# Helper function for inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)


# Example usage
bst = BinarySearchTree()
root = None

# Inserting nodes
keys = [4, 58, 9, 7, 6, 8, 69, 75]
for key in keys:
    root = insert(root, key)

bst.root = root


print("Inorder traversal of the given tree")
inorder(root)

print("\n\nDelete 4")
bst.delete(4)
print("Inorder traversal of the modified tree")
inorder(bst.root)
   