class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    

def displayTree(root):

    if root:
        print((str(root.left.data) if root.left else 'None') + \
        ' --> ' + str(root.data) + ' <-- ' + \
        (str(root.right.data) if root.right else 'None'))
        displayTree(root.left)
        displayTree(root.right)

    


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

    displayTree(root)


arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62,
        None, 70, None, None, 87, None, None]

constructTree(arr)

