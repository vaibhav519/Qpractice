import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(self, preorder, inorder):
    if not preorder or not inorder: return None
    
    root = Node(preorder[0])
    mid = inorder.index(preorder[0])
    
    root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
    root.right = self.buildTree(preorder[mid + 1: ], inorder[mid + 1:])
    
    return root


def constructTree(arr):
    root = Node(arr[0])
    stack = [[root, 1]]

    i = 0
    while len(stack) != 0:
        root, state = stack[-1]

        if state == 1:
            i += 1
            stack[-1][1] += 1
            if arr[i] != None:
                node = Node(arr[i])
                root.left = node
                stack.append([node, 1])

        elif state == 2:
            i += 1
            stack[-1][1] += 1
            if arr[i] != None:
                node = Node(arr[i])
                root.right = node
                stack.append([node, 1])

        elif state == 3:
            stack.pop()
    largestBST(root)


arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62,
       None, 70, None, None, 87, None, None]
constructTree(arr)
