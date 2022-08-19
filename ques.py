class Node:
    def __init__(self, data):
        self.data = data
        self.child = []


def rootToNodePath(root, ele):
    if root.data == ele:
        return [root.data]

    for child in root.child:
        sub_ans = rootToNodePath(child, ele)
        if len(sub_ans) > 0:
            sub_ans.append(root.data)
            return sub_ans
    return []


def distanceBetweenNodes(root, ele1, ele2):
    path1 = rootToNodePath(root, ele1)
    path2 = rootToNodePath(root, ele2)

    i = len(path1) - 1
    j = len(path2) - 1
    while i >= 0 and j >= 0 and path1[i] == path2[j]:
        i -= 1
        j -= 1
    
    i += 1
    j += 1

    return i + j

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
    print(distanceBetweenNodes(root, 70, 110))
    #levelOrder(root)


arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80,
       110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1]
constructTree(arr)