# Last updated: 4/21/2025, 4:29:29 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height)-1
        current_max = 0

        while left< right:
            width = right - left
            length = min(height[left], height[right])
            current_area = width * length

            current_max = max(current_max, current_area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return current_max
        