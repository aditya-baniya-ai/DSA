
def finalSolution(root, targetSum):
    currentSum = 0
    
    # root xaina or empty xa bhane return false
    if not root:
        return False
    
    # then call our function which will return a boolean value and we will return that as a final ans
    return pathSum(root, currentSum, targetSum)

def pathSum(node, currentSum, targetSum):
    
    # this means we are in the leaf node
    if not node:
        return False
    
    # when we move forward we will add every node value to the currentSum
    currentSum += node.val
    
    left = pathSum(node.left, currentSum, targetSum)
    right = pathSum(node.right, currentSum, targetSum)
    
    # and check if currentSum is equal to targetSum, then we will return True
    # and we will check this only if this is a leaf node that means it doesnot have right or left node
    
    if (not node.right) and (not node.left):
    
        if currentSum == targetSum:
            return True
    
    return left or right