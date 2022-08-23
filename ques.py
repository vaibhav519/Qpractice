class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def iterativePreOrder(root):
    if not root: return None
    stack = [root]
    while stack:
        root = stack.pop()
        print(root.data)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
    



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
    iterativePreOrder(root)


arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62,
       None, 70, None, None, 87, None, None]

constructTree(arr)
