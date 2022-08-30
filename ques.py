import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(root):
    if root:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)


def isValidBST(root):

    return validate(root, -sys.maxsize, sys.maxsize)


def validate(root, minsize, maxsize):

    if root is None:
        return True

    if root.data < maxsize and root.data > minsize:

        return validate(root.left, minsize, root.data) and validate(root.right, root.data, maxsize)

    else:
        return False


def constructFromPreorder(preorder):
    if not preorder:
        return None

    root = Node(preorder[0])
    temp = root
    stack = [root]
    stack2 = [root]
    i = 1
    while stack and i < len(preorder):
        root = stack.pop()

        if preorder[i] < root.data:
            node = Node(preorder[i])
            root.left = node
            if isValidBST(temp):
                stack.append(node)
                i += 1
            else:
                root = stack2.pop()

        else:
            node = Node(preorder[i])
            root.right = node
            if isValidBST(temp):
                stack.append(node)
                i += 1
            else:
                root = stack2.pop()


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


arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62,
       None, 70, None, None, 87, None, None]

preorder = [8, 5, 1, 7, 10, 12]
constructTree(arr)
