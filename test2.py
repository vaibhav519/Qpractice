"""for _ in range(int(input())):
    n, a, b = map(int, input().split())
    lst_right = []
    lst_left = []
    for i in range(1, b):
        lst_right.append(i)
    for j in range(a + 1, n + 1):
        lst_left.append(j)
    for k in lst_right:
        if k in lst_left:
            lst_left.remove(k)
    for g in lst_left:
        if g in lst_right:
            lst_right.remove(g)
    if a in lst_right:
        lst_right.remove(a)
    if b in lst_left:
        lst_left.remove(b)
    if len(lst_right) < (n / 2) - 1 or len(lst_left) < (n / 2) - 1:
        print(-1)
    else:
        print(a, lst_left, b, lst_right)
for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    count = 0
    flag = b[n - 1] > a[n - 1]
    if flag:
        count += 1
    for i in range(n - 2, -1, - 1):
        if b[i] > a[i]:
            flag = True
            count += 1
        elif b[i] < a[i]:
            flag = False
        else:
            if flag:
                count += 1
    print(count)


def recur(ques, s):
    if len(ques) == 0:
        print(s)
        return

    ch = ques[0]
    ros = ques[1:]

    recur(ros, s + ch)
    recur(ros, s + '_')


recur('abc', '')


def recur(ques, ans):
    if len(ans) == len(ques):
        print(ans)
        return

    for i in range(len(ques)):
        if ques[i] not in ans:
            recur(ques, ans + ques[i])


recur('abc', "")

def recur(ques, ans):
    if len(ques) == 0:
        print(ans)
        return

    for i in range(len(ques)):
        s = ''
        for j in range(0, i + 1):
            s += ques[j]
        if 0 < int(s) <= 26:
            recur(ques[i + 1:], ans + chr(96 + int(s)))


recur('123', '')


def recur(r, c, dp, ans):
    if r == len(dp) and c == len(dp[0]):
        print(ans)
        return

    if 0 < r <= len(dp) and 0 < c <= len(dp[0]) and dp[r - 1][c - 1] == 0:
        dp[r - 1][c - 1] = 1
        recur(r - 1, c, dp, ans + 't')
        recur(r, c - 1, dp, ans + 'l')
        recur(r + 1, c, dp, ans + 'd')
        recur(r, c + 1, dp, ans + 'r')


lst = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
recur(1, 1, lst, "")


def recur(r, c, dp, ans):
    if r == len(dp) - 1 and c == len(dp[0]) - 1:
        print(ans)
        return

    if 0 <= r < len(dp) and 0 <= c < len(dp[0]) and dp[r][c] == 0:
        dp[r][c] = 1
        recur(r - 1, c, dp, ans + 't')
        recur(r, c - 1, dp, ans + 'l')
        recur(r + 1, c, dp, ans + 'd')
        recur(r, c + 1, dp, ans + 'r')
        dp[r][c] = 0


lst = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
recur(0, 0, lst, "")


def recur(nums, ind, s, ss, t):
    if ind == len(nums):
        if ss == t:
            print(s)
        return

    recur(nums, ind + 1, s + str(nums[ind]) + ", ", nums[ind] + ss, t)
    recur(nums, ind + 1, s, ss, t)


lst = [10, 20, 30, 40, 50, 60]
recur(lst, 0, "", 0, 60)


def safe(chess, row, col):
    i, j = row, col
    while i >= 0:                       # Vertical
        if chess[i][j] == 1:
            return False
        i -= 1

    i, j = row, col
    while i >= 0 and j >= 0:            # left diagonal
        if chess[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < len(chess[0]):  # right diagonal
        if chess[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def recur(chess, ans, row):
    if row == len(chess):
        print(ans)
        return

    for col in range(len(chess)):
        if safe(chess, row, col):
            chess[row][col] = 1
            recur(chess, ans + str(row) + "-" + str(col) + ", ", row + 1)
            chess[row][col] = 0


dp = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
recur(dp, "", 0)


def recur(chess, row, col, ans, count):
    if count == 25:
        print(ans)
        return

    if 0 <= row < len(chess) and 0 <= col < len(chess[0]) and chess[row][col] == 0:
        chess[row][col] = 1
        count += 1
        recur(chess, row - 2, col + 1, ans + str(row - 2) + "-" + str(col + 1) + ", ", count)
        recur(chess, row - 1, col + 2, ans + str(row - 1) + "-" + str(col + 2) + ", ", count)
        recur(chess, row + 1, col + 2, ans + str(row + 1) + "-" + str(col + 2) + ", ", count)
        recur(chess, row + 2, col + 1, ans + str(row + 2) + "-" + str(col + 1) + ", ", count)
        recur(chess, row + 2, col - 1, ans + str(row + 2) + "-" + str(col - 1) + ", ", count)
        recur(chess, row + 1, col - 2, ans + str(row + 1) + "-" + str(col - 2) + ", ", count)
        recur(chess, row - 1, col - 2, ans + str(row - 1) + "-" + str(col - 2) + ", ", count)
        recur(chess, row - 2, col - 1, ans + str(row - 2) + "-" + str(col - 1) + ", ", count)
        chess[row][col] = 0
        count -= 1


dp = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
recur(dp, 2, 2, "", 0)


def displayBoard(chess):
    for i in range(len(chess)):
        for j in range(len(chess)):
            print(chess[i][j], end=" ")
        print()
    print()


def recur(chess, row, col, count):
    if row < 0 or col < 0 or row > len(chess) - 1 or col > len(chess) - 1 or chess[row][col] > 0:
        return
    elif count == len(chess) * len(chess):
        chess[row][col] = count
        displayBoard(chess)
        chess[row][col] = 0
        return

    chess[row][col] = count
    recur(chess, row - 2, col + 1, count + 1)
    recur(chess, row - 1, col + 2, count + 1)
    recur(chess, row + 1, col + 2, count + 1)
    recur(chess, row + 2, col + 1, count + 1)
    recur(chess, row + 2, col - 1, count + 1)
    recur(chess, row + 1, col - 2, count + 1)
    recur(chess, row - 1, col - 2, count + 1)
    recur(chess, row - 2, col - 1, count + 1)
    chess[row][col] = 0


dp = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
recur(dp, 2, 2, 1)


def memoization(n, m):
    if n == 0 or n == 1:
        return n
    if m[n] != 0:
        return m[n]

    fs1 = memoization(n - 1, m)
    fs2 = memoization(n - 2, m)
    f = fs1 + fs2
    m[n] = f
    return f


print(memoization(8, [0, 0, 0, 0, 0, 0, 0, 0, 0]))


def recur(n, count, s):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    if s[n] > 0:
        return s[n]

    a = recur(n - 1, count, s)
    b = recur(n - 2, count, s)
    c = recur(n - 3, count, s)
    count += a + b + c
    s[n] = count
    return count


print(recur(3, 0, [0, 0, 0, 0]))

grid = [[0, 1, 4, 2], [4, 3, 6, 5], [1, 2, 4, 1], [3, 1, 5, 9]]
dp = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

r, c = len(grid), len(grid[0])

for i in range(r - 1, -1, -1):
    dp[i][c - 1] = grid[i][c - 1]

for p in range(c - 2, -1, -1):
    for q in range(r):

        if q == 0:
            dp[q][p] = max(dp[q][p + 1], dp[q + 1][p + 1]) + grid[q][p]
        elif 0 < q < r - 1 and 0 <= p <= c - 2:
            dp[q][p] = max(dp[q - 1][p + 1], dp[q][p + 1], dp[q + 1][p + 1]) + grid[q][p]
        elif q == r - 1:
            dp[q][p] = max(dp[q - 1][p + 1], dp[q][p + 1]) + grid[q][p]

print(dp)
"""

