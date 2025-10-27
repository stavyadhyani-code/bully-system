class BSTNode:
    def __init__(self, complaint):
        self.complaint = complaint
        self.left = None
        self.right = None
        
class SeverityBST:
    def __init__(self):
        self.root = None

    def insert(self, complaint):
        def _insert(node, complaint):
            if not node:
                return BSTNode(complaint)
            if complaint.severity < node.complaint.severity:
                node.left = _insert(node.left, complaint)
            else:
                node.right = _insert(node.right, complaint)
            return node

        self.root = _insert(self.root, complaint)

    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.complaint)
                _inorder(node.right)
        _inorder(self.root)
