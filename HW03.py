#Lintcode 376
class Solution:
    """
    Your submission beats 68.00% Submissions!
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def __init__(self):
        self.path = []
        self.res = []

    def binaryTreePathSum(self, root, target):
        if root == None:
            return []

        self.path.append(root.val)
        self.binaryTreePathSum(root.left, target)
        self.binaryTreePathSum(root.right, target)
        if sum(self.path) == target and root.left == None and root.right == None:
            path_lcl = [elem for elem in self.path]
            self.res.append(path_lcl)
        self.path.pop()
        return self.res

#Leetcode 95
#Runtime: 60 ms, faster than 86.29% of Python3 online submissions
#Memory Usage: 14.8 MB, less than 80.15% of Python3 online submissions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def form_bst(low,high):
            if low > high:
                return [None]#this means return a null treenode
            BSTs = []
            #an exhaustion algorithm for all possible heads
            for i in range(low, high+1):
                left_sub_trees = form_bst(low, i-1)
                right_sub_trees = form_bst(i+1, high)
                #all unique combination of left and right sub trees for the node you are at
                for left_tree in left_sub_trees:
                    for right_tree in right_sub_trees:
                        head = TreeNode(i)
                        head.left = left_tree
                        head.right = right_tree
                        BSTs.append(head)
            return BSTs
        if n == 0:
            return []
        return form_bst(1,n)

#Leetcode 200
# Runtime: 124 ms, faster than 17.93% of Python3 online submissions
# Memory Usage: 14.1 MB, less than 78.35% of Python3 online submissions
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        def isInside(x, y, grid):
            if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0:
                return False
            return True

        movement = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def DFS(x, y, grid):
            if not isInside(x, y, grid):
                return
            if grid[x][y] == "0":
                return
            if grid[x][y] == "1":
                for i in range(len(movement)):
                    move = movement[i]
                    grid[x][y] = "0"
                    dx = move[0]
                    dy = move[1]
                    DFS(x + dx, y + dy, grid)

        numOfIsland = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    DFS(x, y, grid)
                    numOfIsland += 1
        return numOfIsland

#Leetcode 107
#Runtime: 40 ms, faster than 91.10% of Python3 online submissions
#Memory Usage: 13.4 MB, less than 64.72% of Python3 online submissions
#you can write it in DFS as well
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            level = []
            for count in range(len(queue)):
                node = queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                level.append(node.val)
            res.append(level)
        res.reverse()
        return res