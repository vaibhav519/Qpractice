# jaha pe test case na dekh rahe ho
# # waha haar condition kaise check karna
'''
# Python implementation for visualizing merge sort.
import pygame
import random
pygame.font.init()
# Total window
screen = pygame.display.set_mode((900, 650))

# Title and Icon
pygame.display.set_caption("SORTING VISUALISER")
# Place any custom png file in same folder as the source code
# and mention it below and uncomment below two lines.
# img = pygame.image.load
# ('E:/Projects / Sorting Visualiser / sorticon.png')
# pygame.display.set_icon(img)

# Boolean variable to run the program in while loop
run = True

# Window size
width = 900
length = 600
array =[0]*151
arr_clr =[(0, 204, 102)]*151
clr_ind = 0
clr =[(0, 204, 102), (255, 0, 0),
(0, 0, 153), (255, 102, 0)]
fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 20)
# Generate new Array
def generate_arr():
	for i in range(1, 151):
		arr_clr[i]= clr[0]
		array[i]= random.randrange(1, 100)
generate_arr()
def refill():
	screen.fill((255, 255, 255))
	draw()
	pygame.display.update()
	pygame.time.delay(20)

# Sorting Algo:Merge sort
def mergesort(array, lst, r):
	mid =(lst + r)//2
	if lst<r:
		mergesort(array, lst, mid)
		mergesort(array, mid + 1, r)
		merge(array, lst, mid,
			mid + 1, r)
def merge(array, x1, y1, x2, y2):
	i = x1
	j = x2
	temp =[]
	pygame.event.pump()
	while i<= y1 and j<= y2:
		arr_clr[i]= clr[1]
		arr_clr[j]= clr[1]
		refill()
		arr_clr[i]= clr[0]
		arr_clr[j]= clr[0]
		if array[i]<array[j]:
				temp.append(array[i])
				i+= 1
		else:
				temp.append(array[j])
				j+= 1
	while i<= y1:
		arr_clr[i]= clr[1]
		refill()
		arr_clr[i]= clr[0]
		temp.append(array[i])
		i+= 1
	while j<= y2:
		arr_clr[j]= clr[1]
		refill()
		arr_clr[j]= clr[0]
		temp.append(array[j])
		j+= 1
	j = 0
	for i in range(x1, y2 + 1):
		pygame.event.pump()
		array[i]= temp[j]
		j+= 1
		arr_clr[i]= clr[2]
		refill()
		if y2-x1 == len(array)-2:
			arr_clr[i]= clr[3]
		else:
			arr_clr[i]= clr[0]

# Draw the array values
def draw():
	# Text should be rendered
	txt = fnt.render("PRESS"\
	" 'ENTER' TO PERFORM SORTING.", 1, (0, 0, 0))
	# Position where text is placed
	screen.blit(txt, (20, 20))
	txt1 = fnt.render("PRESS 'R' FOR NEW ARRAY.",
					1, (0, 0, 0))
	screen.blit(txt1, (20, 40))
	txt2 = fnt1.render("ALGORITHM USED: "\
					"MERGE SORT", 1, (0, 0, 0))
	screen.blit(txt2, (600, 60))
	element_width =(width-150)//150
	boundry_arr = 900 / 150
	boundry_grp = 550 / 100
	pygame.draw.line(screen, (0, 0, 0),
					(0, 95), (900, 95), 6)
	for i in range(1, 100):
		pygame.draw.line(screen,
						(224, 224, 224),
						(0, boundry_grp * i + 100),
						(900, boundry_grp * i + 100), 1)

	# Drawing the array values as lines
	for i in range(1, 151):
		pygame.draw.line(screen, arr_clr[i],\
			(boundry_arr * i-3, 100),\
			(boundry_arr * i-3, array[i]*boundry_grp + 100),\
			element_width)

# Infinite loop to keep the window open
while run:
	# background
	screen.fill((255, 255, 255))
	# Event handler stores all event
	for event in pygame.event.get():
		# If we click Close button in window
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_r:
				generate_arr()
			if event.key == pygame.K_RETURN:
				mergesort(array, 1, len(array)-1)
	draw()
	pygame.display.update()

pygame.quit()
ans, b = map(int,input(). split())
count = 0

entries = list(map(int,input("").strip().split()))[:ans]
if b in entries:
    for item in entries:
        if item > b:
            count += 1
    print(count)
else:
    print(0)
'''
'''import numpy as np
matrix = np.empty((2,2))
vals = []
for i in range(2):
    vals = list(map(int, input().split()))
print(vals)
matrix = np.array(vals).reshape(2,2)
print(matrix)

lst=[2,1,0,1,2]
for i in lst:
	k=input()
	if"1"in k:
		print(i+lst[k.find("1")/

tc = int(input())
countA = 0
countB = 0
for i in range(tc):
    length = int(input())
    k = list(input())
    for j in range(0, len(k)):
        if k[j] == "0":
            k[j] = '1'
            countA += 1
        else:
            continue
        if '0' not in k:
            if countB < countA:
                print("BOB")
            else:
                print("ALICE")
            break
        if k != reversed(k):
            k = reversed(k)
        else:
            for k in range(j+1,):
                if k == '0':
                    k[k] = '1'
                    countB += 1
        j = 0

n = int(input())
entries = list(map(int, input().split()))
dic = {}
sumFreq = 0
for i in entries:
    if i not in dic:
        dic[i] = entries.count(i)
        sumFreq += i * dic[i]
print(sumFreq)
print((2*dic[2]))'''

