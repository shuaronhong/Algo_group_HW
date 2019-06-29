#Leetcode 784
# Runtime: 72 ms, faster than  87.17%% of Python3 online submissions
# Memory Usage: 14.3 MB, less than 21.42% of Python3 online submissions
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def helper(s, i):
            if i == len(s):
                res.append("".join(s))
                return
            helper(s, i + 1)
            if not s[i].isalpha():
                return
            else:
                if s[i].isupper():
                    s[i] = s[i].lower()
                else:
                    s[i] = s[i].upper()
                helper(s, i + 1)

        res = []
        s = list(S)
        helper(s, 0)
        return res

#Leetcode 17
#Runtime: 36 ms, faster than 93.79% of Python3 online submissions
#Memory Usage: 13.2 MB, less than 37.38% of Python3 online submissions
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
                   '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        def helper(nums, i):
            if i == len(nums) - 1:
                return list(letters[nums[i]])
            rs = helper(nums, i+1)
            chars = list(letters[nums[i]])
            new_rs = []
            for r in rs:
                for char in chars:
                    new_rs.append(char+r)
            return new_rs
        if digits =="":
            return []
        res = []
        nums = list(digits)
        res = helper(nums, 0)
        return res

#Leetcode 40
# Runtime: 40 ms, faster than 99.11% of Python3 online submissions for Combination Sum II.
# Memory Usage: 13.2 MB, less than 55.79% of Python3 online submissions for Combination Sum II.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return []
        cand = candidates.copy()
        cand.sort()

        def helper(nums, i):
            if i == len(cand):
                return
            for idx in range(i, len(cand)):
                if idx > i and cand[idx] == cand[idx - 1]:
                    continue
                if sum(nums) + cand[idx] == target:
                    res.append(nums[1:] + [cand[idx]])
                    return
                elif sum(nums) + cand[idx] > target:
                    return
                else:
                    helper(nums + [cand[idx]], idx + 1)

        res = []
        nums = [0]
        helper(nums, 0)
        return res

#Leetcode 46
# Runtime: 48 ms, faster than 91.80% of Python3 online submissions
# Memory Usage: 13.2 MB, less than 57.21% of Python3 online submissions
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        res = []
        next_res = []
        for i in range(len(nums)):
            next_res = self.permute(nums[:i] + nums[i + 1:])
            res += [[nums[i]] + x for x in next_res]
        return res

#Leetcode 47
#Runtime: 68 ms, faster than 94.65% of Python3 online submissions
#Memory Usage: 13.4 MB, less than 57.61% of Python3 online submissions
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        nums.sort()
        res = []
        next_res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                next_res = self.permuteUnique(nums[:i]+nums[i+1:])
                res += [[nums[i]]+x for x in next_res]
        return res

#Leetcode 37
# Runtime: 1116 ms, faster than 8.54% of Python3 online submissions
# Memory Usage: 13.3 MB, less than 42.63% of Python3
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        emptyIdx = []
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    emptyIdx.append((row, col))

        def isUsed(row, col, num):
            return usedInRow(row, num) or usedInCol(col, num) or usedInBox(row, col, num)

        def usedInRow(rowIdx, num):
            for col in range(9):
                if board[rowIdx][col] == str(num):
                    return True
            return False

        def usedInCol(colIdx, num):
            for row in range(9):
                if board[row][colIdx] == str(num):
                    return True
            return False

        def usedInBox(rowIdx, colIdx, num):
            leftRowIdx = rowIdx - rowIdx % 3
            topColIdx = colIdx - colIdx % 3
            for row in range(leftRowIdx, leftRowIdx + 3):
                for col in range(topColIdx, topColIdx + 3):
                    if board[row][col] == str(num):
                        return True
            return False

        def allFilled():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        return False
            return True

        def solve(i):
            if allFilled() and i <= len(emptyIdx):
                return True
            for num in range(1, 10):
                row = emptyIdx[i][0]
                col = emptyIdx[i][1]
                if not isUsed(row, col, num):
                    board[row][col] = str(num)
                    if not solve(i + 1):
                        board[row][col] = '.'
                    else:
                        # to make the bottom most base transfer upward
                        return True
            return False

        solve(0)

#Leetcode 90
# Runtime: 44 ms, faster than 90.88% of Python3 online submissions
# Memory Usage: 13 MB, less than 95.23% of Python3 online submissions
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        res = []
        nums.sort()
        sub_res = self.subsetsWithDup(nums[1:])
        res += sub_res
        for sub in sub_res:
            if [nums[0]] + sub not in res:
                res.append([nums[0]] + sub)
        return res

#Leetcode 216
# Runtime: 32 ms, faster than 95.74% of Python3 online submissions
# Memory Usage: 13.2 MB, less than 46.66% of Python3 online submissions
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k, maxk, start, target):
            if k == 1:
                if target in range(start, 10):
                    return [[target]]

            res = []
            for i in range(start, 9):
                next_res = helper(k - 1, maxk, i + 1, target - i)
                res += [[i] + num for num in next_res]
            return res

        if k == 0:
            return []
        if k == 1 and n > 0 and n <= 9:
            return [[n]]

        return helper(k, k, 1, n)

#Leetcode 51
# Runtime: 268 ms, faster than 9.04% of Python3 online submissions for N-Queens.
# Memory Usage: 13.6 MB, less than 21.26% of Python3 online submissions
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def setAttackRange(board, qRow, qCol):
            for i in range(n):
                for j in range(n):
                    if board[i][j] != -1 and i == qRow and j != qCol:
                        board[i][j] = -1
                    if board[i][j] != -1 and j == qCol and i != qRow:
                        board[i][j] = -1
                    if board[i][j] != -1 and i - qRow != 0 and abs(i - qRow) == abs(j - qCol):
                        board[i][j] = -1
            return board

        def solve(board, start):
            if start == n:
                res.append(convToStr(board))
                return True

            for i in range(start, n):
                succ = False
                for j in range(n):
                    if board[i][j] == 0:
                        brd = [[cell for cell in brdRow] for brdRow in board]
                        brd[i][j] = 1
                        brd = setAttackRange(brd, i, j)
                        succ = solve(brd, i + 1)
                if not succ:
                    return False
            return False

        def convToStr(board):
            res_list = ["".join(["Q" if cell == 1 else "." for cell in brdRow]) for brdRow in board]
            return res_list

        res = []

        board = [[0] * n for x in range(n)]
        succ = solve(board, 0)
        return res