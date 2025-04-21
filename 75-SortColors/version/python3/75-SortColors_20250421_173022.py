# Last updated: 4/21/2025, 5:30:22 PM
'''
low: the next position to place a 0

mid: the current index being evaluated

high: the next position to place a 2
'''

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid =0
        high = len(nums)-1

        while mid<= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low +=1
                mid +=1
            elif nums[mid] ==1:
                mid +=1
            else: #nums[mid]==2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -=1
             