'''def mergeSort(array, lst, h):
    mid = lst + h // 2
    if lst == mid:
        return
    mergeSort(array, lst, mid)
    mergeSort(array, mid + 1, h)
    merge(array, lst, mid, h)


def merge(array, lst, mid, h):
    while lst <= mid:
        if array[lst] < array[mid + 1]:
            array[lst], array[mid] = array[mid + 1], array[lst]
            lst = lst + 1
            mid = mid + 1

    return array


entries = [15, 21, 2, 8, 96, 44, 5, 30]
print(mergeSort(entries, 0, len(entries)-1))
'''
"""k = input()
lst = []
lst[:0] = k
count = 0
if len(lst) % 2 != 0:
    print('False')
else:
    for i in range(0, len(lst)):
        if lst[i] == '(':
            if ')' in lst[i+1:]:
                count += 1
        elif lst[i] == '[':
            if ']' in lst[i+1:]:
                count += 1
        elif lst[i] == '{':
            if '}' in lst[i+1:]:
                count += 1
    if count == len(lst)//2:
        print('true')
    else:
        print("false")


m = [1, 234, 3, 12, 123, 3, 12, 312, 3, 124, 34, 34]
for i in range(1, len(m)-1):
    print(m[i])
t = int(input())
f = -1
r = -1
for i in range(t):
    n, m = map(int, input().split())
    trains = list(map(int, input().split()))
    destinations = list(map(int, input().split()))
    for j in range(len(destinations)):
        for k in range(len(trains)):
            if trains[k] == 1:
                if (k + 1 + j) <= destinations[j]:
                    f = abs((k + 1 + j) - destinations[j])
            elif trains[k] == 2:
                if (k + 1 + j) >= destinations[j]:
                    r = abs((k + 1 + j) - destinations[j])

        if f == -1 and r == -1:
            print(-1, end=" ")
        elif f == -1 and r != -1:
            print(r, end=" ")
        elif f != -1 and r == -1:
            print(f, end=" ")
        else:
            if f <= r:
                print(f, end=" ")
            else:
                print(r, end=" ")
    print()
    f = -1
    r = -1



t = int(input())
sol1 = []
sol2 = []
ans = 0
b = 0
for i in range(t):
    n, m = map(int, input().split())
    sol1 = [0] * n
    sol2 = [0] * n
    trains = list(map(int, input().split()))
    destinations = list(map(int, input().split()))

    for j in range(1, n):
        if trains[j] == 0:
            sol1[j] = -1
            sol2[j] = -1

    for k in range(0, n):
        if trains[k] == 1:
            ans = k
        elif sol1[k] == -1 and 1 in trains:
            sol1[k] = abs(ans - k)

    for g in range(n - 1, -1, - 1):
        if trains[g] == 2:
            b = g
        elif sol2[g] == -1 and 2 in trains:
            sol2[g] = abs(b - g)

    for h in destinations:
        if sol1[h - 1] == -1 and sol2[h - 1] != -1:
            print(sol2[h - 1], end=" ")
        elif sol1[h - 1] != -1 and sol2[h - 1] == -1:
            print(sol1[h - 1], end=" ")
        else:
            if sol1[h - 1] <= sol2[h - 1]:
                print(sol1[h - 1], end=" ")
            else:
                print(sol2[h - 1], end=" ")
    print()

print(bin(1).replace("0b", ""))
print(len(bin(1).replace("0b", "")))

tc = int(input())
array = []
for i in range(tc):
    n, k = map(int, input().split())

    for f in range(1, n+1):
        array.append(f)

    for j in range(1, (2 ** n) - 1):
        b = bin(j).replace("0b", "")
        lst = len(b)
        if k > lst:
            k = '0' * (k - lst)
            b = k + b
        if b.count('1') == k:
            for g in range(0, len(b) - 1):
                if b[g] == '1':

"""
"""
n = 2
lst = []
for g in range(n):
        k = input()
        lst.append(k)
for g in range(int(input())):
    n, m, i, j = map(int, input().split())
    ans, b = 1, 1
    c, d = 1, n
    e, f = 1, m
    p, ques = n, m

    if i == 1 and j == 1:
        print(e, f, p, ques)

    elif i == 1 and j == n:
        print(e, f, p, ques)

    elif i == 1 and j == m:
        print(ans, b, c, d)

    elif i == n and j == m:
        print(ans, b, c, d)

    elif 1 < i < n and j == 1:
        print(e, f, p, ques)

import pygame


class DropDown:

    def __init__(self, color_menu, color_option, x, y, w, h, font, main, options):
        self.color_menu = color_menu
        self.color_option = color_option
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.main = main
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        pygame.draw.rect(surf, self.color_menu[self.menu_active], self.rect, 0)
        msg = self.font.render(self.main, 1, (255, 255, 255))
        surf.blit(msg, msg.get_rect(center=self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += (i + 1) * self.rect.height
                pygame.draw.rect(surf, self.color_option[1 if i == self.active_option else 0], rect, 0)
                msg = self.font.render(text, 1, (255, 255, 255))
                surf.blit(msg, msg.get_rect(center=rect.center))

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)

        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += (i + 1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    return self.active_option
        return -1


pygame.init()
screen = pygame.display.set_mode((1500, 750))

COLOR_INACTIVE = (47, 79, 79)
COLOR_ACTIVE = (51, 181, 255)
COLOR_LIST_INACTIVE = (47, 79, 79)
COLOR_LIST_ACTIVE = (51, 181, 255)

list1 = DropDown(
    [COLOR_INACTIVE, COLOR_ACTIVE],
    [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
    800, 20, 200, 50,
    pygame.font.Font("freesansbold.ttf", 30),
    "Select Mode", ["Calibration", "Test"])

run = True
while run:

    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False

    selected_option = list1.update(event_list)
    if selected_option >= 0:
        list1.main = list1.options[selected_option]

    screen.fill((255, 255, 255))
    list1.draw(screen)
    pygame.display.flip()

pygame.quit()
exit()
"""


