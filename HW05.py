#Leetcode 50:
#Runtime: 32 ms, faster than 91.23% of Python3 online submissions
#Memory Usage: 13 MB, less than 92.10% of Python3 online submissions
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        return self.myPow(x,n%2)*self.myPow(x*x,n//2)

#Leetcode 14
# Runtime: 36 ms, faster than 85.90% of Python3 online submissions
# Memory Usage: 13.2 MB, less than 73.63% of Python3 online submissions
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def combHelper(left_pre, right_pre):
            minLen = min(len(left_pre), len(right_pre))
            for i in range(minLen):
                if left_pre[i] != right_pre[i]:
                    return left_pre[:i]
            return left_pre[:minLen]

        def divHelper(strs, l, r):
            if l == r:
                return strs[l]
            m = (l + r) // 2
            left_pre = divHelper(strs, l, m)
            right_pre = divHelper(strs, m + 1, r)
            return combHelper(left_pre, right_pre)

        if strs == []:
            return ""
        return divHelper(strs, 0, len(strs) - 1)

#Leetcode 23
# Runtime: 76 ms, faster than 76.59% of Python3 online submissions
# Memory Usage: 16.3 MB, less than 84.17% of Python3 online submissions
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def divHelp(lists, l, r):
            if l == r:
                return lists[l]
            m = (l + r) // 2
            left_head = divHelp(lists, l, m)
            right_head = divHelp(lists, m + 1, r)
            return comHelp(left_head, right_head)

        def comHelp(l1, l2):
            head = ListNode(0)
            prev = head
            curr1 = l1
            curr2 = l2
            while True:
                if curr1 is None:
                    prev.next = curr2
                    break
                if curr2 is None:
                    prev.next = curr1
                    break
                if curr1.val < curr2.val:
                    prev.next = curr1
                    prev = curr1
                    curr1 = curr1.next
                else:
                    prev.next = curr2
                    prev = curr2
                    curr2 = curr2.next

            return head.next

        if not lists or lists == []:
            return
        return divHelp(lists, 0, len(lists) - 1)

#Leetcode 4:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(A: List[int], B: List[int], k: int, aStart: int, aEnd: int, bStart: int, bEnd: int):
            aLen = aEnd - aStart + 1
            bLen = bEnd - bStart + 1
            # base cases
            if aLen == 0:
                return B[bStart + k]
            if bLen == 0:
                return A[aStart + k]
            if k == 0:
                return A[aStart] if A[aStart] < B[bStart] else B[bStart]

            # relationship i+j == k-1. i, j, k are zero-based indices
            aMid = math.floor(aLen * k / (aLen + bLen))
            bMid = k - aMid - 1
            aMidIndex = aMid + aStart
            bMidIndex = bMid + bStart

            if A[aMidIndex] > B[bMidIndex]:
                k = k - (bMid + 1)
                aEnd = aMid + aStart
                bStart = bMid + bStart + 1
            else:
                k = k - (aMidIndex - aStart + 1)
                bEnd = bMidIndex
                aStart = aMidIndex + 1
            return findKth(A, B, k, aStart, aEnd, bStart, bEnd)

        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 != 0:
            k = math.floor((m + n) / 2)
            return float(findKth(nums1, nums2, k, 0, m - 1, 0, n - 1))
        else:
            k = math.floor((m + n) / 2)
            return float(
                (findKth(nums1, nums2, k - 1, 0, m - 1, 0, n - 1) + findKth(nums1, nums2, k, 0, m - 1, 0, n - 1)) / 2.0)