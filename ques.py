class Node:
    def __init__(self, data):
        self.data = data
        self.child = []


diameter = 0
def findDiameter(root):
    global diameter
    max_depth = -1
    second_max_depth = -1

    for child in root.child:
        child_max = findDiameter(child)
        if child_max > max_depth:
            second_max_depth = max_depth
            max_depth = child_max
        elif child_max > second_max_depth:
            second_max_depth = child_max
    
    if max_depth + second_max_depth + 2 > diameter:
        diameter = max_depth + second_max_depth + 2
    
    return max_depth + 1


def levelOrder(root):
    queue = [root]
    while len(queue) != 0:

        for _ in range(len(queue)):
            root = queue.pop(0)
            print(root.data, end=" ")
            for child in root.child:
                queue.append(child)
        print()


def constructTree(arr):
    root = None
    stack = []
    for i in range(len(arr)):
        if arr[i] == -1:
            stack.pop()
        else:
            t = Node(arr[i])
            if len(stack) > 0:
                stack[-1].child.append(t)
            else:
                root = t
            stack.append(t)
    findDiameter(root)
    print(diameter)


arr = [10, 20, 50, -1, 60, 65, -1, -1, -1, 30, 70, -1, 80,
       110, 115, -1, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1]

constructTree(arr)