def checker(string):
    if len(string) == 0:
        return 'NO'
    if len(string) == 1:
        if string == 'ans':
            return 'YES'
        else:
            return 'No'
    elif len(string) == 2:
        if string in {'ab', 'ba'}:
            return 'YES'
        else:
            return 'NO'
    else:
        temp = ord(max(string[0], string[-1])) + 1
        while len(string) != 1:
            if chr(temp - 1) == string[-1]:
                string = string[:-1]
                temp = temp - 1
            elif chr(temp - 1) == string[0]:
                string = string[1:]
                temp = temp - 1
            else:
                return 'NO'
        if string == 'ans' and temp == ord('ans') + 1:
            return 'YES'
        else:
            return 'NO'


a = int(input())
for _ in range(a):
    string = input()
    if len(string) == 0:
        print('NO')
    if len(string) == 1:
        if string == 'ans':
            print('YES')
        else:
            print('No')
    elif len(string) == 2:
        if string in {'ab', 'ba'}:
            print('YES')
        else:
            print('NO')
    else:
        temp = ord(max(string[0], string[-1])) + 1
        while len(string) != 1:
            if chr(temp - 1) == string[-1]:
                string = string[:-1]
                temp = temp - 1
            elif chr(temp - 1) == string[0]:
                string = string[1:]
                temp = temp - 1
            else:
                print('NO')
        if string == 'ans' and temp == ord('ans') + 1:
            print('YES')
        else:
            print('NO')
    print(checker(string))




