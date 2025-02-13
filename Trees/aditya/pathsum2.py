def pathSum(self, root, targetSum):
        final = []

        if not root:
            return final

        self.path_finder(root, targetSum, [], final)
        return final

def path_finder(self, node, targetSum, current, final):
    if not node:
        return

    current.append(node.val)

    if (not node.left) and (not node.right):
        if sum(current) == targetSum:
            final.append(list(current))

    self.path_finder(node.left, targetSum, current, final)
    self.path_finder(node.right, targetSum, current, final)

    current.pop()
    
    return
