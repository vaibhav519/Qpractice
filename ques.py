class Node:
    def __init__(self, data):
        self.data = data
        self.child = []


def getTail(root):
    while len(root.child) == 1:
        root = root.child[0]

    return root


def flatTree(root):
    if len(root.child) == 0:
        return root

    last_node = flatTree(root.child[-1])
    while len(root.child) > 1:
        last_child = root.child.pop()
        second_last = root.child[-1]
        second_last_tail = flatTree(second_last)
        second_last_tail.child.append(last_child)
    return last_node


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
    flatTree(root)
    levelOrder(root)


arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80,
       110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1]
constructTree(arr)