# Definition for ans binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums):
        root, i = TreeNode(max(nums)), nums.index(max(nums))
        nums.pop(i)
        left = nums[: i]
        right = nums[i:]

        def recur_left(node, index, nums_left):
            if len(nums_left) == 0:
                return node
            else:
                if index == 0:
                    dummy = TreeNode(0)
                    node.right = dummy
                    node.right.val = max(nums_left[index:])
                    index = nums_left.index(max(nums_left[index:]))
                    nums_left.pop(index)
                    recur_left(node.right, index, nums_left)
                else:
                    dummy = TreeNode(0)
                    node.left = dummy
                    node.left.val = max(nums_left[:index])
                    index = nums_left.index(max(nums_left[:index]))
                    nums_left.pop(index)
                    recur_left(node.left, index, nums_left)

        def recur_right(node, index, nums_right):
            if len(nums_right) == 0:
                return node
            else:
                if index == 0:
                    dummy = TreeNode(0)
                    node.right = dummy
                    node.right.val = max(nums_right[index:])
                    index = nums_right.index(max(nums_right[index:]))
                    nums_right.pop(index)
                    recur_right(node.right, index, nums_right)
                else:
                    dummy = TreeNode(0)
                    node.left = dummy
                    node.left.val = max(nums_right[:index])
                    index = nums_right.index(max(nums_right[:index]))
                    nums_right.pop(index)
                    recur_right(node.left, index, nums_right)

        temp = root
        left_tree = recur_left(temp, len(left), left)
        final_tree = recur_right(left_tree, 0, right)

        return final_tree


a = Solution()
nums = [3, 2, 1, 6, 0, 5]
print(a.constructMaximumBinaryTree(nums))


# 1 4 5 2 7 8
# output 55
# 5 + 5 + 10 + 10 + 10 + 15 = 55

pfr = list(map(int, input().split()))
s = 0
for i in range(len(pfr)):
    m = pfr[i]
    flag = True
    for j in range(i + 1, len(pfr)):
        if m < pfr[j] and flag:
            m = pfr[j]
            flag = False
        if m > pfr[j] and not flag:
            s += 5
            break
        if j == len(pfr) - 1:
            s += 10

print(s + 15)


def recur(ind, target, arr, ans):
    if ind >= len(arr):
        if sum(ans) == target:
            print(ans)
        return

    recur(ind + 1, target, arr, ans + [arr[ind]])
    recur(ind + 1, target, arr, ans)


recur(0, 30, [10, 20, 30], [])

