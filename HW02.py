#Leetcode 69
#Runtime: 36 ms, faster than 95.35% of Python3 online submissions for Sqrt(x)
#Memory Usage: 13.1 MB, less than 88.09% of Python3 online submissions for Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        start = 0
        end = x
        while start < end:
            mid = (start + end) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid+1
            else:
                end = mid
        return start-1

#Leetcode 852
#Runtime: 40 ms, faster than 80.97% of Python3 online submissions
#Memory Usage: 14.2 MB, less than 58.93% of Python3 online submissions
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        start = 0
        end = len(A)
        while start < end:
            mid = (start + end) // 2
            if A[mid-1] < A[mid] and A[mid] > A[mid+1]:
                return mid
            elif A[mid-1] < A[mid] and A[mid] < A[mid+1]:
                start = mid+1
            elif A[mid-1] > A[mid] and A[mid] > A[mid+1]:
                end = mid
            else:
                print("impossible")
        return mid

#leetcode 74
class Solution:
    #Runtime: 32 ms, faster than 98.03% of Python3 online submissions
    #Memory Usage: 13.9 MB, less than 64.94% of Python3 online submissions
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        start = 0
        end = m * n
        while start < end:
            mid = (start + end) // 2
            elem = matrix[mid // n][mid % n]
            if elem == target:
                return True
            elif elem < target:
                start = mid+1
            else:
                end = mid
        return False

#Leetcode 34
#Runtime: 32 ms, faster than 98.13% of Python3 online submissions
#Memory Usage: 13.8 MB, less than 83.47% of Python3 online submissions
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def helper(nums: List[int], target: int, left: bool):
            start = 0
            end = len(nums)
            found = False
            while start < end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid+1
                elif nums[mid] == target and left:
                    found = True
                    end = mid
                elif nums[mid] == target and not left:
                    found = True
                    start = mid+1
                else:
                    end = mid
            if not found:
                return -1
            return end if left else start-1
        if len(nums) == 0:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        return [helper(nums, target, True), helper(nums, target, False)]

#Leetcode 240
# Runtime: 76 ms, faster than 5.41% of Python3 online submissions
# Memory Usage: 17.4 MB, less than 95.00% of Python3 online submissions
# Try two pointer solution later
class Solution:
    def searchMatrix(self, matrix, target):
        def helper(matrix, target, row_start, row_end, col_start, col_end, is_row):
            row_mid = (row_start + row_end) // 2
            col_mid = (col_start + col_end) // 2
            res1 = res2 = False
            if (row_start < row_end and is_row) or (col_start < col_end and not is_row):
                if matrix[row_mid][col_mid] == target:
                    return True
                if matrix[row_mid][col_mid] < target:
                    res1 = helper(matrix, target, row_mid + 1, row_end, col_start, col_end, True)
                    res2 = helper(matrix, target, row_start, row_end, col_mid + 1, col_end, False)
                else:
                    res1 = helper(matrix, target, row_start, row_mid, col_start, col_end, True)
                    res2 = helper(matrix, target, row_start, row_end, col_start, col_mid, False)
            return res1 or res2

        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        return helper(matrix, target, 0, m, 0, n, True) or helper(matrix, target, 0, m, 0, n, False)

#Leetcode 302
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    Your submission beats 79.40% Submissions!
    """
    def minArea(self, image, x, y):
        # write your code here
        def helper(image, start, end, is_row):
            while abs(end - start) > 1:
                mid = (start + end) // 2
                if check_black(image, mid, is_row):
                    end = mid
                else:
                    start = mid
            if check_black(image, start, is_row):
                return start
            else:
                return end
        def check_black(image, mid, is_row):
            if is_row:
                for pixel in image[mid]:
                    if pixel == "1":
                        return True
                return False
            else:
                for row in image:
                    if row[mid] == "1":
                        return True
                return False
        m = len(image)
        if m == 0:
            return 0
        n = len(image[0])
        if n == 0:
            return 0
        top_most = helper(image, 0, x, True)
        bottom_most = helper(image, m-1, x, True)
        left_most = helper(image, 0, y, False)
        right_most = helper(image, n-1, y, False)
        print(top_most, bottom_most,left_most, right_most)
        return (right_most - left_most + 1) * (bottom_most-top_most + 1)

#Leetcode 33
# Runtime: 32 ms, faster than 95.41% of Python3 online submissions
# Memory Usage: 13.2 MB, less than 65.11% of Python3 online submissions
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[start] and nums[mid] < nums[end]:
                if nums[mid] > target:
                    end = mid
                else:
                    start = mid
            elif nums[mid] < nums[start] and nums[mid] < nums[end]:
                if nums[mid] > target:
                    end = mid
                elif nums[mid] < target and target >= nums[start]:
                    end = mid
                elif nums[mid] < target and target < nums[start]:
                    start = mid
            elif nums[mid] > nums[start] and nums[mid] > nums[end]:
                if nums[mid] < target:
                    start = mid
                elif nums[mid] > target and target >= nums[start]:
                    end = mid
                elif nums[mid] > target and target < nums[start]:
                    start = mid
            else:
                print("impossible")

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        print(start, end)
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

#Leetcode 278
#Runtime: 32 ms, faster than 93.90% of Python3 online submissions for First Bad Version.
#Memory Usage: 13 MB, less than 89.96% of Python3 online submissions for First Bad Version.
#The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        start = 1
        end = n
        while start+1 < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        return start if isBadVersion(start) else end

#Leetcode 300
#Runtime: 32 ms, faster than 99.18% of Python3 online submissions
#Memory Usage: 13.2 MB, less than 68.09% of Python3 online submissions
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        res = []
        for num in nums:
            leng = len(res)
            if leng == 0 or res[leng-1] < num:
                res.append(num)
            else:
                start = 0
                end = leng
                same_num_flg = False
                while start < end:
                    mid = (start + end) // 2
                    if res[mid] < num:
                        start = mid+1
                    else:
                        end = mid
                res[start] = num
        return len(res)