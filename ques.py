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


diameter = 0
def findDiameter(root):
    if not root: return -1

    global diameter
    max_depth = -1
    second_max_depth = -1

    max_left = findDiameter(root.left)
    max_right = findDiameter(root.right)

    child_max = max(max_left, max_right)
    
    if child_max > max_depth:
        second_max_depth = max_depth
        max_depth = child_max
    elif child_max > second_max_depth:
        second_max_depth = child_max
    
    if max_depth + second_max_depth + 2 > diameter:
        diameter = max_depth + second_max_depth + 2
    
    return max_depth + 1

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
    print(findDiameter(root))
    


arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62,
       None, 70, None, None, 87, None, None]

constructTree(arr)
