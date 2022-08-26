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

tilt_sum = 0
def tiltSum(root):
    global tilt_sum
    if not root: return 0

    left_res = tiltSum(root.left)
    right_res = tiltSum(root.right)

    tilt_sum += abs(left_res - right_res)

    return left_res + right_res + root.data


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
    tiltSum(root)
    


arr = [50, 25, 12, None, None, 37, 30, None, None, None, 75, 62,
       None, 70, None, None, 87, None, None]

constructTree(arr)
print(tilt_sum)
