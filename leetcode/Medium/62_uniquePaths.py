# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maze = [[None for y in range(n)] for x in range(m)]

        for i in range(m):
            maze[i][n - 1] = 1
        for i in range(n):
            maze[m - 1][i] = 1

        i = m - 1 - 1
        while i >= 0:
            j = n - 1 - 1
            while j >= 0:
                maze[i][j] = maze[i + 1][j] + maze[i][j + 1]
                j -= 1
            i -= 1
        return maze[0][0]