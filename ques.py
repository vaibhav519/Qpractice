class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def printAllRootToLeavePaths(root, res, s, l, h):
    if not root: return

    if root.left == None and root.right == None:
        s += root.data
        if l <= s <= h:
            print(res + str(root.data))
        return
    
    printAllRootToLeavePaths(root.left, res + str(root.data) + ' ', s + root.data, l, h)
    printAllRootToLeavePaths(root.right, res + str(root.data) + ' ', s + root.data, l, h)
    


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
    printAllRootToLeavePaths(root, " ", 0, 90, 300)


arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62,
       None, 70, None, None, 87, None, None]

constructTree(arr)
