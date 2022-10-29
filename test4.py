# """def permutation(boxes, ci, ti):
#     if ci > ti:
#         for i in range(len(boxes)):
#             print(boxes[i], end=" ")
#         print()
#         return

#     for i in range(len(boxes)):
#         if boxes[i] == 0:
#             boxes[i] = ci
#             permutation(boxes, ci + 1, ti)
#             boxes[i] = 0


# b = [0] * 3
# t = 3
# permutation(b, 1, t)


# # Combination

# def combination(cb, tb, ssf, ts, asf):
#     if cb > len(tb):
#         if ssf == ts:
#             print(asf)
#         return

#     combination(cb + 1, tb, ssf + 1, ts, asf + str(tb[ssf]))
#     combination(cb + 1, tb, ssf, ts, asf + '_')


# boxes = [1, 2, 3, 4]
# items = 2
# combination(1, boxes, 0, items, "")

# print(ord('a'))
# """


# # Python program to perform iterative preorder traversal

# # A binary tree node
# class Node:

#     # Constructor to create a new node
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# leftCount = []
# # An iterative process to print preorder traversal of BT
# def iterativePreorder(root):
#     # Base CAse
#     if root is None:
#         return

#     # create an empty stack and push root to it
#     nodeStack = []

#     nodeStack.append(root)

#     # Pop all items one by one. Do following for every popped item
#     # a) print it
#     # b) push its right child
#     # c) push its left child
#     # Note that right child is pushed first so that left
#     # is processed first */
#     while (len(nodeStack) > 0):
#         i = []
#         # Pop the top item from stack and print it
#         node = nodeStack.pop()
#         print(node.data, end=" ")

#         # Push right and left children of the popped node
#         # to stack
#         if node.right is not None:
#             nodeStack.append(node.right)
#         if node.left is not None:
#             nodeStack.append(node.left)
#             global leftCount
#             leftCount.append(node.left.data)


# # Driver program to test above function
# root = Node(8)

# root.left = Node(9)
# root.right = Node(10)
# root.right.left = Node(13)
# root.right.left.left = Node(7)
# root.left.right = Node(12)
# root.left.right.left = Node(6)
# root.right.right = Node(7)
# root.right.right.left = Node(15)
# root.right.right.right = Node(11)
# root.left.left = Node(11)
# root.left.left.left = Node(6)
# root.left.left.right = Node(9)
# iterativePreorder(root)
# print(leftCount)

s1 = 'bank'
s2 = 'kanb'

s1[0] += 'b'
print(s1)