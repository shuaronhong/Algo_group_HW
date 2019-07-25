#Leetcode 190
#Runtime: 8 ms, faster than 99.28% of Python online submissions for Reverse Bits.
#Memory Usage: 11.8 MB, less than 17.14% of Python online submissions
class Solution:
    def reverseBits(self, n):
        rev = 0
        count = 0
        while count < 32:
            rev = rev << 1
            if n & 1 == 1:
                rev = rev ^ 1
            n = n >> 1
            count += 1
        return int(rev)

#Leetcode 201
#Runtime: 28 ms, faster than 99.07% of Python online submissions for Bitwise AND of Numbers Range.
#Memory Usage: 11.7 MB, less than 75.95% of Python online submissions
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        if m == n:
            return m
        p = 0
        while n - m > 2**p:
            p += 1
        l = (2**32-1)<<p
        return m & n & l

#Leetcode 338
#Runtime: 60 ms, faster than 97.21% of Python online submissions for Counting Bits.
#Memory Usage: 15.8 MB, less than 39.17% of Python online submissions for Counting Bits.
class Solution(object):
    def countBits(self, num):
        res = [0]*(num+1)
        for i in range(1, num+1):
            base = res[i>>1]
            if i & 1 == 1:
                res[i] = base + 1
            else:
                res[i] = base
        return res

#Leetcode 1125 BackTracking version.
# Runtime: 88 ms, faster than 90.91% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions
from collections import defaultdict
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        self.shortest = list(range(len(people)))
        self.target = 2 ** (len(req_skills)) - 1
        skill_indices = {req_skills[i]: i for i in range(len(req_skills))}
        for i in range(len(people)):
            for j in range(len(people)):
                if i != j and set(people[i]).issubset(set(people[j])):
                    people[i] = []

        skills_to_people = defaultdict(list)
        person_skills = []
        for i in range(len(people)):
            pskls = people[i]
            skills = 0
            for sk in pskls:
                idx = skill_indices[sk]
                skills_to_people[idx].append(i)
                skills += 2 ** idx
            person_skills.append(skills)

        def helper(sk, res, team):
            if res == self.target:
                if len(team) < len(self.shortest):
                    self.shortest = team[:]
                return
            if res == (res | 2 ** sk):
                helper(sk + 1, res, team)
                return
            for j in skills_to_people[sk]:
                skills = person_skills[j]
                tmp = res
                res = res | skills
                team.append(j)
                helper(sk + 1, res, team)
                team.pop(-1)
                res = tmp

        helper(0, 0, [])
        return self.shortest

#Leetcode 260
# Runtime: 64 ms, faster than 92.86% of Python3 online submissions
# Memory Usage: 15.8 MB, less than 5.55% of Python3 online submissions
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums:
            res ^= num

        setNum = set(nums)
        for num in setNum:
            if (num ^ res in setNum):
                return [num, num ^ res]

#Leetcode 477
# Runtime: 628 ms, faster than 68.18% of Python3 online submissions
# Memory Usage: 15.2 MB, less than 16.88% of Python3 online submissions
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        count = 0
        for i in range(32):
            num_ones = 0
            for j in range(len(nums)):
                num = nums[j]
                num_ones += (num >> i) & 1
            count += num_ones * (len(nums) - num_ones)
        return count
