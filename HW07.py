#Leetcode 207
# Runtime: 44 ms, faster than 89.32% of Python3 online submissions
# Memory Usage: 14.2 MB, less than 84.51% of Python3 online submissions
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * (numCourses)
        graph = [[] for i in range(numCourses)]
        for course, preq in prerequisites:
            indegree[course] += 1
            graph[preq].append(course)

        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        path = []
        while queue:
            curr = queue.pop(0)
            path.append(curr)
            courses = graph[curr]
            for course in courses:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)

        return len(path) == numCourses

#Leetcode 399
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def helper(numer, denom, visited, value):
            if numer not in visited:
                visited.append(numer)
            else:
                return -1.0

            if numer == denom:
                return value

            outedges = graph[numer]
            for den, val in outedges:
                result = helper(den, denom, visited, value * val)
                if result != -1.0:
                    return result
            return -1.0

        graph = defaultdict(list)
        for i in range(len(equations)):
            value = values[i]
            numer = equations[i][0]
            denom = equations[i][1]
            graph[numer].append((denom, value))
            graph[denom].append((numer, 1.0 / value))

        res = []
        for numer, denom in queries:
            if numer not in graph or denom not in graph:
                res.append(-1.0)
            else:
                visited = []
                res.append(helper(numer, denom, visited, 1.0))

        return res

#Leetcode 787
# Runtime: 260 ms, faster than 7.46% of Python3 online submissions
# Memory Usage: 16.4 MB, less than 47.88% of Python3 online submissions
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        min_price = sys.maxsize
        queue = [(src, 0, 0)]

        while queue:
            curr = queue.pop(0)
            u = curr[0]
            stops = curr[1]
            total_price = curr[2]
            if u == dst:
                min_price = min(min_price, total_price)
                continue
            if stops <= K and total_price < min_price:
                for v, w in graph[u]:
                    queue.append((v, stops + 1, total_price + w))

        return min_price if min_price != sys.maxsize else -1


from collections import defaultdict

#Lintcode 783
class Solution:
    def getMinRiskValue(self, n, m, x, y, w):
        def helper(start, end, weight, min_w, visited, graph):
            if start == end:
                return weight

            if weight >= min_w:
                return sys.maxsize
            visited[start] = True
            for point, wei in graph[start]:
                if visited.get(point, False):
                    continue
                min_w = min(min_w, helper(point, end, max(weight, wei), min_w, visited, graph))
            visited[start] = False

            return min_w

        graph = defaultdict(list)
        # this is undirected, do not forget to add the revert version back
        for i in range(m):
            graph[x[i]].append((y[i], w[i]))
            graph[y[i]].append((x[i], w[i]))

        visited = {}
        return helper(0, n, 0, sys.maxsize, visited, graph)

#Leetcode 892
# Your submission beats 87.40% Submissions!
from heapq import heapify, heappush, heappop
class Solution:
    def alienOrder(self, words):
        graph = {char: [] for word in words for char in word}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            leng = min(len(w1), len(w2))
            for j in range(leng):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break

        indegree = {key: 0 for key in graph.keys()}
        for prev in graph.keys():
            for curr in graph[prev]:
                val = indegree.get(curr, 0)
                indegree[curr] = val + 1

        queue = []
        heapify(queue)
        for curr in indegree:
            if indegree[curr] == 0:
                heappush(queue, curr)

        res = []
        while queue:
            curr = heappop(queue)
            res.append(curr)
            for char in graph[curr]:
                indegree[char] -= 1
                if indegree[char] == 0:
                    heappush(queue, char)

        if len(res) != len(indegree.keys()):
            return ""

        return "".join(res)

#Leetcode 924
# Runtime: 304 ms, faster than 43.43% of Python3 online submissions
# Memory Usage: 14.6 MB, less than 98.46% of Python3 online submissions
class DSU:
    def __init__(self, N):
        self.parents = list(range(N))
        self.set_size = [1] * N

    def find(self, x):
        if self.parents[x] == x:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        x_head = self.find(x)
        y_head = self.find(y)
        if x_head != y_head:
            self.parents[x_head] = y_head
            self.set_size[y_head] += self.set_size[x_head]


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        num_nodes = len(graph)
        dsu = DSU(num_nodes)

        for i in range(num_nodes):
            for j in range(i, num_nodes):
                if graph[i][j] == 1:
                    dsu.union(i, j)

        set_count = {}
        for node in initial:
            head = dsu.find(node)
            val = set_count.get(head, 0)
            set_count[head] = val + 1

        max_size = 0
        res = min(initial)
        for node in initial:
            head = dsu.find(node)
            if set_count[head] == 1:
                size = dsu.set_size[head]
                if size > max_size:
                    max_size = size
                    res = node
                elif size == max_size and node < res:
                    res = node
        return res