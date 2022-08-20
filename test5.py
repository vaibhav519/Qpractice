"""
print decreasing
def recur(n):
    if n == 0:
        return
    print(n)
    recur(n - 1)
recur(5)
TnS = o(n) o(n)




print increasing
def recur(n):
    if n == 0:
        return
    recur(n - 1)
    print(n)
recur(5)
TnS = o(n) o(n)



print dec/inc
def recur(n):
    if n == 0:
        return
    print(n)
    recur(n - 1)
    print(n)
recur(5)
TnS = o(n) o(n)



factorial
def recur(n):
    if n == 1:
        return 1
    res = n * recur(n - 1)
    return res
recur(5)
TnS = o(n) o(n)



calculate power
def recur(x, n):
    if n == 0:
        return 1

    res1 = recur(x, n - 1)
    res2 = x ** res1
    return res2
print(recur(2, 1))
TnS = o(n) o(n)



logarithic solution
def recur(x, n):
    if n == 0:
        return 1
    res1 = recur(x, n // 2)
    res2 = res1 * res1
    if n % 2 != 0:
        return res2 * x
    return res2
recur(2, 4)
TnS = o(logn) o(logn)




print zig zag
def recur(n):
    if n == 0:
        return
    print(n)
    recur(n - 1)
    print(n)
    recur(n - 1)
    print(n)
recur(2)
TnS = o(2^n) o(2^n)



tower of hanoi
def recur(n, a, b, c):
    if n == 0:
        return

    recur(n - 1, a, c, b)
    print(n, str(a) + "->" + str(b))
    recur(n - 1, c, b, a)
    
recur(3, 10, 11, 12)
TnS = o(2^n) o(2^n)




print array
def recur(arr, n):
    if n == len(arr):
        return
    print(arr[n])
    recur(arr, n + 1)
recur([1, 2, 3, 4, 5], 0)
TnS = o(n), o(n)




print array reverse
def recur(arr, n):
    if n == len(arr):
        return
    recur(arr, n + 1)
    print(arr[n])
recur([1, 2, 3, 4, 5], 0)
TnS = o(n), o(n)




get max
def recur(arr, n):
    if n == len(arr) - 1:
        return arr[n]
    m = recur(arr, n + 1)
    if m > arr[n]:
        return m
    else:
        return arr[n]
print(recur([8, 2, 6, 4, 5], 0))
TnS = o(n), o(n)




get first occurrence
def recur(arr, n, target):
    if n == len(arr):
        return -1
    if arr[n] == target:
        return n

    res = recur(arr, n + 1, target)
    return res
print(recur([1, 2, 6, 4, 5], 0, 8))
TnS = o(n), o(n)





get last occurrence
def recur(arr, n, target):
    if n == len(arr):
        return -1
    res = recur(arr, n + 1, target)
    if arr[n] == target:
        return n
    return res
print(recur([1, 2, 6, 4, 5], 0, 8))
TnS = o(n), o(n)





get all occurrence
def recur(arr, n, target):
    if n == len(arr):
        return []
    res = recur(arr, n + 1, target)
    if arr[n] == target:
        res.append(n)
    return res
print(recur([1, 2, 8, 6, 4, 8, 5], 0, 8))
TnS = o(n), o(n)




 get subsequence
 def recur(s):
    if len(s) == 0:
        return [""]
    ch = s[0]
    s = s[1:]
    res = recur(s)
    mres = []
    for ss in res:
        mres.append(('_' + ss))
        mres.append((ch + ss))
    return mres
print(recur('abc'))
n = len('abc')
TnS = o(n) + o(2^n) o(2^n) + o(n)



get keypad combinations
keypad = ['a', 'b', 'mnop', 'uv', 'jkl']
def recur(n):
    if len(n) == 0:
        return ['']
    ch = n[0]
    n = n[1:]
    comb = recur(n)
    res = []
    word = keypad[int(ch)]
    for i in word:
        for j in comb:
            res.append(i + j)
    return res
print(recur('234'))
TnS = o(n) + o(4^n) o(n) + o(4^n)




get stair path
def recur(n):
    if n == 0:
        return ['']
    if n < 0:
        return []
    path1 = recur(n - 1)
    path2 = recur(n - 2)
    path3 = recur(n - 3)
    p = []
    for path in path1:
        p.append('1' + path)
    for path in path2:
        p.append('2' + path)
    for path in path3:
        p.append('3' + path)
    return p
print(recur(4))
TnS = o(3^n) o(3^n)




get maze paths
def recur(sr, sc, dr, dc):
    if sr == dr and sc == dc:
        return [""]
    if sr > dr:
        return []
    if sc > dc:
        return []
    if 1 <= sr <= dr:
        hpaths = recur(sr, sc + 1, dr, dc)
    if 1 <= sc <= dc:
        cpaths = recur(sr + 1, sc, dr, dc)
    res = []
    for hp in hpaths:
        res.append('h' + hp)
    for cp in cpaths:
        res.append('v' + cp)
    return res
print(recur(1, 1, 4, 4))
TnS = O(2^n*m) O(2^n*m) 




print subsequence
def recur(s, ans):
    if len(s) == 0:
        print(ans)
        return
    ch = s[0]
    s = s[1:]
    recur(s, ans + '_')
    recur(s, ans + ch)
recur('abc', "")
TnS = o(2^n) o(n)




print keypad comnbination
keypad = ['a', 'b', 'mnop', 'uv', 'jkl']
def recur(n, ans):
    if len(n) == 0:
        print(ans)
        return
    ch = n[0]
    n = n[1:]
    word = keypad[int(ch)]
    for w in word:
        recur(n, ans + w)
recur('234', '')
TnS = o(4^n) o(n + 1) * n




print stair paths
def recur(n, ans):
    if n == 0:
        print(ans)
        return
    if n < 0:
        return
    recur(n - 1, '1' + ans)
    recur(n - 2, '2' + ans)
    recur(n - 3, '3' + ans)
recur(4, "")
TnS = o(3^n) o(n)




print maze paths
def recur(sr, sc, dr, dc, ans):
    if sr == dr and sc == dc:
        print(ans)
        return
    if sr > dr:
        return
    if sc > dc:
        return
    if 1 <= sr <= dr:
        recur(sr, sc + 1, dr, dc, ans + 'h')
    if 1 <= sc <= dc:
        recur(sr + 1, sc, dr, dc, ans + 'v')
recur(1, 1, 3, 3, "")




print permutation
def recur(s, ans):
    if len(s) == 0:
        print(ans)
        return
    
    for i in range(len(s)):
        ch = s[i]
        ss = s[:i] + s[i + 1:]
        recur(ss, ans + ch)
recur('abc', "")
TnS = o(n!) o(s)





print encodings
def recur(ques, ans):
    if len(ques) == 0:
        print(ans)
        return

    if ques[0] == '0':
        return

    ch0 = ques[0]
    ros = ques[1:]
    char = chr(96 + int(ch0))
    recur(ros, ans + char)
     
    if len(ques) >= 2:
        val2 = int(ques[:2])
        ch1 = chr(96 + int(val2))
        ros2 = ques[2:]

        if val2 <= 26:
            recur(ros2, ans + ch1)
recur('123', '')
TnS = o(2 ^ n) o(n)





flood fill
def recur(arr, r, c, ans):
    if r == len(arr) - 1 and c == len(arr[0]) - 1:
        print(ans)
        return
    if 0 <= r < len(arr) and 0 <= c < len(arr[0]) and arr[r][c] == 0:
        arr[r][c] = 1
        recur(arr, r - 1, c, ans + 'u')
        recur(arr, r + 1, c, ans + 'd')
        recur(arr, r, c - 1, ans + 'l')
        recur(arr, r, c + 1, ans + 'r')
        arr[r][c] = 0
    return 
mat = [[0, 0, 0], [1, 0, 1], [0, 0, 0]]
recur(mat, 0, 0, "")
TnS = 4 ^ (n^2) o(n ^ 2)




target subset
def recur(arr, ind, target, ans):
    if ind == len(arr):
        if sum(ans) == target:
            print(ans)
        return
    
    recur(arr, ind + 1, target, ans + [arr[ind]])
    recur(arr, ind + 1, target, ans)
arr = [10, 20, 30]
recur(arr, 0, 30, [])
TnS = o(2^n) o(n)





N queen
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
TnS = o(n!) o(n)





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
TnS = o(8*(n^2)) o(n)




Dynamic programming:




def decodeWays(n):
    dp = [0] * len(n)
    dp[0] = 1

    for i in range(1, len(n)):
        if 0 < int(n[i]) <= 9:
            dp[i] += dp[i - 1]
        if 10 <= int(n[i - 1] + n[i]) <= 26:
            dp[i] += dp[i - 1]

    return dp

number = "231011"
print(decodeWays(number))
TnS = o(n) o(n)




def countSub(s):
    a = 0
    ab = 0
    abc = 0
    for ch in s:
        if ch == 'a':
            a = 2 * a + 1
        elif ch == 'b':
            ab = 2 * ab + a
        elif ch == 'c':
            abc = 2 * abc + ab
    return abc
print(countSub('abcabc'))
TnS = o(len(s)) o(1)




def maxSum(arr):
    inc = arr[0]
    exc = 0

    for i in range(1, len(arr)):
        temp = inc
        inc = arr[i] + exc
        exc = max(temp, exc)

    return max(inc, exc)

arr = [5, 10, 10, 100, 5, 6]
print(maxSum(arr))
TnS = O(n) O(1)



def paintHouse(arr):
    r = arr[0][0]
    b = arr[0][1]
    g = arr[0][2]

    for i in range(1, len(arr)):
        nr = arr[i][0] + min(b, g)
        nb = arr[i][1] + min(r, g)
        ng = arr[i][2] + min(r, b)
        
        r = nr
        b = nb
        g = ng

    return min(r, b, g)
    
arr = [[1, 5, 7], [5, 8, 4], [3, 2, 9], [1, 2, 4]]
print(paintHouse(arr))
TnS = O(n) O(1)




def paintHouse2(arr):

    for i in range(1, len(arr)):
        for j in range(len(arr[0])):
            if j == 0:
                arr[i][j] = arr[i][j] + min(arr[i - 1][j + 1: ])
            elif 0 < j < len(arr[0]) - 1:
                arr[i][j] = arr[i][j] + min(arr[i - 1][0 : j] + arr[i - 1][j + 1:])
            else:
                arr[i][j] = arr[i][j] + min(arr[i - 1][0 : j])

    return arr

arr = [[1, 5, 7, 2, 1, 4], [5, 8, 4, 3, 6, 1],
     [3, 2, 9, 7, 2, 3], [1, 2, 4, 9, 1, 7]]
print(paintHouse2(arr))
TnS = O(n^3) O(1)




def paintFence(n, k):
    same = k
    diff = k * (k - 1)
    total = same + diff

    for i in range(2, n):
        same = diff
        diff = total * (k - 1)
        total = same + diff

    return total

print(paintFence(5, 3))
TnS = O(n) O(1) 




def tiling(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[-1]

print(tiling(5))
TnS = O(n) O(n) 




def tilingM1(m, n):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i < m:
            dp[i] = 1
        elif i == m:
            dp[i] = 2
        else:
            dp[i] = dp[i - 1] + dp[i - m]
    
    return dp

print(tiling(6, 7))
TnS = O(n) O(n)




def friendsPairing(n):
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * (i - 1)
    
    return dp[-1]

print(friendsPairing(5))
TnS = O(n) O(n)




def buySell(arr):

    p1 = 0
    p2 = 1
    diff = arr[p2] - arr[p1]
    m = diff if diff > 0 else 0

    while p2 < len(arr):
        if arr[p1] > arr[p2]:
            p1 = p2
            p2 = p1 + 1
        else:
            if arr[p2] - arr[p1] > m:
                m = arr[p2] - arr[p1]
            p2 += 1
    return m


arr = [1, 6]
print(buySell(arr))
TnS = O(n) O(n)



def buySell2(arr):

    bd = 0
    sd = 0
    profit = 0

    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            sd += 1
        else:
            profit += arr[sd] - arr[bd]
            bd = sd = i

    return profit


arr = [3, 1, 2, 3]
print(buySell2(arr))
TnS = O(n) O(1)




def buySell3(prices, fee):
    obsp = -prices[0]
    ossp = 0
    

    for i in range(1, len(prices)):
        nbsp = 0
        nssp = 0
        if ossp - prices[i] > obsp:
            nbsp = ossp - prices[i]
        else:
            nbsp = obsp

        if obsp + prices[i] - fee > ossp:
            nssp = obsp + prices[i] - fee
        else:
            nssp = ossp

        obsp = nbsp
        ossp = nssp

    return ossp


arr = [10, 15, 17, 20, 16, 18, 22, 20, 22, 20, 23, 25]
print(buySell3(arr, 3))
TnS = O(n) O(1)




def buySell4(prices, fee):
    obsp = -prices[0]
    ossp = 0
    ocsp = 0

    for i in range(1, len(prices)):
        nbsp = 0
        nssp = 0
        ncsp = 0
        if ocsp - prices[i] > obsp:
            nbsp = ocsp - prices[i]
        else:
            nbsp = obsp

        if obsp + prices[i] > ossp:
            nssp = obsp + prices[i]
        else:
            nssp = ossp

        if ossp > ocsp:
            ncsp = ossp
        else:
            ncsp = ocsp

        obsp = nbsp
        ossp = nssp
        ocsp = ncsp

    return ossp


arr = [10, 15, 17, 20, 16, 18, 22, 20, 22, 20, 23, 25]
print(buySell4(arr, 3))
TnS = O(n) O(1)





def buySell5(arr):
    max_profit_sold = 0
    least = arr[0]
    dp_max_profit_right = [0] * len(arr)

    for i in range(1, len(arr)):
        if arr[i] < least:
            least = arr[i]

        max_profit_sold = arr[i] - least
        if max_profit_sold > dp_max_profit_right[i - 1]:
            dp_max_profit_right[i] = max_profit_sold
        else:
            dp_max_profit_right[i] = dp_max_profit_right[i - 1]
    
    max_profit_bought = 0
    max_profit_left = arr[len(arr) - 1]
    dp_max_profit_left = [0] * len(arr)

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_profit_left:
            max_profit_left = arr[i]

        max_profit_bought = max_profit_left - arr[i] 

        if max_profit_bought > dp_max_profit_left[i + 1]:
            dp_max_profit_left[i] = max_profit_bought
        else:
            dp_max_profit_left[i] = dp_max_profit_left[i + 1]
        
    max_point = 0
    for i in range(len(arr)):
         if dp_max_profit_left[i] + dp_max_profit_right[i] > max_point:
            max_point = dp_max_profit_left[i] + dp_max_profit_right[i]


    return max_point

arr = [6, 9, 6, 7, 6, 3, 8, 1]
print(buySell5(arr))
TnS = O(2n) O(2n)




def buySell6(arr, k):
    dp = [[0] * len(arr)] * (k + 1)
    
    for i in range(1, len(dp)):
        m = 0
        for j in range(1, len(dp[0])):
            if dp[i - 1][j - 1] - arr[j - 1] > m:
                m = dp[i - 1][j - 1] - arr[j - 1]
            
            if m + arr[j] > dp[i][j - 1]:
                dp[i][j] = m + arr[j]
            else:
                dp[i][j] = dp[i][j - 1]
        
                
    return dp


arr = [9, 6, 7, 6, 3, 8]
print(buySell6(arr, 3))
TnS = o(n^2) (n^2)




def hillWay(km, toll, cost, dbt):
    dp = [0] * (km + 1)
    dic = {}
    dp[0] = 0

    for i in range(len(toll)):
        dic[toll[i]] = cost[i]

    for i in range(1, km + 1):
        if i not in dic:
            dp[i] = dp[i - 1]
        else:
            board_not = dp[i - 1]
            board = dic[i]
            if i >= dbt + 1:
                board += dp[i - dbt - 1]
            dp[i] = max(board_not, board)

    return dp[km]


toll = [6, 8, 12, 14, 16]
cost = [5, 8, 5, 3, 1]
print(hillWay(20, toll, cost, 3))
tnS = O(km) O(km)





Generic Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.child = []


def display(root):
    s = str(root.data) + " --> "
    for i in range(len(root.child)):
        s += str(root.child[i].data) + ', '
    s += '.'
    print(s)

    for child in root.child:
        display(child)

TnS = (n) (n)

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
    display(root)
TnS = O(n) O(n)




def sizeOf(root):
    count = 0
    for child in root.child:
        count += sizeOf(child)
    count += 1
    return count
TnS = o(n) o(1)





class Node:
    def __init__(self, data):
        self.data = data
        self.child = []


def findMaxHeight(root):
    h = -1

    for child in root.child:
        sub_h = findMaxHeight(child)
        h = max(h, sub_h)
    final_h = 1 + h
    return final_h

TnS = O(n) O(1)
 
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

    print(findMaxHeight(root))


arr = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80,
       110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1]
constructTree(arr)





def printOrder(root):
    print("Node pre " + str((root.data)))
    for child in root.child:
        print("Edge Pre " + str(root.data) + "--" + str(child.data))
        printOrder(child)
        print("Edge Post " + str(root.data) + "--" + str(child.data))

    print("Node Post " + str((root.data))
TnS = O(n) O(1)





def levelOrder(root):
    queue = [root]
    while len(queue) != 0: 
        root = queue.pop(0)
        print(root.data, end=" ")
        for child in root.child:
            queue.append(child)  
TnS = O(n) o(max(root.child))





def levelOrder(root): # linewise
    queue = [root]
    while len(queue) != 0: 

        for _ in range(len(queue)):
            root = queue.pop(0)
            print(root.data, end=" ")
            for child in root.child:
                queue.append(child)
        print()  
TnS = O(n) o(max(root.child))





def levelOrderZigZag(root):
    queue = [root]
    flag = True
    a = []
    while len(queue) != 0: 
        for _ in range(len(queue)):
            root = queue.pop(0)
            a.append(root.data)
            for child in root.child:
                queue.append(child)
        if flag:
            flag = False
            print(a)
        else:
            flag = True
            print(a[::-1])
        a.clear()
        print()
TnS = O(n) (h/2 * n) o(2 * max(root.child))




def printMirror(root):
    if root is None: return None

    n = len(root.child)
    if n < 2:
        return 

    root.child = root.child[::-1]
    
    for child in root.child:
        printMirror(child)
TnS = o(n^2) O(1)





def removeLeaves(root):
    if root is None: return None
    queue = [root]
    while len(queue) != 0: 

        for _ in range(len(queue)):
            root = queue.pop(0)
            newChild = []
            for child in root.child:
                if len(child.child) != 0:
                    newChild.append(child)
                    queue.append(child)
            root.child = newChild
TnS = O(n) O(2max(root.child))




def removeLeaves(root):
    if root is None: return None
    
    for i in range(len(root.child) - 1, -1, -1):
        child = root.child[i]
        if len(child.child) == 0:
            root.child.pop(i)
    
    for child in root.child:
        removeLeaves(child)
TnS = O(n) O(1)




def getTail(root):
    while len(root.child) == 1:
        root = root.child[0]
    
    return root


def flatTree(root):
    for child in root.child:
        flatTree(child)

    while len(root.child) > 1:
        last_child = root.child.pop()
        second_last = root.child[-1]
        second_last_tail = getTail(second_last)
        second_last_tail.child.append(last_child)
TnS = O(n^2) O(1)





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
TnS = O(n) O(1)




def findElement(root, ele):
    if root.data == ele:
        return True

    for child in root.child:
        sub_ans = findElement(child, ele)
        if sub_ans:
            return True
    return False
TnS = O(n) O(1)




def rootToNodePath(root, ele):
    if root.data == ele:
        return [root.data]

    for child in root.child:
        sub_ans = rootToNodePath(child, ele)
        if len(sub_ans) > 0:
            sub_ans.append(root.data)
            return sub_ans
    return []
TnS = O(n) O(path)




def lowestCommonAncestor(root, ele1, ele2):
    path1 = rootToNodePath(root, ele1)
    path2 = rootToNodePath(root, ele2)

    i = len(path1) - 1
    j = len(path2) - 1
    while i >= 0 and j >= 0 and path1[i] == path2[j]:
        i -= 1
        j -= 1
    
    i += 1
    j += 1

    return path1[i]
TnS = O(2n) + O(path) + O(path1) + O(path2)





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
TnS = O(2n) + O(path) + O(path1) + O(path2)




def isSimilar(root1, root2):

    if len(root1.child) != len(root2.child):
        return False
    for child1, child2 in zip(root1.child, root2.child):
        if isSimilar(child1, child2) == False:
            return False
    return True
arr1 = [10, 20, 50, -1, 60, -1, -1, 30, 70, -1, 80,
        110, -1, 120, -1, -1, 90, -1, -1, 40, 100, -1, -1]

arr2 = [1, 2, 5, -1, 6, -1, -1, 3, 7, -1, 8,
        11, -1, 12, -1, -1, 9, -1, -1, 4, 10, -1, -1]
root1 = constructTree(arr1)
root2 = constructTree(arr2)
print(isSimilar(root1, root2))
TnS = O(n) O(1)




def isMirror(root1, root2):
    queue = [(root1, root2)]
    while len(queue) != 0:

        for _ in range(len(queue)):
            root1, root2 = queue.pop(0)
            n1 = len(root1.child)
            n2 = len(root2.child)
            for i, j in zip(range(n1), range(n2 - 1, -1, -1)):
                if root1.child[i] and root2.child[j]:
                    queue.append((root1.child[i], root2.child[j]))
                else:
                    return False

    return True
TnS = O(n) o(max(root.child))




def isMirror(root1, root2):
    if len(root1.child) != len(root2.child):
        return False
    for i in range(len(root1.child)):
        root1 = root1.child[i]
        root2 = root2.child[len(root1.child) - 1 - i]
        if isMirror(root1, root2) == False:
            return False
    return True
TnS = O(n) O(1)




def isSymmetry(root):
    return isMirror(root, root)
TnS = O(n) O(1)





predecessor = None
successor = None
state = 0
def printSuccessorPredecessor(root, ele):
    global state
    if state == 0:
        if root.data == ele:
            state = 1
        else:
            global predecessor
            predecessor = root
    elif state == 1:
        global successor
        successor = root
        state = 2

    for child in root.child:
        printSuccessorPredecessor(child, ele)

    return predecessor, successor
TnS = O(n) O(1)




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
TnS = O(n) O(1)

"""


