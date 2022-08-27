from functools import lru_cache


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


isBBT = True


def balancedBT(root):
    global isBBT
    if not root: return 0

    left_res = balancedBT(root.left)
    right_res = balancedBT(root.right)

    final_res = abs(left_res - right_res)
    isBBT = True if final_res <= 1 else False

    return max(left_res, right_res) + 1


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
    balancedBT(root)


arr = [3, 9, None, None, 20, 18, None, None, 7, None, None]

constructTree(arr)
print(isBBT)
