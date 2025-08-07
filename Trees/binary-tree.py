class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def search(self, target):
        if target == self.val:
            return True
        elif target < self.val:
            return self.left.search(target) if self.left else False
        else:  # target > self.val
            return self.right.search(target) if self.right else False

class BinaryTree:
    def __init__(self):
        self.root = None

    def search(self, target):
        return self.root.search(target) if self.root else False
