# Last updated: 9/21/2025, 10:06:23 PM
class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
             return 0

        left, right= 0, len(height)-1
        left_max = right_max = water = 0

        while left<right:
            if height[left]< height[right]:
                left_max = max(left_max, height[left])

                water += left_max - height[left]

                left +=1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]

                right -=1
        return water
        