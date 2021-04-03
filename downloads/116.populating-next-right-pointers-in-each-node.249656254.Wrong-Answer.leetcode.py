class Solution(object):
    def connect(self, root):
        if root is None:
            return
        nodes = [root]
        while nodes:
            next_step = []
            last = None
            for node in nodes:
                if node.left:
                    next_step += [node.left]
                if node.right:
                    next_step += [node.right]
                last = node
            nodes = next_step
        return root

