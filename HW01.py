#leetcode 783
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.prevNode = None
        self.minDiff = sys.maxsize
        def inOrderTraverse(node: TreeNode):
            if node is None:
                return
            inOrderTraverse(node.left)
            if self.prevNode is None:
                self.prevNode = node
            else:
                self.minDiff = min(node.val - self.prevNode.val, self.minDiff)
                self.prevNode = node
            inOrderTraverse(node.right)
        inOrderTraverse(root)
        return self.minDiff

#leetcode 247
class Solution:
    def findStrobogrammatic(self, n):
        # write your code here
        def helper(n, max_n):
            if n == 0:
                return [""]
            elif n == 1:
                return ["0","1","8"]
            elif n == 2:
                if max_n != 2:
                    return ["00","11","69","88","96"]
                else:
                    return ["11","69","88","96"]
            else:
                center = helper(n-2, max_n)
                res = []
                for num in center:
                    res.append("1"+num+"1")
                    res.append("6"+num+"9")
                    res.append("8"+num+"8")
                    res.append("9"+num+"6")
                    if n != max_n:
                        res.append("0"+num+"0")
                return res
        return helper(n, n)

#leetcode 544
class Solution:
    def findContestMatch(self, n):
        # write your code here
        def form_res(tmp, curlen):
            res = []
            for i in range(curlen):
                if i < curlen - i - 1:
                    res.append("(" + tmp[i] + "," + tmp[curlen - i - 1] + ")")
            return res

        def helper(n, curlen):
            if n == curlen:
                tmp = [str(i) for i in range(1, curlen + 1)]
            else:
                tmp = helper(n, curlen * 2)

            return form_res(tmp, curlen)

        res = helper(n, 2)
        return str(res).replace("[", "").replace("]", "").replace("'", "")

#leetcode 698
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sum_nums = sum(nums)
        if sum_nums % k != 0:
            return False
        target = sum(nums) / k
        nums.sort()
        group = [0] * k
        def search(group, nums, target):
            if nums == []:
                return True
            val = nums.pop()
            if val > target:
                return False
            for i in range(k):
                if group[i] + val <= target:
                    group[i] += val
                    if search(group, nums, target):
                        return True
                    group[i] -= val
                if group[i] == 0:
                    break
            nums.append(val)
            return False
        return search(group, nums, target)

#leetcode 761
class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        def helper(S):
            if S == "10":
                return "10"

            prefix_diff = 0  # for trying to find a special string
            begin = 0
            res = []
            for i in range(len(S)):
                if prefix_diff < 0:
                    print("this is not a valid input")
                    return
                prefix_diff = prefix_diff + 1 if S[i] == "1" else prefix_diff - 1

                if prefix_diff == 0:  # meaning you found one special string
                    res.append("1" + helper(S[begin + 1:i]) + "0")
                    begin = i + 1
            res.sort(reverse=True)
            res_str = ""
            for special_str in res:
                res_str += special_str
            return res_str
        return helper(S)