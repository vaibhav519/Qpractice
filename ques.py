from turtle import goto


class Node:
    def __init__(self, data):
        self.data = data
        self.child = []


nextSmallest = float('-inf')
nextLargest = float('inf')
state = 0
def printCeilFloor(root, ele):
    if root.data < ele:
        global nextSmallest
        nextSmallest = max(nextSmallest, root.data)
        global state
    elif root.data > ele and state == 0:
        global nextLargest
        nextLargest = root.data
        state = 1

    for child in root.child:
        printCeilFloor(child, ele)

    return nextSmallest, nextLargest


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
    printCeilFloor(root, 12)

arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, 110, - 1, 120, -1, -1, 80,
       -1, 90, -1, -1, 40, 100, -1, -1]


constructTree(arr)
print(nextSmallest)
print(nextLargest)