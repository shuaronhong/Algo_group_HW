#Leetcode 70
class Solution:
    def climbStairs(self, n: int) -> int:
        # #Iterative version
        # dp = [0]*(n+1)
        # if n >=1:
        #     dp[1] = 1
        # if n >=2:
        #     dp[2] = 2
        # if n >=3:
        #     for i in range(3, len(dp)):
        #         dp[i] = dp[i-1]+dp[i-2]
        # return dp[n]
        #Recursive version
        def helper(i, memo):
            if memo[i] > 0:
                return memo[i]
            if i == 1:
                memo[i] = 1
            elif i == 2:
                memo[i] = 2
            else:
                memo[i] = helper(i-1,memo) + helper(i-2,memo)
            return memo[i]
        memo = [0] * (n+1)
        return helper(n,memo)

#Leetcode 53
# Runtime: 44 ms, faster than 70.43% of Python3 online submissions
# Memory Usage: 13.4 MB, less than 94.95% of Python3 online submissions
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        maxSoFar = nums[0]
        maxSum = nums[0]

        # dp = [nums[0]]*len(nums)
        for i in range(1, len(nums)):
            maxSoFar = max(maxSoFar + nums[i], nums[i])
            maxSum = max(maxSoFar, maxSum)
        return maxSum

#Leetcode 647
# Runtime: 432 ms, faster than 25.95% of Python3 online submissions
# Memory Usage: 21.6 MB, less than 17.18% of Python3 online submissions
class Solution:
    def countSubstrings(self, s: str) -> int:
        # Iterative
        if len(s) == 0 or len(s) == 1:
            return len(s)
        dp = [[False for j in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        count = len(s)
        for subLen in range(2, len(s) + 1):
            for start in range(len(s) - subLen + 1):
                end = start + subLen - 1
                if start == end - 1:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and dp[start + 1][end - 1]
                if dp[start][end] == True:
                    count += 1
        return count

#Leetcode 483
# Runtime: 36 ms, faster than 88.01% of Python3 online submissions
# Memory Usage: 13 MB, less than 90.73% of Python3 online submissions
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # #Recursive
        # def helper(nums, start, end, memo):
        #     if memo[start][end] is None:
        #         if start == end:
        #             memo[start][end] = nums[start]
        #         else:
        #             score_left = nums[start] - helper(nums, start +1, end, memo)
        #             score_right = nums[end] - helper(nums, start, end -1, memo)
        #             memo[start][end] = max(score_left, score_right)
        #     return memo[start][end]
        # memo = [[None for j in range(len(nums))] for i in range(len(nums))]
        # return helper(nums, 0, len(nums)-1, memo) >= 0
        # Iterative
        if len(nums) == 1:
            return True
        dp = [[0 for j in range(len(nums))] for i in range(len(nums))]

        for start in range(len(nums) - 2, -1, -1):
            dp[start][start] = nums[start]
            for end in range(start + 1, len(nums)):
                score_left = nums[start] - dp[start + 1][end]
                score_right = nums[end] - dp[start][end - 1]
                dp[start][end] = max(score_left, score_right)

        return dp[0][len(nums) - 1] >= 0

#Leetcode 64
# Runtime: 60 ms, faster than 40.16% of Python3 online submissions
# Memory Usage: 15 MB, less than 17.45% of Python3 online submissions
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        dp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[0][0] = grid[0][0]
                elif i == 0 and j != 0:
                    dp[0][j] = grid[0][j] + dp[0][j - 1]
                elif i != 0 and j == 0:
                    dp[i][0] = grid[i][0] + dp[i - 1][0]
                else:
                    from_above = grid[i][j] + dp[i - 1][j]
                    from_left = grid[i][j] + dp[i][j - 1]
                    dp[i][j] = min(from_above, from_left)
        return dp[m - 1][n - 1]

#Leetcode 718
# Runtime: 3440 ms, faster than 62.13% of Python3 online submissions
# Memory Usage: 39.5 MB, less than 6.61% of Python3 online submissions
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        if len(A) == 0 or len(B) == 0:
            return 0

        dp = [[0 for j in range(len(B))] for i in range(len(A))]

        for i in range(0, len(A)):
            for j in range(0, len(B)):
                if A[i] == B[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
        return max([max(row) for row in dp])