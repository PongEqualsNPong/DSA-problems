# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i =0
        j =len(height)-1
        maxArea = 0
        while i != j:
            lower = i if height[i] <= height[j] else j
            higher = i if lower != i else j
            currentArea = height[lower] * abs((i - j))
            maxArea = currentArea if currentArea > maxArea else maxArea
            if i == lower:
                i+=1
            else:
                j-=1
        return maxArea