# Python3 code to print subtree of all nodes

# arrays for keeping position at
# each dfs traversal for each node
start = [None] * 100001
end = [None] * 100001

# Storing dfs order
dfs_order = []
adj = [[] for i in range(100001)]
visited = [False] * 100001

# Recursive function for dfs traversal dfsUtil()
def dfs(a, b):

	# keep track of node visited
	visited[a] = 1
	b += 1
	start[a] = b
	dfs_order.append(a)

	for it in adj[a]:
		if not visited[it]:
			b = dfs(it, b)

	end[a] = b
	return b

# Function to print the subtree nodes
def Print(n):

	for i in range(0, n):

		# If node is leaf node
		# start[i] is equals to endd[i]
		if start[i] != end[i]:

			print("subtree of node", i, "is", end = " ")
			for j in range(start[i]+1, end[i]+1):

				print(dfs_order[j-1], end = " ")

			print()

# Driver code
if __name__ == "__main__":

	# No of nodes n = 10
	n, c = 10, 0

	adj[0].append(1)
	adj[0].append(2)
	adj[0].append(3)
	adj[1].append(4)
	adj[1].append(5)
	adj[4].append(7)
	adj[4].append(8)
	adj[2].append(6)
	adj[6].append(9)

	# Calling dfs for node 0
	# Considering root node at 0
	dfs(0, c)

	# Print child nodes
	Print(n)

# This code is contributed by Rituraj Jain
